document.addEventListener("DOMContentLoaded", () => {
    // Variables y elementos del DOM
    const btnJugar = document.getElementById("btnjugar");
    const ContenedorLetras = document.querySelector(".teclado");
    const palabradisplay = document.querySelector(".palabra-display");
    const FigAhorcado = document.querySelector(".figura img");
    const Modal = document.querySelector(".Modal");
    const AgainBtn = document.querySelector(".again");
    const Puntos1 = document.querySelector(".puntos1");
    const Pista = document.getElementById("pista");
    const overlayContainer = document.querySelector(".overlay-container");
    const inputUsuario = document.getElementById("txtusuario");
    const spanUsuarioNombre = document.getElementById("usuario_nombre");
    const ayudaIcon = document.getElementById("ayuda");
    const acertadoDiv = document.getElementById("acertados");
    const fallidoDiv = document.getElementById("fallidos");
    const cantIntentos = document.getElementById("cant_intentos");
    
    let APalabra = "",
      LIncorrectas = 0,
      LCorrectas = new Set(),
      puntuacion = 0,
      vidas = 3,
      aciertos = [],
      fallos = [],
      letraRevelada = false,
      ayudaUsada = false; // Nuevo estado para verificar si la ayuda ha sido usada
    
    const maxGuess = 6;
    const imagePath = "/static/images/";
    const wonImage = `${imagePath}gano.gif`;
    const lostImage = `${imagePath}perdio.gif`;
    
    const qwertyLayout = [
      ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
      ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
      ["Z", "X", "C", "V", "B", "N", "M"],
    ];
    
    // Función para crear el teclado
    function CrearTeclado() {
      qwertyLayout.forEach((fila) => {
        const divFila = document.createElement("div");
        divFila.className = "fila";
    
        fila.forEach((letra) => {
          const buttonIn = document.createElement("button");
          buttonIn.textContent = letra;
          buttonIn.dataset.letra = letra; // Añadir un atributo data
          divFila.appendChild(buttonIn);
          buttonIn.addEventListener("click", (e) => initGame(e.target, letra));
        });
    
        ContenedorLetras.appendChild(divFila);
      });
    }
    
    // Función para reiniciar el juego
    const resetGame = () => {
      if (!APalabra) {
        console.error("APalabra no está definido.");
        return;
      }
      LCorrectas.clear(); // Utiliza Set.clear() para eliminar todas las letras correctas
      LIncorrectas = 0;
      puntuacion = 0;
      FigAhorcado.src = `${imagePath}0.png`;
      ContenedorLetras.querySelectorAll("button").forEach(
        (button) => {
          button.disabled = false;
          button.classList.remove("correcto", "incorrecto");
        }
      );
      palabradisplay.innerHTML = APalabra.split("")
        .map(() => '<li class="letra"></li>')
        .join("");
      Puntos1.innerText = `Puntuación: ${puntuacion}`;
      cantIntentos.innerText = `Intentos: ${maxGuess - LIncorrectas}`;
      Modal.classList.remove("show");
      ayudaUsada = false; // Reiniciar el estado de ayuda al reiniciar el juego
    };
    
    // Función para reiniciar los botones
    const resetButtons = () => {
      ContenedorLetras.querySelectorAll("button").forEach((button) => {
        button.classList.remove("correcto", "incorrecto");
        button.disabled = false;
      });
    };
    
    // Función para obtener una pista aleatoria
    const getRandomP = () => {
      console.log(
        `Categoria ID: ${
          document.getElementById("txtcategoria").value
        }, Dificultad ID: ${document.getElementById("txtnivel").value}`
      );
      fetch(
        `/obtener_pista/?categoria_id=${
          document.getElementById("txtcategoria").value
        }&dificultad_id=${document.getElementById("txtnivel").value}`
      )
        .then((response) => response.json())
        .then((data) => {
          APalabra = data.palabra.toUpperCase(); // Convertir palabra a mayúsculas
          Pista.textContent = data.pista;
          resetGame();
          resetButtons();
        })
        .catch((error) => console.error("Error:", error));
    };
    
    // Función para manejar el botón de intentar de nuevo
    const againButtonHandler = () => {
      Modal.classList.remove("show");
      overlayContainer.style.display = "flex";
      setTimeout(() => {
        reiniciarJuego();
        AgainBtn.removeEventListener("click", againButtonHandler);
      }, 3000);
    };
    
    // Función para reiniciar el juego
    const reiniciarJuego = () => {
      vidas = 3;
      overlayContainer.style.display = "none";
      actualizarCorazones();
      getRandomP();
    };
    
    // Función para mostrar el resultado del juego
    const GaOv = (Win) => {
      setTimeout(() => {
        const ModalText = Win
          ? "¡Correcto! La palabra era: "
          : "La palabra correcta era: ";
        Modal.querySelector("img").src = Win ? wonImage : lostImage;
        Modal.querySelector("h4").innerText = `${
          Win ? "Felicidades" : "Perdiste"
        }`;
        Modal.querySelector("p").innerHTML = `${ModalText}<b>${APalabra}</b>`;
        Modal.classList.add("show");
    
        if (Win) {
          aciertos.push({ palabra: APalabra, puntaje: puntuacion });
        } else {
          fallos.push({ palabra: APalabra, puntaje: puntuacion });
          vidas--;
          actualizarCorazones();
          if (vidas === 0) {
            abandonarPartida(); // Aplicar la lógica de abandonar partida si se pierden todos los corazones
          }
        }
    
        mostrarResultados();
      }, 200);
    };
    
    // Función para mostrar resultados
    const mostrarResultados = () => {
      acertadoDiv.innerHTML = "";
      fallidoDiv.innerHTML = "";
    
      aciertos.forEach((acierto) => {
        const p = document.createElement("p");
        p.textContent = `${acierto.palabra} - Puntuación: ${acierto.puntaje}`;
        acertadoDiv.appendChild(p);
      });
    
      fallos.forEach((fallo) => {
        const p = document.createElement("p");
        p.textContent = `${fallo.palabra} - Puntuación: ${fallo.puntaje}`;
        fallidoDiv.appendChild(p);
      });
    };
    
    // Función para manejar el juego
    const initGame = (button, clickletra) => {
      if (!APalabra) {
        console.error("APalabra no está definido.");
        return;
      }
    
      clickletra = clickletra.toUpperCase(); // Convertir letra a mayúsculas
    
      if (APalabra.includes(clickletra)) {
        [...APalabra].forEach((letra, index) => {
          if (letra === clickletra) {
            LCorrectas.add(letra); // Usar Set.add() para agregar letras correctas
            const letrasDisplay = palabradisplay.querySelectorAll(".letra");
            letrasDisplay[index].innerText = letra;
            letrasDisplay[index].classList.add("guessed");
            button.classList.add("correcto");
            APuntuacion(10);
          }
        });
      } else {
        LIncorrectas++;
        FigAhorcado.src = `${imagePath}${LIncorrectas}.png`;
        button.classList.add("incorrecto");
        APuntuacion(-5);
      }
    
      // Actualizar el contador de intentos restantes
      cantIntentos.innerText = `Intentos: ${maxGuess - LIncorrectas}`;
    
      button.disabled = true;
    
      if (LIncorrectas === maxGuess) return GaOv(false);
      if (APalabra.split("").every((letra) => LCorrectas.has(letra)))
        return GaOv(true);
    };
    
    // Función para actualizar la puntuación
    function APuntuacion(puntos) {
      puntuacion += puntos;
      if (puntuacion < 0) {
        puntuacion = 0;
      }
      Puntos1.innerText = `Puntuación: ${puntuacion}`;
    }
    
    // Función para actualizar los corazones
    const actualizarCorazones = () => {
      const corazones = document.querySelectorAll(".fa-heart");
      corazones.forEach((corazon, index) => {
        corazon.style.display = index < vidas ? "inline-block" : "none";
      });
    };
    
    // Función para validar el input de usuario
    const validarUsuario = () => {
      const usuario = inputUsuario.value.trim();
      if (!usuario) {
        alert("Por favor, ingrese un nombre de usuario.");
        return false;
      }
      spanUsuarioNombre.textContent = usuario;
      return true;
    };
    
    // Función para abandonar partida
    const abandonarPartida = () => {
      const confirmar = confirm(
        "¿Estás seguro de que deseas abandonar la partida?"
      );
      if (confirmar) {
        location.reload(); // Recargar la página para reiniciar el juego
      }
    };
    
    // Función para proporcionar ayuda revelando una letra al azar
    const proporcionarAyuda = () => {
      if (ayudaUsada) {
          alert("Ya has usado la ayuda para esta palabra.");
          return;
      }

      // Encontrar letras que aún no han sido reveladas
      const letrasNoReveladas = [...APalabra].filter(
        (letra, index) => !LCorrectas.has(letra) && letra !== " "
    );

    if (letrasNoReveladas.length === 0) {
        alert("No hay más letras por revelar.");
        return;
    }
    
      // Elegir una letra al azar
      const letraAleatoria =
      letrasNoReveladas[Math.floor(Math.random() * letrasNoReveladas.length)];
    
      // Revelar la letra
      const letrasDisplay = palabradisplay.querySelectorAll(".letra");
      letrasDisplay.forEach((letraDisplay, index) => {
          if (APalabra[index] === letraAleatoria) {
              letraDisplay.innerText = letraAleatoria;
              letraDisplay.classList.add("guessed");
          }
      });
  
      LCorrectas.add(letraAleatoria);
      ayudaUsada = true; // Marcar la ayuda como usada
    
      // Desactivar el botón correspondiente en el teclado
      const botonLetra = ContenedorLetras.querySelector(`button[data-letra="${letraAleatoria}"]`);
    if (botonLetra) {
        botonLetra.disabled = true;
    }
    
    // Verificar si la palabra está completa
    if (APalabra.split("").every((letra) => LCorrectas.has(letra))) {
      GaOv(true);
  }
};

    // Inicializar el teclado y el juego
    CrearTeclado();
    btnJugar.addEventListener("click", () => {
      if (validarUsuario()) {
        getRandomP();
        // Cambiar el botón de jugar a abandonar partida
        btnJugar.textContent = "Abandonar partida";
        btnJugar.removeEventListener("click", () => {
          if (validarUsuario()) {
            getRandomP();
          }
        });
        btnJugar.addEventListener("click", abandonarPartida);
      }
    });
    
    AgainBtn.addEventListener("click", getRandomP);
    ayudaIcon.addEventListener("click", proporcionarAyuda);
  });
  