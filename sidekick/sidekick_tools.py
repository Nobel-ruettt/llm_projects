from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
import os
import smtplib
from dotenv import load_dotenv
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit,FileManagementToolkit
from playwright.async_api import async_playwright
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import Tool
from langchain_experimental.tools import PythonREPLTool
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun

load_dotenv(override=True)  # Load environment variables from .env file

smtp_configuration = {
    "server": os.getenv("SMTP_SERVER"),
    "port": os.getenv("SMTP_PORT"),
    "username": os.getenv("SMTP_USERNAME"),
    "password": os.getenv("SMTP_PASSWORD"),
    "from": os.getenv("SMTP_SENDER_EMAIL")
}

def push(text: str):
     """Send a push notification as an email to the user"""
     msg = MIMEMultipart()
     msg['From'] = smtp_configuration["from"]
     msg['To'] = "nobelnurulislam@gmail.com"
     msg['Subject'] = "New Notification from LangGraph"
     msg['Date'] = formatdate(localtime=True) 

     msg.attach(MIMEText(text, 'html'))

     with smtplib.SMTP_SSL(smtp_configuration["server"], smtp_configuration["port"]) as server:
            server.login(smtp_configuration["username"], smtp_configuration["password"])
            # Combine all recipients
            recipients = ["nobelnurulislam@gmail.com"]
            server.sendmail(smtp_configuration["from"], recipients, msg.as_string())
     return "success"

def get_push_tool():
    """Returns the push notification tool."""
    return Tool(
        name="send_push_notification", 
        func=push,
        description="Use this tool when you want to send a push notification"
    )

def get_file_tools():
    toolkit = FileManagementToolkit(root_dir="sandbox")
    return toolkit.get_tools()

def get_search_tool():
    search = GoogleSerperAPIWrapper()
    tool_search =Tool(
        name="search",
        func=search.run,
        description="Use this tool when you want to get the results of an online web search"
    )
    return tool_search

def get_wiki_tool():
    """Returns the Wikipedia query tool."""
    wikipedia = WikipediaAPIWrapper()
    wiki_tool = WikipediaQueryRun(api_wrapper=wikipedia)
    return wiki_tool

def get_python_repl_tool():
    """Returns the Python REPL tool."""
    return PythonREPLTool()