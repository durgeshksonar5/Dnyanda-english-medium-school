import os

base_path = "e:/Durgesh work/dnyanda school"

# 1. Update index.html footer link
index_path = os.path.join(base_path, "index.html")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    old_link = '<li><a href="javascript:void(0)">Image Gallery</a></li>'
    new_link = '<li><a href="gallery.html">School Gallery</a></li>'
    if old_link in content:
        content = content.replace(old_link, new_link)
        print("Updated footer link in index.html to point to gallery.html")
    with open(index_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

# 2. Update title in admission.html
admission_path = os.path.join(base_path, "admission.html")
if os.path.exists(admission_path):
    with open(admission_path, "r", encoding="utf-8") as f:
        content = f.read()
    old_title = "<title>Image Gallery - Dnyanda English Medium School</title>"
    new_title = "<title>Admission - Dnyanda English Medium School</title>"
    if old_title in content:
        content = content.replace(old_title, new_title)
        print("Updated title in admission.html to Admission")
    with open(admission_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

# 3. Update title in gallery.html
gallery_path = os.path.join(base_path, "gallery.html")
if os.path.exists(gallery_path):
    with open(gallery_path, "r", encoding="utf-8") as f:
        content = f.read()
    old_title = "<title>Image Gallery - Dnyanda English Medium School</title>"
    new_title = "<title>School Gallery - Dnyanda English Medium School</title>"
    if old_title in content:
        content = content.replace(old_title, new_title)
        print("Updated title in gallery.html to School Gallery")
    with open(gallery_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

print("Finished fixing titles and footer gallery links.")
