function debounce(func, wait = 20, immediate = true) {
      let timeout;
      return function() {
        let context = this;
        let args = arguments;
        let later = () => {
          timeout = null;
          if (!immediate) func.apply(context, args);
        };
        let callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
    };
}

const sliderImages = document.querySelectorAll(".slider-in")

const checkSlide = (e) => {

}

