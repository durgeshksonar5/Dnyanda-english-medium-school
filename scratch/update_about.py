path = "e:/Durgesh work/dnyanda school/about.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

print("Updating about.html...")

# 1. Main About Us Paragraphs
about_h2 = '<h2 class="section-title has-theme-blue mb-20">About Dnyanda English Medium School</h2>'
about_h2_new = '<h2 class="section-title has-theme-blue mb-20">About Our School</h2>'

old_desc1 = """At Dnyanda English Medium School, education goes beyond textbooks and classrooms We believe in empowering students to explore their passions challenge conventions and discover their potential through meaningful experiences Our distinguished faculty
                                members are leaders their respective fields dedicated to delivering world-class education that integrates theory with practical support application With cutting-edge facilities modern laboratories and a vibrant learning
                                environment we ensure that every student has the tools and support to excel academically and personally."""

new_desc1 = """Dnyanda English Medium School is a primary school dedicated to nurturing confident, creative, and compassionate learners. We understand that every child is unique. Some children learn through reading, some through activities, some through questions, and some through hands-on experiences. That is why our teaching approach goes beyond textbooks."""

old_desc2 = """Our diverse community welcomes students from across the globe, fostering cultural exchange and mutual understanding Through international collaborations research initiatives, and innovation hubs we provide opportunities for
                                students to engage with global challenges and contribute to sustainable solutions. At the heart of Dnyanda English Medium School lies a commitment to excellence inclusivity gain the skills confidence and perspective to lead in an ever-changing
                                world."""

new_desc2 = """We create a learning environment where children feel safe to ask questions, express ideas, explore talents, and build good habits. Our school focuses on academic excellence, communication skills, discipline, creativity, physical fitness, moral values, and life skills. We prepare students not just for the next class, but for the future."""

content = content.replace(about_h2, about_h2_new)
content = content.replace(old_desc1, new_desc1)
content = content.replace(old_desc2, new_desc2)


# 2. Educational Trust Message (replaces the quote wrapper)
old_quote_block = """                            <div class="rs-quote-wrapper">
                                <div class="rs-quote-icon">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24">
                                        <path d="M0 0V24L12 12V0H0Z"></path>
                                        <path d="M20 0V24L32 12V0H20Z"></path>
                                    </svg>
                                </div>
                                <p class="rs-quote-desc">“Our diverse community welcomes students from across the globe fostering cultural exchange and mutual understanding Through international collaborations research initiatives, and innovation hubs we provide opportunities
                                    for students to engage with global challenges and contribute to sustainable solutions”</p>
                                <h5 class="rs-quote-author">
                                    - Kathryn Murphy
                                </h5>
                            </div>"""

new_quote_block = """                            <div class="rs-quote-wrapper">
                                <div class="rs-quote-icon">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 24">
                                        <path d="M0 0V24L12 12V0H0Z"></path>
                                        <path d="M20 0V24L32 12V0H20Z"></path>
                                    </svg>
                                </div>
                                <h4 style="color: var(--rs-text-blue); font-weight: 700; margin-bottom: 15px;">Welcome to a School Where Every Child Matters</h4>
                                <p class="rs-quote-desc" style="font-size: 16px; line-height: 1.8; color: #4c4c4c; font-style: normal;">
                                    Education is not just about preparing children for examinations; it is about preparing them for life.<br><br>
                                    At Dnyanda English Medium School, we believe that every child is unique, capable, and full of potential. Our mission is to nurture curious minds, build strong values, and inspire young learners to become confident, compassionate, and future-ready individuals.<br><br>
                                    Since 2021, we have been creating an environment where learning goes beyond textbooks—where creativity is encouraged, questions are welcomed, talents are celebrated, and every achievement is valued. We strive to provide a balanced education that combines academic excellence, life skills, technology, innovation, sports, and character development.<br><br>
                                    As we continue our journey of shaping young minds, we remain committed to empowering children with the knowledge, confidence, and values they need to succeed in a rapidly changing world. We invite you to join a learning community where children are encouraged to dream big, think independently, and grow into responsible citizens.<br><br>
                                    <strong>Together, let us build a brighter future — one child at a time.</strong>
                                </p>
                                <h5 class="rs-quote-author" style="margin-top: 20px;">
                                    - Educational Trust
                                </h5>
                            </div>"""

content = content.replace(old_quote_block, new_quote_block)


# 3. Vision and Mission Section
old_vision_block = """                            <h3 class="section-title has-theme-blue mb-15">Our Vision</h3>
                            <p class="section-desc">Our vision is to create a world where education empowers every individual to achieve their fullest potential. We strive to be a leading global institution recognized for academic excellence innovation, and social responsibility
                                Our goal is to nurture creative thinkers ethical leaders and lifelong learners who contribute positively to society Through cutting-edge research inclusive learning environments and global partnerships inspire change and
                                foster sustainable development.</p>"""

new_vision_block = """                            <h3 class="section-title has-theme-blue mb-15">Our Vision</h3>
                            <p class="section-desc" style="margin-bottom: 30px;">To nurture young learners into confident, responsible, value-driven, and future-ready individuals who can contribute positively to society.</p>
                            
                            <h3 class="section-title has-theme-blue mb-15">Our Mission</h3>
                            <p class="section-desc">Our mission is to provide quality education with strong values, modern learning methods, and holistic development. We aim to: build a strong academic foundation; develop good manners, discipline, and moral values; encourage creativity, curiosity, and confidence; promote communication, teamwork, and leadership skills; provide exposure to technology, sports, arts, and life skills; and help every child discover their strengths and grow with purpose.</p>"""

content = content.replace(old_vision_block, new_vision_block)


