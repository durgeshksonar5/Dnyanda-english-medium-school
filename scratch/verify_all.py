import re
import os

files = [
    "index.html", 
    "about.html", 
    "service.html", 
    "contact.html", 
    "admission.html", 
    "gallery.html", 
    "service/service-single.html"
]

placeholders = [
    r'\+1270', r'Fall River', r'Kentucky', r'Kathryn', r'infoexmple', r'Huston Ave', r'209-555'
]

print("Starting validation checks...")

has_errors = False

for file in files:
    path = os.path.join("e:/Durgesh work/dnyanda school", file)
    if os.path.exists(path):
        # 1. Check file encoding/BOM
        with open(path, "rb") as f:
            raw = f.read(3)
        if raw == b'\xef\xbb\xbf':
            print(f"  [ERROR] {file} has UTF-8 BOM encoding!")
            has_errors = True
        else:
            print(f"  [OK] {file} has no BOM")

        # 2. Check for placeholders
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        for p in placeholders:
            matches = [m.start() for m in re.finditer(p, content, re.IGNORECASE)]
            if matches:
                print(f"  [ERROR] Placeholder '{p}' found in {file} at lines:")
                has_errors = True
                for pos in matches:
                    line_no = content[:pos].count("\n") + 1
                    print(f"    Line {line_no}")

        # 3. Check for specific placeholders left
        if file == "contact.html":
            if "infoexmple" in content:
                print(f"  [ERROR] infoexmple found in contact.html")
                has_errors = True

if not has_errors:
    print("\nSUCCESS: All files successfully validated! No placeholders or BOM found.")
else:
    print("\nFAILURE: Validation errors found. Please check logs.")
