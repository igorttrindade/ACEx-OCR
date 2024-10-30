import { mostrarNotificacao } from './mostrarNotific.js';

document.getElementById('batidaPontoForm').addEventListener('submit', function (event){
    event.preventDefault()
    registrarBatida()
})

async function registrarBatida() {
    try {
        const response = await fetch("/ponto", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ horario: new Date().toISOString() })
        });
        
        const data = await response.json();
        document.getElementById("responseMessage").textContent = data.message;
        
        if (response.ok) {
            location.reload(); 
        }
    } catch (error) {
        console.error("Erro ao registrar batida:", error);
        document.getElementById("responseMessage").textContent = "Erro ao registrar batida de ponto.";
    }
}
