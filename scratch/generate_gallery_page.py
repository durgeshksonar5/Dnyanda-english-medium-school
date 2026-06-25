import os
import re

base_path = "e:/Durgesh work/dnyanda school"
admission_path = os.path.join(base_path, "admission.html")
gallery_path = os.path.join(base_path, "gallery.html")

if not os.path.exists(admission_path):
    print("Error: admission.html not found!")
    exit(1)

with open(admission_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Title
html = html.replace("<title>Admission Requirements - Dnyanda English Medium School</title>", 
                    "<title>School Gallery - Dnyanda English Medium School</title>")
html = html.replace("<title>Admission Requirements - Dnyanda English Medium School</title>", 
                    "<title>School Gallery - Dnyanda English Medium School</title>")

# 2. Inject Custom Styles in <head>
custom_styles = """    <style>
        /* Gallery Filter Buttons */
        .portfolio-filter-btn {
            margin-bottom: 40px;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
        }
        .portfolio-filter-btn button {
            background-color: transparent;
            color: #1b1b1b;
            border: 2px solid #e0e0e0;
            padding: 8px 22px;
            font-size: 15px;
            font-weight: 600;
            border-radius: 30px;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .portfolio-filter-btn button:hover,
        .portfolio-filter-btn button.active {
            background-color: var(--rs-theme-red);
            border-color: var(--rs-theme-red);
            color: var(--rs-white);
            box-shadow: 0 4px 15px rgba(223, 7, 15, 0.2);
        }

        /* Gallery Grid Items */
        .rs-gallery-item {
            background: var(--rs-white);
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
            transition: all 0.4s ease;
            height: 100%;
            display: flex;
            flex-direction: column;
            border: 1px solid rgba(0, 0, 0, 0.03);
        }
        .rs-gallery-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        }
        .rs-gallery-thumb {
            position: relative;
            overflow: hidden;
            width: 100%;
            height: 250px;
        }
        .rs-gallery-thumb img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }
        .rs-gallery-item:hover .rs-gallery-thumb img {
            transform: scale(1.08);
        }
        .rs-gallery-overlay {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(223, 7, 15, 0.8);
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: all 0.4s ease;
        }
        .rs-gallery-item:hover .rs-gallery-overlay {
            opacity: 1;
        }
        .rs-gallery-overlay i {
            color: var(--rs-white);
            font-size: 32px;
            background: rgba(255, 255, 255, 0.2);
            width: 60px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            backdrop-filter: blur(5px);
            transform: scale(0.8);
            transition: all 0.4s ease;
        }
        .rs-gallery-item:hover .rs-gallery-overlay i {
            transform: scale(1);
        }
        .rs-gallery-content {
            padding: 20px;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
        }
        .gallery-cat {
            font-size: 13px;
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 1px;
            margin-bottom: 5px;
        }
        .gallery-title {
            font-size: 18px;
            font-weight: 700;
            line-height: 1.4;
            margin: 0;
            color: #1b1b1b;
        }
        .gallery-title a {
            color: inherit;
        }
        .gallery-title a:hover {
            color: var(--rs-theme-red);
        }
    </style>
</head>"""

html = html.replace("</head>", custom_styles)

# 3. Define Gallery Content Block (to replace admission wrapper)
gallery_content = """        <!-- breadcrumb area start -->
        <section class="rs-breadcrumb-area rs-breadcrumb-one p-relative section-space">
            <div class="rs-breadcrumb-bg-thumb include-bg" data-background="assets/school-main.JPG">
            </div>
            <div class="rs-breadcrumb-shape">
                <img src="assets/images/shape/arrow-shape-two.webp" alt="image">
            </div>
            <div class="container-fluid g-0">
                <div class="row">
                    <div class="col-xl-7 col-lg-10">
                        <div class="rs-breadcrumb-wrapper">
                            <div class="rs-breadcrumb-menu">
                                <nav>
                                    <ul>
                                        <li class="rs-breadcumb-item">
                                            <a href="index.html">Home</a>
                                            <span class="rs-breadcrumb-icon">
                                                <svg class="e-font-icon-svg e-fas-angle-double-right" viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg">
                                                    <path d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"></path>
                                                </svg>
                                            </span>
                                        </li>
                                        <li class="rs-breadcumb-item">
                                            School Gallery
                                        </li>
                                    </ul>
                                </nav>
                            </div>
                            <div class="rs-breadcrumb-title-wrapper">
                                <h1 class="rs-breadcrumb-title">School Gallery</h1>
                                <span class="rs-breadcrumb-line"></span>
                            </div>
                            <p class="rs-breadcrumb-desc">Explore the vibrant activities, modern classes, and visual highlights of Dnyanda English Medium School.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- breadcrumb area end -->

        <!-- gallery area start -->
        <section class="rs-gallery-area section-space-top section-space-bottom">
            <div class="container">
                <div class="row align-items-center mb-40">
                    <div class="col-xl-6 col-lg-8">
                        <div class="section-title-wrapper">
                            <span class="section-subtitle has-theme-red is-uppercase">
                                <svg xmlns="http://www.w3.org/2000/svg" width="41" height="41" viewBox="0 0 41 41">
                                   <path d="M11.0523 34.2847V36.1916C11.0386 36.577 11.1671 36.954 11.4132 37.2509C13.7169 39.9512 16.816 40.6162 20.1857 40.6162C23.5554 40.6162 26.6568 39.9512 28.9582 37.2509C29.206 36.9548 29.3352 36.5774 29.3212 36.1916V34.2847C29.3212 32.3305 28.663 30.5636 27.6014 29.2876C26.5668 28.0389 25.1445 27.2659 23.5893 27.2659H16.7842C15.2287 27.2659 13.8067 28.0393 12.7699 29.2876C11.7104 30.5634 11.0523 32.3305 11.0523 34.2847ZM24.2629 15.4167C23.4567 14.6105 22.4295 14.0615 21.3112 13.839C20.193 13.6166 19.0339 13.7307 17.9805 14.1671C16.9271 14.6034 16.0268 15.3423 15.3933 16.2903C14.7599 17.2383 14.4218 18.3529 14.4218 19.493C14.4218 20.6332 14.7599 21.7477 15.3933 22.6958C16.0268 23.6438 16.9271 24.3827 17.9805 24.819C19.0339 25.2553 20.193 25.3695 21.3112 25.147C22.4295 24.9246 23.4567 24.3756 24.2629 23.5693C24.7983 23.0341 25.223 22.3986 25.5128 21.6992C25.8025 20.9997 25.9517 20.2501 25.9517 19.493C25.9517 18.736 25.8025 17.9863 25.5128 17.2869C25.223 16.5875 24.7983 15.952 24.2629 15.4167ZM30.5065 36.9331C32.445 37.1473 34.8477 37.0413 36.6058 36.4417C37.9546 35.9946 39.1535 35.1833 40.0701 34.0976C40.276 33.8504 40.3828 33.5356 40.3699 33.2141V31.5371C40.3699 29.8376 39.7997 28.3005 38.8778 27.1914C37.9807 26.1118 36.7523 25.4423 35.4066 25.4423H29.4289C28.284 25.4423 27.2494 25.9202 26.4289 26.6911C26.4195 26.6997 26.4123 26.7104 26.4079 26.7223C26.4035 26.7342 26.402 26.747 26.4035 26.7596C26.4051 26.7722 26.4096 26.7843 26.4168 26.7948C26.4239 26.8053 26.4335 26.7843 26.4168 26.7948C26.4239 26.8053 26.4335 26.814 26.4447 26.82C29.0142 28.2107 30.5041 31.2242 30.5041 34.2851V36.192C30.5047 36.4087 30.4821 36.6247 30.4365 36.8365C30.434 36.8476 30.434 36.859 30.4363 36.87C30.4385 36.881 30.4431 36.8915 30.4497 36.9006C30.4563 36.9098 30.4648 36.9174 30.4745 36.9231C30.4843 36.9288 30.4951 36.9323 30.5063 36.9335L30.5065 36.9331ZM34.753 15.7909C34.1873 15.2255 33.4667 14.8405 32.6823 14.6845C31.8978 14.5286 31.0848 14.6088 30.3459 14.915C29.607 15.2211 28.9755 15.7395 28.5312 16.4045C28.0868 17.0695 27.8497 17.8514 27.8497 18.6512C27.8497 19.451 28.0868 20.2328 28.5312 20.8978C28.9755 21.5629 29.607 22.0812 30.3459 22.3874C31.0848 22.6935 31.8978 22.7737 32.6823 22.6178C33.4667 22.4619 34.1873 22.0769 34.753 21.5115C35.5115 20.7528 35.9375 19.724 35.9375 18.6512C35.9375 17.5784 35.5115 16.5496 34.753 15.7909ZM11.3387 15.7909C10.773 15.2252 10.0523 14.8399 9.26759 14.6838C8.48292 14.5277 7.66959 14.6079 6.93045 14.914C6.19131 15.2202 5.55955 15.7386 5.11507 16.4039C4.67059 17.0691 4.43335 17.8511 4.43335 18.6512C4.43335 19.4512 4.67059 20.2333 5.11507 20.8985C5.55955 21.5637 6.19131 22.0822 6.93045 22.3883C7.66959 22.6945 8.48292 22.7746 9.26759 22.6185C10.0523 22.4625 10.773 22.0772 11.3387 21.5115C12.0965 20.7524 12.5221 19.7237 12.5221 18.6512C12.5221 17.5786 12.0965 16.5499 11.3387 15.7909ZM21.8806 3.20963L20.2575 0.0423162C20.2506 0.0295193 20.2403 0.0188307 20.2278 0.0113816C20.2153 0.0039325 20.2011 0 20.1865 0C20.172 0 20.1577 0.0039325 20.1452 0.0113816C20.1327 0.0188307 20.1224 0.0295193 20.1155 0.0423162L18.5039 3.18436C18.4593 3.28308 18.3908 3.36916 18.3046 3.43486C18.2185 3.50056 18.1173 3.54382 18.0103 3.56077L14.4987 4.12426C14.4842 4.12666 14.4706 4.13302 14.4595 4.14263C14.4484 4.15225 14.4402 4.16474 14.4358 4.17874C14.4313 4.19273 14.4308 4.20768 14.4343 4.22194C14.4378 4.2362 14.4452 4.24921 14.4557 4.25953L16.9645 6.78394C17.0372 6.85636 17.0916 6.945 17.1234 7.04257C17.1551 7.14015 17.1632 7.24387 17.1471 7.3452L16.5993 10.8614C16.597 10.8759 16.5987 10.8908 16.6044 10.9044C16.61 10.918 16.6193 10.9298 16.6312 10.9384C16.6431 10.9471 16.6572 10.9522 16.6718 10.9534C16.6865 10.9545 16.7012 10.9515 16.7143 10.9448L19.8901 9.33775C19.9821 9.29155 20.0837 9.26749 20.1866 9.26749C20.2896 9.26749 20.3911 9.29155 20.4831 9.33775L23.6589 10.9448C23.6719 10.9515 23.6865 10.9544 23.701 10.9533C23.7156 10.9521 23.7295 10.9469 23.7412 10.9382C23.753 10.9295 23.7621 10.9177 23.7674 10.9042C23.7728 10.8906 23.7743 10.8758 23.7717 10.8614L23.2307 7.37906C23.2087 7.27269 23.2133 7.16256 23.2439 7.05836C23.2745 6.95416 23.3303 6.85909 23.4063 6.78154L25.9174 4.25953C25.9276 4.24909 25.9348 4.23609 25.9381 4.22191C25.9415 4.20773 25.9409 4.1929 25.9365 4.17901C25.9321 4.16512 25.924 4.15269 25.9131 4.14304C25.9021 4.1334 25.8888 4.12691 25.8745 4.12426L22.3627 3.55888C22.2604 3.54292 22.1634 3.50294 22.0796 3.44221C21.9957 3.38149 21.9275 3.30175 21.8804 3.20954L21.8806 3.20963ZM9.86912 36.1924V34.2847C9.86912 31.2238 11.3568 28.2102 13.9285 26.8196C13.9397 26.8135 13.9493 26.8049 13.9564 26.7944C13.9636 26.7839 13.9681 26.7718 13.9697 26.7592C13.9712 26.7466 13.9697 26.7338 13.9653 26.7218C13.9609 26.7099 13.9537 26.6992 13.9443 26.6907C13.1216 25.9198 12.087 25.4419 10.9443 25.4419H4.96656C3.62095 25.4419 2.39256 26.1114 1.49545 27.191C0.573602 28.3003 0.00108664 29.8376 0.00108664 31.5371V33.2141C-0.0121295 33.536 0.0955974 33.8512 0.303071 34.0976C2.30911 36.453 5.01614 37.0301 7.95529 37.0301C8.59373 37.0331 9.23185 37.0008 9.86671 36.9331C9.87784 36.9317 9.88856 36.9281 9.89821 36.9224C9.90785 36.9166 9.91621 36.909 9.92277 36.8999C9.92933 36.8908 9.93394 36.8804 9.93631 36.8695C9.93869 36.8585 9.93878 36.8472 9.93658 36.8362C9.89097 36.6244 9.86829 36.4083 9.86895 36.1917L9.86912 36.1924Z"></path>
                                </svg>
                                School Activities
                            </span>
                            <h2 class="section-title">Explore Our Gallery</h2>
                        </div>
                    </div>
                </div>

                <!-- Gallery Filters -->
                <div class="row">
                    <div class="col-lg-12">
                        <div class="portfolio-filter-btn">
                            <button class="active" data-filter="*">All Photos</button>
                            <button data-filter=".academics">Academics & Classes</button>
                            <button data-filter=".sports">Sports & Activities</button>
                            <button data-filter=".co-scholastic">Moral & Life Skills</button>
                            <button data-filter=".campus">Campus & Labs</button>
                        </div>
                    </div>
                </div>

                <!-- Gallery Grid -->
                <div class="row g-4 grid mt-10">
                    <!-- Photo 1: Science Exhibition -->
                    <div class="col-xl-4 col-md-6 grid-item academics">
                        <div class="rs-gallery-item">
                            <div class="rs-gallery-thumb">
                                <a class="popup-image" href="assets/1.JPG">
                                    <img src="assets/1.JPG" alt="Science Exhibition">
                                    <div class="rs-gallery-overlay">
                                        <i class="ri-zoom-in-line"></i>
                                    </div>
                                </a>
                            </div>
                            <div class="rs-gallery-content">
                                <span class="gallery-cat text-red">Academics</span>
                                <h5 class="gallery-title"><a href="javascript:void(0)">Science Exhibition Projects</a></h5>
                            </div>
                        </div>
                    </div>

                    <!-- Photo 2: Activity-Based Learning -->
                    <div class="col-xl-4 col-md-6 grid-item academics">
                        <div class="rs-gallery-item">
                            <div class="rs-gallery-thumb">
                                <a class="popup-image" href="assets/Activity-Based Learning.JPG">
                                    <img src="assets/Activity-Based Learning.JPG" alt="Activity-Based Learning">
                                    <div class="rs-gallery-overlay">
                                        <i class="ri-zoom-in-line"></i>
                                    </div>
                                </a>
                            </div>
                            <div class="rs-gallery-content">
                                <span class="gallery-cat text-red">Academics</span>
                                <h5 class="gallery-title"><a href="javascript:void(0)">Interactive Activity-Based Class</a></h5>
                            </div>
                        </div>
                    </div>

                    <!-- Photo 3: CBSE-Oriented Academics -->
                    <div class="col-xl-4 col-md-6 grid-item academics">
                        <div class="rs-gallery-item">
                            <div class="rs-gallery-thumb">
                                <a class="popup-image" href="assets/CBSE-Oriented Academics.JPG">
                                    <img src="assets/CBSE-Oriented Academics.JPG" alt="CBSE-Oriented Academics">
                                    <div class="rs-gallery-overlay">
                                        <i class="ri-zoom-in-line"></i>
                                    </div>
                                </a>
                            </div>
                            <div class="rs-gallery-content">
                                <span class="gallery-cat text-red">Academics</span>
                                <h5 class="gallery-title"><a href="javascript:void(0)">CBSE-Oriented Scholastic Study</a></h5>
                            </div>
                        </div>
                    </div>

                    <!-- Photo 4: Sports Day -->
                    <div class="col-xl-4 col-md-6 grid-item sports">
                        <div class="rs-gallery-item">
                            <div class="rs-gallery-thumb">
                                <a class="popup-image" href="assets/3.JPG">
                                    <img src="assets/3.JPG" alt="Sports Day">
                                    <div class="rs-gallery-overlay">
                                        <i class="ri-zoom-in-line"></i>
                                    </div>
                                </a>
                            </div>
                            <div class="rs-gallery-content">
                                <span class="gallery-cat text-red">Sports</span>
                                <h5 class="gallery-title"><a href="javascript:void(0)">Annual Sports & Athletics Meet</a></h5>
                            </div>
                        </div>
                    </div>

                    <!-- Photo 5: Moral & Life Skills -->
                    <div class="col-xl-4 col-md-6 grid-item co-scholastic">
                        <div class="rs-gallery-item">
                            <div class="rs-gallery-thumb">
                                <a class="popup-image" href="assets/Moral & Life Skills.JPG">
                                    <img src="assets/Moral & Life Skills.JPG" alt="Moral & Life Skills">
                                    <div class="rs-gallery-overlay">
                                        <i class="ri-zoom-in-line"></i>
                                    </div>
                                </a>
                            </div>
                            <div class="rs-gallery-content">
                                <span class="gallery-cat text-red">Co-Scholastic</span>
                                <h5 class="gallery-title"><a href="javascript:void(0)">Yoga & Character Building Session</a></h5>
                            </div>
                        </div>
                    </div>

                    <!-- Photo 6: School Celebrations -->
                    <div class="col-xl-4 col-md-6 grid-item co-scholastic">
                        <div class="rs-gallery-item">
                            <div class="rs-gallery-thumb">
                                <a class="popup-image" href="assets/WhatsApp Image 2026-06-24 at 12.05.15 AM.jpeg">
                                    <img src="assets/WhatsApp Image 2026-06-24 at 12.05.15 AM.jpeg" alt="School Celebrations">
                                    <div class="rs-gallery-overlay">
                                        <i class="ri-zoom-in-line"></i>
                                    </div>
                                </a>
                            </div>
                            <div class="rs-gallery-content">
                                <span class="gallery-cat text-red">Co-Scholastic</span>
                                <h5 class="gallery-title"><a href="javascript:void(0)">Cultural Festivals & Gatherings</a></h5>
                            </div>
                        </div>
                    </div>

                    <!-- Photo 7: School Campus Gate -->
                    <div class="col-xl-4 col-md-6 grid-item campus">
                        <div class="rs-gallery-item">
                            <div class="rs-gallery-thumb">
                                <a class="popup-image" href="assets/school-main.JPG">
                                    <img src="assets/school-main.JPG" alt="School Gate">
                                    <div class="rs-gallery-overlay">
                                        <i class="ri-zoom-in-line"></i>
                                    </div>
                                </a>
                            </div>
                            <div class="rs-gallery-content">
                                <span class="gallery-cat text-red">Campus</span>
                                <h5 class="gallery-title"><a href="javascript:void(0)">School Main Gate & Building</a></h5>
                            </div>
                        </div>
                    </div>

                    <!-- Photo 8: Robotics Lab -->
                    <div class="col-xl-4 col-md-6 grid-item campus">
                        <div class="rs-gallery-item">
                            <div class="rs-gallery-thumb">
                                <a class="popup-image" href="assets/Robotics & Technology.JPG">
                                    <img src="assets/Robotics & Technology.JPG" alt="Robotics Lab">
                                    <div class="rs-gallery-overlay">
                                        <i class="ri-zoom-in-line"></i>
                                    </div>
                                </a>
                            </div>
                            <div class="rs-gallery-content">
                                <span class="gallery-cat text-red">Campus</span>
                                <h5 class="gallery-title"><a href="javascript:void(0)">Robotics & Technology Innovation Lab</a></h5>
                            </div>
                        </div>
                    </div>

                    <!-- Photo 9: Student Activity Area -->
                    <div class="col-xl-4 col-md-6 grid-item campus">
                        <div class="rs-gallery-item">
                            <div class="rs-gallery-thumb">
                                <a class="popup-image" href="assets/2.JPG">
                                    <img src="assets/2.JPG" alt="Student Area">
                                    <div class="rs-gallery-overlay">
                                        <i class="ri-zoom-in-line"></i>
                                    </div>
                                </a>
                            </div>
                            <div class="rs-gallery-content">
                                <span class="gallery-cat text-red">Campus</span>
                                <h5 class="gallery-title"><a href="javascript:void(0)">School Student Activities & Recreation</a></h5>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- gallery area end -->"""

# 4. We replace the main wrapper content
main_wrapper_pattern = r'<!-- breadcrumb area start -->[\s\S]*<!-- admission area end -->'
matches = re.findall(main_wrapper_pattern, html)
if matches:
    html = re.sub(main_wrapper_pattern, gallery_content, html)
    print("Successfully replaced main content with custom gallery grid")
else:
    print("Error: Could not find main content block to replace!")
    exit(1)

# 5. Inject custom script before </body>
custom_script = """    <script>
        jQuery(document).ready(function($) {
            // Init Isotope
            var $grid = $('.grid').imagesLoaded( function() {
                $grid.isotope({
                    itemSelector: '.grid-item',
                    percentPosition: true,
                    masonry: {
                        columnWidth: '.grid-item'
                    }
                });
            });
            
            // Filter items on button click
            $('.portfolio-filter-btn').on('click', 'button', function() {
                var filterValue = $(this).attr('data-filter');
                $grid.isotope({ filter: filterValue });
                $('.portfolio-filter-btn button').removeClass('active');
                $(this).addClass('active');
            });
        });
    </script>
</body>"""

html = html.replace("</body>", custom_script)

with open(gallery_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(html)

print("gallery.html page successfully generated!")
