function debounce(func, wait = 20, immediate = true) {
      let timeout;
      return function() {
        let args = arguments;
        let later = () => {
          timeout = null;
          if (!immediate) func.apply(this, args);
        };
        let callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(this, args);
      };
    }