import os

base_path = "e:/Durgesh work/dnyanda school"

# 1. Fix footer map in index.html to match other pages (using width: 100% in CSS)
index_path = os.path.join(base_path, "index.html")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Old iframe in index.html
    old_iframe = '                                       <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d55459.80970305274!2d73.870329803516!3d18.714726957359417!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2c95194015a35%3A0xc780074b4d10b8ed!2sDnyanda%20English%20Medium%20School!5e0!3m2!1sen!2sin!4v1782376077447!5m2!1sen!2sin" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>'
    
    # New iframe matching other pages
    new_iframe = '                                        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3779.265287452299!2d73.88793749999999!3d18.6969375!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2c95194015a35%3A0xc780074b4d10b8ed!2sDnyanda%20English%20Medium%20School!5e0!3m2!1sen!2sin!4v1782375696828!5m2!1sen!2sin" style="border:0; width: 100%; height: 160px; border-radius: 8px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
    
    if old_iframe in content:
        content = content.replace(old_iframe, new_iframe)
        print("Updated footer map in index.html to be fully responsive")
    else:
        # Fallback split check
        print("Warning: exact old iframe not found in index.html, trying simple replace")
        content = content.replace('width="400" height="300" style="border:0;"', 'style="border:0; width: 100%; height: 160px; border-radius: 8px;"')
        content = content.replace('referrerpolicy="strict-origin-when-cross-origin"', 'referrerpolicy="no-referrer-when-downgrade"')
        
    with open(index_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

# 2. Fix main map in contact.html to be fully responsive on mobile
contact_path = os.path.join(base_path, "contact.html")
if os.path.exists(contact_path):
    with open(contact_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Old main map iframe
    old_main_map = '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3779.265287452299!2d73.88793749999999!3d18.6969375!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2c95194015a35%3A0xc780074b4d10b8ed!2sDnyanda%20English%20Medium%20School!5e0!3m2!1sen!2sin!4v1782375696828!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>'
    
    # New main map iframe with style="width: 100%; height: 450px; border-radius: 12px;"
    new_main_map = '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3779.265287452299!2d73.88793749999999!3d18.6969375!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2c95194015a35%3A0xc780074b4d10b8ed!2sDnyanda%20English%20Medium%20School!5e0!3m2!1sen!2sin!4v1782375696828!5m2!1sen!2sin" style="border:0; width: 100%; height: 450px; border-radius: 12px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'
    
    if old_main_map in content:
        content = content.replace(old_main_map, new_main_map)
        print("Updated main map in contact.html to be fully responsive")
    else:
        print("Warning: exact main map iframe not found in contact.html")
        content = content.replace('width="600" height="450" style="border:0;"', 'style="border:0; width: 100%; height: 450px; border-radius: 12px;"')
        content = content.replace('referrerpolicy="strict-origin-when-cross-origin"', 'referrerpolicy="no-referrer-when-downgrade"')
        
    with open(contact_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

print("Finished updating map iframes.")
