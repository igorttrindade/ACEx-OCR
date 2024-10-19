import {mostrarNotificacao} from './mostrarNotific.js'

document.addEventListener('DOMContentLoaded', () => {
    const createFuncForm = document.querySelector('#employeeForm')
    if (createFuncForm) {
        createFuncForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const formData = new FormData(this);
            const data = Object.fromEntries(formData.entries());

            fetch('/funcionario/cadastro-funcionarios', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })
            .then(response => {
                if (!response.ok) {
                    return response.json().then(err => {
                        throw new Error(err.error || 'Erro na criação do funcionário');
                    });
                }
                return response.json();
            })
            .then(data => {
                mostrarNotificacao("Funcionário criado com sucesso!", 'green');
                window.location.reload();
            })
            .catch((error) => {
                mostrarNotificacao("Erro ao criar funcionário!", "red");
                console.error('Error:', error);
            });
        });
    }
});
