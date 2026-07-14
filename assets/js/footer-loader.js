document.addEventListener("DOMContentLoaded", function () {
    // Dynamically calculate path prefix based on the script's src attribute
    let prefix = "";
    const script = document.querySelector('script[src*="footer-loader.js"]');
    if (script) {
        const src = script.getAttribute("src");
        const idx = src.indexOf("assets/js/footer-loader.js");
        if (idx > 0) {
            prefix = src.substring(0, idx);
        }
    }

    // 1. Load footer if placeholder exists
    const placeholder = document.getElementById("footer-placeholder");
    if (placeholder) {
        fetch(prefix + "components/footer.html")
            .then(response => {
                if (!response.ok) {
                    throw new Error("Failed to load footer: " + response.statusText);
                }
                return response.text();
            })
            .then(html => {
                placeholder.outerHTML = html;
            })
            .catch(err => {
                console.error("Error loading centralized footer:", err);
            });
    }

    // 2. Load floating action buttons dynamically
    if (!document.querySelector(".floating-contact-wrap")) {
        fetch(prefix + "components/floating-buttons.html")
            .then(response => {
                if (!response.ok) {
                    throw new Error("Failed to load floating buttons: " + response.statusText);
                }
                return response.text();
            })
            .then(html => {
                const tempDiv = document.createElement("div");
                tempDiv.innerHTML = html.trim();
                if (tempDiv.firstElementChild) {
                    document.body.appendChild(tempDiv.firstElementChild);
                }
            })
            .catch(err => {
                console.error("Error loading centralized floating buttons:", err);
            });
    }

    // 3. Load Leads Management Integration script dynamically
    const leadScript = document.createElement("script");
    leadScript.src = prefix + "assets/js/lead-integration.js";
    document.body.appendChild(leadScript);
});
