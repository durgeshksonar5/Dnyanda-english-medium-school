import re

with open("e:/Durgesh work/dnyanda school/index.html", "r", encoding="utf-8") as f:
    content = f.read()

comments = re.findall(r'<!--\s*(.*?)\s*-->', content)
for comment in comments:
    if "start" in comment or "end" in comment or "area" in comment:
        # find line number
        pos = content.find(f"<!-- {comment} -->")
        if pos == -1:
            pos = content.find(f"<!--{comment}-->")
        line_no = content[:pos].count("\n") + 1 if pos != -1 else "unknown"
        print(f"Line {line_no}: <!-- {comment} -->")
