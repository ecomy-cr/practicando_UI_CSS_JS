from crypt import methods
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/log',methods=['POST', 'GET'])
def log():
    return render_template('log.html')



@app.route('/',methods=['POST', 'GET'])
def home():
    return render_template('home.html')



@app.route('/marketplace',methods=['POST', 'GET'])
def marketplace():
    return render_template('tipo_phone.html')




@app.route('/atencion_al_cliente',methods=['POST', 'GET'])
def atencion_al_cliente():
    return render_template('atencion_al_cliente.html')
@app.route('/servicios_detallados',methods=['POST', 'GET'])
def servicios_detallados():
    return render_template('servicios_detallados.html')

@app.route('/crear_empresa', methods=['POST', 'GET'])
def crear_empresa():
    return render_template('crear_empresa.html', mensaje='No se ha recibido nada')











@app.route('/empresa_perfil', methods=['POST', 'GET'])
def empresa_perfil():
    
    return render_template('empresarios/dash.html', mensaje='No se ha recibido nada')


@app.route('/ventas_empresa', methods=['POST', 'GET'])
def ventas_empresa():
    
    return render_template('empresarios/ventas.html', mensaje='No se ha recibido nada')



@app.route('/productos', methods=['POST', 'GET'])
def productos_empresa():
    return render_template('empresarios/productos.html', mensaje='No se ha recibido nada')

@app.route('/reportes', methods=['POST', 'GET'])
def reportes_empresa():
    return render_template('empresarios/reportes.html', mensaje='No se ha recibido nada')

@app.route('/facturas', methods=['POST', 'GET'])
def facturas_empresa():
    return render_template('empresarios/ventas.html', mensaje='No se ha recibido nada')

@app.route('/empleo', methods=['POST', 'GET'])
def empleo_empresa():
    return render_template('empresarios/empleo.html', mensaje='No se ha recibido nada')

@app.route('/perfil', methods=['POST', 'GET'])
def perfil_empresa():
    return render_template('empresarios/perfil.html', mensaje='No se ha recibido nada')

@app.route('/config', methods=['POST', 'GET'])
def confi_empresa():
    return render_template('empresarios/confi.html', mensaje='No se ha recibido nada')


@app.route('/markett', methods=['POST', 'GET'])
def markett():
    return render_template('marketplace.html', mensaje='No se ha recibido nada')

@app.route('/forget', methods=['POST', 'GET'])
def forget():
    return render_template('forget.html', mensaje='No se ha recibido nada')

@app.route('/tipo_phone',methods=['POST', 'GET'])
def tipo_phone():
    return render_template('tipo_phone.html')

@app.route('/crear_nueva_empresa_ecomy',methods=['POST', 'GET'])
def crear_nueva_empresa_ecomy():
    return redirect(url_for('.log'))

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port = 5677)