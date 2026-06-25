import re
import os

files = ["index.html", "about.html", "service.html", "contact.html", "image-gallery.html"]
for file in files:
    path = os.path.join("e:/Durgesh work/dnyanda school", file)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        matches = re.findall(r'href="[^"]*service-single[^"]*"', content)
        if matches:
            print(f"File {file} has links to service-single:")
            for m in matches:
                print(f"  {m}")
