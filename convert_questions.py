import json
import re

# Read the markdown file
with open(r'e:\题目\第一章.md', 'r', encoding='utf-8') as f:
    content = f.read()

questions = []
qid = 1
category = "第一章 进入近代后中华民族的磨难与抗争"

def split_options(text):
    """Split options that may be on one line like 'A. xxx B. xxx C. xxx D. xxx'"""
    # Match option markers like A. or A、 followed by text
    parts = re.split(r'\s+(?=[A-D][.、])', text.strip())
    result = []
    for p in parts:
        p = p.strip()
        m = re.match(r'^[A-D][.、]\s*(.+)', p)
        if m:
            result.append(m.group(1).strip())
    return result if len(result) >= 2 else []

# Split by question type sections
sections = content.split('## ')
for section in sections:
    if '单选题' in section:
        lines = section.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            m = re.match(r'^(\d+)\.\s*(.+)', line)
            if m:
                q_text = m.group(2).strip()
                # Options: may be single line or multiple lines
                options = []
                j = i + 1
                
                # First try: collect lines until we hit "答案"
                option_lines = []
                while j < len(lines):
                    nl = lines[j].strip()
                    if re.match(r'^答案[：:]', nl) or re.match(r'^\d+\.', nl):
                        break
                    if nl:
                        option_lines.append(nl)
                    j += 1
                
                # Parse options from collected lines
                if option_lines:
                    combined = ' '.join(option_lines)
                    options = split_options(combined)
                
                # Find answer
                answer_line = ""
                while j < len(lines):
                    nl = lines[j].strip()
                    if re.match(r'^答案[：:]', nl):
                        answer_line = nl
                        break
                    if re.match(r'^\d+\.', nl):
                        break
                    j += 1
                
                ans_match = re.match(r'答案[：:]\s*([A-D]+)', answer_line)
                if ans_match and options:
                    answer_letters = ans_match.group(1)
                    answer_index = ord(answer_letters[0]) - ord('A')
                    correct_text = options[answer_index] if answer_index < len(options) else ""
                    q = {
                        "id": qid,
                        "type": "choice",
                        "category": category,
                        "difficulty": "medium",
                        "question": q_text,
                        "options": options,
                        "answer": answer_index,
                        "explanation": f"正确答案是 {answer_letters[0]}。{correct_text}"
                    }
                    questions.append(q)
                    qid += 1
                i = j
            else:
                i += 1
    
    elif '多选题' in section:
        lines = section.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            m = re.match(r'^(\d+)\.\s*(.+)', line)
            if m:
                q_text = m.group(2).strip()
                options = []
                j = i + 1
                
                option_lines = []
                while j < len(lines):
                    nl = lines[j].strip()
                    if re.match(r'^答案[：:]', nl) or re.match(r'^\d+\.', nl):
                        break
                    if nl:
                        option_lines.append(nl)
                    j += 1
                
                if option_lines:
                    combined = ' '.join(option_lines)
                    options = split_options(combined)
                
                # Find answer
                answer_line = ""
                while j < len(lines):
                    nl = lines[j].strip()
                    if re.match(r'^答案[：:]', nl):
                        answer_line = nl
                        break
                    if re.match(r'^\d+\.', nl):
                        break
                    j += 1
                
                ans_match = re.match(r'答案[：:]\s*([A-D]+)', answer_line)
                if ans_match and options:
                    answer_letters = ans_match.group(1)
                    answer_indices = [ord(c) - ord('A') for c in answer_letters]
                    q = {
                        "id": qid,
                        "type": "multiChoice",
                        "category": category,
                        "difficulty": "medium",
                        "question": q_text,
                        "options": options,
                        "answer": answer_indices,
                        "explanation": f"正确答案是 {', '.join(answer_letters)}。"
                    }
                    questions.append(q)
                    qid += 1
                i = j
            else:
                i += 1

print(f"Parsed {len(questions)} questions")

# Save to questions.json
output_path = r'e:\quiz-app\data\questions.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Saved to {output_path}")

# Verify
with open(output_path, 'r', encoding='utf-8') as f:
    test = json.load(f)
print(f"Verification OK: {len(test)} questions")
for q in test[:5]:
    print(f"  ID {q['id']}: [{q['type']}] {q['question'][:50]}...")
    print(f"    Options: {q['options']}")
    print(f"    Answer: {q['answer']}")