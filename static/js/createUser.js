import { mostrarNotificacao } from './mostrarNotific.js'
import { excluirUsuario } from './deleteUser.js'

document.addEventListener('DOMContentLoaded', function() {
    const createUserForm = document.querySelector('#createUserForm')
    const deleteUser = document.querySelectorAll('#btn_delete')
    if (createUserForm) {
        createUserForm.addEventListener('submit', function(event) {
            event.preventDefault()

            const formData = new FormData(this)
            const data = Object.fromEntries(formData.entries())
            fetch('/usuarios/criar-usuario', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Erro na criação do usuário')
                }
                return response.json()
            })
            .then(data => {
                mostrarNotificacao("Usuário criado com sucesso!", 'green')
                window.location.reload()
            })
            .catch((error) => {
                mostrarNotificacao("Erro ao criar usuário!","red")
                console.error('Error:', error);
            });
        });
    }
    deleteUser.forEach(button => {
        button.addEventListener('click', () => {
            const userId = button.getAttribute('data-user-id')
            excluirUsuario(userId)
        })
    })
});
