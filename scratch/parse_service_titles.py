import re

with open("e:/Durgesh work/dnyanda school/service.html", "r", encoding="utf-8") as f:
    content = f.read()

titles = re.findall(r'<h5 class="rs-program-title">.*?<a[^>]*>(.*?)</a>', content, re.DOTALL)
print("Found program titles:")
for t in titles:
    print(t.strip())
