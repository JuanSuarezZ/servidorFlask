from flask import Flask,request
import requests, json
from ingresar import BD

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


'''
    listaCliente = []

    socketio = SocketIO(app)

    @socketio.on('connect')
    def handleMessage():
        
        currentSocketId = request.sid

        a = {'message': 'mensaje de bienvenida'} 
        socketio.emit('message',a,currentSocketId)
    
        print("identificador = ",currentSocketId)    
        print("Conectado!")

    

    @socketio.on('newCX')
    def newClient(socketCX):
        
        print("el socket es = ",socketio)


    @socketio.on('message')
    def Message(mensaje):
        
        a = {'message': 'respuesta socket a cliente'} 
        socketio.emit('message',a)
        print("message= ",mensaje)
'''

@app.route('/',)
def hello_world():

    return 'Hello from Flask xd!'

#new client
@app.route('/xxx', methods=["POST"])
def ingresarToken():
    
    data = request.json
    print(data)
    return "llego"


@app.route('/message',methods=["GET"])
def message():
    values = {
        "notification":{
            "title": "Titulo de la notification",
            "body": "Bienvenido!"
        },
        "priority": "high",
        "data": {
            "product":"Agua men"
        },
        "to" : "/topics/allDevices"
    }
    header ={ 'Content-Type': 'application/json; UTF-8', 'Authorization': "key=AAAAYxmyANQ:APA91bHvgJNF6UTDqPGEayyXnKNG-AbEY3Vdr98C8v4_qQa9esmW1r7OrYMQKs8HTUnGKL7dLSEc17EjyEQOu8NCvGWy9u_bb8pOZiGF_r1uYqQT3YckmdmnmE3sPWhQoRxm3SqFpXzX"}
    url = 'https://fcm.googleapis.com/fcm/send'
    r =  requests.post(url, data=json.dumps(values), headers=header)
    return str(r)



@app.route('/registrarP', methods=["POST"])
def ingresarP():

    data = request.json
    bd = BD()
    return bd.nuevoPaciente(data)

@app.route('/registrarDoc', methods=["POST"])
def ingresarD():

    data = request.json
    bd = BD()
    return bd.nuevoMedico(data)

@app.route('/login', methods=["POST"])
def loginP():


    data = request.json

    print(data["token"])
    bd = BD()
    return bd.logPaciente(data)


@app.route('/loginD', methods=["GET"])
def loginD():

    nombreUser = request.args.get('nombreu')
    contra = request.args.get('contra')
    bd = BD()
    return bd.logDoctor(nombreUser,contra)

@app.route('/recuperacionM', methods=["GET"])
def recuperacion():

    correo = request.args.get('correo')  
    bd = BD()
    return bd.recuperacionM(correo)

@app.route('/CambiarM', methods=["POST"])
def CambiarM():

    data = request.json
    bd = BD()
    return bd.CambiarM(data)

@app.route('/recuperacionP', methods=["GET"])
def recuperacionP():

    correo = request.args.get('correo')  
    bd = BD()
    return bd.recuperacionP(correo)

@app.route('/CambiarP', methods=["POST"])
def CambiarP():

    data = request.json
    bd = BD()
    return bd.CambiarP(data)

@app.route('/verDatosDoc', methods=["GET"])
def verDatosDoc():

    userN = request.args.get('userN')  
    bd = BD()

    return bd.verDatosDoc(userN)

@app.route('/CitasPecDoc', methods=["GET"])
def CitasPecDoc():

    fecha = request.args.get('fecha')
    idDoc = request.args.get('id_Doc')  
    bd = BD()
    return bd.verCitasPenDoc(idDoc,fecha)

@app.route('/UpdateCita', methods=["POST"])
def UpdateCita():

    data = request.json
    bd = BD()
    return bd.UpdateCita(data)

@app.route('/verEspecialidades', methods=["GET"])
def verEspecialidades():

    bd = BD()
    return bd.verEspecialidades()

@app.route('/verCitasAllDoc', methods=["GET"])
def verCitasAllDoc():

    bd = BD()
    return bd.verCitasAllDoc()

@app.route('/verCitaDia', methods=["GET"])
def verCitaDia():

    fecha = request.args.get('fechax')
    bd = BD()
    return bd.verCitaDia(fecha)

@app.route('/verCitaMensual', methods=["GET"])
def verCitaMensual():

    fecha = request.args.get('fechax')
    bd = BD()
    return bd.verCitaMensual(fecha)

@app.route('/verCitaDoc', methods=["GET"])
def verCitaDoc():
    
    id = request.args.get('id')
    bd = BD()
    return bd.verCitaDoc(id)
 


@app.route('/RegistroEsp', methods=["POST"])
def RegistroEsp():
    
    data = request.json
    bd = BD()
    return bd.RegistroEsp(data)


@app.route('/BuscarCitas', methods=["POST"])
def BuscarCitas():
    
    data = request.json
    bd = BD()
    return bd.BuscarCitas(data)

@app.route('/verPacientes', methods=["POST"])
def verPacientes():
    
    data = request.json
    bd = BD()
    return bd.verPacientes(data)


@app.route('/historiasMedicas', methods=["POST"])
def historiasMedicas():

    data = request.json
    bd = BD()
    return bd.historiasMedicas(data)


@app.route('/verDataPac', methods=["POST"])
def verDataPac():

    data = request.json
    bd = BD()
    return bd.verDataPac(data)

@app.route('/mishistoriasMedicas', methods=["POST"])
def mishistoriasMedicas():

    data = request.json
    bd = BD()
    return bd.mishistoriasMedicas(data)

@app.route('/verDocEspecialidad', methods=["POST"])
def verDocEspecialidad():

    data = request.json
    bd = BD()
    return bd.verDocEspecialidad(data)

@app.route('/AgregarCita', methods=["POST"])
def AgregarCita():

    data = request.json
    bd = BD()
    return bd.AgregarCita(data)

@app.route('/verDoctores', methods=["GET"])
def verDoctores():

    bd = BD()
    return bd.verDoctores()


@app.route('/verImg', methods=["GET"])
def verImg():

    bd = BD()
    return bd.verImg()


@app.route('/UpdatecitaDoc', methods=["POST"])
def UpdatecitaDoc():


    data = request.json
    bd = BD()
    return bd.UpdatecitaDoc(data)


@app.route('/logAdmin', methods=["POST"])
def logAdmin():


    data = request.json
    bd = BD()
    return bd.logAdmin(data)


@app.route('/verDataAdmin', methods=["GET"])
def verDataAdmin():
    

    nombre = request.args.get('nombre')
    bd = BD()
    return bd.verDataAdmin(nombre)


@app.route('/pruebas', methods=["GET"])
def pruebas():
   
    bd = BD()
    return str(bd.pruebas())


if __name__ == "__main__":
    app_flask = app
    app_flask.run(debug=True,host="0.0.0.0")



