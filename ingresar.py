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
    '''
    def __init__(self):
        self.con = psycopg2.connect(
            database="xlamntnr",
            user="xlamntnr",
            password="r6pZNRyJEOJ2P1PdsYpmS3ncBQR_gmwe",
            host="ziggy.db.elephantsql.com",
            port="5432"
        )
    '''
    """clientes"""

    def AllClientes(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM cliente"
        cursor.execute(query)
        self.con.commit()
        clientes = cursor.fetchall()

        data = []
        for cliente in clientes:
            temp = {
                'identificacion': cliente[0],
                'nombre': cliente[1],
                'fecha_registro': cliente[2],
                'correo_electronico': cliente[3],
                'direccion': cliente[4]
            }
            data.append(temp)

        return json.dumps(data, indent=4, sort_keys=True, default=str)

    def ClienteById(self, id):
        cursor = self.con.cursor()
        query = "SELECT * FROM cliente where identificacion = '" + id + "'"
        cursor.execute(query)
        self.con.commit()
        cliente = cursor.fetchone()

        data =[
            {
                'identificacion': cliente[0],
                'nombre': cliente[1],
                'fecha_registro': cliente[2],
                'correo_electronico': cliente[3],
                'direccion': cliente[4]
            }
        ]

        return json.dumps(data, indent=4, sort_keys=True, default=str)

    def AddCliente(self, id, name, date, email, address):
        cursor = self.con.cursor()
        query = '''INSERT INTO cliente
                (identificacion,nombre,fecha_registro,correo_electronico,direccion) 
                VALUES (%s,%s,%s,%s,%s)'''
        cursor.execute(query, (id, name, date, email, address))
        self.con.commit()

    def DeleteCliente(self, id):
        cursor = self.con.cursor()
        query = "DELETE FROM cliente where identificacion = '" + id + "'"
        cursor.execute(query)
        self.con.commit()

    """proveedores"""

    def AllProveedores(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM proveedor"
        cursor.execute(query)
        self.con.commit()
        proveedores = cursor.fetchall()

        data = []
        for proveedor in proveedores:
            temp = {
                'id_proveedor': proveedor[0],
                'nombre': proveedor[1],
                'direccion': proveedor[2],
                'personacontacto': proveedor[3],
            }
            data.append(temp)

        return json.dumps(data)

    def ProveedoresById(self, id):
        cursor = self.con.cursor()
        query = "SELECT * FROM proveedor where id_proveedor = '" + id + "'"
        cursor.execute(query)
        self.con.commit()
        proveedor = cursor.fetchone()

        data = [
            {
                'id_proveedor': proveedor[0],
                'nombre': proveedor[1],
                'direccion': proveedor[2],
                'personacontacto': proveedor[3],
            }
        ]

        return json.dumps(data)

    def AddProveedor(self, id, name, address, contact):
        cursor = self.con.cursor()
        query = '''INSERT INTO proveedor
                        (id_proveedor,nombre,direccion,personacontacto) 
                        VALUES (%s,%s,%s,%s)'''
        cursor.execute(query, (id, name, address, contact))
        self.con.commit()

    def DeleteProveedor(self, id):
        cursor = self.con.cursor()
        query = "DELETE FROM proveedor where id_proveedor = '" + id + "'"
        cursor.execute(query)
        self.con.commit()

    """mueble"""

    def AddMueble(self, id_proveedor, material, code, imagen, color, precio, dimensiones, stock):
        cursor = self.con.cursor()
        query = '''insert into mueble 
                   (id_proveedor,material,cod_de_mueble,imagen,color,precio,dimensiones,stock)
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'''

        cursor.execute(query, (id_proveedor, material, code, imagen , color, precio, dimensiones, stock))

        self.con.commit()

    def AllMuebles(self):
        cursor = self.con.cursor()
        query = "SELECT m.id_mueble,m.id_proveedor,p.nombre,m.material,m.cod_de_mueble,m.imagen,m.color,m.precio,m.dimensiones,m.stock FROM mueble m join proveedor p on m.id_proveedor = p.id_proveedor"
        cursor.execute(query)
        self.con.commit()
        muebles = cursor.fetchall()

        data = []
        for mueble in muebles:
            temp = {
                'id': mueble[0],
                'id_proveedor': mueble[1],
                'nombre_proveedor' : mueble[2],
                'material': mueble[3],
                'code': mueble[4],
                'imagen': mueble[5],
                'color': mueble[6],
                'precio': mueble[7],
                'dimensiones': mueble[8],
                'stock': mueble[9],
            }
            data.append(temp)

        return json.dumps(data)

    def MuebleById(self, id):
        cursor = self.con.cursor()
        query = "SELECT * FROM mueble where id_mueble = '" + id + "'"
        cursor.execute(query)
        self.con.commit()
        mueble = cursor.fetchone()

        data = [
            {
                'id': mueble[0],
                'id_proveedor': mueble[1],
                'material': mueble[2],
                'code': mueble[3],
                'imagen': mueble[4],
                'color': mueble[5],
                'precio': mueble[6],
                'dimensiones': mueble[7],
                'stock': mueble[8],
            }
        ]

        return json.dumps(data)

    def DeleteMuebleById(self, id):
        cursor = self.con.cursor()
        query = "DELETE FROM mueble where id_mueble  = '" + id + "'"
        cursor.execute(query)
        self.con.commit()

    """pedido"""

    def AllPedidos(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM pedido"
        cursor.execute(query)
        self.con.commit()
        pedidos = cursor.fetchall()

        data = []
        for pedido in pedidos:
            temp = {
                'id_pedido': pedido[0],
                'id_proveedor': pedido[1],
                'precio': pedido[2],
                'id_mueble': pedido[3],
                'cantidad ': pedido[4],
                'fecha_entrega': pedido[5],
                'estado': pedido[6],
                'fecha_pedido': pedido[7],
            }
            data.append(temp)

        return json.dumps(data, indent=4, sort_keys=True, default=str)

    def PedidoById(self, id):
        cursor = self.con.cursor()
        query = "SELECT * FROM pedido where id_pedido = '" + id + "'"
        cursor.execute(query)
        self.con.commit()
        pedido = cursor.fetchone()

        data = [
            {
                'id_pedido': pedido[0],
                'id_proveedor': pedido[1],
                'precio': pedido[2],
                'id_mueble': pedido[3],
                'cantidad ': pedido[4],
                'fecha_entrega': pedido[5],
                'estado': pedido[6],
                'fecha_pedido': pedido[7],
            }
        ]

        return json.dumps(data, indent=4, sort_keys=True, default=str)

    def NewPedido(self, id_proveedor, precio, id_mueble, cantidad, fecha_entrega, estado, fecha_pedido):
        cursor = self.con.cursor()
        query = '''insert into pedido 
                           (id_proveedor, precio, id_mueble, cantidad, fecha_entrega, estado, fecha_pedido)
                           VALUES (%s,%s,%s,%s,%s,%s,%s)'''

        cursor.execute(query, (id_proveedor, precio, id_mueble, cantidad, fecha_entrega, estado, fecha_pedido))

        self.con.commit()

    def SetStatePedido(self, id):
        cursor = self.con.cursor()
        query = "Update pedido set estado = " + str(1) + " where id_pedido  = '" + id + "'"
        cursor.execute(query)
        self.con.commit()

    """vendedor"""

    def AllVendedores(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM vendedor"
        cursor.execute(query)
        self.con.commit()
        vendedores = cursor.fetchall()

        data = []
        for vendedor in vendedores:
            temp = {
                'id_vendedor': vendedor[0],
                'fecha_ingreso': vendedor[1],
                'telefono': vendedor[2],
                'direccion': vendedor[3],
                'correo_electronico': vendedor[4],
                'salario': vendedor[5],
                'nombre': vendedor[6]
            }
            data.append(temp)

        return json.dumps(data, indent=4, sort_keys=True, default=str)

    def VendedorById(self, id):
        cursor = self.con.cursor()
        query = "SELECT * FROM vendedor where id_vendedor = '" + id + "'"
        cursor.execute(query)
        self.con.commit()
        vendedor = cursor.fetchone()

        data = [
            {
                'id_vendedor': vendedor[0],
                'fecha_ingreso': vendedor[1],
                'telefono': vendedor[2],
                'direccion': vendedor[3],
                'correo_electronico': vendedor[4],
                'salario': vendedor[5],
                'nombre': vendedor[6]
            }
        ]

        return json.dumps(data, indent=4, sort_keys=True, default=str)

    def AddVendedor(self, id, date, tel, address, email, salary, nombre):
        cursor = self.con.cursor()
        query = '''insert into vendedor 
                                   (id_vendedor, fecha_ingreso, telefono, direccion, correo_electronico, salario, nombre)
                                   VALUES (%s,%s,%s,%s,%s,%s,%s)'''
        cursor.execute(query, (id, date, tel, address, email, salary, nombre))

        self.con.commit()

    """venta"""

    def AllVentas(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM venta"
        cursor.execute(query)
        self.con.commit()
        ventas = cursor.fetchall()

        data = []
        for venta in ventas:
            temp = {
                'id_venta': venta[0],
                'id_vendedor': venta[1],
                'identificacion': venta[2],
                'id_mueble ': venta[3],
                'precio_total': venta[4],
                'fecha_venta': venta[5],
                'cantidad': venta[6],
                'envio': venta[7],
                'instalacion': venta[8]
            }
            data.append(temp)

        return json.dumps(data, indent=4, sort_keys=True, default=str)

    def VentasById(self, id):
        cursor = self.con.cursor()
        query = "SELECT * FROM venta where id_venta = '" + id + "'"
        cursor.execute(query)
        self.con.commit()
        venta = cursor.fetchone()

        data = [
            {
                'id_venta': venta[0],
                'id_vendedor': venta[1],
                'identificacion': venta[2],
                'id_mueble': venta[3],
                'precio_total': venta[4],
                'fecha_venta': venta[5],
                'cantidad': venta[6],
                'envio': venta[7],
                'instalacion': venta[8]
            }
        ]

        return json.dumps(data, indent=4, sort_keys=True, default=str)

    def AddVenta(self, id, id_vendedor, id_cliente, id_mueble, precio, date, cantidad, envio, instalacion):
        cursor = self.con.cursor()
        query = '''insert into vendedor 
                    (id_venta, id_vendedor, identificacion, id_mueble, precio_total, fecha_venta, cantidad, envio, instalacion)
                                           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        cursor.execute(query, (id, id_vendedor, id_cliente, id_mueble, precio, date, cantidad, envio, instalacion))

        self.con.commit()
       

