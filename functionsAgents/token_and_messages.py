from langchain_core.tools import tool

from pathlib import Path
import os
import requests
import smtplib
from email.mime.text import MIMEText

@tool
def env_config(keys: str, value: str) -> str:
    """Save or update a variable in .env"""

    route = Path(".env")
    line = f"{keys}={value}"

    # si no existe
    if not route.exists():
        route.write_text(line + "\n")
        return f"{keys} saved"

    lines = route.read_text().splitlines()
    new_list = []
    env_found = False

    for l in lines:
        if l.startswith(keys + "="):
            new_list.append(line)
            env_found = True
        else:
            new_list.append(l)

    if not env_found:
        new_list.append(line)

    route.write_text("\n".join(new_list) + "\n")

    if env_found:
        return f"{keys} Updated"
    else:
        return f"{keys} Added"
    
@tool
def discord_message(message: str) -> str:
    """Sending message using discord webhook"""

    webhook = os.getenv("DISCORD_WEBHOOK")
    if not webhook:
        webhook = os.getenv("DISCORD_WEBHOOK_URL")

    if not webhook:
        return "There is no DISCORD_WEBHOOK in .env"

    try:
        requests.post(webhook, json={"content": message}) 
        return "Message sent"
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def email_message(to_user: str, subject: str, message: str) -> str:
    """Send a message using email"""

    user = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_APP_PASSWORD")
    if not password:
        password = os.getenv("EMAIL_PASSWORD")

    if not user or not password:
        return "There is no email configuration"

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = to_user

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(user, password)
            server.send_message(msg)

        return "Email enviado correctamente"
    except Exception as e:
        return f"Error: {str(e)}"

 
# NEXT WHATSAPP, TELEGRAM, ETC.
