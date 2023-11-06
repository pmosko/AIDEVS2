from lib import Task, answer, openai, json

if __name__ == '__main__':
    with Task('functions') as task:
        system = "I am function body generator. Return only JSON response."
        example_user = 'send me definition of function named orderPizza that require 1 param: ' \
            'name (string). Set type of function to "object"'
        example_response = '''
        {
            "name": "orderPizza",
            "description": "select pizza in pizzeria based on pizza name",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "provide name of the pizza"
                    }
                }
        }'''
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": example_user},
                {"role": "assistant", "content": example_response},
                {"role": "user", "content": task.content['msg']},
            ]
        )
        ai_answer = json.loads(completion.choices[0].message.content) # cannot send unformated response :/
        task.answer = answer(ai_answer)