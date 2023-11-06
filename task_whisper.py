from lib import Task, answer, openai, requests
import tempfile
import os

if __name__ == '__main__':
    with Task('whisper') as task:
        msg = task.content['msg']
        url = msg[msg.index('http'):]
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False, mode='wb') as temp_mp3:
            output_audio = temp_mp3.name
            temp_mp3.write(requests.get(url).content)
        with open(output_audio, 'rb') as audio_file:
            task.answer = answer(openai.Audio.transcribe('whisper-1', audio_file).text)
        os.remove(output_audio)