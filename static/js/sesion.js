window.addEventListener('DOMContentLoaded', iniciar);

function iniciar() {
    iniciadoPor();
}



let user;
async function iniciadoPor() {
    try {
        let respuesta = await fetch('/user')
        if (!respuesta) throw new Error('No se ha ejecutado en 1');
        let datos = await respuesta.json();
        let user=document.querySelector('.name > span');
        user.textContent=datos;
    } catch (error) {
        console.log(error);
    }
}
