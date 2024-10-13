function registrarBatida() {
    fetch('/batida-de-ponto', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            usuarioId: '123', 
        }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao registrar a batida de ponto');
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('responseMessage').innerText = "Batida de ponto registrada com sucesso!";
    })
    .catch(error => {
        document.getElementById('responseMessage').innerText = error.message;
        console.error('Error:', error);
    });
}
