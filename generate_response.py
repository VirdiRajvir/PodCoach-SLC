from langchain_ollama import ChatOllama

global first_run
first_run = True
llm = ChatOllama(model="llama3")
with open('static/script/coaching_script.txt', 'r') as file:
    transcript = file.read()
messages = [
    {
        "role": "system",
        "content": f"You are a coach. You are given a transcipt of a coaching session you just conducted. Your task is to answer any questions about the session, and also to provide answers to questions the client may ask. Here is the transcript: {transcript}"
    }
]

def generate_response(prompt, session_messages):
    """
    Generate a response using the LLM based on the provided prompt.
    
    Args:
        prompt (str): The input prompt for the LLM.
        
    Returns:
        str: The generated response from the LLM.
    """

    session_messages.append({"role": "user", "content": prompt})
    response = llm.invoke(session_messages)
    append_message(response.content)
    return response.content

def append_message(response):
    """
    Append the LLM's response to the messages list.
    
    Args:
        response (str): The response from the LLM.
    """
    messages.append({"role": "assistant", "content": response})