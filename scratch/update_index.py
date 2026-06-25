import re

path = "e:/Durgesh work/dnyanda school/index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

print("Updating index.html...")

# 1. Hero Section Slider Content
# Slide 1
slide1_old_title = """                                                <h1 class="rs-banner-title">
                                                     <span class="banner-title-primary">International</span>
                                                     <span class="banner-title-secondary">
                                           <img class="rs-banner-shape" src="assets/images/shape/logo-white-two.webp"
                                              alt="image">
                                           School</span>
                                                 </h1>"""

slide1_new_title = """                                                <h1 class="rs-banner-title">
                                                     <span class="banner-title-primary">Every Child</span>
                                                     <span class="banner-title-secondary">
                                           <img class="rs-banner-shape" src="assets/images/shape/logo-white-two.webp"
                                              alt="image">
                                           Matters</span>
                                                 </h1>"""

slide1_old_btn = """                                                <div class="rs-banner-btn">
                                                     <a class="rs-btn has-icon has-theme-red" href="service.html">
                                                         <span class="btn-text-wrap">
                                              <span class="text-default">View All Programs</span>
                                                         <span class="text-hover">View All Programs</span>
                                                         </span>"""

slide1_new_btn = """                                                <div class="rs-banner-btn">
                                                     <a class="rs-btn has-icon has-theme-red" href="contact.html">
                                                         <span class="btn-text-wrap">
                                              <span class="text-default">Admissions Open for Grade 1 to 5</span>
                                                         <span class="text-hover">Admissions Open for Grade 1 to 5</span>
                                                         </span>"""

# Let's replace the first slide title and button, then the second slide title and button
# To be extremely precise, let's find the exact occurrences.
# Let's check how many times slide1_old_title appears. It should appear twice (for slide 1 and slide 2).
# We can replace them.
if slide1_old_title in content:
    content = content.replace(slide1_old_title, slide1_new_title)
    print("  Replaced Hero titles")
else:
    print("  WARNING: Hero titles not found")

if slide1_old_btn in content:
    content = content.replace(slide1_old_btn, slide1_new_btn)
    print("  Replaced Hero buttons")
else:
    print("  WARNING: Hero buttons not found")


# 2. Why Choose Us Columns (Program area, lines 444-709)
# Column 1
col1_old = """                                    <h5 class="rs-program-title">Junior School</h5>
                                    <p class="rs-program-desc">Our programs are designed to develop skilled legal.</p>"""

col1_new = """                                    <h5 class="rs-program-title">Academics & Values</h5>
                                    <p class="rs-program-desc">A strong scholastic foundation focused on concept clarity, discipline, and moral growth.</p>"""

links1_old = """                                                        <li>
                                                             <a href="javascript:void(0)">
                                                                 Summer Workouts <span class="arrow-icon">"""

links1_new = """                                                        <li>
                                                             <a href="javascript:void(0)">
                                                                 CBSE-Oriented Approach <span class="arrow-icon">"""

links2_old = """                                                        <li>
                                                             <a href="javascript:void(0)">
                                                                 Visual Arts <span class="arrow-icon">"""

links2_new = """                                                        <li>
                                                             <a href="javascript:void(0)">
                                                                 Activity-Based Learning <span class="arrow-icon">"""

links3_old = """                                                        <li>
                                                             <a href="javascript:void(0)">
                                                                 Performing Arts <span class="arrow-icon">"""

links3_new = """                                                        <li>
                                                             <a href="javascript:void(0)">
                                                                 Moral & Value Education <span class="arrow-icon">"""

content = content.replace(col1_old, col1_new)
content = content.replace(links1_old, links1_new)
content = content.replace(links2_old, links2_new)
content = content.replace(links3_old, links3_new)

# Column 2
col2_old = """                                    <h5 class="rs-program-title">Boarding School</h5>
                                    <p class="rs-program-desc">Our programs are designed to develop skilled legal.</p>"""

col2_new = """                                    <h5 class="rs-program-title">Co-Scholastic Learning</h5>
                                    <p class="rs-program-desc">Nurturing creativity and self-expression through sports, arts, and creative competitions.</p>"""

col2_links1_old = """                                                                 Strength Conditioning"""
col2_links1_new = """                                                                 Sports and Fitness"""

col2_links2_old = """                                                                 Sports Medicine"""
col2_links2_new = """                                                                 Drawing and Craft"""

col2_links3_old = """                                                                 Alumni Athletes"""
col2_links3_new = """                                                                 Music and Dance"""

content = content.replace(col2_old, col2_new)
content = content.replace(col2_links1_old, col2_links1_new)
content = content.replace(col2_links2_old, col2_links2_new)
content = content.replace(col2_links3_old, col2_links3_new)

