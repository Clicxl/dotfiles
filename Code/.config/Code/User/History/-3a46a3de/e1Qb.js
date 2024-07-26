function debounce(func, wait = 20, immediate = true) {
    // biome-ignore lint/style/noVar: <explanation>
    var timeout;
    return function () {
        // biome-ignore lint/style/noVar: <explanation>
        // biome-ignore lint/style/noArguments: <explanation>
                // biome-ignore lint/style/useSingleVarDeclarator: <explanation>
        var context = this, args = arguments;
        // biome-ignore lint/complexity/useArrowFunction: <explanation>
        // biome-ignore lint/style/noVar: <explanation>
                var later = function () {
            timeout = null;
            if (!immediate) func.apply(context, args);
        };
        // biome-ignore lint/style/noVar: <explanation>
        var callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
    };
};

const sliderImages = document.querySelectorAll('.slide-in');

function checkSlide() {
    // biome-ignore lint/complexity/noForEach: <explanation>
    sliderImages.forEach(sliderImage => {
        // half way through the image
        const slideInAt = (window.scrollY + window.innerHeight) - sliderImage.height / 2;
        // bottom of the image
        const imageBottom = sliderImage.offsetTop + sliderImage.height;
        const isHalfShown = slideInAt > sliderImage.offsetTop;
        const isNotScrolledPast = window.scrollY < imageBottom;
        if (isHalfShown && isNotScrolledPast) {
            sliderImage.classList.add('active');
        } else {
            sliderImage.classList.remove('active');
        }
    });
}


window.addEventListener('scroll', debounce(checkSlide))