🤖 Amie - AI Agent (Local, Open Source)
-------------------------------------------
Amie is a local AI agent designed to interact with the user, operating system, automate tasks, and serve as a foundation for collaborative open-source projects.
Unlike other solutions, Amie is not tied to a specific model: 
users download or choose their desired AI model through Ollama, allowing for greater flexibility and control over the agent's performance and capabilities.

A) Objective:
  To create a solid foundation for local AI agents that can:
  Chat with the user,
  Control the system,
  Automate tasks,
  Be freely modified by the community,
  Adapt to different AI models according to user needs

B) Installation:
  1. Clone the repository
  2. Create a virtual environment
  3. Install dependencies:
      pip install ollama,
      pip install langchain,
      pip install langchain-ollama,
      pip install python-dotenv,
      pip install platformdirs

C) Using the Model:
  Amie uses local models via Ollama. You must download or select the model you want to use before running the agent.
  
  Example with Qwen:
  ollama run qwen2.5:7b
  
  You can also use other Ollama-compatible models depending on your needs.
  IMPORTANT: Not all models can function as agents.

D) Performance:
  The system functions correctly, but with relatively long response times such as:
  Creating folders: > 1 minute,
  
  Opening files: up to 5 minutes,
  
  Moving/copying files: > 3 minutes,
  
  Checking date/time: ~ 1 minute

E) Important Considerations:
  Prompts should be clear and detailed.
  
  The operating system language affects behavior:
  "Downloads" ≠ "Descargas"
  
  Not all LLM models work well as agents.
  
  Navigates in complex directories, such as Ollama, are limited.
  
  Performance will depend on the chosen Ollama model and the available hardware.

The test was performed using Python 3.12.3

-------------------------------------------------------------------------------------------

▶️ How to use Amie (Step by step)
--------------------------------

Follow these steps to run the project correctly:

1. Ensure Ollama is running

On some systems (especially Linux), you need to start it manually:

ollama serve

(On Windows and macOS, it's usually already running in the background.)



2. Download a model

Example:

ollama pull qwen2.5:7b

IMPORTANT: Not all models can function as agents.


3. Configure the model in the code

Open the main.py file and find where the model is defined.

Example:

llm = ChatOllama(model="qwen2.5:7b")

Replace "qwen2.5:7b" with the model you downloaded.


4. Run the program
python main.py
