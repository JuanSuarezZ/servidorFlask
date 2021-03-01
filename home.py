from flask import Flask, request
from ingresar import BD

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

db = BD()

"""clientes"""

@app.route('/AllClientes')
def getALlClientes():
    data = db.AllClientes()
    return str(data)

@app.route('/ClientesById')
def getClientesById():
    try:
        id = request.args.get('id')
        data = db.ClienteById(id)
        return str(data)
    except:
        return "Cliente no encontrado", 400

@app.route('/AddCliente')
def AddClientes():
    try:
        id = int(request.args.get('id'))
        name = request.args.get('name')
        date = request.args.get('date')
        email = request.args.get('email')
        address = request.args.get('address')

        db.AddCliente(id, name, date, email, address)

        return "Cliente se agrego"
    except:
        return "Cliente no se pudo Agregar", 400

@app.route('/DeleteCliente')
def DeleteCliente():
    try:
        id = request.args.get('id')
        db.DeleteCliente(id)
        return "Cliente se ha eliminado"
    except:
        return "Cliente no se pudo eliminar", 400

"""proveedor"""

@app.route('/AllProveedores')
def getAllProveedores():
    data = db.AllProveedores()
    return str(data)

@app.route('/ProveedoresById')
def getProveedoresById():
    try:
        id = request.args.get('id')
        data = db.ProveedoresById(id)
        return str(data)
    except:
        return "Proveedor no encontrado", 400

@app.route('/AddProveedor')
def AddProveedor():
    try:
        id = int(request.args.get('id'))
        name = request.args.get('name')
        address = request.args.get('address')
        contact = request.args.get('contact')

        db.AddProveedor(id, name, address, contact)

        return "Proveedor se agrego"
    except:
        return "Proveedor no se pudo Agregar", 400

@app.route('/DeleteProveedor')
def DeleteProveedor():
    try:
        id = request.args.get('id')
        db.DeleteProveedor(id)
        return "Proveedor se ha eliminado"
    except:
        return "Proveedor no se pudo eliminar", 400

"""mueble"""

@app.route('/AddMueble')
def AddMueble():
    try:
        id_proveedor = int(request.args.get('id_proveedor'))
        material = request.args.get('material')
        code = request.args.get('code')
        imagen = request.args.get('imagen')
        color = request.args.get('color')
        precio = int(request.args.get('precio'))
        dimensiones = request.args.get('dimensiones')
        stock = int(request.args.get('stock'))

        db.AddMueble(id_proveedor, material, code, imagen, color, precio, dimensiones, stock)
        return "Mueble ha sido Agregado"
    except:
        return "Mueble no ha sido Agregado", 400

@app.route('/AllMuebles')
def AllMuebles():
    data = db.AllMuebles()
    return str(data)

@app.route('/MuebleById')
def MuebleById():
    try:
        id = request.args.get('id')
        data = db.MuebleById(id)

        return str(data)
    except:
        return "Mueble no ha sido Encontrado", 400

@app.route('/DeleteMuebleById')
def DeleteMuebleById():
    try:
        id = request.args.get('id')
        db.DeleteMuebleById(id)
        return "Mueble ha sido eliminado"
    except:
        return "Mueble no ha sido eliminado", 400

"""pedido"""

@app.route('/AllPedidos')
def AllPedidos():
    try:
        data = db.AllPedidos()
        return str(data)
    except:
        return "Error", 400

@app.route('/NewPedido')
def NewPedido():
    try:
        id_proveedor = request.args.get('id_proveedor')
        precio = request.args.get('precio')
        id_mueble = request.args.get('id_mueble')
        cantidad = request.args.get('cantidad')
        fecha_entrega = request.args.get('fecha_entrega')
        estado = request.args.get('estado')
        fecha_pedido = request.args.get('fecha_pedido')

        db.NewPedido(id_proveedor, precio, id_mueble, cantidad, fecha_entrega, estado, fecha_pedido)
        return "Pedido ha sido agregado"
    except:
        return "Pedido no ha sido agregado", 400

@app.route('/PedidoById')
def PedidoById():
    try:
        id = request.args.get('id')
        data = db.PedidoById(id)
        return str(data)
    except:
        return "Pedido no encontrado", 400

@app.route('/SetStatePedido')
def SetStatePedido():
    try:
        id = request.args.get('id')
        db.SetStatePedido(id)
        return "Pedido ha sido actualizado"
    except:
        return "Pedido no ha sido actualizado", 400

"""vendedor"""

@app.route('/AllVendedores')
def AllVendedores():
    try:
        data = db.AllVendedores()
        return str(data)
    except:
        return "error", 400

@app.route('/VendedoresById')
def VendedoresById():
    try:
        id = request.args.get('id')
        data = db.VendedorById(id)
        return str(data)
    except:
        return "Vendedor no encontrado", 400

@app.route('/AddVendedor')
def AddVendedor():
    try:
        id = request.args.get('id')
        date = request.args.get('date')
        tel = request.args.get('tel')
        address = request.args.get('address')
        email = request.args.get('email')
        salary = request.args.get('salary')

        db.AddVendedor(id, date, tel, address, email, salary)
        return "Vendedor ha sido agregado"
    except:
        return "Vendedor no ha sido agregado", 400

"""ventas"""

@app.route('/AllVentas')
def AllVentas():
    try:
        data = db.AllVentas()
        return str(data)
    except:
        return "error", 400

@app.route('/VentaById')
def VentaById():
    try:
        id = request.args.get('id')
        data = db.VentasById(id)
        return str(data)
    except:
        return "Venta no encontrado", 400

@app.route('/AddVenta')
def AddVenta():
    try:
        id = request.args.get('id')
        id_vendedor = request.args.get('id_vendedor')
        id_cliente = request.args.get('id_cliente')
        id_mueble = request.args.get('id_mueble')
        precio = request.args.get('precio')
        date = request.args.get('date')
        cantidad = request.args.get('cantidad')
        envio = request.args.get('envio')
        instalacion = request.args.get('instalacion')

        db.AddVendedor(id, id_vendedor, id_cliente, id_mueble, precio, date, cantidad, envio, instalacion)
        return "Venta ha sido agregado"
    except:
        return "Venta no ha sido agregado", 400

if __name__=='__main__':
    app_flask = app
    app_flask.run(debug=True,host="0.0.0.0")

