function toggleNav() {
    const sideNav = document.getElementById("sideNav");
    const navToggleBtn = document.getElementById("navToggleBtn");
    if (sideNav.style.width === "200px") {
        sideNav.style.width = "0";
        navToggleBtn.innerHTML = "☰";
    } else {
        sideNav.style.width = "200px";
        navToggleBtn.innerHTML = "x";
    }
    navToggleBtn.classList.toggle('open-btn');
    navToggleBtn.classList.toggle('close-btn');
}

//JS for search bar animation
document.addEventListener('DOMContentLoaded', function () {
    const searchIcon = document.getElementById('search-icon');
    const searchInput = document.getElementById('search-input');
    const barSearchIcon = document.getElementById('bar-search-icon');
    const barSearchInput = document.getElementById('bar-search-input');
    searchIcon.addEventListener('click', function () {
        searchInput.classList.toggle('expanded');

    });
    barSearchIcon.addEventListener('click', function () {
        barSearchInput.classList.toggle('expanded');

    });

    searchInput.addEventListener('focus', function () {
        this.placeholder = '';
    });

    barSearchInput.addEventListener('focus', function () {
        this.placeholder = '';
    });
    searchInput.addEventListener('blur', function () {
        if (this.value === '') {
            this.placeholder = 'Search for movie...';
        }
    });
    barSearchInput.addEventListener('blur', function () {
        if (this.value === '') {
            this.placeholder = 'Search for movie...';
        }
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const textarea = document.querySelector('.gpt-input-textarea');
    if (textarea) {
        textarea.addEventListener('input', function () {
            this.style.height = 'auto';
            this.style.height = this.scrollHeight + 'px';
        });
    }
});
