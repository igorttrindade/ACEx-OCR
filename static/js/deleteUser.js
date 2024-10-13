import { mostrarNotificacao } from "./mostrarNotific.js";

export function excluirUsuario(userId) {
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