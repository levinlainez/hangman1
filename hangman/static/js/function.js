document.addEventListener('DOMContentLoaded', () => {
const qwertyLayout = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
];

const ContenedorLetras = document.querySelector('.teclado');

function CrearTeclado() {
    qwertyLayout.forEach(fila => {
        const divFila = document.createElement('div');
        divFila.className = 'fila';

        fila.forEach(letra => {
            const buttonIn = document.createElement('button');
            buttonIn.textContent = letra;
            divFila.appendChild(buttonIn);
            buttonIn.addEventListener("click", e => initGame(e.target, letra));
        });

        ContenedorLetras.appendChild(divFila);
    });
}

CrearTeclado();
});

document.addEventListener('DOMContentLoaded', () => {
    const Startbtn = document.querySelector('.btnjugar');
    const overlaycompleto = document.querySelector('.overlay-container');
    Startbtn.addEventListener('click', () => {
        overlaycompleto.style.display = 'flex'; 
       setTimeout(() => {
            overlaycompleto.style.display = 'none';
        }, 3000); 
    });
  });