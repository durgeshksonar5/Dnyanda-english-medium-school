import os
import re

files_root = [
    "index.html",
    "about.html",
    "admission.html",
    "service.html",
    "contact.html"
]

subpage_file = "service/service-single.html"

base_path = "e:/Durgesh work/dnyanda school"

# 1. Update index.html blog events links and view gallery button
index_path = os.path.join(base_path, "index.html")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace view school gallery button
    old_gallery_btn = """                            <a class="rs-btn has-icon has-bg-primary hover-red" href="image-gallery.html">
                                <span class="btn-text-wrap">
                           <span class="text-default">View School Gallery</span>
                                <span class="text-hover">View School Gallery</span>
                                </span>"""
                                
    new_gallery_btn = """                            <a class="rs-btn has-icon has-bg-primary hover-red" href="admission.html">
                                <span class="btn-text-wrap">
                           <span class="text-default">Apply for Admission</span>
                                <span class="text-hover">Apply for Admission</span>
                                </span>"""
                                
    if old_gallery_btn in content:
        content = content.replace(old_gallery_btn, new_gallery_btn)
        print("Updated view school gallery button in index.html")
        
    # Replace all other href="image-gallery.html" with href="javascript:void(0)"
    content = content.replace('href="image-gallery.html"', 'href="javascript:void(0)"')
    print("Replaced event links in index.html")
    
    with open(index_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

# 2. Update footer links in all root files
for fname in files_root:
    path = os.path.join(base_path, fname)
    if not os.path.exists(path):
        continue
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # footer link replacement
    old_footer_link = '<li><a href="image-gallery.html">Image Gallery</a></li>'
    new_footer_link = '<li><a href="admission.html">Admission</a></li>'
    
    if old_footer_link in content:
        content = content.replace(old_footer_link, new_footer_link)
        print(f"Updated footer explore link in {fname}")
        
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

# 3. Update footer links in subpage file
sub_path = os.path.join(base_path, subpage_file)
if os.path.exists(sub_path):
    with open(sub_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    old_footer_link_sub = '<li><a href="../image-gallery.html">Image Gallery</a></li>'
    new_footer_link_sub = '<li><a href="../admission.html">Admission</a></li>'
    
    if old_footer_link_sub in content:
        content = content.replace(old_footer_link_sub, new_footer_link_sub)
        print(f"Updated footer explore link in {subpage_file}")
        
    with open(sub_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

print("Finished fixing gallery links.")
