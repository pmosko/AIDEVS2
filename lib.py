import requests
import urllib
import functools
import json
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['AIDEV_TOKEN']
URL = "https://zadania.aidevs.pl"

def auth_task(taskname: str) -> str:
    """Get token for task"""
    url = functools.reduce(urllib.parse.urljoin, (URL, 'token/', taskname))
    load = {
        "apikey": TOKEN,
    }
    return json.loads(requests.post(url=url, json=load).text)['token']

def get_task(token: str=None, task_name: str=None) -> dict:
    """Get Task via token or task name"""
    if not token:
        token = auth_task(task_name)
    url = functools.reduce(urllib.parse.urljoin, (URL, 'task/', token))
    return json.loads(requests.get(url=url).text)

def send_answer(token: str, answer: dict, headers: dict=None) -> dict:
    """Send Task answer"""
    url = functools.reduce(urllib.parse.urljoin, (URL, 'answer/', token))
    return json.loads(requests.post(url=url, json=answer, headers=headers).text)

def answer(answer=None, *args, **kwargs):
    """Parse response to JSON response format"""
    response = {}
    if answer is not None:
        response['answer'] = answer
    for arg in args:
        response.update(*arg)
    response.update(**kwargs)
    return response

class Task:
    def __init__(self, task_name: str, send_response=True, get_task=True) -> None:
        self.task_name = task_name
        self.send_response = send_response
        self.answer = None
        self.answer_send = False
        if get_task:
            self.get_task()

    def get_task(self) -> dict:
        """Get Task content"""
        self.task_token = auth_task(self.task_name)
        self.content = get_task(self.task_token)
        return self.content
    
    def send_answer(self, answer: str=None, headers: dict=None) -> dict:
        """Send Task answer"""
        if answer is None:
            answer = self.answer
        self.answer_send = True
        return send_answer(self.task_token, answer=answer, headers=headers)
    
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        if self.send_response and not self.answer_send:
            self.send_answer()
        return