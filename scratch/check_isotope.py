with open("e:/Durgesh work/dnyanda school/assets/js/main.js", "r", encoding="utf-8") as f:
    js_content = f.read()

import re
matches = [m.start() for m in re.finditer(r'isotope', js_content, re.IGNORECASE)]
print(f"Found {len(matches)} occurrences of isotope.")
for idx, pos in enumerate(matches):
    line_no = js_content[:pos].count("\n") + 1
    snippet = js_content[max(0, pos-40):pos+80].replace("\n", " ")
    print(f"Occurrence {idx+1} at Line {line_no}: {snippet}")
