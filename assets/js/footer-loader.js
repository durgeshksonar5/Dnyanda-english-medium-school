document.addEventListener("DOMContentLoaded", function () {
    const placeholder = document.getElementById("footer-placeholder");
    if (!placeholder) return;

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

    fetch(prefix + "components/footer.html")
        .then(response => {
            if (!response.ok) {
                throw new Error("Failed to load footer: " + response.statusText);
            }
            return response.text();
        })
        .then(html => {
            // Inject footer content into placeholder
            placeholder.outerHTML = html;
        })
        .catch(err => {
            console.error("Error loading centralized footer:", err);
        });
});
