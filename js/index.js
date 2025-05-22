// ---------------------------first slider-------------------
const swiper = new Swiper('.swiper', {
    direction: 'horizontal',
    loop: true,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});

// --------------------------flower effect-------------------
const showFlowerShower = () => {
    const slider = document.getElementById('slide');
    for (let i = 0; i < 20; i++) {
        const flower = document.createElement('div');
        flower.className = 'flower';
        flower.textContent = ['🌸', '🌼', '🌺',][Math.floor(Math.random() * 3)];
        flower.style.left = Math.random() * 100 + '%';
        flower.style.top = '-20px';
        flower.style.fontSize = `${16 + Math.random() * 16}px`;
        slider.appendChild(flower);
        setTimeout(() => flower.remove(), 2000);
    }
}

// -------------------------hamburger-----------------------
const openNav = () => {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("hamburger").style.marginLeft = "250px";
}

const closeNav = () => {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("hamburger").style.marginLeft = "0";
}

// ---------------------slider two-------------------------
const swiperTwo = new Swiper('.mySwiperTwo', {
    loop: true,
});

// -------------------------mark effect------------------------
const goToSlide = (index) => {
    swiperTwo.slideToLoop(index);
    const images = document.querySelectorAll('.gallery img');
    images.forEach(img => {
        img.addEventListener('click', () => {
            images.forEach(i => i.classList.remove('dimmed'));
            images.forEach(i => i.classList.add('usual'));
            img.classList.remove('usual');
            img.classList.add('dimmed');
        });
    });
}

// ----------------------slider three-----------------------
const swiperThree = new Swiper('.mySwiperThree', {
    loop: true,
    breakpoints: {
        375: {
            slidesPerView: 0.45,
        },
        630: {
            slidesPerView: 0.6,
        },
        768: {
            slidesPerView: 0.75,
        },
        1024: {
            slidesPerView: 1,
        },
    },
});

// -----------------------slider four-----------------------
const swiperFour = new Swiper('.mySwiperFour', {
    loop: true,
    breakpoints: {

        375: {
            slidesPerView: 0.45,
        },
        480: {
            slidesPerView: 0.5,
        },
        767: {
            slidesPerView: 0.6,
        },
        1024: {
            slidesPerView: 1,
        },
    },
})

// ----------------------slider three-----------------------
const swiperFive = new Swiper('.mySwiperFive', {
    loop: true,
    breakpoints: {
        375: {
            slidesPerView: 0.5,
        },
        630: {
            slidesPerView: 0.6,
        },
        768: {
            slidesPerView: 0.75,
        },
        1024: {
            slidesPerView: 1,
        },
    },
});

// -------------------toggle button-------------------------
const btn1 = document.getElementById('btn1');
const btn2 = document.getElementById('btn2');

function toggleButtons(activeBtn, inactiveBtn) {
    activeBtn.classList.remove('white');
    activeBtn.classList.add('black');

    inactiveBtn.classList.remove('black');
    inactiveBtn.classList.add('white');
}

btn1.addEventListener('click', () => {
    toggleButtons(btn1, btn2);
});

btn2.addEventListener('click', () => {
    toggleButtons(btn2, btn1);
});