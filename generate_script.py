from langchain_ollama import ChatOllama

def generate_script(goal, name):
    system_prompt = f"You are an AI coach helping users achieve {goal} for {name}. Generate a motivational coaching script for {name} that lasts about 20 minutes, encouraging and guiding {name} through their goal. The script should be engaging, supportive, and provide actionable steps. Use a friendly and encouraging tone."
    llm = ChatOllama(model="llama3",
                 temperature=0.1)

    response = llm.invoke(system_prompt)


    system_prompt = f"You are a summarizer assistant. Summarize the following coaching transcript highlighting the key points and actionable steps: {response.content}"
    with open('static/summary/summary.txt', 'w') as file:
        summary_response = llm.invoke(system_prompt)
        file.write(summary_response.content)
    return response.content