# 4. Why Choose Us columns (Affordability, Academics, Student Life)
# Item 1
content = content.replace('<h5 class="rs-why-choose-title">Affordability</h5>', '<h5 class="rs-why-choose-title">CBSE-Oriented Academics</h5>')
content = content.replace('<p class="rs-why-choose-desc">Dnyanda English Medium School provides transparent, competitive tuition fees and flexible payment.</p>', 
                          '<p class="rs-why-choose-desc">We offer a balanced, CBSE-oriented learning approach focusing on concept clarity and spoken English confidence.</p>')

# Item 2
# Note: heading was Academics already
content = content.replace('<p class="rs-why-choose-desc">At Dnyanda English Medium School, we offer world-class academic programs expert faculty guidance </p>',
                          '<p class="rs-why-choose-desc">We introduce robotics, financial literacy, and coding to build logical reasoning and future-ready tech skills.</p>')

# Item 3
content = content.replace('<h5 class="rs-why-choose-title">Student Life</h5>', '<h5 class="rs-why-choose-title">Co-Scholastic & Care</h5>')
content = content.replace('<p class="rs-why-choose-desc">Dnyanda English Medium School, student goes beyond academics offering vibrant activities cultural events. </p>',
                          '<p class="rs-why-choose-desc">A caring environment focusing on discipline, sports, physical fitness, drawing, craft, dance, and music.</p>')


# 5. Parent Commitment (replaces "Our Campus Tour" text block)
old_tour_block = """                            <h3 class="section-title has-theme-blue mb-15">Our Campus Tour</h3>
                            <p class="section-desc">Our diverse community welcomes students from across the globe, fostering cultural exchange and mutual understanding Through international collaborations research initiatives, and innovation hubs we provide opportunities for
                                students to engage with global challenges and contribute to sustainable solutions. At the heart of Dnyanda English Medium School.</p>"""

new_tour_block = """                            <h3 class="section-title has-theme-blue mb-15">Our Commitment to Parents</h3>
                            <p class="section-desc">We understand that parents trust us with their most precious responsibility — their child. That is why we are committed to maintaining a transparent, caring, and supportive relationship with parents. We work together with families to support every child’s learning, behavior, confidence, and overall growth. Your child’s progress is not only the school’s responsibility. It is a shared journey between the school, parents, and teachers.</p>"""

content = content.replace(old_tour_block, new_tour_block)


# 6. Principal's Message Section (replaces the Student Feedback swiper)
# We find:
# <h3 class="section-title has-theme-blue mt-30 mb-15">Student Feedback</h3>
# <p class="section-desc">Our vision is to create a world where education empowers every individual to achieve their fullest potential. We strive to be a leading global institution recognized for academic excellence innovation, and social responsibility
#     Our goal.</p>
# <div class="rs-testimonial-three has-bg-white rs-swiper">
#    ...
# </div>

# Let's target the swiper block replacement
import re
slider_pattern = r'<h3 class="section-title has-theme-blue mt-30 mb-15">Student Feedback</h3>.*?<div class="rs-testimonial-three has-bg-white rs-swiper">.*?<!-- about area end -->'
# Wait, let's check if the pattern works. We can find the start of Student Feedback and the end of the div
start_pos = content.find('<h3 class="section-title has-theme-blue mt-30 mb-15">Student Feedback</h3>')
end_pos = content.find('<!-- about area end -->')

if start_pos != -1 and end_pos != -1:
    print(f"  Found Student Feedback block boundaries: {start_pos} to {end_pos}")
    
    # We replace from start_pos up to end_pos
    principal_message_section = """<h3 class="section-title has-theme-blue mt-30 mb-15">Principal’s Message</h3>
                            <h6 class="rs-notice-title text-blue mb-25" style="font-size: 18px; font-weight: 700;">“Educating the Mind, Enriching the Heart, and Empowering the Future.”</h6>
                            <div class="rs-testimonial-item" style="padding: 40px; border-radius: 10px; background-color: var(--rs-bg-white); box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-bottom: 30px;">
                                <p class="section-desc" style="color: #4c4c4c; font-size: 16px; line-height: 1.8; margin-bottom: 20px; font-style: normal;">
                                    Dear Parents,<br><br>
                                    In today’s rapidly changing world, education must go beyond textbooks and examinations. Children need knowledge, but they also need values, confidence, wisdom, discipline, and the skills required for the future.<br><br>
                                    At Dnyanda English Medium School, we are committed to the holistic development of every child. We focus on intellectual, physical, emotional, social, and moral growth.<br><br>
                                    We believe that true education shapes not only successful students but also responsible citizens, compassionate human beings, and future leaders.<br><br>
                                    Inspired by timeless moral and spiritual values, we strive to cultivate discipline, integrity, respect, gratitude, and a spirit of service in our students. Along with academic excellence, we encourage creativity, critical thinking, confidence, and lifelong learning.<br><br>
                                    Our mission is simple yet meaningful: to build strong character, nurture young minds, and prepare children to face the challenges of tomorrow with courage, wisdom, and faith.<br><br>
                                    Together, let us shape a generation that excels in knowledge, stands firm in values, and contributes positively to society.
                                </p>
                                <div class="rs-testimonial-avater-wrapper mt-30">
                                    <div class="rs-testimonial-avater-info">
                                        <h5 class="rs-testimonial-avater-title" style="margin-bottom: 5px;">Principal</h5>
                                        <span class="rs-testimonial-avater-designation">Dnyanda English Medium School</span>
                                    </div>
                                </div>
                            </div>
                            """
    content = content[:start_pos] + principal_message_section + content[end_pos:]
    print("  Replaced Student Feedback testimonials with Principal's Message")
else:
    print("  WARNING: Could not locate Student Feedback block boundaries")

with open(path, "w", encoding="utf-8", newline="\n") as f:
    f.write(content)

print("About page (about.html) successfully updated!")
