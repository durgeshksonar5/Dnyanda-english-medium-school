with open("e:/Durgesh work/dnyanda school/service.html", "r", encoding="utf-8") as f:
    s1 = f.read()

with open("e:/Durgesh work/dnyanda school/service/service-single.html", "r", encoding="utf-8") as f:
    s2 = f.read()

print(f"File sizes: service.html={len(s1)}, service-single.html={len(s2)}")
if s1 == s2:
    print("Files are identical!")
else:
    # Print the lines where they differ
    l1 = s1.split("\n")
    l2 = s2.split("\n")
    diffs = 0
    for idx, (line1, line2) in enumerate(zip(l1, l2)):
        if line1 != line2:
            print(f"Diff at line {idx+1}:")
            print(f"  service.html: {line1[:80]}")
            print(f"  service-single: {line2[:80]}")
            diffs += 1
            if diffs > 5:
                break
