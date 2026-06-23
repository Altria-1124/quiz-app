import json, base64

with open(r'e:\quiz-app\data\online_base64.txt', 'r', encoding='utf-8') as f:
    data = f.read().strip()

text = base64.b64decode(data).decode('utf-8')
d = json.loads(text)
print(f'Online JSON valid. Count: {len(d)}')
q20 = d[19]['question']
print(f'ID 20 question: {q20[:60]}')