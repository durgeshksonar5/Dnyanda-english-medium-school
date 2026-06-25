import re

def scan_file(filepath):
    print(f"\n=========================================\nFILE: {filepath}\n=========================================\n")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # First find all comments
    comments = re.findall(r'<!--\s*(.*?)\s*-->', content)
    print("--- STRUCTURAL COMMENTS ---")
    for comment in comments:
        if any(w in comment for w in ["start", "end", "area", "widget"]):
            pos = content.find(f"<!-- {comment} -->")
            if pos == -1:
                pos = content.find(f"<!--{comment}-->")
            line_no = content[:pos].count("\n") + 1 if pos != -1 else "unknown"
            print(f"Line {line_no}: <!-- {comment} -->")
            
    # Then find text highlights
    lines = content.split("\n")
    print("\n--- TEXT HIGHLIGHTS ---")
    for idx, line in enumerate(lines):
        stripped = line.strip()
        match = re.search(r'>([^<]+)<', stripped)
        if match and match.group(1).strip():
            text = match.group(1).strip()
            # print lines with headers, interesting school content
            if any(tag in stripped for tag in ["<h1", "<h2", "<h3", "<h4", "<h5", "<h6", "<p"]):
                if len(text) > 8 and not text.startswith("&"):
                    print(f"Line {idx+1}: {stripped}")

scan_file("e:/Durgesh work/dnyanda school/about.html")
scan_file("e:/Durgesh work/dnyanda school/service.html")
scan_file("e:/Durgesh work/dnyanda school/service/service-single.html")
