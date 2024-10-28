import { mostrarNotificacao } from './mostrarNotific.js';

document.getElementById('batidaPontoForm').addEventListener('submit', function (event){
    event.preventDefault()
    registrarBatida()
})

function registrarBatida() {
    const dataAtual = new Date().toISOString();
    const id_funcionario = sessionStorage.getItem('id_funcionario')
    fetch('/ponto', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ horario: dataAtual,id_funcionario:id_funcionario })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao registrar a batida de ponto');
        }
        return response.json();
    })
    .then(data => {
        mostrarNotificacao("Batida realizada com sucesso!", 'success');
    })
    .catch(error => {
        mostrarNotificacao("Erro ao realizar a batida!", 'error');
        console.error('Error:', error);
    });
}