path = "e:/Durgesh work/dnyanda school/contact.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

print("Updating contact.html...")

# 1. Phone number block
phone_block_old = """                                    <div class="rs-contact-links">
                                        <a href="tel:+12705550117">(+1) 270-555-0117</a>
                                        <a href="tel:2095550104">(209) 555-0104</a>
                                    </div>"""

phone_block_new = """                                    <div class="rs-contact-links">
                                        <a href="tel:+917557333222">+91 7557333222</a>
                                    </div>"""

content = content.replace(phone_block_old, phone_block_new)

# 2. Admission phone block
adm_block_old = """                                    <div class="rs-contact-links">
                                        <a href="tel:+990123%20456%20789">+91 7557333222</a>
                                        <a href="tel:1270--555-0117">(+1) 270-555-0117</a>
                                    </div>"""

adm_block_new = """                                    <div class="rs-contact-links">
                                        <a href="tel:+917557333222">+91 7557333222</a>
                                    </div>"""

content = content.replace(adm_block_old, adm_block_new)

# 3. Email block
email_block_old = """                                    <div class="rs-contact-links">
                                        <a href="mailto:infoexmple@Dnyanda English Medium School.edu">infoexmple@Dnyanda English Medium School.edu </a>
                                        <a href="mailto:info@dnyanda.edu">info@dnyanda.edu </a>
                                    </div>"""

email_block_new = """                                    <div class="rs-contact-links">
                                        <a href="mailto:info@dnyanda.edu">info@dnyanda.edu</a>
                                    </div>"""

content = content.replace(email_block_old, email_block_new)

# 4. Address block
address_old = "<p> 4517 Huston Ave. Kuchu, Kentucky 39495 </p>"
address_new = "<p> Hanumanwadi, Alandi, Pune - 412105 </p>"

content = content.replace(address_old, address_new)

with open(path, "w", encoding="utf-8", newline="\n") as f:
    f.write(content)

print("Contact page (contact.html) successfully updated!")
