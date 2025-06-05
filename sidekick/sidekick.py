import uuid
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
from sidekick.sidekick_nodes import SideKickNodesAndRouters, State
from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, START, END

load_dotenv(override=True)  


#Here we define a TypedDict for the state of the Sidekick graph.


class SideKick:
    def __init__(self):
        self.graph = None
        self.conversation_id = str(uuid.uuid4())
        self.memory = MemorySaver()
        self.nodes_and_routers = SideKickNodesAndRouters()

    async def setup(self):
        await self.nodes_and_routers.setup()
        self.build_graph()
    
    def cleanup(self):
        self.nodes_and_routers.cleanup()
    

    def build_graph(self):
        # Set up Graph Builder with State
        graph_builder = StateGraph(State)

        # Add nodes
        graph_builder.add_node("worker", self.nodes_and_routers.worker)
        graph_builder.add_node("tools", ToolNode(tools=self.nodes_and_routers.tools))
        graph_builder.add_node("evaluator", self.nodes_and_routers.evaluator)

        # Add edges
        graph_builder.add_edge(START, "worker")
        graph_builder.add_conditional_edges("worker", self.nodes_and_routers.worker_router, {"tools": "tools", "evaluator": "evaluator"})
        graph_builder.add_edge("tools", "worker")
        graph_builder.add_conditional_edges("evaluator", self.nodes_and_routers.route_based_on_evaluation, {"worker": "worker", "END": END})
        

        # Compile the graph
        self.graph = graph_builder.compile(checkpointer=self.memory)
    
    async def run_superstep(self, message, success_criteria, history):
        config = {"configurable": {"thread_id": self.conversation_id}}

        state = {
            "messages": message,
            "success_criteria": success_criteria or "The answer should be clear and accurate",
            "feedback_on_work": None,
            "success_criteria_met": False,
            "user_input_needed": False
        }

        result = await self.graph.ainvoke(state, config=config)
        user = {"role": "user", "content": message}
        reply = {"role": "assistant", "content": result["messages"][-2].content}
        feedback = {"role": "assistant", "content": result["messages"][-1].content}
        return history + [user, reply, feedback]


