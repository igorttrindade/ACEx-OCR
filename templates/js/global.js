const perfil = document.querySelector('.circle-perfil')
perfil.addEventListener('click', function () {
    const dropdownMenu = document.querySelector('.dropdownMenu');
    // Alterna a classe 'active' para mostrar/esconder o menu
    dropdownMenu.classList.toggle('active');
});