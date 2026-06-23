import json
import urllib.request

url = 'https://raw.githubusercontent.com/Altria-1124/quiz-app/master/data/questions.json'
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        text = resp.read().decode('utf-8')
        d = json.loads(text)
        print(f'Online JSON valid. Count: {len(d)}')
        q20 = d[19]['question']
        print(f'ID 20 question: {q20[:80]}')
        q28 = d[27]['question']
        print(f'ID 28 question: {q28[:80]}')
        q30 = d[29]['question']
        print(f'ID 30 question: {q30[:80]}')
except Exception as e:
    print(f'Error: {e}')