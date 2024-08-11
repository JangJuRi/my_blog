/*!
* Start Bootstrap - Clean Blog v6.0.9 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            mainNav.classList.remove('is-visible');
            setTimeout(() => {
                mainNav.classList.remove('is-fixed');
            }, 200);
        } else {
            // Scrolling Down
            if (currentTop > headerHeight) {
                mainNav.classList.add('is-fixed');
                mainNav.classList.add('is-visible');
            }
        }
        scrollPos = currentTop;
    });
})