# Column 3
col3_old = """                                    <h5 class="rs-program-title">Senior School</h5>
                                    <p class="rs-program-desc">Our programs are designed to develop skilled legal.</p>"""

col3_new = """                                    <h5 class="rs-program-title">Future-Ready Skills</h5>
                                    <p class="rs-program-desc">Preparing children for tomorrow through technology, robotics, and financial awareness.</p>"""

col3_links1_old = """                                                                 Technology <span class="arrow-icon">"""
col3_links1_new = """                                                                 Robotics & Coding <span class="arrow-icon">"""

col3_links2_old = """                                                                 Social Studies <span class="arrow-icon">"""
col3_links2_new = """                                                                 Financial Literacy <span class="arrow-icon">"""

col3_links3_old = """                                                                 Math <span class="arrow-icon">"""
col3_links3_new = """                                                                 Phonics & Communication <span class="arrow-icon">"""

content = content.replace(col3_old, col3_new)
content = content.replace(col3_links1_old, col3_links1_new)
content = content.replace(col3_links2_old, col3_links2_new)
content = content.replace(col3_links3_old, col3_links3_new)


# 3. Welcome / About Section Tabs & Accordions (Vision, Mission, Values)
# Mission tab
mission_tab_old = """                                         <div class="tab-pane fade show active" id="pills-item-one" role="tabpanel" aria-labelledby="pills-item-one-tab" tabindex="0">
                                             <div class="rs-about-tab-content">
                                                  <p>Education is not just about preparing children for examinations; it is about preparing them for life. Our mission is to nurture curious minds, build strong values, and inspire young learners to become confident, compassionate, and future-ready individuals.</p>
                                             </div>
                                         </div>"""

mission_tab_new = """                                         <div class="tab-pane fade show active" id="pills-item-one" role="tabpanel" aria-labelledby="pills-item-one-tab" tabindex="0">
                                             <div class="rs-about-tab-content">
                                                  <p>Our mission is to provide quality education with strong values, modern learning methods, and holistic development.<br><br>We aim to:<br>• Build a strong academic foundation.<br>• Develop good manners, discipline, and moral values.<br>• Encourage creativity, curiosity, and confidence.<br>• Promote communication, teamwork, and leadership skills.<br>• Provide exposure to technology, sports, arts, and life skills.<br>• Help every child discover their strengths and grow with purpose.</p>
                                             </div>
                                         </div>"""

# Vision tab
vision_tab_old = """                                         <div class="tab-pane fade" id="pills-item-two" role="tabpanel" aria-labelledby="pills-item-two-tab" tabindex="0">
                                             <div class="rs-about-tab-content">
                                                  <p>Since 2021, we have been creating an environment where learning goes beyond textbooks—where creativity is encouraged, questions are welcomed, talents are celebrated, and every achievement is valued.</p>
                                             </div>
                                         </div>"""

vision_tab_new = """                                         <div class="tab-pane fade" id="pills-item-two" role="tabpanel" aria-labelledby="pills-item-two-tab" tabindex="0">
                                             <div class="rs-about-tab-content">
                                                  <p>To nurture young learners into confident, responsible, value-driven, and future-ready individuals who can contribute positively to society.</p>
                                             </div>
                                         </div>"""

# Values tab
values_tab_old = """                                         <div class="tab-pane fade" id="pills-item-three" role="tabpanel" aria-labelledby="pills-item-three-tab" tabindex="0">
                                             <div class="rs-about-tab-content">
                                                  <p>We value discipline, integrity, respect, gratitude, and a spirit of service. Together, let’s build a brighter future—one child at a time.</p>
                                             </div>
                                         </div>"""

values_tab_new = """                                         <div class="tab-pane fade" id="pills-item-three" role="tabpanel" aria-labelledby="pills-item-three-tab" tabindex="0">
                                             <div class="rs-about-tab-content">
                                                  <p>We believe that marks are important, but character is even more important. Along with classroom learning, we teach children discipline, respect, kindness, honesty, gratitude, cleanliness, responsibility, and teamwork. A well-educated child should not only know the right answer. The child should also know the right way to behave. That is the kind of education we believe in.</p>
                                             </div>
                                         </div>"""

content = content.replace(mission_tab_old, mission_tab_new)
content = content.replace(vision_tab_old, vision_tab_new)
content = content.replace(values_tab_old, values_tab_new)

# Accordion 1 (Mission) body
acc_mission_old = """                                                        <div class="accordion-body">
                                                             Our mission is to nurture curious minds, build strong values, and inspire young learners to become confident, compassionate, and future-ready individuals. We strive to provide a balanced education combining academic excellence, life skills, technology, innovation, sports, and character development.
                                                         </div>"""

