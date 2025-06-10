from langchain_ollama import ChatOllama

def generate_script(goal, name):
    system_prompt = f"You are an AI coach. Your task is to create a personalized speech for {name}, who wants to work on their goal of {goal}. The speech HAS TO be above 2800 words. "
    llm = ChatOllama(model="llama3",
                 temperature=0.1)

    response = llm.invoke(system_prompt)


    system_prompt = f"You are a summarizer assistant. Summarize the following coaching transcript and write only 3 actionable points: {response.content}"
    with open('static/summary/summary.txt', 'w') as file:
        summary_response = llm.invoke(system_prompt)
        file.write(summary_response.content)
    return response.content
