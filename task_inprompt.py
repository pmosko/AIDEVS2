from lib import Task, answer, openai

if __name__ == '__main__':
    with Task('inprompt') as task:
        question = task.content['question']
        knowledge = task.content['input']
        names = [word for word in question.replace('?', '').split()[1:] if word[0].isupper()]
        filtered_knowledge = [line for line in knowledge for name in names if line.startswith(name)]
        ai_prompt = f"""Given knowledge (Kb) answer question (Q)
            Kb: {filtered_knowledge}
            Q: {question}
        """
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": ai_prompt}])
        task.answer = answer(completion.choices[0].message.content)
    