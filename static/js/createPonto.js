document.addEventListener("DOMContentLoaded", () => {
    const inicioInput = document.getElementById("periodo-inicio");
    const fimInput = document.getElementById("periodo-fim");
    const diasContainer = document.getElementById("dias-container");

    if (inicioInput && fimInput) {
        inicioInput.addEventListener("change", generateFields);
        fimInput.addEventListener("change", generateFields);
    }

    function generateFields() {
        const inicio = new Date(inicioInput.value);
        const fim = new Date(fimInput.value);

        if (!isNaN(inicio) && !isNaN(fim) && fim >= inicio) {
            diasContainer.innerHTML = "";
            const dias = Math.floor((fim - inicio) / (1000 * 60 * 60 * 24)) + 1;

            for (let i = 0; i < dias; i++) {
                const dia = new Date(inicio);
                dia.setDate(inicio.getDate() + i);

                const diaDiv = document.createElement("div");
                diaDiv.classList.add("dia");
                diaDiv.innerHTML = `
                    <h4>Dia ${dia.toLocaleDateString()}</h4>
                    <label>Entrada:</label>
                    <input type="time" name="entrada_${i + 1}">
                    
                    <label>Início Intervalo:</label>
                    <input type="time" name="inicio_intervalo_${i + 1}">
                    
                    <label>Término Intervalo:</label>
                    <input type="time" name="termino_intervalo_${i + 1}">
                    
                    <label>Saída:</label>
                    <input type="time" name="saida_${i + 1}">
                `;

                diasContainer.appendChild(diaDiv);
            }
        }
    }
});
