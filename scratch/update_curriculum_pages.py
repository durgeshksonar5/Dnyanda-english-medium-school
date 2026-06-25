import os

def update_file(filename, asset_prefix):
    filepath = os.path.join("e:/Durgesh work/dnyanda school", filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
        
    print(f"Updating {filename}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Breadcrumb / Title Updates
    breadcrumb_old_title = '<h1 class="rs-breadcrumb-title">All Programs</h1>'
    breadcrumb_new_title = '<h1 class="rs-breadcrumb-title">School Curriculum</h1>'
    
    breadcrumb_old_desc = '<p class="rs-breadcrumb-desc">Education goes beyond textbooks and classrooms. We believe in empowering students to explore their passions challenge conventions.</p>'
    breadcrumb_new_desc = '<p class="rs-breadcrumb-desc">Our curriculum is thoughtfully designed to support the holistic development of every child. We follow a balanced learning approach combining scholastic and co-scholastic experiences.</p>'

    content = content.replace(breadcrumb_old_title, breadcrumb_new_title)
    content = content.replace(breadcrumb_old_desc, breadcrumb_new_desc)
    
    # Also page title:
    if filename == "service.html":
        content = content.replace("<title>Services - Dnyanda English Medium School</title>", "<title>Curriculum - Dnyanda English Medium School</title>")
    else:
        content = content.replace("<title>Service Details - Dnyanda English Medium School</title>", "<title>Curriculum Details - Dnyanda English Medium School</title>")

    # 2. Sidebar Filters
    # Faculties -> Learning Areas
    content = content.replace('<h6 class="filter-title">Faculties</h6>', '<h6 class="filter-title">Learning Areas</h6>')
    content = content.replace('<label for="faculty-education">Faculty of Education</label>', '<label for="faculty-education">Scholastic (Core Academics)</label>')
    content = content.replace('<label for="faculty-law">Faculty of Law</label>', '<label for="faculty-law">Co-Scholastic (Arts & Sports)</label>')
    content = content.replace('<label for="faculty-it">IT Faculty</label>', '<label for="faculty-it">Future Skills (Tech & Literacy)</label>')
    # Hide other faculties options to keep it tidy
    content = content.replace('<div class="filter-option">\n                                    <input type="checkbox" id="faculty-health" name="faculty" value="health">\n                                    <label for="faculty-health">Faculty of Health Sciences</label>\n                                </div>', '')
    content = content.replace('<div class="filter-option">\n                                    <input type="checkbox" id="faculty-social" name="faculty" value="social">\n                                    <label for="faculty-social">Faculty of Social Sciences</label>\n                                </div>', '')
    content = content.replace('<button type="button" class="show-more-btn">Show More</button>', '')

    # Departments -> Grade Levels
    content = content.replace('<h6 class="filter-title">Departments</h6>', '<h6 class="filter-title">Grade Levels</h6>')
    content = content.replace('<label for="dept-curriculum">Department of Curriculum & Instruction</label>', '<label for="dept-curriculum">Grade 1</label>')
    content = content.replace('<label for="dept-leadership">Department of Educational Leadership</label>', '<label for="dept-leadership">Grade 2</label>')
    content = content.replace('<label for="dept-criminal">Department of Criminal Justice</label>', '<label for="dept-criminal">Grade 3</label>')
    content = content.replace('<label for="dept-international">Department of International Law</label>', '<label for="dept-international">Grade 4</label>')
    content = content.replace('<label for="dept-data">Department of Data Science</label>', '<label for="dept-data">Grade 5</label>')

    # Program Level -> Focus Areas
    content = content.replace('<h6 class="filter-title">Program Level</h6>', '<h6 class="filter-title">Focus Areas</h6>')
    content = content.replace('<label for="level-graduate">Graduate</label>', '<label for="level-graduate">Concept Clarity</label>')
    content = content.replace('<label for="level-phd">PhD</label>', '<label for="level-phd">Activity-Based</label>')
    content = content.replace('<label for="level-undergraduate">Undergraduate</label>', '<label for="level-undergraduate">Experiential</label>')

    # 3. Total Results Count
    content = content.replace('<span class="rs-result-count">28</span>', '<span class="rs-result-count">8</span>')

    # 4. Program Items replacement
    # We replace from the start of the rs-program-item-wrapper to its end.
    start_wrapper = content.find('<div class="rs-program-item-wrapper">')
    end_wrapper = content.find('</div>\n                            <div class="row">', start_wrapper) # ends wrapper
    
    if start_wrapper != -1 and end_wrapper != -1:
        print(f"  Found program item wrapper in {filename}")
        
        cards_html = f"""<div class="rs-program-item-wrapper">
                                <div class="rs-program-item">
                                    <div class="rs-program-content">
                                        <h5 class="rs-program-title"><a href="javascript:void(0)">Phonics</a></h5>
                                        <div class="rs-program-tag-wrapper">
                                            <span class="rs-program-tag">Scholastic</span>
                                            <span class="rs-program-tag">Grade 1 to 5</span>
                                        </div>
                                        <p class="rs-program-desc">
                                            Focuses on language foundation, pronunciation, and early reading confidence through structured phonics learning.
                                        </p>
                                        <div class="rs-program-btn">
                                            <a class="rs-btn has-icon has-text is-text-blue" href="about.html">
                                                <span class="btn-text-wrap">
                                       <span class="text-default">Read More</span>
                                                <span class="text-hover">Read More</span>
                                                </span>
                                                <span class="icon-box has-rotate">
                                       <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 15">
                                          <path
                                             d="M10.5 7.5C10.5 8.32843 9.82843 9 9 9C8.17157 9 7.5 8.32843 7.5 7.5C7.5 6.67157 8.17157 6 9 6C9.82843 6 10.5 6.67157 10.5 7.5Z">
                                          </path>
                                          <path
                                             d="M10.5 13.5C10.5 14.3284 9.82843 15 9 15C8.17157 15 7.5 14.3284 7.5 13.5C7.5 12.6716 8.17157 12 9 12C9.82843 12 10.5 12.6716 10.5 13.5Z">
                                          </path>
                                          <path
                                             d="M3 7.5C3 8.32843 2.32843 9 1.5 9C0.671573 9 0 8.32843 0 7.5C0 6.67157 0.671573 6 1.5 6C2.32843 6 3 6.67157 3 7.5Z">
                                          </path>
                                          <path
                                             d="M18 7.5C18 8.32843 17.3284 9 16.5 9C15.6716 9 15 8.32843 15 7.5C15 6.67157 15.6716 6 16.5 6C17.3284 6 18 6.67157 18 7.5Z">
                                          </path>
                                          <path
                                             d="M10.5 1.5C10.5 2.32843 9.82843 3 9 3C8.17157 3 7.5 2.32843 7.5 1.5C7.5 0.671573 8.17157 0 9 0C9.82843 0 10.5 0.671573 10.5 1.5Z">
                                          </path>
                                       </svg>
                                    </span>
                                            </a>
                                        </div>
                                    </div>
                                    <div class="rs-program-thumb">
                                        <a href="javascript:void(0)"><img src="{asset_prefix}assets/images/program/program-thumb-05.webp" alt="image"></a>
                                    </div>
                                </div>
                                <div class="rs-program-item">
                                    <div class="rs-program-content">
                                        <h5 class="rs-program-title"><a href="javascript:void(0)">Robotics</a></h5>
                                        <div class="rs-program-tag-wrapper">
                                            <span class="rs-program-tag">Future Skills</span>
                                            <span class="rs-program-tag">Grade 1 to 5</span>
                                        </div>
                                        <p class="rs-program-desc">
                                            Introduces technology, logical thinking, and basic coding in a hands-on, age-appropriate, and engaging way.
                                        </p>
                                        <div class="rs-program-btn">
                                            <a class="rs-btn has-icon has-text is-text-blue" href="about.html">
                                                <span class="btn-text-wrap">
                                       <span class="text-default">Read More</span>
                                                <span class="text-hover">Read More</span>
                                                </span>
                                                <span class="icon-box has-rotate">
                                       <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 15">
                                          <path
                                             d="M10.5 7.5C10.5 8.32843 9.82843 9 9 9C8.17157 9 7.5 8.32843 7.5 7.5C7.5 6.67157 8.17157 6 9 6C9.82843 6 10.5 6.67157 10.5 7.5Z">
                                          </path>
                                          <path
                                             d="M10.5 13.5C10.5 14.3284 9.82843 15 9 15C8.17157 15 7.5 14.3284 7.5 13.5C7.5 12.6716 8.17157 12 9 12C9.82843 12 10.5 12.6716 10.5 13.5Z">
                                          </path>
                                          <path
                                             d="M3 7.5C3 8.32843 2.32843 9 1.5 9C0.671573 9 0 8.32843 0 7.5C0 6.67157 0.671573 6 1.5 6C2.32843 6 3 6.67157 3 7.5Z">
                                          </path>
                                          <path
                                             d="M18 7.5C18 8.32843 17.3284 9 16.5 9C15.6716 9 15 8.32843 15 7.5C15 6.67157 15.6716 6 16.5 6C17.3284 6 18 6.67157 18 7.5Z">
                                          </path>
                                          <path
                                             d="M10.5 1.5C10.5 2.32843 9.82843 3 9 3C8.17157 3 7.5 2.32843 7.5 1.5C7.5 0.671573 8.17157 0 9 0C9.82843 0 10.5 0.671573 10.5 1.5Z">
                                          </path>
                                       </svg>
                                    </span>
                                            </a>
                                        </div>
                                    </div>
                                    <div class="rs-program-thumb">
                                        <a href="javascript:void(0)"><img src="{asset_prefix}assets/images/program/program-thumb-06.webp" alt="image"></a>
                                    </div>
                                </div>
                                <div class="rs-program-item">
                                    <div class="rs-program-content">
                                        <h5 class="rs-program-title"><a href="javascript:void(0)">Financial Literacy</a></h5>
                                        <div class="rs-program-tag-wrapper">
                                            <span class="rs-program-tag">Future Skills</span>
                                            <span class="rs-program-tag">Grade 1 to 5</span>
                                        </div>
                                        <p class="rs-program-desc">
                                            Builds a strong foundation in smart money habits, saving concepts, and basic financial awareness for life.
                                        </p>
                                        <div class="rs-program-btn">
                                            <a class="rs-btn has-icon has-text is-text-blue" href="about.html">
                                                <span class="btn-text-wrap">
                                       <span class="text-default">Read More</span>
                                                <span class="text-hover">Read More</span>
                                                </span>
                                                <span class="icon-box has-rotate">
                                       <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 15">
                                          <path
                                             d="M10.5 7.5C10.5 8.32843 9.82843 9 9 9C8.17157 9 7.5 8.32843 7.5 7.5C7.5 6.67157 8.17157 6 9 6C9.82843 6 10.5 6.67157 10.5 7.5Z">
                                          </path>
                                          <path
                                             d="M10.5 13.5C10.5 14.3284 9.82843 15 9 15C8.17157 15 7.5 14.3284 7.5 13.5C7.5 12.6716 8.17157 12 9 12C9.82843 12 10.5 12.6716 10.5 13.5Z">
                                          </path>
                                          <path
                                             d="M3 7.5C3 8.32843 2.32843 9 1.5 9C0.671573 9 0 8.32843 0 7.5C0 6.67157 0.671573 6 1.5 6C2.32843 6 3 6.67157 3 7.5Z">
                                          </path>
                                          <path
                                             d="M18 7.5C18 8.32843 17.3284 9 16.5 9C15.6716 9 15 8.32843 15 7.5C15 6.67157 15.6716 6 16.5 6C17.3284 6 18 6.67157 18 7.5Z">
                                          </path>
                                          <path
                                             d="M10.5 1.5C10.5 2.32843 9.82843 3 9 3C8.17157 3 7.5 2.32843 7.5 1.5C7.5 0.671573 8.17157 0 9 0C9.82843 0 10.5 0.671573 10.5 1.5Z">
                                          </path>
                                       </svg>
                                    </span>
                                            </a>
                                        </div>
                                    </div>
                                    <div class="rs-program-thumb">
                                        <a href="javascript:void(0)"><img src="{asset_prefix}assets/images/program/program-thumb-07.webp" alt="image"></a>
                                    </div>
                                </div>
                                <div class="rs-program-item">
                                    <div class="rs-program-content">
                                        <h5 class="rs-program-title"><a href="javascript:void(0)">Library Reading</a></h5>
                                        <div class="rs-program-tag-wrapper">
                                            <span class="rs-program-tag">Scholastic</span>
                                            <span class="rs-program-tag">Grade 1 to 5</span>
                                        </div>
                                        <p class="rs-program-desc">
                                            Nurtures curious minds, vocabulary expansion, and a lifelong love for books through structured reading sessions.
                                        </p>
                                        <div class="rs-program-btn">
                                            <a class="rs-btn has-icon has-text is-text-blue" href="about.html">
                                                <span class="btn-text-wrap">
                                       <span class="text-default">Read More</span>
                                                <span class="text-hover">Read More</span>
                                                </span>
                                                <span class="icon-box has-rotate">
                                       <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 15">
                                          <path
                                             d="M10.5 7.5C10.5 8.32843 9.82843 9 9 9C8.17157 9 7.5 8.32843 7.5 7.5C7.5 6.67157 8.17157 6 9 6C9.82843 6 10.5 6.67157 10.5 7.5Z">
                                          </path>
                                          <path
                                             d="M10.5 13.5C10.5 14.3284 9.82843 15 9 15C8.17157 15 7.5 14.3284 7.5 13.5C7.5 12.6716 8.17157 12 9 12C9.82843 12 10.5 12.6716 10.5 13.5Z">
                                          </path>
                                          <path
                                             d="M3 7.5C3 8.32843 2.32843 9 1.5 9C0.671573 9 0 8.32843 0 7.5C0 6.67157 0.671573 6 1.5 6C2.32843 6 3 6.67157 3 7.5Z">
                                          </path>
                                          <path
                                             d="M18 7.5C18 8.32843 17.3284 9 16.5 9C15.6716 9 15 8.32843 15 7.5C15 6.67157 15.6716 6 16.5 6C17.3284 6 18 6.67157 18 7.5Z">
                                          </path>
                                          <path
                                             d="M10.5 1.5C10.5 2.32843 9.82843 3 9 3C8.17157 3 7.5 2.32843 7.5 1.5C7.5 0.671573 8.17157 0 9 0C9.82843 0 10.5 0.671573 10.5 1.5Z">
                                          </path>
                                       </svg>
                                    </span>
                                            </a>
                                        </div>
                                    </div>
                                    <div class="rs-program-thumb">
                                        <a href="javascript:void(0)"><img src="{asset_prefix}assets/images/program/program-thumb-08.webp" alt="image"></a>
                                    </div>
                                </div>
                                <div class="rs-program-item">
                                    <div class="rs-program-content">
                                        <h5 class="rs-program-title"><a href="javascript:void(0)">Sports & Physical Education</a></h5>
                                        <div class="rs-program-tag-wrapper">
                                            <span class="rs-program-tag">Co-Scholastic</span>
                                            <span class="rs-program-tag">Grade 1 to 5</span>
                                        </div>
                                        <p class="rs-program-desc">
                                            Promotes physical fitness, teamwork, discipline, self-expression, and general health through sports and games.
                                        </p>
                                        <div class="rs-program-btn">
                                            <a class="rs-btn has-icon has-text is-text-blue" href="about.html">
                                                <span class="btn-text-wrap">
                                       <span class="text-default">Read More</span>
                                                <span class="text-hover">Read More</span>
                                                </span>
                                                <span class="icon-box has-rotate">
                                       <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 15">
                                          <path
                                             d="M10.5 7.5C10.5 8.32843 9.82843 9 9 9C8.17157 9 7.5 8.32843 7.5 7.5C7.5 6.67157 8.17157 6 9 6C9.82843 6 10.5 6.67157 10.5 7.5Z">
                                          </path>
                                          <path
                                             d="M10.5 13.5C10.5 14.3284 9.82843 15 9 15C8.17157 15 7.5 14.3284 7.5 13.5C7.5 12.6716 8.17157 12 9 12C9.82843 12 10.5 12.6716 10.5 13.5Z">
                                          </path>
                                          <path
                                             d="M3 7.5C3 8.32843 2.32843 9 1.5 9C0.671573 9 0 8.32843 0 7.5C0 6.67157 0.671573 6 1.5 6C2.32843 6 3 6.67157 3 7.5Z">
                                          </path>
                                          <path
                                             d="M18 7.5C18 8.32843 17.3284 9 16.5 9C15.6716 9 15 8.32843 15 7.5C15 6.67157 15.6716 6 16.5 6C17.3284 6 18 6.67157 18 7.5Z">
                                          </path>
                                          <path
                                             d="M10.5 1.5C10.5 2.32843 9.82843 3 9 3C8.17157 3 7.5 2.32843 7.5 1.5C7.5 0.671573 8.17157 0 9 0C9.82843 0 10.5 0.671573 10.5 1.5Z">
                                          </path>
                                       </svg>
                                    </span>
                                            </a>
                                        </div>
                                    </div>
                                    <div class="rs-program-thumb">
                                        <a href="javascript:void(0)"><img src="{asset_prefix}assets/images/program/program-thumb-02.webp" alt="image"></a>
                                    </div>
                                </div>
                                <div class="rs-program-item">
                                    <div class="rs-program-content">
                                        <h5 class="rs-program-title"><a href="javascript:void(0)">Arts & Creative Activities</a></h5>
                                        <div class="rs-program-tag-wrapper">
                                            <span class="rs-program-tag">Co-Scholastic</span>
                                            <span class="rs-program-tag">Grade 1 to 5</span>
                                        </div>
                                        <p class="rs-program-desc">
                                            Encourages drawing, craft, dance, music, self-expression, and creative thinking among students.
                                        </p>
                                        <div class="rs-program-btn">
                                            <a class="rs-btn has-icon has-text is-text-blue" href="about.html">
                                                <span class="btn-text-wrap">
                                       <span class="text-default">Read More</span>
                                                <span class="text-hover">Read More</span>
                                                </span>
                                                <span class="icon-box has-rotate">
                                       <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 15">
                                          <path
                                             d="M10.5 7.5C10.5 8.32843 9.82843 9 9 9C8.17157 9 7.5 8.32843 7.5 7.5C7.5 6.67157 8.17157 6 9 6C9.82843 6 10.5 6.67157 10.5 7.5Z">
                                          </path>
                                          <path
                                             d="M10.5 13.5C10.5 14.3284 9.82843 15 9 15C8.17157 15 7.5 14.3284 7.5 13.5C7.5 12.6716 8.17157 12 9 12C9.82843 12 10.5 12.6716 10.5 13.5Z">
                                          </path>
                                          <path
                                             d="M3 7.5C3 8.32843 2.32843 9 1.5 9C0.671573 9 0 8.32843 0 7.5C0 6.67157 0.671573 6 1.5 6C2.32843 6 3 6.67157 3 7.5Z">
                                          </path>
                                          <path
                                             d="M18 7.5C18 8.32843 17.3284 9 16.5 9C15.6716 9 15 8.32843 15 7.5C15 6.67157 15.6716 6 16.5 6C17.3284 6 18 6.67157 18 7.5Z">
                                          </path>
                                          <path
                                             d="M10.5 1.5C10.5 2.32843 9.82843 3 9 3C8.17157 3 7.5 2.32843 7.5 1.5C7.5 0.671573 8.17157 0 9 0C9.82843 0 10.5 0.671573 10.5 1.5Z">
                                          </path>
                                       </svg>
                                    </span>
                                            </a>
                                        </div>
                                    </div>
                                    <div class="rs-program-thumb">
                                        <a href="javascript:void(0)"><img src="{asset_prefix}assets/images/program/program-thumb-04.webp" alt="image"></a>
                                    </div>
                                </div>
                                <div class="rs-program-item">
                                    <div class="rs-program-content">
                                        <h5 class="rs-program-title"><a href="javascript:void(0)">Moral & Value-Based Education</a></h5>
                                        <div class="rs-program-tag-wrapper">
                                            <span class="rs-program-tag">Scholastic</span>
                                            <span class="rs-program-tag">Grade 1 to 5</span>
                                        </div>
                                        <p class="rs-program-desc">
                                            Develops good manners, respect, gratitude, kindness, honesty, and responsible citizenship from the early years.
                                        </p>
                                        <div class="rs-program-btn">
                                            <a class="rs-btn has-icon has-text is-text-blue" href="about.html">
                                                <span class="btn-text-wrap">
                                       <span class="text-default">Read More</span>
                                                <span class="text-hover">Read More</span>
                                                </span>
                                                <span class="icon-box has-rotate">
                                       <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 15">
                                          <path
                                             d="M10.5 7.5C10.5 8.32843 9.82843 9 9 9C8.17157 9 7.5 8.32843 7.5 7.5C7.5 6.67157 8.17157 6 9 6C9.82843 6 10.5 6.67157 10.5 7.5Z">
                                          </path>
                                          <path
                                             d="M10.5 13.5C10.5 14.3284 9.82843 15 9 15C8.17157 15 7.5 14.3284 7.5 13.5C7.5 12.6716 8.17157 12 9 12C9.82843 12 10.5 12.6716 10.5 13.5Z">
                                          </path>
                                          <path
                                             d="M3 7.5C3 8.32843 2.32843 9 1.5 9C0.671573 9 0 8.32843 0 7.5C0 6.67157 0.671573 6 1.5 6C2.32843 6 3 6.67157 3 7.5Z">
                                          </path>
                                          <path
                                             d="M18 7.5C18 8.32843 17.3284 9 16.5 9C15.6716 9 15 8.32843 15 7.5C15 6.67157 15.6716 6 16.5 6C17.3284 6 18 6.67157 18 7.5Z">
                                          </path>
                                          <path
                                             d="M10.5 1.5C10.5 2.32843 9.82843 3 9 3C8.17157 3 7.5 2.32843 7.5 1.5C7.5 0.671573 8.17157 0 9 0C9.82843 0 10.5 0.671573 10.5 1.5Z">
                                          </path>
                                       </svg>
                                    </span>
                                            </a>
                                        </div>
                                    </div>
                                    <div class="rs-program-thumb">
                                        <a href="javascript:void(0)"><img src="{asset_prefix}assets/images/program/program-thumb-05.webp" alt="image"></a>
                                    </div>
                                </div>
                                <div class="rs-program-item">
                                    <div class="rs-program-content">
                                        <h5 class="rs-program-title"><a href="javascript:void(0)">Life Skills & Personality Development</a></h5>
                                        <div class="rs-program-tag-wrapper">
                                            <span class="rs-program-tag">Co-Scholastic</span>
                                            <span class="rs-program-tag">Grade 1 to 5</span>
                                        </div>
                                        <p class="rs-program-desc">
                                            Builds communication, confidence, leadership, self-discipline, teamwork, and positive attitudes for life.
                                        </p>
                                        <div class="rs-program-btn">
                                            <a class="rs-btn has-icon has-text is-text-blue" href="about.html">
                                                <span class="btn-text-wrap">
                                       <span class="text-default">Read More</span>
                                                <span class="text-hover">Read More</span>
                                                </span>
                                                <span class="icon-box has-rotate">
                                       <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 15">
                                          <path
                                             d="M10.5 7.5C10.5 8.32843 9.82843 9 9 9C8.17157 9 7.5 8.32843 7.5 7.5C7.5 6.67157 8.17157 6 9 6C9.82843 6 10.5 6.67157 10.5 7.5Z">
                                          </path>
                                          <path
                                             d="M10.5 13.5C10.5 14.3284 9.82843 15 9 15C8.17157 15 7.5 14.3284 7.5 13.5C7.5 12.6716 8.17157 12 9 12C9.82843 12 10.5 12.6716 10.5 13.5Z">
                                          </path>
                                          <path
                                             d="M3 7.5C3 8.32843 2.32843 9 1.5 9C0.671573 9 0 8.32843 0 7.5C0 6.67157 0.671573 6 1.5 6C2.32843 6 3 6.67157 3 7.5Z">
                                          </path>
                                          <path
                                             d="M18 7.5C18 8.32843 17.3284 9 16.5 9C15.6716 9 15 8.32843 15 7.5C15 6.67157 15.6716 6 16.5 6C17.3284 6 18 6.67157 18 7.5Z">
                                          </path>
                                          <path
                                             d="M10.5 1.5C10.5 2.32843 9.82843 3 9 3C8.17157 3 7.5 2.32843 7.5 1.5C7.5 0.671573 8.17157 0 9 0C9.82843 0 10.5 0.671573 10.5 1.5Z">
                                          </path>
                                       </svg>
                                    </span>
                                            </a>
                                        </div>
                                    </div>
                                    <div class="rs-program-thumb">
                                        <a href="javascript:void(0)"><img src="{asset_prefix}assets/images/program/program-thumb-06.webp" alt="image"></a>
                                    </div>
                                </div>
                            """
        
        # Replace the wrapper HTML block
        content = content[:start_wrapper] + cards_html + content[end_wrapper:]
        print(f"  Replaced cards HTML in {filename}")
        
        # Also remove Load More button
        load_more_start = content.find('<div class="row">\n                                <div class="col-xl-12">\n                                    <div class="rs-load-more-btn')
        if load_more_start != -1:
            load_more_end = content.find('</div>\n                                </div>\n                            </div>', load_more_start)
            if load_more_end != -1:
                content = content[:load_more_start] + content[load_more_end + len('</div>\n                                </div>\n                            </div>'):]
                print(f"  Removed Load More button in {filename}")

    # Write BOM-free UTF-8 file
    with open(filepath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"  Successfully updated and saved {filename}")

update_file("service.html", "")
update_file("service/service-single.html", "../")
