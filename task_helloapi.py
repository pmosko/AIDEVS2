from lib import Task, answer

if __name__ == '__main__':
    with Task('helloapi') as task:
        task.answer = answer(task.content['cookie'])
