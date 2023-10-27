from lib import Task, answer, openai

if __name__ == '__main__':
    with Task('liar', get_task=False) as task:
        question = 'Name a river in Poland'
        response = task.send_task(answer(question, key='question'))['answer']
        guard = f"""Check if answer is truthfull and relevant to the question. Respond only with YES or NO.
            Q: {question}
            A: {response}
        """
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": guard}])
        task.answer = answer(completion.choices[0].message.content)
    