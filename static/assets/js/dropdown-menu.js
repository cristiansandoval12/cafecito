// dropdown_menu.js
document.addEventListener('DOMContentLoaded', function() {
    const profilePic = document.querySelector('.profile-pic');
    const dropdownMenu = document.querySelector('.dropdown-menu');

    profilePic.addEventListener('click', function(event) {
        event.stopPropagation(); // Evitar que se cierre el menú al hacer clic en la foto o nombre

        if (dropdownMenu.style.display === 'block') {
            dropdownMenu.style.display = 'none';
        } else {
            dropdownMenu.style.display = 'block';
        }
    });

    document.addEventListener('click', function(event) {
        if (dropdownMenu.style.display === 'block') {
            dropdownMenu.style.display = 'none';
        }
    });

    const informacionLink = document.querySelector('#informacion-link');
    informacionLink.addEventListener('click', function(event) {
        event.preventDefault();
        window.location.href = '{% url "informacion_usuario" %}';
    });
});