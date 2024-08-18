// static/js/binary_operations.js

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('binaryForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Evitar el envío del formulario

        // Obtener los valores de los inputs
        const binary1 = document.getElementById('binary1').value;
        const binary2 = document.getElementById('binary2').value;

        // Validar que los inputs solo contengan caracteres binarios
        if (!/^[01]+$/.test(binary1) || !/^[01]+$/.test(binary2)) {
            alert('Por favor, ingrese solo números binarios (0 y 1).');
            return;
        }

        // Convertir los números binarios a enteros
        const num1 = parseInt(binary1, 2);
        const num2 = parseInt(binary2, 2);

        // Realizar las operaciones
        const sum = (num1 + num2).toString(2); // Suma y convertir de vuelta a binario
        const product = (num1 * num2).toString(2); // Multiplicación y convertir de vuelta a binario

        // Mostrar los resultados
        document.getElementById('sumResult').textContent = 'Suma: ' + sum;
        document.getElementById('productResult').textContent = 'Multiplicación: ' + product;
    });
});
