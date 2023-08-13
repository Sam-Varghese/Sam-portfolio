(function (C, A, L) {
    let p = function (a, ar) {
        a.q.push(ar);
    };
    let d = C.document;
    C.Cal =
        C.Cal ||
        function () {
            let cal = C.Cal;
            let ar = arguments;
            if (!cal.loaded) {
                cal.ns = {};
                cal.q = cal.q || [];
                d.head.appendChild(d.createElement("script")).src = A;
                cal.loaded = true;
            }
            if (ar[0] === L) {
                const api = function () {
                    p(api, arguments);
                };
                const namespace = ar[1];
                api.q = api.q || [];
                typeof namespace === "string"
                    ? (cal.ns[namespace] = api) && p(api, ar)
                    : p(cal, ar);
                return;
            }
            p(cal, ar);
        };
})(window, "https://app.cal.com/embed/embed.js", "init");
Cal("init", { origin: "https://app.cal.com" });

Cal("inline", {
    elementOrSelector: "#my-cal-inline",
    calLink: "sam-varghese/15min",
});

Cal("ui", {
    styles: { branding: { brandColor: "#0b0c10" } },
    hideEventTypeDetails: false,
});




var introNavItem = document.getElementById("introNavItem");
educationNavItem = document.getElementById("educationNavItem");
achievementsNavItem = document.getElementById("achievementsNavItem");
certificationsNavItem = document.getElementById("certificationsNavItem");
projectsNavItem = document.getElementById("projectsNavItem");
contactNavItem = document.getElementById("contactNavItem");

introNavItem.onclick = () => {
    document.getElementById("nameHeading").scrollIntoView();
};
educationNavItem.onclick = () => {
    document.getElementById("educationPageHeading").scrollIntoView();
};
achievementsNavItem.onclick = () => {
    document.getElementById("achievementsHeadingPage").scrollIntoView();
};
certificationsNavItem.onclick = () => {
    document.getElementById("certificationsPageHeading").scrollIntoView();
};
newsNavItem.onclick = () => {
    document.getElementById("newsPageHeading").scrollIntoView();
};
projectsNavItem.onclick = () => {
    document.getElementById("projectsPageHeading").scrollIntoView();
};
contactNavItem.onclick = () => {
    document.getElementById("contactPageHeading").scrollIntoView();
};

//   Animation on visiblity

// Create an Intersection Observer instance
const observer = new IntersectionObserver(
    (entries, observer) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("applyAnimation");
                observer.unobserve(entry.target);
            }
        });
    },
    { threshold: 0.5 }
);

//   // Observe the target element
//   const target = document.querySelector('.heading');
//   observer.observe(target);

const headings = document.querySelectorAll(".heading");
headings.forEach((heading) => {
    observer.observe(heading);
});

// Animations for all images

const observer1 = new IntersectionObserver(
    (entries, observer) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("applyImageAnimations");
                entry.target.style.opacity = 1;
                observer.unobserve(entry.target);
            }
        });
    },
    { threshold: 0.1 }
);

const images = document.querySelectorAll("img");
images.forEach((image) => {
    observer1.observe(image);
});

window.dataLayer = window.dataLayer || [];
function gtag() {
    dataLayer.push(arguments);
}
gtag("js", new Date());

gtag("config", "G-R1NXRPRLNV");