acc_mission_new = """                                                        <div class="accordion-body">
                                                             Our mission is to provide quality education with strong values, modern learning methods, and holistic development. We aim to: build a strong academic foundation; develop good manners, discipline, and moral values; encourage creativity, curiosity, and confidence; promote communication, teamwork, and leadership skills; and help every child discover their strengths and grow with purpose.
                                                         </div>"""

# Accordion 2 (Vision) body
acc_vision_old = """                                                        <div class="accordion-body">
                                                             To inspire children to dream big, think independently, and grow into responsible global citizens who contribute positively to society.
                                                         </div>"""

acc_vision_new = """                                                        <div class="accordion-body">
                                                             To nurture young learners into confident, responsible, value-driven, and future-ready individuals who can contribute positively to society.
                                                         </div>"""

# Accordion 3 (Values) body
acc_values_old = """                                                        <div class="accordion-body">
                                                             We value discipline, integrity, respect, gratitude, and a spirit of service. We are committed to the holistic development of every child—intellectual, physical, emotional, social, and spiritual.
                                                         </div>"""

acc_values_new = """                                                        <div class="accordion-body">
                                                             We believe that marks are important, but character is even more important. Along with classroom learning, we teach children discipline, respect, kindness, honesty, gratitude, cleanliness, responsibility, and teamwork. A well-educated child should not only know the right answer. The child should also know the right way to behave. That is the kind of education we believe in.
                                                         </div>"""

content = content.replace(acc_mission_old, acc_mission_new)
content = content.replace(acc_vision_old, acc_vision_new)
content = content.replace(acc_values_old, acc_values_new)


# About list (Academic details)
list_item1_old = "<p>CBSE Curriculum</p>"
list_item1_new = "<p>CBSE-Oriented Approach</p>"

list_item2_old = "<p>Activity-Based Learning</p>"
list_item2_new = "<p>Activity-Based & Experiential Learning</p>"

list_item3_old = "<p>Experiential Learning</p>"
list_item3_new = "<p>Phonics & Language Development</p>"

list_item4_old = "<p>Robotics, Financial Literacy, Phonics, Library, Sports, Arts</p>"
list_item4_new = "<p>Robotics, Financial Literacy, Sports & Arts</p>"

content = content.replace(list_item1_old, list_item1_new)
content = content.replace(list_item2_old, list_item2_new)
content = content.replace(list_item3_old, list_item3_new)
content = content.replace(list_item4_old, list_item4_new)


# 4. Curriculum Highlights (Faculty area, lines 1117-1288)
title_fac_old = '<h2 class="section-title rs-split-text-enable split-in-left">Academic Curriculum</h2>'
title_fac_new = '<h2 class="section-title rs-split-text-enable split-in-left">Curriculum Highlights</h2>'

desc_fac_old = '<p class="section-desc">Our curriculum integrates critical thinking, communication, collaboration, creativity, technology, life skills, physical education, and value-based learning to develop future-ready individuals.</p>'
desc_fac_new = '<p class="section-desc">Our curriculum is designed to support the holistic development of every child, blending scholastic and co-scholastic learning for a strong personal foundation.</p>'

item1_fac_old = 'LLB in Criminal Justice'
item1_fac_new = 'CBSE-Oriented Academics'

item2_fac_old = 'LLB in International Law'
item2_fac_new = 'Activity-Based Learning'

item3_fac_old = 'Bachelor of Public Health'
item3_fac_new = 'Robotics & Technology'

item4_fac_old = 'M.Sc. in Mathematics'
item4_fac_new = 'Moral & Life Skills'

content = content.replace(title_fac_old, title_fac_new)
content = content.replace(desc_fac_old, desc_fac_new)
content = content.replace(item1_fac_old, item1_fac_new)
content = content.replace(item2_fac_old, item2_fac_new)
content = content.replace(item3_fac_old, item3_fac_new)
content = content.replace(item4_fac_old, item4_fac_new)


# 5. notices Section (Lines 1289-1497)
notice_sec_old = 'Dnyanda English Medium School Life'
notice_sec_new = "Principal's Message"

notice_item2_old = 'Holistic development — intellectual, physical, emotional, social, and spiritual — is at the heart of our school.'
notice_item2_new = 'Holistic development — intellectual, physical, emotional, social, and moral growth — is at the heart of our school.'

content = content.replace(notice_sec_old, notice_sec_new)
content = content.replace(notice_item2_old, notice_item2_new)


# 6. Testimonial Section (Lines 1664-1814)
test_subtitle_old = '<p class="section-desc">Enroll now to begin your transformative academic journey with us.</p>'
test_subtitle_new = '<p class="section-desc">Read what parents say about their experience with Dnyanda English Medium School.</p>'

