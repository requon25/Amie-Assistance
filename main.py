from langchain_ollama import ChatOllama
from langchain.agents import create_agent

from dotenv import load_dotenv
from pathlib import Path

from functionsAgents.internet_browser import open_url 
from functionsAgents.date_time import date_and_time
from functionsAgents.file_creation import txt_creation
from functionsAgents.token_and_messages import env_config, discord_message, email_message
from functionsAgents.file_managing import create_folder, open_file, rename_item, delete_item, search_file, move_file, copy_file

# --- Load .env ---
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# --- model ---
llm = ChatOllama(model="qwen2.5:7b")

# --- list of imported functions ---
tools = [open_url, date_and_time, txt_creation, env_config, discord_message, email_message, create_folder, open_file, rename_item, delete_item, search_file, move_file, copy_file]

# --- create agent ---
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
        You are Amie, the user's personal assistant.
        - You answer questions
        - You help with tasks
        - You are friendly but direct
        - You can open the browser if requested
        - You can open and create folders
        - You can add information to a file
        - If you don't know something, say so
        - You can send messages to messaging apps
        - Remind the user to check the .env file in case of an error during message sending
    """
)

# Memory limitations
history = []
MAX_TURNOS = 4

def chat(pregunta: str):
    history.append({"role": "user", "content": pregunta})
    
    # limit history 
    if len(history) > MAX_TURNOS * 2:
        history[:] = history[-MAX_TURNOS * 2:]

    respuesta = agent.invoke({
        "messages": history
    })

    output = respuesta["messages"][-1].content

    history.append({"role": "assistant", "content": output})

    print(f"\nAI Agent: {output}\n")
    return output

# creation of .env file
def env_creation():
    """Save o update .env variables"""

    ruta = Path(".env")
    ruta.touch()

env_creation()

# --- AI Start ---
print("Chat started. Write 'exit' to end the program.\n")
print("Hi, my name is Amie. What can i do for you?")

while True:
    pregunta = input("USER: ")

    if pregunta.lower() == "exit":
        print("¡Bye!")
        break

    if pregunta.strip() == "":
        continue

    chat(pregunta)