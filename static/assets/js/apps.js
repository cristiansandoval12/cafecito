// app.js
document.getElementById("dataForm").addEventListener("submit", function(event) {
    event.preventDefault();

    // Obtener los valores ingresados en el formulario
    const name = document.querySelector('input[name="name"]').value;
    const status = document.querySelector('input[name="status"]').value;
    const date = document.querySelector('input[name="date"]').value;
    const price = document.querySelector('input[name="price"]').value;

    // Crear una nueva fila en la tabla con los datos ingresados
    const newRow = document.createElement("tr");
    newRow.innerHTML = `
        <td>${document.getElementById("salesTable").rows.length}</td>
        <td class="txt-oflo">${name}</td>
        <td>${status}</td>
        <td class="txt-oflo">${date}</td>
        <td><span class="${price < 0 ? 'text-danger' : 'text-success'}">$${Math.abs(price)}</span></td>
    `;

    // Agregar la nueva fila al final de la tabla
    document.getElementById("salesTable").appendChild(newRow);

    // Limpiar los campos del formulario
    document.getElementById("dataForm").reset();
});