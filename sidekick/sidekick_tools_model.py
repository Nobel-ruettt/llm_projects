from sidekick.sidekick_tools import get_file_tools, get_push_tool, get_python_repl_tool, get_search_tool, get_wiki_tool

class SidekickToolsModel:
    def __init__(self):
        self.push_notification_tool = get_push_tool()
        self.file_tools = get_file_tools()
        self.search_tool = get_search_tool()
        self.wiki_tool = get_wiki_tool()
        self.python_repl_tool = get_python_repl_tool()
    
    def get_all_tools(self):
        return self.file_tools + [self.push_notification_tool, 
                                  self.search_tool , 
                                  self.python_repl_tool, 
                                  self.wiki_tool]
    