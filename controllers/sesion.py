from database.migrations.conexionBDD import conectar
from flask import render_template, request, Flask

class sesion:
    def __init__(self):
        pass
    def home(self):
        return render_template('services/main.html', extiende = True)

    def entrada(self):
        return render_template('services/entrada.html', extiende = False)

    def salida(self):
        return render_template('services/salida.html', extiende = False)
    def posicionamiento(self):
        return render_template('services/posicionamiento.html', extiende = False)
        
    def horarios(self):
        return render_template('services/horarios.html', extiende = False)
    
    def personas(self):
        return render_template('services/personas.html', extiende = False)
    
    def camaras(self):
        return render_template('services/camaras.html', extiende = False)
    def cerrarSesion(self):
        pass