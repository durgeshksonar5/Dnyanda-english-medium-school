(function () {
    'use strict';

    const API_ENDPOINT = 'https://leadsmanagment.hindustandigitalservices.com/api/forms/submit/b5d0e787-4ebb-45ad-8f63-76fd0851a5b7';

    // Helper to submit lead payload to API
    async function submitLead(payload) {
        const response = await fetch(API_ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const errText = await response.text();
            throw new Error(errText || `Server responded with status ${response.status}`);
        }

        return await response.json();
    }

    // Helper to show visual feedback message on form submission
    function showFeedback(form, message, type) {
        let feedbackDiv = form.querySelector('.form-feedback-message');
        if (!feedbackDiv) {
            feedbackDiv = document.getElementById('form-messages');
        }
        
        if (!feedbackDiv) {
            feedbackDiv = document.createElement('div');
            feedbackDiv.className = 'form-feedback-message alert';
            feedbackDiv.style.marginTop = '15px';
            feedbackDiv.style.padding = '12px';
            feedbackDiv.style.fontSize = '14px';
            feedbackDiv.style.borderRadius = '5px';
            
            // Insert before the submit button or append to form
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                form.insertBefore(feedbackDiv, submitBtn);
            } else {
                form.appendChild(feedbackDiv);
            }
        }

        // Apply classes
        feedbackDiv.className = `form-feedback-message alert alert-${type === 'success' ? 'success' : 'danger'}`;
        feedbackDiv.innerText = message;
        feedbackDiv.classList.remove('d-none');
    }

    // Helper to disable button and show loading state
    function setLoadingState(submitBtn, isLoading) {
        if (!submitBtn) return;
        
        if (isLoading) {
            submitBtn.disabled = true;
            submitBtn.dataset.originalHtml = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin" style="margin-right: 8px;"></i> Submitting...';
        } else {
            submitBtn.disabled = false;
            if (submitBtn.dataset.originalHtml) {
                submitBtn.innerHTML = submitBtn.dataset.originalHtml;
            }
        }
    }

    // Initialize forms
    function initForms() {
        // 1. Admission Enquiry Form (Index Hero)
        const heroForm = document.querySelector('.hero-form-box form');
        if (heroForm) {
            heroForm.addEventListener('submit', async function (e) {
                e.preventDefault();
                
                if (!heroForm.checkValidity()) {
                    heroForm.reportValidity();
                    return;
                }

                const nameInput = heroForm.querySelector('[name="parent-name"]');
                const phoneInput = heroForm.querySelector('[name="phone"]');
                const gradeSelect = heroForm.querySelector('[name="grade"]');

                const name = nameInput ? nameInput.value.trim() : "";
                const phone = phoneInput ? phoneInput.value.trim() : "";
                const gradeVal = gradeSelect ? gradeSelect.value : "";

                // Additional input check
                if (!name || !phone || !gradeVal) {
                    showFeedback(heroForm, "Please fill in all fields.", "error");
                    return;
                }

                const phoneRegex = /^[0-9]{10}$/;
                if (!phoneRegex.test(phone)) {
                    showFeedback(heroForm, "Please enter a valid 10-digit mobile number.", "error");
                    return;
                }

                const submitBtn = heroForm.querySelector('button[type="submit"]');
                setLoadingState(submitBtn, true);

                try {
                    const payload = {
                        name: name,
                        email: "",
                        phone: phone,
                        message: `Grade Choice: ${gradeVal}`,
                        source: "Website",
                        page_url: window.location.href,
                        page_title: document.title,
                        form_type: "Admission Enquiry"
                    };

                    await submitLead(payload);
                    showFeedback(heroForm, "Thank you! Your enquiry has been submitted successfully.", "success");
                    heroForm.reset();
                    
                    // Reset nice-select if initialized
                    if (window.jQuery && window.jQuery(gradeSelect).niceSelect) {
                        window.jQuery(gradeSelect).val('').niceSelect('update');
                    }
                } catch (err) {
                    console.error("API submission error:", err);
                    showFeedback(heroForm, "Unable to submit enquiry. Please try again later.", "error");
                } finally {
                    setLoadingState(submitBtn, false);
                }
            });
        }

        // 2. Begin Child's Journey Admission Form (Index Body)
        const admissionForm = document.getElementById('admission-form');
        if (admissionForm) {
            admissionForm.addEventListener('submit', async function (e) {
                e.preventDefault();

                if (!admissionForm.checkValidity()) {
                    admissionForm.reportValidity();
                    return;
                }

                const nameInput = admissionForm.querySelector('[name="name"]');
                const emailInput = admissionForm.querySelector('[name="email"]');
                const phoneInput = admissionForm.querySelector('[name="phone"]');
                const gradeSelect = admissionForm.querySelector('[name="grade"]');

                const name = nameInput ? nameInput.value.trim() : "";
                const email = emailInput ? emailInput.value.trim() : "";
                const phone = phoneInput ? phoneInput.value.trim() : "";
                const gradeVal = gradeSelect ? gradeSelect.value : "";

                if (!name || !email || !phone) {
                    showFeedback(admissionForm, "Please fill in all fields.", "error");
                    return;
                }

                // Email validation
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(email)) {
                    showFeedback(admissionForm, "Please enter a valid email address.", "error");
                    return;
                }

                // Phone validation
                const phoneRegex = /^[0-9]{10}$/;
                if (!phoneRegex.test(phone)) {
                    showFeedback(admissionForm, "Please enter a valid 10-digit mobile number.", "error");
                    return;
                }

                const submitBtn = admissionForm.querySelector('button[type="submit"]');
                setLoadingState(submitBtn, true);

                try {
                    const payload = {
                        name: name,
                        email: email,
                        phone: phone,
                        message: `Selected Grade: ${gradeVal}`,
                        source: "Website",
                        page_url: window.location.href,
                        page_title: document.title,
                        form_type: "Admissions Open Form"
                    };

                    await submitLead(payload);
                    showFeedback(admissionForm, "Your admission form has been submitted successfully.", "success");
                    admissionForm.reset();

                    // Reset nice-select if initialized
                    if (window.jQuery && window.jQuery(gradeSelect).niceSelect) {
                        window.jQuery(gradeSelect).val('').niceSelect('update');
                    }
                } catch (err) {
                    console.error("API submission error:", err);
                    showFeedback(admissionForm, "Unable to submit application. Please try again.", "error");
                } finally {
                    setLoadingState(submitBtn, false);
                }
            });
        }

        // 3. Contact Form (Contact Page)
        const contactForm = document.getElementById('contact-form');
        if (contactForm) {
            // Unbind existing jQuery submit handler to avoid double posting or mailer.php fallback errors
            if (window.jQuery) {
                window.jQuery(contactForm).off('submit');
            }

            contactForm.addEventListener('submit', async function (e) {
                e.preventDefault();

                const nameInput = contactForm.querySelector('#name');
                const phoneInput = contactForm.querySelector('#phone');
                const emailInput = contactForm.querySelector('#email');
                const messageInput = contactForm.querySelector('#message');

                const name = nameInput ? nameInput.value.trim() : "";
                const phone = phoneInput ? phoneInput.value.trim() : "";
                const email = emailInput ? emailInput.value.trim() : "";
                const message = messageInput ? messageInput.value.trim() : "";

                // Verify fields manually because HTML lacks 'required' attributes
                if (!name || !phone || !email || !message) {
                    showFeedback(contactForm, "Please fill in all required fields marked with *", "error");
                    return;
                }

                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(email)) {
                    showFeedback(contactForm, "Please enter a valid email address.", "error");
                    return;
                }

                const submitBtn = contactForm.querySelector('button[type="submit"]');
                setLoadingState(submitBtn, true);

                try {
                    const payload = {
                        name: name,
                        email: email,
                        phone: phone,
                        message: message,
                        source: "Website",
                        page_url: window.location.href,
                        page_title: document.title,
                        form_type: "Get in Touch Form"
                    };

                    await submitLead(payload);
                    showFeedback(contactForm, "Thank you! Your message has been sent successfully.", "success");
                    contactForm.reset();
                } catch (err) {
                    console.error("API submission error:", err);
                    showFeedback(contactForm, "Unable to send message. Please check your internet connection.", "error");
                } finally {
                    setLoadingState(submitBtn, false);
                }
            });
        }
    }

    let modalOverlay = null;
    let callForm = null;
    let callUrl = "tel:+917557333222";

    function initModalElements() {
        modalOverlay = document.getElementById('call-request-modal');
        if (!modalOverlay) return;

        callForm = modalOverlay.querySelector('#call-request-form');
        if (!callForm) return;

        if (callForm.dataset.initialized) return;
        callForm.dataset.initialized = "true";

        const fullnameInput = callForm.querySelector('#modal-fullname');
        const phoneInput = callForm.querySelector('#modal-phone');
        const fullnameError = callForm.querySelector('#modal-fullname-error');
        const phoneError = callForm.querySelector('#modal-phone-error');
        const feedbackBox = modalOverlay.querySelector('#modal-feedback');
        const cancelBtn = modalOverlay.querySelector('#call-modal-cancel-btn');
        const closeBtn = modalOverlay.querySelector('#call-modal-close-btn');
        const submitBtn = callForm.querySelector('#call-modal-submit-btn');

        // Only allow numbers in mobile input
        phoneInput.addEventListener('input', function() {
            this.value = this.value.replace(/[^0-9]/g, '');
        });

        // Close on Cancel
        cancelBtn.addEventListener('click', closeCallModal);
        // Close on X
        closeBtn.addEventListener('click', closeCallModal);
        // Close on click outside
        modalOverlay.addEventListener('click', function(e) {
            if (e.target === modalOverlay) {
                closeCallModal();
            }
        });

        // ESC key closes modal
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && modalOverlay.classList.contains('active')) {
                closeCallModal();
            }
        });

        function closeCallModal() {
            modalOverlay.classList.remove('active');
            callForm.reset();
            fullnameError.innerText = "";
            phoneError.innerText = "";
            feedbackBox.className = "modal-feedback-box";
            feedbackBox.style.display = "none";
        }

        // Form Submit
        callForm.addEventListener('submit', async function (e) {
            e.preventDefault();

            // Clear previous errors
            fullnameError.innerText = "";
            phoneError.innerText = "";
            feedbackBox.className = "modal-feedback-box";
            feedbackBox.style.display = "none";

            const fullname = fullnameInput.value.trim();
            const phoneNum = phoneInput.value.trim();

            let hasError = false;

            // Full name validation: required, min 3 characters
            if (!fullname) {
                fullnameError.innerText = "Full Name is required.";
                hasError = true;
            } else if (fullname.length < 3) {
                fullnameError.innerText = "Name must be at least 3 characters.";
                hasError = true;
            }

            // Mobile number validation: required, numbers only, 10 digits
            if (!phoneNum) {
                phoneError.innerText = "Mobile Number is required.";
                hasError = true;
            } else if (!/^[0-9]{10}$/.test(phoneNum)) {
                phoneError.innerText = "Mobile Number must be exactly 10 digits.";
                hasError = true;
            }

            if (hasError) return;

            // Show loading state
            setLoadingState(submitBtn, true);

            try {
                const now = new Date();
                const payload = {
                    name: fullname,
                    email: "",
                    phone: phoneNum,
                    message: `Callback requested via Floating Call Button. Date: ${now.toLocaleDateString()}, Time: ${now.toLocaleTimeString()}`,
                    source: "Floating Contact Button",
                    button_type: "Call",
                    form_type: "Call",
                    submission_date: now.toLocaleDateString(),
                    submission_time: now.toLocaleTimeString(),
                    page_url: window.location.href,
                    page_title: document.title
                };

                await submitLead(payload);

                // Success state
                feedbackBox.innerText = "Thank you! Connecting your call...";
                feedbackBox.className = "modal-feedback-box success";
                feedbackBox.style.display = "block";

                // Wait 1.5 seconds then open dialer and close modal
                setTimeout(() => {
                    window.location.href = callUrl;
                    closeCallModal();
                    setLoadingState(submitBtn, false);
                }, 1500);

            } catch (err) {
                console.error("API Callback submission error:", err);
                feedbackBox.innerText = "Unable to connect. Please check your internet connection.";
                feedbackBox.className = "modal-feedback-box error";
                feedbackBox.style.display = "block";
                setLoadingState(submitBtn, false);
            }
        });
    }

    // Initialize floating button tracking (using event delegation)
    function initFloatingButtons() {
        document.body.addEventListener('click', function (e) {
            const waLink = e.target.closest('.floating-whatsapp');
            const callLink = e.target.closest('.floating-call');

            if (waLink) {
                const payload = {
                    name: "Website Visitor",
                    phone: "",
                    source: "Floating Button",
                    button_type: "WhatsApp",
                    page_url: window.location.href,
                    page_title: document.title
                };

                fetch(API_ENDPOINT, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload),
                    keepalive: true
                }).catch(err => console.error("Error tracking WhatsApp click:", err));
            }

            if (callLink) {
                e.preventDefault();
                callUrl = callLink.getAttribute('href') || "tel:+917557333222";
                
                initModalElements();
                
                if (modalOverlay) {
                    modalOverlay.classList.add('active');
                    const fullnameInput = modalOverlay.querySelector('#modal-fullname');
                    if (fullnameInput) {
                        setTimeout(() => fullnameInput.focus(), 100);
                    }
                }
            }
        });
    }

    // Run setup
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            initForms();
            initFloatingButtons();
        });
    } else {
        initForms();
        initFloatingButtons();
    }
})();
