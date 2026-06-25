with open("e:/Durgesh work/dnyanda school/contact.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    stripped = line.strip()
    if any(tag in stripped for tag in ["<h1", "<h2", "<h3", "<h4", "<h5", "<h6", "<p", "<span"]):
        # only show lines with text between tags
        import re
        match = re.search(r'>([^<]+)<', stripped)
        if match and match.group(1).strip() and len(match.group(1).strip()) > 5:
            print(f"Line {idx+1}: {stripped}")
