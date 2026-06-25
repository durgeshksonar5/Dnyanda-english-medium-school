sections = [
    ("Banner (319-443)", 319, 443),
    ("Program (444-710)", 444, 710),
    ("About (711-983)", 711, 983),
    ("Text Slider (984-1116)", 984, 1116),
    ("Faculty (1117-1288)", 1117, 1288),
    ("Campus Life (1289-1497)", 1289, 1497),
    ("Event (1498-1663)", 1498, 1663),
    ("Testimonial (1664-1814)", 1664, 1814),
    ("Blog (1815-1984)", 1815, 1984),
    ("Contact/Admission (1985-2107)", 1985, 2107),
    ("Footer (2108-2247)", 2108, 2247)
]

with open("e:/Durgesh work/dnyanda school/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for name, start, end in sections:
    print(f"\n=== {name} ===")
    content = lines[start-1:end]
    # Filter lines that have actual text content to keep display clean
    import re
    for i, line in enumerate(content):
        line_num = start + i
        stripped = line.strip()
        # Find lines with text between tags
        match = re.search(r'>([^<]+)<', stripped)
        if match and match.group(1).strip():
            print(f"Line {line_num}: {stripped}")
