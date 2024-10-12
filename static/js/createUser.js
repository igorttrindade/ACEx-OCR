document.addEventListener('DOMContentLoaded', function() {
    const createUserForm = document.getElementById('createUserForm');
    
    if (createUserForm) {
        createUserForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Evita o envio padrão do formulário

            const formData = new FormData(this);
            const data = Object.fromEntries(formData.entries()); // Converte FormData para objeto

            // Envia os dados para a rota do Flask
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
                const responseMessage = document.getElementById('responseMessage');
                responseMessage.innerText = 'Usuário criado com sucesso!';
                responseMessage.className = 'notification success';
                responseMessage.style.display = 'block';
                setTimeout(() => {
                    window.location.reload();
                }, 5000);
            })
            .catch((error) => {
                const responseMessage = document.getElementById('responseMessage');
                responseMessage.innerText = 'Erro ao criar usuário.';
                responseMessage.className = 'notification error'; // Adiciona a classe de erro
                responseMessage.style.display = 'block'; // Mostra a caixa de notificação
                
                // Oculta a notificação após 5 segundos
                setTimeout(() => {
                    responseMessage.style.display = 'none';
                }, 5000);
                
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
                // Se a resposta não for ok, trate o erro
                return response.json().then(err => Promise.reject(err));
            }
            return response.json(); // Retorna a resposta como JSON se for bem-sucedida
        })
        .then(data => {
            mostrarNotificacao(data.message, "green"); // Mostra mensagem de sucesso
            // Recarrega a página após a exclusão
            setTimeout(() => {
                window.location.reload();
            }, 5000);
        })
        .catch(err => {
            // Trata erros retornados pelo servidor
            mostrarNotificacao(err.error || "Erro ao excluir usuário.", "red");
            console.error('Erro:', err);
        });
    }
}
function mostrarNotificacao(mensagem, cor) {
    const responseMessage = document.getElementById('responseMessage');
    responseMessage.innerText = mensagem;
    responseMessage.style.backgroundColor = cor; // Altera a cor do fundo conforme o status
    responseMessage.style.display = 'block'; // Torna a notificação visível
    setTimeout(() => {
        responseMessage.style.display = 'none';
    }, 5000);
}
