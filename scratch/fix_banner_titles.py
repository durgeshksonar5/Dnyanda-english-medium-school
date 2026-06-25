with open("e:/Durgesh work/dnyanda school/index.html", "r", encoding="utf-8") as f:
    content = f.read()

print("Fixing index.html banner titles and buttons...")

# Replace Slide 1 Title
content = content.replace('<span class="banner-title-primary">International</span>', '<span class="banner-title-primary">Every Child</span>', 1)
content = content.replace('School</span>', 'Matters</span>', 1)

# Replace Slide 2 Title
content = content.replace('<span class="banner-title-primary">International</span>', '<span class="banner-title-primary">Preparing For</span>', 1)
content = content.replace('School</span>', 'Life</span>', 1)

# Replace buttons in banner
# First replace the button links
# (they are the first two href="service.html" inside rs-banner-area)
banner_area_pos = content.find('class="rs-banner-area')
if banner_area_pos != -1:
    banner_section = content[banner_area_pos:banner_area_pos+15000]
    # Replace href="service.html" with href="contact.html" in this section
    banner_section_updated = banner_section.replace('href="service.html"', 'href="contact.html"', 2)
    content = content[:banner_area_pos] + banner_section_updated + content[banner_area_pos+15000:]
    print("  Replaced button links to contact.html in banner section")

# Replace button text "View All Programs" with "Admissions Open for Grade 1 to 5"
content = content.replace('View All Programs', 'Admissions Open for Grade 1 to 5', 4)

with open("e:/Durgesh work/dnyanda school/index.html", "w", encoding="utf-8", newline="\n") as f:
    f.write(content)

print("Done fixing banner!")
