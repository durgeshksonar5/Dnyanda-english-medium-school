import os
import re

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

# Let's map filename to the active menu item key
menu_active_map = {
    "index.html": "Home",
    "about.html": "About",
    "admission.html": "Admission",
    "gallery.html": "Gallery",
    "service.html": "Services",
    "contact.html": "Contact"
}

# The menu structure we want for root pages:
def get_menu_html(active_item, is_subpage=False):
    prefix = "../" if is_subpage else ""
    items = [
        ("Home", prefix + "index.html"),
        ("About", prefix + "about.html"),
        ("Admission", prefix + "admission.html"),
        ("Gallery", prefix + "gallery.html"),
        ("Services", prefix + "service.html"),
        ("Contact", prefix + "contact.html")
    ]
    
    html_lines = ['                                <ul class="multipage-menu">']
    for name, link in items:
        # Check active status
        if name == active_item:
            html_lines.append(f'                                    <li class="active"><a href="{link}">{name}</a></li>')
        else:
            html_lines.append(f'                                    <li><a href="{link}">{name}</a></li>')
    html_lines.append('                                </ul>')
    return "\n".join(html_lines)

# Process root files
for fname in files_root:
    path = os.path.join(base_path, fname)
    if not os.path.exists(path):
        print(f"File {fname} does not exist!")
        continue
        
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace multipage-menu blocks
    active_key = menu_active_map.get(fname)
    new_menu = get_menu_html(active_key, is_subpage=False)
    
    pattern = r'<ul class="multipage-menu">[\s\S]*?</ul>'
    matches = re.findall(pattern, content)
    if matches:
        content = re.sub(pattern, new_menu, content)
        print(f"Updated menus in {fname} ({len(matches)} matches found)")
    else:
        print(f"Warning: no multipage-menu found in {fname}")
        
    # Now let's connect the header Admission Open buttons if they are not already connected
    old_btn = 'class="rs-btn has-icon has-theme-red hover-black" href="javascript:void(0)"'
    new_btn = 'class="rs-btn has-icon has-theme-red hover-black" href="admission.html"'
    if old_btn in content:
        content = content.replace(old_btn, new_btn)
        print(f"Updated header buttons in {fname}")
        
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

# Process subpage file
subpage_path = os.path.join(base_path, subpage_file)
if os.path.exists(subpage_path):
    with open(subpage_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    new_menu_sub = get_menu_html("Services", is_subpage=True)
    pattern = r'<ul class="multipage-menu">[\s\S]*?</ul>'
    matches = re.findall(pattern, content)
    if matches:
        content = re.sub(pattern, new_menu_sub, content)
        print(f"Updated menus in {subpage_file}")
        
    old_btn = 'class="rs-btn has-icon has-theme-red hover-black" href="javascript:void(0)"'
    new_btn = 'class="rs-btn has-icon has-theme-red hover-black" href="../admission.html"'
    if old_btn in content:
        content = content.replace(old_btn, new_btn)
        print(f"Updated header buttons in {subpage_file}")
        
    with open(subpage_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
else:
    print(f"Subpage file {subpage_file} does not exist!")

print("All navigation updates completed!")
