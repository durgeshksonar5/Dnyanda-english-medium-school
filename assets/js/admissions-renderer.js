(function () {
    let currentPage = 1;
    const itemsPerPage = 2; // Show 2 notices per page for responsive pagination layout

    function renderAdmissions() {
        const placeholder = document.getElementById('admissions-info-section-placeholder');
        if (!placeholder) return;

        const store = window.AdmissionsDB.getStore();
        const status = store.status;
        const info = store.info;
        const docs = store.documents;

        // Render skeleton template if not already present
        if (!placeholder.querySelector('#admissions-info')) {
            placeholder.innerHTML = `
                <div class="admissions-section-area default-padding" id="admissions-info">
                    <div class="container">
                        <!-- Section Title -->
                        <div class="row justify-content-center">
                            <div class="col-xl-8">
                                <div class="section-title-wrapper text-center section-title-space">
                                    <h4 class="sub-title" style="color: var(--color-primary);">Admissions Process & Notices</h4>
                                    <h2 class="section-title has-theme-blue mb-15">Admissions Status</h2>
                                    <p class="section-desc">Find all dynamic information, important timelines, eligibility criteria, and recent announcements below.</p>
                                </div>
                            </div>
                        </div>

                        <div class="row g-4">
                            <!-- Left Side: Status and Information (Unified Card) -->
                            <div class="col-lg-4 col-md-12">
                                <div class="admission-info-card mb-30">
                                    <div class="text-center mb-25 pb-20" style="border-bottom: 2px solid var(--border-color);">
                                        <div id="admissions-status-badge-container"></div>
                                        <p class="text-muted mb-0" style="font-size: 12px;">Last Updated: <span id="admissions-last-updated">-</span></p>
                                    </div>
                                    <h4 class="mb-20" style="font-weight: 700; border-bottom: 2px solid var(--color-primary); padding-bottom: 10px; color: var(--color-dark); font-size: 18px;">Quick Facts</h4>
                                    <ul class="admission-info-list" id="admissions-facts-list"></ul>
                                </div>
                            </div>

                            <!-- Right Side: Important Notices Area -->
                            <div class="col-lg-8 col-md-12">
                                <div class="admission-info-card" style="height: auto;">
                                    <h4 class="mb-20" style="font-weight: 700; border-bottom: 2px solid var(--color-secondary); padding-bottom: 10px; color: var(--color-dark);">Important Notices</h4>
                                    
                                    <!-- Search & Filter Row -->
                                    <div class="row g-3 mb-20">
                                        <div class="col-md-5">
                                            <input type="text" id="notice-search" class="form-control" placeholder="Search notices..." style="border: 1px solid var(--border-color); border-radius: 5px; height: 100%; min-height: 42px;">
                                        </div>
                                        <div class="col-md-4 col-sm-6">
                                            <select id="notice-category-filter" class="form-select" style="border: 1px solid var(--border-color); border-radius: 5px; height: 100%; min-height: 42px; padding: 6px 12px;">
                                                <option value="all">All Categories</option>
                                                <option value="General">General</option>
                                                <option value="Fee">Fee Structure</option>
                                                <option value="Documents">Documents</option>
                                                <option value="Scholarship">Scholarship</option>
                                                <option value="Timing">School Timings</option>
                                            </select>
                                        </div>
                                        <div class="col-md-3 col-sm-6">
                                            <select id="notice-sort" class="form-select" style="border: 1px solid var(--border-color); border-radius: 5px; height: 100%; min-height: 42px; padding: 6px 12px;">
                                                <option value="newest">Newest First</option>
                                                <option value="priority">Priority First</option>
                                            </select>
                                        </div>
                                    </div>

                                    <!-- Notices Grid -->
                                    <div class="row g-4" id="notices-grid-container"></div>

                                    <!-- Pagination -->
                                    <div class="d-flex justify-content-center mt-30" id="notices-pagination-container"></div>
                                </div>
                            </div>
                        </div>

                        <!-- Quick Information Cards Row -->
                        <div class="quick-info-box-wrapper">
                            <div class="row justify-content-center mb-30">
                                <div class="col-xl-8 text-center">
                                    <h3 style="font-weight:700; margin-bottom: 10px; color: var(--color-dark);">Quick Information Guides</h3>
                                    <p class="text-muted">Click any guide below to read detailed information instantly.</p>
                                </div>
                            </div>
                            <div class="row g-4">
                                <div class="col-lg-4 col-md-6 col-12">
                                    <div class="quick-info-grid-card" data-info-key="admissionProcess">
                                        <i class="fa-solid fa-list-check"></i>
                                        <h5>✓ Admission Process</h5>
                                    </div>
                                </div>
                                <div class="col-lg-4 col-md-6 col-12">
                                    <div class="quick-info-grid-card" data-info-key="requiredDocuments">
                                        <i class="fa-solid fa-file-invoice"></i>
                                        <h5>✓ Required Documents</h5>
                                    </div>
                                </div>
                                <div class="col-lg-4 col-md-6 col-12">
                                    <div class="quick-info-grid-card" data-info-key="feeStructure">
                                        <i class="fa-solid fa-indian-rupee-sign"></i>
                                        <h5>✓ Fee Structure</h5>
                                    </div>
                                </div>
                                <div class="col-lg-4 col-md-6 col-12">
                                    <div class="quick-info-grid-card" data-info-key="eligibility">
                                        <i class="fa-solid fa-user-graduate"></i>
                                        <h5>✓ Scholarship Information</h5>
                                    </div>
                                </div>
                                <div class="col-lg-4 col-md-6 col-12">
                                    <div class="quick-info-grid-card" data-info-key="schoolTimingText">
                                        <i class="fa-solid fa-clock"></i>
                                        <h5>✓ School Timing Details</h5>
                                    </div>
                                </div>
                                <div class="col-lg-4 col-md-6 col-12">
                                    <div class="quick-info-grid-card" data-info-key="admissionGuidelines">
                                        <i class="fa-solid fa-circle-info"></i>
                                        <h5>✓ General Guidelines</h5>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- CTA Buttons Row -->
                        <div class="row mt-50 justify-content-center">
                            <div class="col-12 text-center">
                                <div class="admissions-actions">
                                    <a href="#admission" class="btn btn-gradient animation" style="background: var(--color-primary); color: white; border: none; font-weight:700;">Apply for Admission</a>
                                    <a href="#" id="cta-download-prospectus" class="btn btn-theme animation" style="background: var(--color-secondary); color: white; border: none; font-weight:700;">Download Prospectus</a>
                                    <a href="tel:+917557333222" id="cta-contact-admission" class="btn btn-theme animation" style="background: var(--color-dark); color: white; border: none; font-weight:700;">Contact Admission Office</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Modals -->
                <div class="modal fade" id="noticeDetailsModal" tabindex="-1" aria-hidden="true" style="z-index: 10500;">
                    <div class="modal-dialog modal-dialog-centered">
                        <div class="modal-content" style="border-radius: 12px;">
                            <div class="modal-header" style="border-radius: 12px 12px 0 0; background: var(--color-light); display: flex; justify-content: space-between; align-items: center; padding: 15px 20px;">
                                <h5 class="modal-title" style="font-weight: 700; color: var(--color-dark); margin: 0;">Notice Details</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" style="border: none; background: transparent; font-size: 20px;">&times;</button>
                            </div>
                            <div class="modal-body" id="notice-modal-body" style="padding: 25px;"></div>
                        </div>
                    </div>
                </div>

                <div class="modal fade" id="quickInfoModal" tabindex="-1" aria-hidden="true" style="z-index: 10500;">
                    <div class="modal-dialog modal-dialog-centered modal-lg">
                        <div class="modal-content" style="border-radius: 12px;">
                            <div class="modal-header" style="border-radius: 12px 12px 0 0; background: var(--color-light); display: flex; justify-content: space-between; align-items: center; padding: 15px 20px;">
                                <h5 class="modal-title" style="font-weight: 700; color: var(--color-dark); margin: 0;">Information Guide</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" style="border: none; background: transparent; font-size: 20px;">&times;</button>
                            </div>
                            <div class="modal-body" id="quick-info-modal-body" style="padding: 30px;"></div>
                        </div>
                    </div>
                </div>
            `;

            // Bind filters and events
            document.getElementById('notice-search').addEventListener('input', () => { currentPage = 1; filterAndRenderNotices(); });
            document.getElementById('notice-category-filter').addEventListener('change', () => { currentPage = 1; filterAndRenderNotices(); });
            document.getElementById('notice-sort').addEventListener('change', () => { currentPage = 1; filterAndRenderNotices(); });

            // Bind click for Quick Info Cards
            const placeholderEl = document.getElementById('admissions-info-section-placeholder');
            placeholderEl.querySelectorAll('.quick-info-grid-card').forEach(card => {
                card.addEventListener('click', function () {
                    const key = this.dataset.infoKey;
                    const items = store.info[key] || [];
                    const title = this.querySelector('h5').innerText.replace('✓ ', '');
                    
                    function escapeHtml(text) {
                        return text
                            .replace(/&/g, "&amp;")
                            .replace(/</g, "&lt;")
                            .replace(/>/g, "&gt;")
                            .replace(/"/g, "&quot;")
                            .replace(/'/g, "&#039;");
                    }

                    let contentHtml = "";
                    if (Array.isArray(items)) {
                        const isOrdered = (key === 'admissionProcess');
                        const tag = isOrdered ? 'ol' : 'ul';
                        contentHtml = `<${tag} style="padding-left: 20px; margin: 0;">
                            ${items.map(item => `<li style="margin-bottom: 12px; line-height: 1.6; font-size: 15px; color: var(--text-color);">${escapeHtml(item)}</li>`).join('')}
                        </${tag}>`;
                    } else {
                        contentHtml = `<p style="line-height: 1.6; font-size: 15px; color: var(--text-color);">${escapeHtml(String(items))}</p>`;
                    }

                    const modalBody = document.getElementById('quick-info-modal-body');
                    modalBody.innerHTML = contentHtml;
                    
                    const modalTitle = document.querySelector('#quickInfoModal .modal-title');
                    modalTitle.innerText = title;

                    // Open BS modal
                    const myModal = new bootstrap.Modal(document.getElementById('quickInfoModal'));
                    myModal.show();
                });
            });
        }

        // 1. Render Status Badge
        const badgeContainer = document.getElementById('admissions-status-badge-container');
        if (status.isOpen) {
            badgeContainer.innerHTML = `
                <div class="admission-badge open">
                    <span class="pulse-dot"></span>
                    Admission Open
                </div>
                <h4 style="font-weight: 700; color: var(--color-dark); margin-bottom: 5px;">Year: ${status.academicYear}</h4>
            `;
        } else {
            badgeContainer.innerHTML = `
                <div class="admission-badge closed">
                    <span class="pulse-dot"></span>
                    Admission Closed
                </div>
                <h4 style="font-weight: 700; color: var(--color-dark); margin-bottom: 5px;">Year: ${status.academicYear}</h4>
            `;
        }

        // Render Last Updated Date
        const lastUpdatedEl = document.getElementById('admissions-last-updated');
        if (lastUpdatedEl) {
            const date = new Date(status.lastUpdated);
            lastUpdatedEl.innerText = date.toLocaleDateString() + ' ' + date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        }

        // 2. Render Facts List
        const factsList = document.getElementById('admissions-facts-list');
        factsList.innerHTML = `
            <li><span class="label">Start Date</span><span class="value">${status.startDate}</span></li>
            <li><span class="label">End Date</span><span class="value">${status.endDate}</span></li>
            <li><span class="label">Classes Available</span><span class="value">${status.classesAvailable}</span></li>
            <li><span class="label">Available Seats</span><span class="value">${status.availableSeats}</span></li>
            <li><span class="label">School Hours</span><span class="value">${status.schoolTiming}</span></li>
            <li><span class="label">Office Hours</span><span class="value">${status.officeTiming}</span></li>
            <li><span class="label">Phone</span><span class="value"><a href="tel:${status.contactNumber}">${status.contactNumber}</a></span></li>
            <li><span class="label">Email</span><span class="value"><a href="mailto:${status.admissionEmail}">${status.admissionEmail}</a></span></li>
        `;

        // 3. CTA download documents link
        const ctaProspectus = document.getElementById('cta-download-prospectus');
        if (docs.prospectus) {
            ctaProspectus.href = docs.prospectus;
            ctaProspectus.removeAttribute('onclick');
        } else {
            ctaProspectus.href = "#";
            ctaProspectus.setAttribute('onclick', "alert('Prospectus download file not uploaded by admin yet. Please check back later.'); return false;");
        }

        const ctaContact = document.getElementById('cta-contact-admission');
        if (ctaContact) {
            ctaContact.href = `tel:${status.contactNumber}`;
        }

        // 3. Update admissions form area state (Open/Closed)
        const formSubtitle = document.getElementById('admission-form-subtitle');
        const formWrapper = document.getElementById('admission-form-wrapper');
        const closedWrapper = document.getElementById('admission-closed-wrapper');
        const closedAcademicYear = document.getElementById('closed-academic-year');
        const closedPhoneBtn = document.getElementById('closed-phone-btn');
        const closedEmailBtn = document.getElementById('closed-email-btn');

        if (formSubtitle) {
            formSubtitle.innerText = status.isOpen ? "Admissions Open" : "Admissions Closed";
            if (!status.isOpen) {
                formSubtitle.style.color = "#E63946"; // Red status badge
            } else {
                formSubtitle.style.color = ""; // Default style
            }
        }

        if (closedAcademicYear) {
            closedAcademicYear.innerText = status.academicYear;
        }
        if (closedPhoneBtn) {
            closedPhoneBtn.href = `tel:${status.contactNumber}`;
        }
        if (closedEmailBtn) {
            closedEmailBtn.href = `mailto:${status.admissionEmail}`;
        }

        if (formWrapper && closedWrapper) {
            if (status.isOpen) {
                formWrapper.classList.remove('d-none');
                closedWrapper.classList.add('d-none');
            } else {
                formWrapper.classList.add('d-none');
                closedWrapper.classList.remove('d-none');
            }
        }

        // 4. Trigger notice rendering
        filterAndRenderNotices();
    }

    function filterAndRenderNotices() {
        const store = window.AdmissionsDB.getStore();
        let notices = store.notices.filter(n => n.status === 'published');

        // Filter by Search Query
        const searchQuery = document.getElementById('notice-search').value.toLowerCase().trim();
        if (searchQuery) {
            notices = notices.filter(n => n.title.toLowerCase().includes(searchQuery) || n.description.toLowerCase().includes(searchQuery));
        }

        // Filter by Category
        const categoryVal = document.getElementById('notice-category-filter').value;
        if (categoryVal !== 'all') {
            notices = notices.filter(n => n.category === categoryVal);
        }

        // Sort notices
        const sortVal = document.getElementById('notice-sort').value;
        if (sortVal === 'newest') {
            notices.sort((a, b) => new Date(b.publishDate) - new Date(a.publishDate));
        } else if (sortVal === 'priority') {
            notices.sort((a, b) => a.priority - b.priority);
        }

        // Paginate
        const totalItems = notices.length;
        const totalPages = Math.ceil(totalItems / itemsPerPage);
        const startIndex = (currentPage - 1) * itemsPerPage;
        const paginatedNotices = notices.slice(startIndex, startIndex + itemsPerPage);

        // Render Notices Grid
        const gridContainer = document.getElementById('notices-grid-container');
        if (paginatedNotices.length === 0) {
            gridContainer.innerHTML = `
                <div class="col-12 text-center py-5">
                    <p class="text-muted mb-0"><i class="fa-solid fa-circle-exclamation fa-2x mb-10 text-secondary"></i><br>No notices found matching the filters.</p>
                </div>
            `;
            document.getElementById('notices-pagination-container').innerHTML = '';
            return;
        }

        gridContainer.innerHTML = paginatedNotices.map(notice => {
            const isNewBadge = notice.isNew ? `<span class="notice-new-badge">NEW</span>` : ``;
            const hasPDF = notice.pdfUrl ? `<button class="btn btn-sm btn-outline-secondary download-pdf-btn" data-id="${notice.id}" style="font-size:12px; padding: 4px 10px;"><i class="fa-solid fa-file-pdf"></i> PDF</button>` : ``;
            
            return `
                <div class="col-md-6 col-12">
                    <div class="notice-item-card">
                        <div>
                            <div class="notice-badge-row">
                                <span class="notice-category">${notice.category}</span>
                                ${isNewBadge}
                            </div>
                            <h5 class="notice-title">${notice.title}</h5>
                            <p class="notice-desc">${notice.description.length > 120 ? notice.description.substring(0, 120) + '...' : notice.description}</p>
                        </div>
                        <div>
                            <div class="notice-meta-row">
                                <i class="fa-solid fa-calendar-days"></i> Published: ${notice.publishDate}
                            </div>
                            <div class="d-flex gap-2">
                                <button class="btn btn-sm btn-gradient view-details-btn" data-id="${notice.id}" style="font-size:12px; padding: 4px 10px; background: var(--color-primary); color: white; border: none;">View Details</button>
                                ${hasPDF}
                            </div>
                        </div>
                    </div>
                </div>
            `;
        }).join('');

        // Bind Notice Actions
        gridContainer.querySelectorAll('.view-details-btn').forEach(btn => {
            btn.addEventListener('click', function () {
                const noticeId = this.dataset.id;
                const notice = store.notices.find(n => n.id === noticeId);
                if (notice) {
                    const modalBody = document.getElementById('notice-modal-body');
                    const imgTag = notice.imageUrl ? `<img src="${notice.imageUrl}" alt="${notice.title}" class="img-fluid rounded mb-20" style="max-height: 250px; object-fit: cover; width: 100%;">` : ``;
                    const hasPdfLink = notice.pdfUrl ? `<div class="mt-20"><a href="${notice.pdfUrl}" class="btn btn-gradient text-white btn-sm" download="${notice.title}.pdf" style="background: var(--color-primary); border: none;"><i class="fa-solid fa-file-pdf"></i> Download Attached Document</a></div>` : ``;
                    
                    modalBody.innerHTML = `
                        ${imgTag}
                        <span class="badge mb-10" style="background: rgba(31,122,140,0.1); color: var(--color-secondary);">${notice.category}</span>
                        <h4 style="font-weight: 700; margin-bottom: 10px; color: var(--color-dark);">${notice.title}</h4>
                        <p class="text-muted" style="font-size: 12px; margin-bottom: 15px;"><i class="fa-solid fa-calendar"></i> Published: ${notice.publishDate}</p>
                        <hr>
                        <p style="font-size: 14px; line-height: 1.6; color: var(--text-color); white-space: pre-wrap;">${notice.description}</p>
                        ${hasPdfLink}
                    `;

                    const myModal = new bootstrap.Modal(document.getElementById('noticeDetailsModal'));
                    myModal.show();
                }
            });
        });

        gridContainer.querySelectorAll('.download-pdf-btn').forEach(btn => {
            btn.addEventListener('click', function () {
                const noticeId = this.dataset.id;
                const notice = store.notices.find(n => n.id === noticeId);
                if (notice && notice.pdfUrl) {
                    // Trigger download
                    const link = document.createElement('a');
                    link.href = notice.pdfUrl;
                    link.download = `${notice.title}.pdf`;
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);
                }
            });
        });

        // Render Pagination Controls
        renderPagination(totalPages);
    }

    function renderPagination(totalPages) {
        const container = document.getElementById('notices-pagination-container');
        if (totalPages <= 1) {
            container.innerHTML = '';
            return;
        }

        let buttons = ``;
        for (let i = 1; i <= totalPages; i++) {
            const isActive = i === currentPage ? 'active' : '';
            const btnStyle = i === currentPage ? 'background: var(--color-primary); border-color: var(--color-primary); color: white;' : 'background: transparent; border-color: var(--border-color); color: var(--color-dark);';
            buttons += `<button class="btn btn-sm mx-1 page-num-btn ${isActive}" data-page="${i}" style="${btnStyle} font-weight:700;">${i}</button>`;
        }

        container.innerHTML = buttons;

        container.querySelectorAll('.page-num-btn').forEach(btn => {
            btn.addEventListener('click', function () {
                currentPage = parseInt(this.dataset.page);
                filterAndRenderNotices();
            });
        });
    }

    // Trigger initial render
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            renderAdmissions();
        });
    } else {
        renderAdmissions();
    }

    // Listen to changes in the store to update dynamically without reload
    window.addEventListener('admissionsDataChanged', () => {
        renderAdmissions();
    });
})();
