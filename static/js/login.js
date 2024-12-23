import {mostrarNotificacao} from './mostrarNotific.js'

document.querySelector('.login-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData(this);
    const data = Object.fromEntries(formData.entries());

    fetch('/', { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Erro ao tentar fazer login');
        }
    })
    .then(result => {
        if (result.success) {
            sessionStorage.setItem('id_funcionario', result.id_funcionario)
            mostrarNotificacao("Login bem-sucessido", 'green')
            window.location.href = "/ponto";
        } else {
            mostrarNotificacao('Erro ao logar, verifique suas credenciais!', 'red')
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        mostrarNotificacao('Erro ao realizar o login', 'red')
    });
});
