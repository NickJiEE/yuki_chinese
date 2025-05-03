let startX = 0;

const profileImg = document.getElementById('profile-img');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');

let currentImageIndex = 0;

function switchImage(newIndex) {
    profileImg.classList.add('fade-out');

    setTimeout(() => {
        currentImageIndex = newIndex;
        profileImg.src = images[currentImageIndex];

        profileImg.onload = () => {
            profileImg.classList.remove('fade-out');
        };
    }, 200);
}

prevBtn.addEventListener('click', () => {
    const newIndex = (currentImageIndex - 1 + images.length) % images.length;
    switchImage(newIndex);
});

nextBtn.addEventListener('click', () => {
    const newIndex = (currentImageIndex + 1) % images.length;
    switchImage(newIndex);
});

profileImg.addEventListener('touchstart', (e) => {
    startX = e.touches[0].clientX;
});

profileImg.addEventListener('touchend', (e) => {
    const endX = e.changedTouches[0].clientX;
    const diffX = startX - endX;

    if (Math.abs(diffX) > 30) {
        const direction = diffX > 0 ? 1 : -1;
        const newIndex = (currentImageIndex + direction + images.length) % images.length;
        switchImage(newIndex);
    }
});

setTimeout(() => {
    const hint = document.querySelector('.swipe-hint');
    if (hint) {
        hint.style.transition = 'opacity 1s';
        hint.style.opacity = 0;
        setTimeout(() => hint.remove(), 1000);
    }
}, 1500);