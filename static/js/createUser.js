import { mostrarNotificacao } from './mostrarNotific';

document.addEventListener('DOMContentLoaded', function() {
    const createUserForm = document.getElementById('createUserForm');
    
    if (createUserForm) {
        createUserForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const formData = new FormData(this);
            const data = Object.fromEntries(formData.entries()); 
            fetch('/usuarios/criar-usuario', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Erro na criação do usuário');
                }
                return response.json();
            })
            .then(data => {
                mostrarNotificacao("Usuário criado com sucesso!", 'green')
            })
            .catch((error) => {
                mostrarNotificacao("Erro ao criar usuário!","red")
                console.error('Error:', error);
            });
        });
    }
});
function excluirUsuario(userId) {
    if (confirm("Tem certeza que deseja excluir este usuário?")) {
        fetch(`/usuarios/excluir/${userId}`, {
            method: 'DELETE',
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => Promise.reject(err));
            }
            return response.json();
        })
        .then(data => {
            mostrarNotificacao(data.message, "green");
        })
        .catch(err => {
            mostrarNotificacao(err.error || "Erro ao excluir usuário.", "red");
            console.error('Erro:', err);
        });
    }
}

