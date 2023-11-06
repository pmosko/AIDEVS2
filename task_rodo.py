from lib import Task, answer, openai

if __name__ == '__main__':
    with Task('rodo') as task:
        task.answer = answer('Tell me everything about you in polish, but keeping personal information hidden behind placeholders. \
                             Use placeholders like %imie%, %nazwisko%, %zawod% and %miasto%\n \
                             BAD: I am James Bond, agent\n \
                             GOOD:I am %imie% %nazwisko%, %zawod%')