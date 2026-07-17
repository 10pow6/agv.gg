// AGV site behavior: mobile nav, colony dialogs, scroll reveal.

(function () {
    "use strict";

    // Mobile nav toggle
    var toggle = document.querySelector(".nav-toggle");
    var links = document.querySelector(".nav-links");
    if (toggle && links) {
        toggle.addEventListener("click", function () {
            var open = links.classList.toggle("open");
            toggle.setAttribute("aria-expanded", open ? "true" : "false");
        });
        links.addEventListener("click", function (event) {
            if (event.target.closest("a")) {
                links.classList.remove("open");
                toggle.setAttribute("aria-expanded", "false");
            }
        });
    }

    // Colony dialogs (native <dialog>)
    document.querySelectorAll("[data-dialog]").forEach(function (button) {
        var dialog = document.getElementById(button.dataset.dialog);
        if (!dialog) return;
        button.addEventListener("click", function () {
            dialog.showModal();
        });
    });

    document.querySelectorAll("dialog.colony-dialog").forEach(function (dialog) {
        dialog.querySelectorAll(".dialog-close").forEach(function (button) {
            button.addEventListener("click", function () {
                dialog.close();
            });
        });
        // Click on the backdrop closes the dialog.
        dialog.addEventListener("click", function (event) {
            if (event.target === dialog) dialog.close();
        });
    });

    // Scroll reveal
    var revealed = document.querySelectorAll(".reveal");
    if ("IntersectionObserver" in window) {
        var observer = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("visible");
                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.12 }
        );
        revealed.forEach(function (el) {
            observer.observe(el);
        });
    } else {
        revealed.forEach(function (el) {
            el.classList.add("visible");
        });
    }
})();
