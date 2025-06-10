from langchain_ollama import ChatOllama

def generate_script(goal, name):
    system_prompt = f"You are an AI coach. Your task is to create a personalized speech for {name}, who wants to work on their goal of {goal}. The speech HAS TO be 20 words. Write only text, no markdown, as it will be used in a TTS model."
    llm = ChatOllama(model="llama3",
                 temperature=0.1)

    response = llm.invoke(system_prompt)

    with open('static/script/coaching_script.txt', 'w') as file:
        file.write(response.content)
    system_prompt = f"You are a summarizer assistant. Summarize the following coaching transcript and write only 3 actionable points: {response.content}"
    with open('static/summary/summary.txt', 'w') as file:
        summary_response = llm.invoke(system_prompt)
        file.write(summary_response.content)
    return response.content
