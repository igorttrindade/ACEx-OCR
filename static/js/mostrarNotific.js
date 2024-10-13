export function mostrarNotificacao(mensagem, cor) {
    const responseMessage = document.getElementById('responseMessage');
    responseMessage.innerText = mensagem;
    responseMessage.style.backgroundColor = cor; // Altera a cor do fundo conforme o status
    responseMessage.style.display = 'block'; // Torna a notificação visível
    setTimeout(() => {
        responseMessage.style.display = 'none';
    }, 5000);
    window.location.reload()
}