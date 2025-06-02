from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
import smtplib
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os


class PushNotification(BaseModel):
    """A message to be sent to the user"""
    message: str = Field(..., description="The message to be sent to the user.")

class SendEmailTool(BaseTool):
    name: str = "Send a Push Notification"
    description: str = (
        "This tool is used to send a push notification to the user."
    )
    args_schema: Type[BaseModel] = PushNotification

    def _run(self, message: str) -> str:
        smtp_configuration = {
            "server": os.getenv("SMTP_SERVER"),
            "port": os.getenv("SMTP_PORT"),
            "username": os.getenv("SMTP_USERNAME"),
            "password": os.getenv("SMTP_PASSWORD"),
            "from": os.getenv("SMTP_SENDER_EMAIL")
        }

        msg = MIMEMultipart()
        msg['From'] = smtp_configuration["from"]
        msg['To'] = "nobelnurulislam@gmail.com"
        msg['Subject'] = "Investment Oppurtunity"
        msg['Date'] = formatdate(localtime=True) 

        msg.attach(MIMEText(message, 'html'))

        with smtplib.SMTP_SSL(smtp_configuration["server"], smtp_configuration["port"]) as server:
                server.login(smtp_configuration["username"], smtp_configuration["password"])
                # Combine all recipients
                recipients = ["nobelnurulislam@gmail.com"]
                server.sendmail(smtp_configuration["from"], recipients, msg.as_string())
                
        return '{"notification": "ok"}'