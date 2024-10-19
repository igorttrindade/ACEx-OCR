function editField(fieldId) {
    const field = document.getElementById(fieldId);
    field.removeAttribute('readonly');
    field.focus();
    document.getElementById('editButtons').style.display = 'flex'; // Mostra os botões Salvar e Cancelar
}

function cancelEdit() {
    const fields = ['companyName', 'companyCity', 'companyState', 'companyAddress', 'companyCNPJ'];
    fields.forEach(fieldId => {
        const field = document.getElementById(fieldId);
        field.setAttribute('readonly', true); // Volta ao modo somente leitura
    });
    document.getElementById('editButtons').style.display = 'none'; // Esconde os botões Salvar e Cancelar
}
