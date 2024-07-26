function debounce(func, wait = 20, immediate = true) {
      let timeout;
      return function() {
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
    sliderImages.forEach(sliderImage => {
        const sliderInAt = (window/s     )
    })

}

window.addEventListener('scroll',debounce(checkSlide))