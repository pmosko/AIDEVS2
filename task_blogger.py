from lib import Task, answer, openai

if __name__ == '__main__':
    with Task('blogger') as task:
        paragraphs = task.content['blog']
        task_answer = []
        for paragraph in paragraphs:
            ai_input = task.content['msg'] + "in polish"+ "\n- " + paragraph
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": ai_input}])
            task_answer.append(completion.choices[0].message.content)
        task.answer = answer(task_answer)