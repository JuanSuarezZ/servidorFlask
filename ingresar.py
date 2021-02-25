from re import split
import psycopg2
import json
import os
import random
import numpy as np
import urllib.parse as up
from io import BytesIO
#from PIL import Image
#import PIL, requests


class BD:

    
    def __init__(self):
        self.con = psycopg2.connect(
            database="enlcuxzb",
            user="enlcuxzb",
            password="bUgzbxegz3BGkRNfRPqvY8y-XpAjy8Mj",
            host="ziggy.db.elephantsql.com",
            port="5432"
        )
    
    '''
    def __init__(self):
        
        self.con = psycopg2.connect(
            dbname="pcomponentesfinal2",
            #dbname="pcomponentes4",
            user="postgres",
            password="123456",
            host="localhost",
            port="5432"
        )
    '''

    def nuevoPaciente(self, data):

        cursor = self.con.cursor()
        query = '''INSERT INTO paciente(nombre,edad,fechacreacion,correo,fechaultimacita,nombreu,contrasena) VALUES (%s,%s,%s,%s,%s,%s,%s)'''
        # cursor.execute(query,(2,"juan",19,"20011201","20011201","zoukin","123"))
        cursor.execute(query, (data["nombre"], data["edad"], data["fechacreacion"],
                               data["correo"], data["fechaultimacita"], data["nombreu"], data["contrasena"]))
        self.con.commit()
        self.con.close()
        return "data insertada"

    def nuevoMedico(self, data):

        cursor = self.con.cursor()
        query = "SELECT count(*) FROM medico"
        cursor.execute(query)
        self.con.commit()
        rows = cursor.fetchall()
        #obtento el num de doctores
        aux = rows[0]
        
        if(aux[0] == 10):
           # a = {'mensaje': 'limite de doctores'}
            return "No hay mas cupo para doctores"

        else:
            cursor = self.con.cursor()
            query = '''INSERT INTO medico(nombre,edad,direccion,correo,anose,lugargrado,fechaingreso,nombreu,contrasena) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            cursor.execute(query, (data["nombre"], data["edad"], data["direccion"], data["correo"],
                               data["anose"], data["lugargrado"], data["fechaingreso"], data["nombreu"], data["contrasena"]))
            self.con.commit()
            self.con.close()
            #a = {'mensaje': 'doctor registrado'}
            return "Doctor registrado"

    def logPaciente(self,data):

        cursor = self.con.cursor()
        query = "select contrasena,id_paciente from paciente where nombreu = '" + data["nombreu"] + "'"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()
        try:
            aux = rows[0]
            aux2 = aux[0]  # obtengo la contraseña

            if(aux2 == data["contra"]):
                return "valido"
            else:
                return "errado"
        except:
            return "no existe"

    def logDoctor(self, nombreu, contra):

        cursor = self.con.cursor()
        query = "select contrasena,id_medico from medico where nombreu = '" + nombreu + "'"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()
        try:
            aux = rows[0]
            aux2 = aux[0]  # obtengo la contraseña

            if(aux2 == contra):
                return "valido"
            else:
                return "errado"
        except:
            return "no existe"


    def logAdmin(self,data):
        
        print(data["nombreu"] )
        print(data["contra"] )
        
        cursor = self.con.cursor()
        query = "select contrasena,id_admin from administrador where nombre = '" + data["nombreu"] + "'"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()

        try:
            aux = rows[0]
            aux2 = aux[0]  # obtengo la contraseña

            if(aux2 == data["contra"]):
                return "valido"
            else:
                return "errado"
        except:
            return "no existe"

    def verDataAdmin(self,data):
        
        print(data["nombre"] )
        
        cursor = self.con.cursor()
        query = "select * from administrador where nombre = '" + data["nombreu"] + "'"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()

        try: 
            aux = rows[0]
            
        
            a = {'mensaje': 'existe',
                 'Data': [rows],
                 }
            return a

        except:
            b = {'mensaje': 'no existe'}
            return b


    def recuperacionM(self, correo):

        cursor = self.con.cursor()
        query = "select id_medico from medico where correo = '" + correo + "'"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()
        try:
            aux = rows[0]  # obtengo el id
            aux2 = aux[0]

            if(aux != None):
 
                cod = random.randrange(1000)
                print(cod)
                a = {'mensaje': 'existe', 'cod': cod, 'id': aux2}
                return a
                # enviarle un codigo;

        except:
            b = {'mensaje': 'no existe'}
            return b

    def CambiarM(self, data):

        cursor = self.con.cursor()
        query = '''Update medico set contrasena = %s where id_medico = %s'''
        # cursor.execute(query,(2,"juan",19,"20011201","20011201","zoukin","123"))
        cursor.execute(query, (data["contra"], data["idx"]))
        self.con.commit()
        self.con.close()
        print("data")
        return "data insertada"

    def recuperacionP(self, correo):

        cursor = self.con.cursor()
        query = "select id_paciente from paciente where correo = '" + correo + "'"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()
        try:
            aux = rows[0]  # obtengo el id
            aux2 = aux[0]

            if(aux != None):
                cod = random.randrange(1000)
                print(cod)
                a = {'mensaje': 'existe', 'cod': cod, 'id': aux2}
                return a
                # enviarle un codigo;

        except:
            b = {'mensaje': 'no existe'}
            return b

    def CambiarP(self, data):

        cursor = self.con.cursor()
        query = '''Update paciente set contrasena = %s where id_paciente = %s'''
        cursor.execute(query, (data["contra"], data["idx"]))
        self.con.commit()
        self.con.close()
        
        return "data insertada"

    def verDatosDoc(self, userN):

        cursor = self.con.cursor()
        query = " select * from medico where nombreu = '" + userN + "'"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()

        try:
            aux = rows[0]  # obtengo el id
            
            a = {'mensaje': 'existe', 
                'id': aux[0],
                'nombre': aux[1],
                'edad': aux[2],
                'direccion':aux[3],
                'correo':aux[4],
                'anose':aux[5],
                'lugargrado':aux[6],
                'fechaingreso':aux[7],
                } 
            return a

        except:
            b = {'mensaje': 'no existe'}
            return b
    
    def verCitasPenDoc(self, idDoc,fecha):

        print("id doc: ",idDoc)
        print("fecha: ",fecha)

        cursor = self.con.cursor()
        query = "select * from cita where id_medico_fk = '" + (idDoc) + "' and estado = 1 and CAST (fechacita AS date) = '" + fecha + "' "
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()

        try:
            #rows es la cantidad de citas
            #aux es cada uno de los elementos de esa cita 
            aux = rows[0]
            
         

            a = {'mensaje': 'existe',
                 'Data': [rows],
                 }
            return a

        except:
            b = {'mensaje': 'no existe'}
            return b

    def UpdateCita(self, data):

        cursor = self.con.cursor()
        query = " Update cita set estado = '" + str(data["estado"]) + "' , descripcion = '" + data["descripcion"] + "' where id_cita = '" + str(data["id_cita"]) + "' "
        cursor.execute(query)
        self.con.commit()


        query3 = "select id_especialidad from especialidad where nombre =  '" + data["id_especialidad"] + "' "
        cursor.execute(query3)
        self.con.commit()
        rows = cursor.fetchall()
     

        #agrego a las historia medica del doctor
        query2 = '''insert into historia_medica(id_medico,fechadelacita,descripcion,id_especialidad,id_paciente) values(%s,%s,%s,%s,%s)'''
        cursor.execute(query2, (data["id_medico"],data["fecha"],data["descripcion"],rows[0],data["id_paciente"]))
        self.con.commit()
        self.con.close()
        
        print("data")
        return "data insertada"
    


    def verEspecialidades(self):

        cursor = self.con.cursor()
        query = '''select * from especialidad'''
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()
        try:
            aux = rows[0]
      
            if(aux != None):
    
                a = { 'nombres':rows }
                return a
                

        except:
            b = {'mensaje': 'no existe'}
            return b

    def RegistroEsp(self, data):
        
        
        lista = data["data"]
        print(lista)

        cursor = self.con.cursor()
        query = '''select max(id_medico) from medico'''
        cursor.execute(query)
        self.con.commit()
        rows = cursor.fetchall()
        aux = rows[0]#id

        print(aux)
        
        for x in lista:

            cursor = self.con.cursor()
            query = '''insert into especialidad_medico(id_medico,id_especialidad) values(%s,%s)'''
            cursor.execute(query,(aux[0],x))
            self.con.commit()
      

        self.con.close()
        return "asd";


    def BuscarCitas(self, data):
        
        print(data["fecha"])
        aux = data["fecha"]
        aux2 = aux.split('/')
        new = aux2[1] +"/"+aux2[0]+"/"+aux2[2]

        cursor = self.con.cursor()
        query = "select * from cita where id_medico_fk = '" + data["id_medico_fk"] + "'and CAST (fechacita AS date)  =  '" + new + "'  "
        cursor.execute(query)
        self.con.commit()
        rows = cursor.fetchall()

        a = {'mensaje': 'existe',
                 'Data': [rows],
                 }

        return a

    def verPacientes(self, data):
        
        cursor = self.con.cursor()
        query = "select id_paciente,nombre from paciente"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()

        try:
            aux = rows[0]  # obtengo el id
            
        

            a = {'data': [rows]
                } 
            return a

        except:
            b = {'mensaje': 'no existe'}
            return b
    
    def historiasMedicas(self, data):
        
        cursor = self.con.cursor()
        query = "select h.fechadelacita,h.descripcion,e.nombre from historia_medica h join especialidad e on h.id_especialidad = e.id_especialidad  where h.id_medico = %s and id_paciente = %s"
        #query = "select h.fechadelacita,h.descripcion,e.nombre from historia_medica where id_medico = %s and id_paciente = %s"
        cursor.execute(query,(data["id_medico_fk"],data["id_paciente"]))
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()
        mensaje = "existe"
                

        try:
            aux = rows[0]  # obtengo el id
            
           
            if not rows:   
                mensaje = "no existe"
            
            a = {'data': [rows],'mensaje': mensaje}
            print(a)
            return a

        except:
            b = {'mensaje': 'no existe'}
     
            return b
    
    def verDataPac(self, data):
        

        cursor = self.con.cursor()
        query = "select * from paciente where nombreu = '" + data["nombre"] + "' "
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()
        mensaje = "existe"
                
        try:
            aux = rows[0]  # obtengo el id
            
        
            if not rows:   
                mensaje = "no existe"
            
            a = {'data': [rows],'mensaje': mensaje}
        
            return a

        except:
            b = {'mensaje': 'no existe'}
      
            return b

    def mishistoriasMedicas(self, data):
        
        id = str(data["id_paciente"])
        try:    
            cursor = self.con.cursor()
            query = "select * from cita where id_paciente_fk = '" + id + "' and estado != 1"
            cursor.execute(query)
            rows = cursor.fetchall()
            self.con.commit()
            self.con.close()
            mensaje = "existe"
                    
            try:
                aux = rows[0]  # obtengo el id
                
        
                if not rows:   
                    mensaje = "no existe"
                
                a = {'data': [rows],'mensaje': mensaje}

                return a

            except:
                b = {'mensaje': 'no existe'}
    
                return b
        except:
                b = {'mensaje': 'no existe'}
    
                return b
        
    def verDocEspecialidad(self, data):

        #print(data["especialidad"])

        cursor = self.con.cursor()
        query = "SELECT id_medico,nombre from medico m where m.id_medico IN (select em.id_medico from especialidad e join especialidad_medico em on e.id_especialidad = em.id_especialidad where e.nombre =  '" + data["especialidad"] + "'  )"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()
        mensaje = "existe"
        
        try:
            aux = rows[0]  # obtengo el id
            
      
            if not rows:   
                mensaje = "no existe"
            
            a = {'data': [rows],'mensaje': mensaje}
            print(a)
         
            return a

        except:
            b = {'mensaje': 'no existe'}
            print(b)
            return b
    
    def AgregarCita(self, data):

        cursor = self.con.cursor()
        query = "select count(*) from cita where id_medico_fk = '" + str(data["id_medico_fk"]) + "' and  CAST (fechacita AS date) = '" + data["fecha"] + "' "
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        
        aux = rows[0]
        print("numero de citas ",aux)

        if (aux[0]<10):
     
            cursor = self.con.cursor()
            query = "insert into cita(id_paciente_fk,id_medico_fk,descripcion,nombrepac,nombredoc,fechacita,estado,especialidad) values (%s,%s,'',%s,%s,%s,1,%s)"
            cursor.execute(query,(str(data["id_paciente_fk"]),str(data["id_medico_fk"]),data["nombrepac"],data["nombredoc"],data["fecha"],data["especialidad"]))
            self.con.commit()
            self.con.close()

            return "Cita agendada";

        else:
            print("no mas de 10 citas")
            return "El doctor no puede agendar mas citas";



    def verDoctores(self):

        cursor = self.con.cursor()
        query = "select id_medico,nombre from medico"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()
        mensaje = "existe"
        
        try:
            aux = rows[0]  # obtengo el id
            

            if not rows:   
                mensaje = "no existe"
            print("los doctores son: ",rows )
            a = {'data': [rows],'mensaje': mensaje}
         
            return a

        except:
            b = {'mensaje': 'no existe'}
     
            return b
            
    def verImg(self):
        
        with open("C:/foto.png", "rb") as image:
            f = image.read()
            b = bytearray(f)
        imagen = Image.open(BytesIO(b))
        imagen = imagen.resize([150,150])
        imagen_arreglo = np.asarray(b)


        cursor = self.con.cursor()
        cursor.execute("insert into mueble(id_proveedor,material,cod_de_mueble,imagen,color,precio,dimensiones) values (1,'madera', %s, ,'azul',1233,'1x2')",("asd"))
        cursor.execute(" ")
        self.con.commit()
        self.con.close()
        
    
        imagen_o = PIL.Image.fromarray(np.uint8(imagen_arreglo))
        print(type(imagen_o))
        Image.Image.show(imagen_o)  
        
        b = {'mensaje': 'no existe'}
        return b
      

    def UpdatecitaDoc(self,data):

        #print(data['fecha'])
        #print(data['horacita'])
        #print(data['idcita'])
        
        cursor = self.con.cursor()
        query = " select fechacita from cita where id_cita = '" + str(data["idcita"]) + "'"
        cursor.execute(query)
        self.con.commit()
        rows = cursor.fetchall()
        print(rows)

        n = rows[0]
        aux = str(n[0]).split()
        print(aux)   
           

        if(data["tipo"]=='ambos'):
            
            aux = data['fecha']
            aux2 = aux.split('/')
            new = aux2[1] +"/"+aux2[0]+"/"+aux2[2]


            fechanew = new +' '+ data['horacita'] 
            cursor = self.con.cursor()
            query = " Update cita set fechacita = '" + fechanew + "' where id_cita = '" + str(data["idcita"]) + "' "
            cursor.execute(query)
            self.con.commit()
        
        if(data["tipo"]=='fecha'):
            
            auxf = data['fecha']
            auxf2 = auxf.split('/')
            new = auxf2[1] +"/"+auxf2[0]+"/"+auxf2[2]

            fechanew = new +' '+ aux[1] 

            cursor = self.con.cursor()
            query = " Update cita set fechacita = '" + fechanew + "' where id_cita = '" + str(data["idcita"]) + "' "
            cursor.execute(query)
            self.con.commit()
        
        if(data["tipo"]=='hora'):
            
            fechanew = aux[0] +' '+ data['horacita'] 

            cursor = self.con.cursor()
            query = " Update cita set fechacita = '" + fechanew + "' where id_cita = '" + str(data["idcita"]) + "' "
            cursor.execute(query)
            self.con.commit()

        return "no existe"

    def verCitasAllDoc(self):
    
        cursor = self.con.cursor()
        query = '''select count(id_medico_fk),nombredoc from cita  group by nombredoc'''
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()
        try:
            aux = rows[0]
      
            if(aux != None):
    
                a = { 'data':rows }
                return a

        except:
            b = {'mensaje': 'no existe'}
            return b
        
    def verCitaDia(self, fecha):
    
        print("fecha: ",fecha)
        auxf = fecha
        auxf2 = auxf.split('/')
        new = auxf2[1]+"/"+auxf2[0]+"/"+auxf2[2]

        print(new)

        cursor = self.con.cursor()
        query = "select count(id_medico_fk),nombredoc from cita where CAST (fechacita AS date) = '" + new + "'and estado != 1 group by nombredoc"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()

        try:
            #rows es la cantidad de citas
            #aux es cada uno de los elementos de esa cita 
            aux = rows[0]
        
            a = {'mensaje': 'existe',
                 'Data': [rows],
                 }
            return a

        except:
            b = {'mensaje': 'no existe'}
            return b

    def verCitaMensual(self, fecha):
        
        fecha = fecha.replace("'","")

        meses = {
            "enero" : '1/01/2021 1/31/2021',
            "febrero" :'2/01/2021 2/28/2021',
            "marzo" : '3/01/2021 3/31/2021',
            "abril" : '4/01/2021 4/30/2021',
            "mayo" : '5/01/2021 5/31/2021',
            "junio" : '6/01/2021 6/30/2021',
            "julio" : '7/01/2021 7/31/2021',
            "agosto" :'8/01/2021 8/31/2021',
            "septiembre" :'9/01/2021 9/30/2021',
            "octubre" :'10/01/2021 10/31/2021',
            "noviembre" :'11/01/2021 11/30/2021',
            "diciembre" :'12/01/2021 12/31/2021',
        }
        
        print(meses[fecha])

        fechas = meses[fecha].split()
        inicio = fechas[0]
        fin = fechas[1]
      
        cursor = self.con.cursor()
        query = "select count(id_medico_fk),nombredoc from cita where CAST (fechacita AS date) between '" + str(inicio) + "' and '" + str(fin) + "' and estado != 1 group by nombredoc"
        cursor.execute(query)
        rows = cursor.fetchall()
        self.con.commit()
        self.con.close()
        print(rows)
        try:
            #rows es la cantidad de citas
            #aux es cada uno de los elementos de esa cita 
            aux = rows[0]
            print('llego: ',aux)
            a = {'mensaje': 'existe',
                 'Data': [rows],
                 }
            return a

        except:
            b = {'mensaje': 'no existe'}
            return b
       

