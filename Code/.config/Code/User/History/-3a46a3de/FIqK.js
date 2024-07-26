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

const checkSlide = (e) => {
    // biome-ignore lint/complexity/noForEach: <explanation>
    sliderImages.forEach(sliderImage => {
        const slideInAt = (window.scrollY / window.innerHeight) - sliderImage.height / 2;

        const imageBottom = sliderImage.offsetTop + sliderImage.height;
        const isHalfShown = slideInAt > sliderImage.offsetTop;
        const isNotScrolledPast = window.scrollY < imageBottom;

        if (isHalfShown && isNotScrolledPast) {
            sliderImage.classList.add('active')
        }else {
            sliderImage.classList.remove('active');
        }
    })

}

window.addEventListener('scroll', debounce(checkSlide))