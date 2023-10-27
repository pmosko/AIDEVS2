from lib import Task, answer, openai

if __name__ == '__main__':
    with Task('moderation') as task:
        moderations = [
            int(openai.Moderation.create(input=input)['results'][0]['flagged']) 
            for input in task.content['input']
        ]
        task.answer = answer(moderations)