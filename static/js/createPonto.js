document.addEventListener("DOMContentLoaded", () => {
    const inicioInput = document.getElementById("periodo-inicio");
    const fimInput = document.getElementById("periodo-fim");
    const diasContainer = document.getElementById("dias-container");
    const salvarButton = document.getElementById("salvar-folha");

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
                    <input type="time" name="saida_${i + 1}">`;

                diasContainer.appendChild(diaDiv);
            }
        }
    }

    salvarButton.addEventListener("click", async () => {
        const matricula_func = sessionStorage.getItem('id_funcionario')
        const periodoInicio = document.getElementById("periodo-inicio").value
        const periodoFim = document.getElementById("periodo-fim").value

        let filePath = document.getElementById("upload-pdf").files[0]
        if (!filePath) {
            alert('Por favor, faça o upload de um arquivo PDF')
            return
        }

        let idLinha
        try {
            const response = await fetch('/funcionario/listar-funcionarios/ultima-linha')
            const data = await response.json()
            if (response.ok) {
                idLinha = data.ultimo_id_linha + 1
            } else {
                console.error(data.error)
                return
            }
        } catch (error) {
            console.error('Erro ao buscar a última linha:', error)
            return
        }

        const registros = []
        const diasInputs = document.querySelectorAll("#dias-container .dia")

        diasInputs.forEach((diaDiv, index) => {
            const diaText = diaDiv.querySelector('h4').textContent
            const diaDate = new Date(diaText)

            const entrada = diaDiv.querySelector(`input[name="entrada_${index + 1}"]`).value
            const inicioIntervalo = diaDiv.querySelector(`input[name="inicio_intervalo_${index + 1}"]`).value
            const terminoIntervalo = diaDiv.querySelector(`input[name="termino_intervalo_${index + 1}"]`).value
            const saida = diaDiv.querySelector(`input[name="saida_${index + 1}"]`).value

            const hrTrabalhada = calcularHoraTrabalhada(saida, entrada)

            registros.push({
                matricula_func: matricula_func,
                id_linha: idLinha,
                entrada_funcionario: entrada,
                inicio_intervalo: inicioIntervalo,
                termino_intervalo: terminoIntervalo,
                hora_trabalhada: hrTrabalhada,
                dia_ponto: diaDate.getDate(),
                mes_ponto: diaDate.getMonth() + 1,
                ano_ponto: diaDate.getFullYear(),
                arquivo_ponto: filePath.name,
                periodo_inicio: periodoInicio,
                periodo_fim: periodoFim
            })
            idLinha++
        })

        const response = await fetch('/funcionario/listar-funcionarios/folha-ponto', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(registros)
        })

        const result = await response.json()
        if (response.ok) {
            alert(result.message)
        } else {
            alert(result.error || 'Erro ao salvar a folha de ponto')
        }
    })

})

function calcularHoraTrabalhada(entrada, saida) {
    const entradaDate = new Date(`1970-01-01T${entrada}:00`);
    const saidaDate = new Date(`1970-01-01T${saida}:00`);
    const horaTrabalhada = (saidaDate - entradaDate) / (1000 * 60 * 60);
    return horaTrabalhada;
}
