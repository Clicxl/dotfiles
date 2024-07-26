function debounce(func, wait = 20, immediate = true) {
    let timeout;
    return function () {
        const args = arguments;
        const later = () => {
            timeout = null;
            if (!immediate) func.apply(this, args);
        };
        const callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(this, args);
    };
}

const sliderImages = document.querySelectorAll(".slider-in")

function checkSlide(e) {
    // biome-ignore lint/complexity/noForEach: <explanation>
    sliderImages.forEach(sliderImage => {
        const slideInAt = (window.scrollY / window.innerHeight) - sliderImage.height / 2;

        const imageBottom = sliderImage.offsetTop + sliderImage.height;
        const isHalfShown = slideInAt > sliderImage.offsetTop;
        const isNotScrolledPast = window.scrollY < imageBottom;

        if (isHalfShown && isNotScrolledPast) {
            console.log("Active");
            sliderImage.classList.add('active')
        }else {
            sliderImage.classList.remove('active');
        }
    })

}
47   │     function debounce(func, wait = 20, immediate = true) {
    48   │       var timeout;
    49   │       return function () {
        50   │         var context = this, args = arguments;
        51   │         var later = function () {
            52   │           timeout = null;
            53   │           if (!immediate) func.apply(context, args);
            54   │
        };
        55   │         var callNow = immediate && !timeout;
        56   │         clearTimeout(timeout);
        57   │         timeout = setTimeout(later, wait);
        58   │         if (callNow) func.apply(context, args);
        59   │
    };
    60   │
};
61   │
62   │     const sliderImages = document.querySelectorAll('.slide-in');
63   │
64   │     function checkSlide() {
    65   │       sliderImages.forEach(sliderImage => {
        66   │         // half way through the image
        67   │         const slideInAt = (window.scrollY + window.innerHeight) - sliderImage.height / 2;
        68   │         // bottom of the image
        69   │         const imageBottom = sliderImage.offsetTop + sliderImage.height;
        70   │         const isHalfShown = slideInAt > sliderImage.offsetTop;
        71   │         const isNotScrolledPast = window.scrollY < imageBottom;
        72   │         if (isHalfShown && isNotScrolledPast) {
            73   │           sliderImage.classList.add('active');
            74   │
        } else {
            75   │           sliderImage.classList.remove('active');
            76   │        }

    });

}

    window.addEventListener('scroll', debounce(checkSlide));
window.addEventListener('scroll', debounce(checkSlide))