content = content.replace(test_subtitle_old, test_subtitle_new)

# Testimonial 1
t1_name_old = '<h5 class="rs-testimonial-avater-title">Abdur Rashid</h5>'
t1_name_new = '<h5 class="rs-testimonial-avater-title">Nisha Patil</h5>'
t1_des_old = '<span class="rs-testimonial-avater-designation">Founder & CEO</span>'
t1_des_new = '<span class="rs-testimonial-avater-designation">Mother of Grade 3 Student</span>'
t1_text_old = 'Outstanding support and expertise! Our startup achieved significant growth thanks to their guidance. Truly professional.'
t1_text_new = 'Dnyanda school provides a safe and very caring environment. My child loves going to school every day. The activity-based learning approach has helped a lot with concept clarity.'

content = content.replace(t1_name_old, t1_name_new)
content = content.replace(t1_des_old, t1_des_new)
content = content.replace(t1_text_old, t1_text_new)

# Testimonial 2
t2_name_old = '<h5 class="rs-testimonial-avater-title">Ronald Richards</h5>'
t2_name_new = '<h5 class="rs-testimonial-avater-title">Rahul Kulkarni</h5>'
t2_des_old = '<span class="rs-testimonial-avater-designation">Project Manager</span>'
t2_des_new = '<span class="rs-testimonial-avater-designation">Father of Grade 5 Student</span>'
t2_text_old = 'Exceptional service from start to finish. They understood our needs, delivered on time, and exceeded expectations. Highly recommend!'
t2_text_new = "We chose Dnyanda English Medium School for its focus on values and discipline along with academics. The robotics and financial literacy exposure is a great addition for future-ready kids."

content = content.replace(t2_name_old, t2_name_new)
content = content.replace(t2_des_old, t2_des_new)
content = content.replace(t2_text_old, t2_text_new)

# Testimonial 3
t3_name_old = '<h5 class="rs-testimonial-avater-title">Leslie Alexander</h5>'
t3_name_new = '<h5 class="rs-testimonial-avater-title">Deepa Shinde</h5>'
t3_des_old = '<span class="rs-testimonial-avater-designation">President of Sales</span>'
t3_des_new = '<span class="rs-testimonial-avater-designation">Mother of Grade 1 Student</span>'
t3_text_old = 'We believe that every business is uniquids our approach never one size fits all. We tailor our strategies to fit your goals is and industry.'
t3_text_new = "The personal attention given to every child is commendable. Phonics classes have built immense confidence in my daughter's English reading and spoken communication."

content = content.replace(t3_name_old, t3_name_new)
content = content.replace(t3_des_old, t3_des_new)
content = content.replace(t3_text_old, t3_text_new)

# Testimonial 4
t4_name_old = '<h5 class="rs-testimonial-avater-title">Marry Holder</h5>'
t4_name_new = '<h5 class="rs-testimonial-avater-title">Suresh Deshmukh</h5>'
t4_des_old = '<span class="rs-testimonial-avater-designation">HR Manager</span>'
t4_des_new = '<span class="rs-testimonial-avater-designation">Father of Grade 4 Student</span>'
t4_text_old = 'Professional, knowledgeable, and responsive. Their solutions transformed our operations, making our workflows seamless.'
t4_text_new = 'A perfect blend of academic excellence and co-scholastic activities like sports, music, and arts. The teachers are very supportive and encourage creativity.'

content = content.replace(t4_name_old, t4_name_new)
content = content.replace(t4_des_old, t4_des_new)
content = content.replace(t4_text_old, t4_text_new)


# 7. Admissions Section
adm_title_old = '<h2 class="section-title rs-split-text-enable split-in-left mb-15">Admissions Open Now\n                                     </h2>'
adm_title_new = '<h2 class="section-title rs-split-text-enable split-in-left mb-15">Admissions Open for Grade 1 to Grade 5\n                                     </h2>'

adm_desc_old = '<p class="rs-section-desc">Enroll now to begin your transformative academic journey with us.\n                                     </p>'
adm_desc_new = '<p class="rs-section-desc">Give your child the right start with Dnyanda English Medium School. Let your child learn, grow, explore, and shine in a school where every child matters. Enroll today and take the first step toward a brighter future.\n                                     </p>'

adm_btn_old = 'Send Massage'
adm_btn_new = 'Submit Application'

content = content.replace(adm_title_old, adm_title_new)
content = content.replace(adm_desc_old, adm_desc_new)
content = content.replace(adm_btn_old, adm_btn_new)


# Save changes in BOM-free UTF-8
with open(path, "w", encoding="utf-8", newline="\n") as f:
    f.write(content)

print("Home page (index.html) successfully updated!")
