import re

with open("e:/Durgesh work/dnyanda school/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("Scanning index.html sections...")
for idx, line in enumerate(lines):
    # Print headings, section tags, or text paragraphs to locate content
    match = re.search(r'<(h[1-6]|section|span|p|a)\b[^>]*>(.*?)</\1>', line, re.IGNORECASE)
    if match:
        tag = match.group(1)
        text = match.group(2).strip()
        if len(text) > 10 and not text.startswith("<") and ("School" in text or "founded" in text or "Admissions" in text or "education" in text or "Curriculum" in text or "Academic" in text or "Trust" in text or "Principal" in text or "Choose" in text or "Grade" in text or "Program" in text or "Admission" in text):
            print(f"Line {idx+1}: <{tag}> {text}")
