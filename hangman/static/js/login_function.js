function showRegisterForm() {
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('register-form').style.display = 'block';
}

function showLoginForm() {
    document.getElementById('register-form').style.display = 'none';
    document.getElementById('login-form').style.display = 'block';
}
function login() {
    const usuario = document.getElementById('usuario').value;
    const password = document.getElementById('login-password').value;

    fetch('/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ usuario, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Inicio de sesión exitoso');
            window.location.href = data.redirect_url;  // Redirige usando la URL recibida del backend
        } else {
            alert('Error al iniciar sesión: ' + data.message);
        }
    })
    .catch(error => console.error('Error:', error));
}

function register() {
    const usuario = document.getElementById('registro-usuario').value;
    const password = document.getElementById('registro-contra').value;

    fetch('/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ usuario, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Registro exitoso');
            showLoginForm();  // Muestra el formulario de login después del registro
        } else {
            alert('Error al registrarse: ' + data.message);
        }
    })
    .catch(error => console.error('Error:', error));
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}