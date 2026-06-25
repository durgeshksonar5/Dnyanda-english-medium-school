with open("e:/Durgesh work/dnyanda school/index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = re.findall(r'<iframe[^>]*src="[^"]*"[^>]*>', content)
print("Found iframes:")
for m in matches:
    print(m)
