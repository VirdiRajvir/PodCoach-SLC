from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")

def generate_response(prompt, session):
    """
    Generate a response using the LLM based on the provided prompt.
    
    Args:
        prompt (str): The input prompt for the LLM.
        
    Returns:
        str: The generated response from the LLM.
    """

    session['messages'].append({"role": "user", "content": prompt})
    response = llm.invoke(session['messages'])
    # append_message(response.content)
    return response.content

def append_message(response, session):
    """
    Append the LLM's response to the messages list.
    
    Args:
        response (str): The response from the LLM.
    """
    session['messages'].append({"role": "assistant", "content": response})