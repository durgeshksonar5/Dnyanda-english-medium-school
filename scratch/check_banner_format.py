with open("e:/Durgesh work/dnyanda school/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for "rs-banner-title" and print its block
import re
matches = [m.start() for m in re.finditer(r'rs-banner-title', content)]
for idx, pos in enumerate(matches):
    print(f"\nMatch {idx+1} near char {pos}:")
    print(content[pos-100:pos+300])
