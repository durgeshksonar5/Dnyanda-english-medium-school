import os

files_root = [
    "index.html",
    "about.html",
    "admission.html",
    "gallery.html",
    "service.html",
    "contact.html"
]

subpage_file = "service/service-single.html"

base_path = "e:/Durgesh work/dnyanda school"

for fname in files_root:
    path = os.path.join(base_path, fname)
    if not os.path.exists(path):
        continue
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    old_block = """                                            <li><a href="admission.html">Admission</a></li>
                                            <li><a href="service.html">Services</a></li>"""
                                            
    new_block = """                                            <li><a href="admission.html">Admission</a></li>
                                            <li><a href="gallery.html">Gallery</a></li>
                                            <li><a href="service.html">Services</a></li>"""
                                            
    if old_block in content:
        content = content.replace(old_block, new_block)
        print(f"Updated footer explore list in {fname}")
    else:
        print(f"Warning: Old block not found in {fname}")
        
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

sub_path = os.path.join(base_path, subpage_file)
if os.path.exists(sub_path):
    with open(sub_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    old_block_sub = """                                            <li><a href="../admission.html">Admission</a></li>
                                            <li><a href="../service.html">Services</a></li>"""
                                            
    new_block_sub = """                                            <li><a href="../admission.html">Admission</a></li>
                                            <li><a href="../gallery.html">Gallery</a></li>
                                            <li><a href="../service.html">Services</a></li>"""
                                            
    if old_block_sub in content:
        content = content.replace(old_block_sub, new_block_sub)
        print(f"Updated footer explore list in {subpage_file}")
    else:
        print(f"Warning: Old block not found in {subpage_file}")
        
    with open(sub_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
