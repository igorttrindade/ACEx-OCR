document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.action-button');
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            window.location.href = button.dataset.url;
        });
    });
});
