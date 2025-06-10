from langchain_ollama import ChatOllama

def generate_script(goal):
    system_prompt = f"You are an AI coach helping users achieve {goal}. Generate a motivational coaching script that lasts about 20 minutes, encouraging and guiding the user through their goal. The script should be engaging, supportive, and provide actionable steps. Use a friendly and encouraging tone."
    llm = ChatOllama(model="llama3",
                 temperature=0.1)

    response = llm.invoke(system_prompt)
    #save script to file
    with open('static/script/coaching_script.txt', 'w') as file:
        file.write(response.content)

    return response.content
