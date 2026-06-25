import re
import os

placeholders = [
    r'\+123', r'Fall River', r'Kentucky', r'Kathryn', r'Rashid', r'Ronald', r'Richards', r'Leslie', r'Alexander', r'Marry', r'Holder'
]
files = ["index.html", "about.html", "service.html", "contact.html", "image-gallery.html", "service/service-single.html"]

for file in files:
    path = os.path.join("e:/Durgesh work/dnyanda school", file)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"\nPlaceholder matches in {file}:")
        for p in placeholders:
            matches = [m.start() for m in re.finditer(p, content, re.IGNORECASE)]
            if matches:
                print(f"  Pattern '{p}' matched {len(matches)} times:")
                for pos in matches[:3]:
                    line_no = content[:pos].count("\n") + 1
                    snippet = content[max(0, pos-30):pos+50].replace("\n", " ").strip()
                    print(f"    Line {line_no}: ...{snippet}...")
