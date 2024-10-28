const containerDropdown = document.querySelector('.containerdropdown');
const dropdownMenu = document.querySelector('.dropdownMenu');
containerDropdown.addEventListener('mouseenter', function () {
    dropdownMenu.classList.add('active');
});
containerDropdown.addEventListener('mouseleave', function () {
    dropdownMenu.classList.remove('active');
});

