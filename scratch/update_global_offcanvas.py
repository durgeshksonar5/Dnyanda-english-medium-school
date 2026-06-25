import os

files = [
    "index.html", 
    "about.html", 
    "service.html", 
    "contact.html", 
    "image-gallery.html", 
    "service/service-single.html"
]

about_old = "Welcome to Dnyanda English Medium School. It was founded in 1966, and Dnyanda English Medium School has grown into one of the leading institutions of higher education."
about_new = "Welcome to Dnyanda English Medium School. Established in the academic year 2021–22, Dnyanda English Medium School has been committed to shaping young minds through quality education, strong moral values, and child-centered learning."

addr_old = "374 William S Canning Blvd, Fall River MA Road 2721, USA"
addr_new = "Hanumanwadi, Alandi, Pune - 412105"

phone_old = 'href="tel:+12346691234"> +123-4669-1234'
phone_new = 'href="tel:+917557333222"> +91 7557333222'

print("Starting offcanvas updates...")
for file in files:
    path = os.path.join("e:/Durgesh work/dnyanda school", file)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check and replace
        updated = content
        if about_old in updated:
            updated = updated.replace(about_old, about_new)
            print(f"  Replaced about paragraph in {file}")
        else:
            print(f"  WARNING: old about paragraph not found in {file}")
            
        if addr_old in updated:
            updated = updated.replace(addr_old, addr_new)
            print(f"  Replaced address in {file}")
        else:
            print(f"  WARNING: old address not found in {file}")
            
        if phone_old in updated:
            updated = updated.replace(phone_old, phone_new)
            print(f"  Replaced phone link in {file}")
        else:
            # Let's try matching with different whitespaces
            # (just in case there are variations)
            phone_alt = 'href="tel:+12346691234"> +123-4669-1234 </a>'
            if phone_alt in updated:
                updated = updated.replace(phone_alt, 'href="tel:+917557333222"> +91 7557333222 </a>')
                print(f"  Replaced alt phone link in {file}")
            else:
                print(f"  WARNING: old phone link not found in {file}")
        
        # Save BOM-free UTF-8
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(updated)
        print(f"  Saved {file}")
print("Finished offcanvas updates.")
