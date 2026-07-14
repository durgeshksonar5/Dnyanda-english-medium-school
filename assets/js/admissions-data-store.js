(function () {
    const STORE_KEY = "dnyanda_admissions_data";

    const defaultAdmissionsData = {
        status: {
            isOpen: true,
            academicYear: "2026-2027",
            startDate: "2026-11-01",
            endDate: "2027-03-31",
            classesAvailable: "Nursery to Grade V",
            availableSeats: 45,
            schoolTiming: "8:30 AM - 2:30 PM",
            officeTiming: "9:00 AM - 4:00 PM",
            contactNumber: "+91 7557333222",
            admissionEmail: "admissions@dnyandaschool.com",
            lastUpdated: new Date().toISOString()
        },
        notices: [
            {
                id: "notice-1",
                title: "Admissions Open for Academic Year 2026-2027",
                description: "Registration forms for Nursery to Grade V are now available at the school office and online. Submit completed forms by the due date.",
                category: "General",
                publishDate: new Date().toISOString().split('T')[0],
                expiryDate: "2027-03-31",
                pdfUrl: "",
                imageUrl: "",
                priority: 1,
                status: "published",
                isNew: true,
                isFeatured: true
            },
            {
                id: "notice-2",
                title: "Scholarship Program Details Released",
                description: "Dnyanda School is pleased to announce scholarship schemes for meritorious students and sports achievers. Download details below.",
                category: "Scholarship",
                publishDate: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
                expiryDate: "2026-12-31",
                pdfUrl: "",
                imageUrl: "",
                priority: 2,
                status: "published",
                isNew: true,
                isFeatured: false
            },
            {
                id: "notice-3",
                title: "Required Documents Checklist for Verification",
                description: "All parents seeking admission are requested to bring original copies of Birth Certificate, Aadhar Card, and previous school TC for verification.",
                category: "Documents",
                publishDate: new Date(Date.now() - 5 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
                expiryDate: "2027-03-31",
                pdfUrl: "",
                imageUrl: "",
                priority: 2,
                status: "published",
                isNew: false,
                isFeatured: false
            }
        ],
        documents: {
            prospectus: "",
            admissionForm: "",
            feeStructure: "",
            requiredDocuments: "",
            timetable: "",
            transportDetails: "",
            schoolBrochure: ""
        },
        info: {
            admissionProcess: [
                "Online/Offline Enquiry: Submit an enquiry form online or visit the school office.",
                "Interaction & Assessment: A short informal interaction is conducted with the child and parents.",
                "Document Verification: Submit required documents for verification.",
                "Fee Payment: Secure admission by paying the term fees."
            ],
            eligibility: [
                "Nursery: Child must be 3+ years of age as of 31st December of the academic year.",
                "LKG/UKG: Child must be 4+ / 5+ years of age respectively.",
                "Grade I - V: Age appropriate admission based on performance evaluation and TC from recognized school."
            ],
            requiredDocuments: [
                "Original Birth Certificate",
                "Aadhar Card of Student and Parents",
                "Previous Academic Report Card",
                "Transfer Certificate (TC) from previous school",
                "2 Recent Passport Size Photographs"
            ],
            feeStructure: [
                "Tuition fee, Computer & Lab fees are paid term-wise.",
                "Detailed printed fee structures can be collected from the school office.",
                "Term fees must be paid within 15 days of term start."
            ],
            schoolTimingText: [
                "Nursery & Preschool: 9:00 AM to 12:30 PM (Monday to Friday)",
                "Primary (Grade I to V): 8:30 AM to 2:30 PM (Monday to Friday)",
                "Saturday: Co-curricular clubs only."
            ],
            admissionGuidelines: [
                "Parents are requested to read the school rules before submitting the admission form.",
                "The decision of the management is final regarding admissions.",
                "Incomplete forms will be rejected."
            ]
        }
    };

    function initStore() {
        const current = localStorage.getItem(STORE_KEY);
        if (current) {
            try {
                const parsed = JSON.parse(current);
                if (parsed.info && typeof parsed.info.admissionProcess === 'string') {
                    localStorage.removeItem(STORE_KEY); // Force reset to migrate schema
                }
            } catch (e) {
                localStorage.removeItem(STORE_KEY);
            }
        }
        if (!localStorage.getItem(STORE_KEY)) {
            localStorage.setItem(STORE_KEY, JSON.stringify(defaultAdmissionsData));
        }
    }

    function getStore() {
        initStore();
        try {
            return JSON.parse(localStorage.getItem(STORE_KEY));
        } catch (e) {
            console.error("Error reading admissions store, resetting to default.", e);
            localStorage.setItem(STORE_KEY, JSON.stringify(defaultAdmissionsData));
            return defaultAdmissionsData;
        }
    }

    function saveStore(data) {
        data.status.lastUpdated = new Date().toISOString();
        localStorage.setItem(STORE_KEY, JSON.stringify(data));
        
        // Dispatch custom event to notify other tabs/scripts on same page
        window.dispatchEvent(new CustomEvent('admissionsDataChanged', { detail: data }));
    }

    // Expose DB methods to global scope
    window.AdmissionsDB = {
        getStore: getStore,
        saveStore: saveStore,
        
        getStatus: function () {
            return getStore().status;
        },
        updateStatus: function (newStatus) {
            const store = getStore();
            store.status = { ...store.status, ...newStatus };
            saveStore(store);
            return store.status;
        },
        
        getNotices: function () {
            return getStore().notices;
        },
        addNotice: function (notice) {
            const store = getStore();
            notice.id = 'notice-' + Date.now();
            store.notices.push(notice);
            saveStore(store);
            return notice;
        },
        updateNotice: function (noticeId, updatedFields) {
            const store = getStore();
            const idx = store.notices.findIndex(n => n.id === noticeId);
            if (idx !== -1) {
                store.notices[idx] = { ...store.notices[idx], ...updatedFields };
                saveStore(store);
                return store.notices[idx];
            }
            return null;
        },
        deleteNotice: function (noticeId) {
            const store = getStore();
            const idx = store.notices.findIndex(n => n.id === noticeId);
            if (idx !== -1) {
                const deleted = store.notices.splice(idx, 1)[0];
                saveStore(store);
                return deleted;
            }
            return null;
        },

        getDocuments: function () {
            return getStore().documents;
        },
        updateDocument: function (docKey, base64Data) {
            const store = getStore();
            store.documents[docKey] = base64Data;
            saveStore(store);
            return store.documents;
        },

        getInfo: function () {
            return getStore().info;
        },
        updateInfo: function (newInfo) {
            const store = getStore();
            store.info = { ...store.info, ...newInfo };
            saveStore(store);
            return store.info;
        }
    };
})();
