import re
import os

keywords = ["principal", "founder", "trustee", "trust", "message", "director", "welcome"]
files = ["index.html", "about.html", "service.html", "contact.html", "image-gallery.html", "service/service-single.html"]

for file in files:
    path = os.path.join("e:/Durgesh work/dnyanda school", file)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"\nScanning {file}...")
        for keyword in keywords:
            matches = [m.start() for m in re.finditer(re.escape(keyword), content, re.IGNORECASE)]
            if matches:
                print(f"  Found '{keyword}' {len(matches)} times:")
                for pos in matches[:3]:
                    line_no = content[:pos].count("\n") + 1
                    snippet = content[max(0, pos-40):pos+60].replace("\n", " ").strip()
                    print(f"    Line {line_no}: ...{snippet}...")
