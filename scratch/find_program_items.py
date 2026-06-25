with open("e:/Durgesh work/dnyanda school/service.html", "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'<div class="rs-program-item">', content)]
print(f"Found {len(matches)} occurrences of rs-program-item.")
for idx, pos in enumerate(matches):
    line_no = content[:pos].count("\n") + 1
    # print about 20 lines starting from this position
    lines_subset = content[pos:pos+1500].split("\n")[:15]
    print(f"\n--- Card {idx+1} at Line {line_no} ---")
    print("\n".join(lines_subset))
