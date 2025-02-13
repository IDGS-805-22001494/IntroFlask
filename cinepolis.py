from flask import Flask, render_template, request

app = Flask(__name__)


class Boleto:
    def __init__(self):
        self.boletosPorPersona = 7  
        self.precioBoleto = 12   

    def calcular_total(self, grupoPersonas, numBoletos, tarjeta_cienco):
       
        maximo_permitido = grupoPersonas * self.boletosPorPersona
        if numBoletos > maximo_permitido:
            return None, f"No se pueden comprar más de 7 boletos por persona. Máximo permitido para {grupoPersonas} personas: {maximo_permitido} boletos"

       
        total = numBoletos * self.precioBoleto

        
        if numBoletos > 5:
          
            total = total * 0.85
        elif numBoletos >= 3:
            
            total = total * 0.90

       
        if tarjeta_cienco:
            total = total * 0.90  

        return round(total, 0), None

lista_personas = []

@app.route("/", methods=["GET", "POST"])
def cinepolis():
    total_pagar = None
    mensaje = None
    mostrar_ticket = False
    
    if request.method == "POST":
        nombre = request.form["nombre"]
        grupoPersonas = int(request.form["grupoPersonas"])
        numBoletos = int(request.form["numBoletos"])
        tarjeta_cienco = request.form["cineco"] == "si"

        sistema = Boleto()
        total_pagar, mensaje = sistema.calcular_total(grupoPersonas, numBoletos, tarjeta_cienco)

        if mensaje:
            return render_template("cinepolis.html", mensaje=mensaje, total_pagar=None, 
                                mostrar_ticket=False, lista_personas=lista_personas)

        nueva_compra = {
            "nombre": nombre,
            "boletos": numBoletos,
            "total": total_pagar,
            "tarjeta_cineco": "Sí" if tarjeta_cienco else "No"
        }
        lista_personas.append(nueva_compra)
        mostrar_ticket = True
    
    total_general = sum(p["total"] for p in lista_personas) if lista_personas else 0
    
    return render_template("cinepolis.html", 
                         total_pagar=total_pagar, 
                         mensaje=mensaje, 
                         mostrar_ticket=mostrar_ticket, 
                         lista_personas=lista_personas, 
                         total_general=total_general)

if __name__ == "__main__":
    app.run(debug=True)