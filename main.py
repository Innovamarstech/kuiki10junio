#Dependencias
import os
import sqlite3
from flask import Flask, render_template, request, session, escape
from flask import render_template, request, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message

#Configuracion general del software
app = Flask(__name__)
app.config['DEBUG'] = True

#Configuracion del email
app.config.update(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'masterlist.suppliers@gmail.com',
    MAIL_PASSWORD = 'Celeste:801020363',

)
mail = Mail(app)

#Configuracion para update file
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = './Archivos PDF'


#Base de datos login de user
dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"
DATABASE = "data.db"
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

# Gestion de la base de datos proveedores
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def change_db(query,args=()):
    cur = get_db().execute(query, args)
    get_db().commit()
    cur.close()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



#Proveedr llena formulario
@app.route('/selecionar3', methods=['GET', 'POST'])
def selecionar3():

    if request.method == "GET":
        return render_template("forms/selecionar3.html",contact=None)

    if request.method == "POST":
        contact=request.form.to_dict()
        values=[contact['company'],contact['phone'],contact['mail'],contact['adress'],contact['city'],contact['country'],contact['website'],contact['industry'],contact['description'],contact['transportemedio'],contact['transportequimicos'],contact['managername'],contact['manageremail'],contact['managerphone'],contact['calidadname'],contact['calidademail'],contact['calidadphone'],contact['finanzasname'],contact['finanzasemail'],contact['finanzasphone'],contact['salename'],contact['saleemail'],contact['salephone'],contact['cuentaname'],contact['cuentaswift'],contact['cuentaaba'],contact['cuentanumber'],contact['cuentaaba'],contact['cuentaaddress'],contact['certificados'],contact['certificadoscomentarios'],contact['certificadocumplimiento'],contact['tiemporegistros'],contact['trazabilidad'],contact['datevencimiento'],contact['attach'],contact['attach2'],contact['attach3']]
        change_db("INSERT INTO contact (company,phone,mail,adress,city,country,website,industry,description,transportemedio,transportequimicos,managername,manageremail,managerphone,calidadname,calidademail,calidadphone,finanzasname,finanzasemail,finanzasphone,salename,saleemail,salephone,cuentaname,cuentaswift,cuentaaba,cuentanumber,cuentaaba,cuentaaddress,certificados,certificadoscomentarios,certificadocumplimiento,tiemporegistros,trazabilidad,datevencimiento,attach,attach2,attach3) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",values)
        return redirect(url_for("redifinal"))


@app.route('/selecionar22', methods=['GET', 'POST'])
def selecionar22():

    if request.method == "GET":
        return render_template("forms/selecionar22.html",contact=None)

    if request.method == "POST":
        contact=request.form.to_dict()
        values=[contact['company'],contact['phone'],contact['mail'],contact['adress'],contact['city'],contact['country'],contact['website'],contact['industry'],contact['description'],contact['managername'],contact['manageremail'],contact['managerphone'],contact['finanzasname'],contact['finanzasemail'],contact['finanzasphone'],contact['salename'],contact['saleemail'],contact['salephone'],contact['cuentaname'],contact['cuentaswift'],contact['cuentaaba'],contact['cuentanumber'],contact['cuentaaba'],contact['cuentaaddress']]
        change_db("INSERT INTO contact (company,phone,mail,adress,city,country,website,industry,description,managername,manageremail,managerphone,finanzasname,finanzasemail,finanzasphone,salename,saleemail,salephone,cuentaname,cuentaswift,cuentaaba,cuentanumber,cuentaaba,cuentaaddress) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",values)
        return redirect(url_for("redifinal"))


@app.route('/select3', methods=['GET', 'POST'])
def select3():

    if request.method == "GET":
        return render_template("forms/select3.html",contact=None)

    if request.method == "POST":
        contact=request.form.to_dict()
        values=[contact['company'],contact['phone'],contact['mail'],contact['adress'],contact['city'],contact['country'],contact['website'],contact['industry'],contact['description'],contact['transportemedio'],contact['transportequimicos'],contact['managername'],contact['manageremail'],contact['managerphone'],contact['calidadname'],contact['calidademail'],contact['calidadphone'],contact['finanzasname'],contact['finanzasemail'],contact['finanzasphone'],contact['salename'],contact['saleemail'],contact['salephone'],contact['cuentaname'],contact['cuentaswift'],contact['cuentaaba'],contact['cuentanumber'],contact['cuentaaba'],contact['cuentaaddress'],contact['certificados'],contact['certificadoscomentarios'],contact['certificadocumplimiento'],contact['tiemporegistros'],contact['trazabilidad'],contact['datevencimiento'],contact['attach'],contact['attach2'],contact['attach3']]
        change_db("INSERT INTO contact (company,phone,mail,adress,city,country,website,industry,description,transportemedio,transportequimicos,managername,manageremail,managerphone,calidadname,calidademail,calidadphone,finanzasname,finanzasemail,finanzasphone,salename,saleemail,salephone,cuentaname,cuentaswift,cuentaaba,cuentanumber,cuentaaba,cuentaaddress,certificados,certificadoscomentarios,certificadocumplimiento,tiemporegistros,trazabilidad,datevencimiento,attach, attach2,attach3) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",values)
        return redirect(url_for("redifinal"))


@app.route('/select22', methods=['GET', 'POST'])
def select22():

    if request.method == "GET":
        return render_template("forms/select22.html",contact=None)

    if request.method == "POST":
        contact=request.form.to_dict()
        values=[contact['company'],contact['phone'],contact['mail'],contact['adress'],contact['city'],contact['country'],contact['website'],contact['industry'],contact['description'],contact['managername'],contact['manageremail'],contact['managerphone'],contact['finanzasname'],contact['finanzasemail'],contact['finanzasphone'],contact['salename'],contact['saleemail'],contact['salephone'],contact['cuentaname'],contact['cuentaswift'],contact['cuentaaba'],contact['cuentanumber'],contact['cuentaaba'],contact['cuentaaddress']]
        change_db("INSERT INTO contact (company,phone,mail,adress,city,country,website,industry,description,managername,manageremail,managerphone,finanzasname,finanzasemail,finanzasphone,salename,saleemail,salephone,cuentaname,cuentaswift,cuentaaba,cuentanumber,cuentaaba,cuentaaddress) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",values)
        return redirect(url_for("redifinal"))

#Notificaciones
@app.route ('/redifinal')
def redifinal():
   msg = Message('Nuevo proveedor registrado', sender = 'masterlist.suppliers@gmail.com', recipients = ['najerarodriguez04@gmail.com'])
   msg.body = "Saludos, se registro un nuevo proveedor. En la prueba no se adjunta la informacion del nuevo proveedor"
   mail.send(msg)
   return render_template("inicio/redifinal.html")

# URL de enrutamiento y procesamiento
@app.route("/")
def index():
    contact_list=query_db("SELECT * FROM contact")
    return render_template("user/login.html",contact_list=contact_list)


#Login and signup
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        hashed_pw = generate_password_hash(request.form["password"], method="sha256")
        new_user = Users(username=request.form["username"], password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        return "You've registered successfully."

    return render_template("user/signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form["username"]).first()

        if user and check_password_hash(user.password, request.form["password"]):
            session["username"] = user.username
            return render_template("user/redi.html")
        return render_template("user/loginerror.html")


    return render_template("user/login.html")

@app.route("/loginerror", methods=["GET", "POST"])
def loginerror():
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form["username"]).first()

        if user and check_password_hash(user.password, request.form["password"]):
            session["username"] = user.username
            return render_template("user/redi.html")
        return render_template("user/loginerror.html")

    return render_template("user/login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return render_template("user/login.html")

@app.route("/logoutotros")
def logoutotros():
    session.pop("username", None)
    return render_template("user/loginotros.html")

#Sesion de usuario de compras
@app.route('/new')
def new():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("compras/nuevo.html",contact_list=contact_list)
    return  render_template("index.html")


@app.route('/pendiente')
def pendiente():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("compras/pendiente.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/archivar')
def archivar():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("compras/archivar.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/todos')
def todos():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("compras/todos.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/green')
def green():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("compras/green.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/yellow')
def yellow():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("compras/yellow.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/orange')
def orange():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("compras/orange.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/red')
def red():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("compras/red.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/rcom3')
def rcom3():
    if "username" in session:
        if request.method == "GET":
            return render_template("forms/formulario3.html",contact=None)

        if request.method == "POST":
            contact=request.form.to_dict()
            values=[contact['company'],contact['phone'],contact['mail'],contact['adress'],contact['city'],contact['country'],contact['website'],contact['industry'],contact['description'],contact['transportemedio'],contact['transportequimicos'],contact['managername'],contact['manageremail'],contact['managerphone'],contact['calidadname'],contact['calidademail'],contact['calidadphone'],contact['finanzasname'],contact['finanzasemail'],contact['finanzasphone'],contact['salename'],contact['saleemail'],contact['salephone'],contact['cuentaname'],contact['cuentaswift'],contact['cuentaaba'],contact['cuentanumber'],contact['cuentaaba'],contact['cuentaaddress'],contact['certificados'],contact['certificadoscomentarios'],contact['certificadocumplimiento'],contact['tiemporegistros'],contact['trazabilidad'],contact['attach']]
            change_db("INSERT INTO contact (company,phone,mail,adress,city,country,website,industry,description,transportemedio,transportequimicos,managername,manageremail,managerphone,calidadname,calidademail,calidadphone,finanzasname,finanzasemail,finanzasphone,salename,saleemail,salephone,cuentaname,cuentaswift,cuentaaba,cuentanumber,cuentaaba,cuentaaddress,certificados,certificadoscomentarios,certificadocumplimiento,tiemporegistros,trazabilidad,attach) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",values)
            return redirect(url_for("dashboard"))
    return  render_template("index.html")


@app.route('/rcom22')
def rcom22():
    if "username" in session:
        if request.method == "GET":
            return render_template("forms/formulario22.html",contact=None)

        if request.method == "POST":
            contact=request.form.to_dict()
            values=[contact['company'],contact['phone'],contact['mail'],contact['adress'],contact['city'],contact['country'],contact['website'],contact['industry'],contact['description'],contact['transportemedio'],contact['transportequimicos'],contact['managername'],contact['manageremail'],contact['managerphone'],contact['calidadname'],contact['calidademail'],contact['calidadphone'],contact['finanzasname'],contact['finanzasemail'],contact['finanzasphone'],contact['salename'],contact['saleemail'],contact['salephone'],contact['cuentaname'],contact['cuentaswift'],contact['cuentaaba'],contact['cuentanumber'],contact['cuentaaba'],contact['cuentaaddress'],contact['certificados'],contact['certificadoscomentarios'],contact['certificadocumplimiento'],contact['tiemporegistros'],contact['trazabilidad'],contact['attach']]
            change_db("INSERT INTO contact (company,phone,mail,adress,city,country,website,industry,description,transportemedio,transportequimicos,managername,manageremail,managerphone,calidadname,calidademail,calidadphone,finanzasname,finanzasemail,finanzasphone,salename,saleemail,salephone,cuentaname,cuentaswift,cuentaaba,cuentanumber,cuentaaba,cuentaaddress,certificados,certificadoscomentarios,certificadocumplimiento,tiemporegistros,trazabilidad,attach) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",values)
            return redirect(url_for("dashboard"))
    return  render_template("index.html")


@app.route('/perfil')
def perfil():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("build.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/notificaciones')
def notificaciones():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("build.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/dashboard')
def dashboard():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("data/dashboard.html",contact_list=contact_list)
    return  render_template("index.html")


@app.route('/posicionamiento')
def posicionamiento():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("data/posicionamiento.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/tendencias')
def tendencias():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("data/tendencias.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/paginaweb')
def paginaweb():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("data/paginaweb.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/visitantes')
def visitantes():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("data/visitantes.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/potencialesclientes')
def potencialesclientes():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("data/clientes.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/canalcomunicacion')
def canalcomunicacion():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("data/canales.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/mensajeventas')
def mensajeventas():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("data/mensajes.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/competencia')
def competencia():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("data/competencia.html",contact_list=contact_list)
    return  render_template("index.html")


@app.route('/revision')
def revision():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("compras/dashboard.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/reportes')
def reportes():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")

        return render_template("reportes.html",contact_list=contact_list)
    return render_template("index.html")


@app.route('/create', methods=['GET', 'POST'])
def create():
    if "username" in session:
        if request.method == "GET":
            return render_template("create.html",contact=None)

        if request.method == "POST":
            contact=request.form.to_dict()
            values=[contact['company'],contact['phone'],contact['mail'],contact['adress'],contact['city'],contact['country'],contact['website'],contact['industry'],contact['description'],contact['transportemedio'],contact['transportequimicos'],contact['managername'],contact['manageremail'],contact['managerphone'],contact['calidadname'],contact['calidademail'],contact['calidadphone'],contact['finanzasname'],contact['finanzasemail'],contact['finanzasphone'],contact['salename'],contact['saleemail'],contact['salephone'],contact['cuentaname'],contact['cuentaswift'],contact['cuentaaba'],contact['cuentanumber'],contact['cuentaaba'],contact['cuentaaddress'],contact['certificados'],contact['certificadoscomentarios'],contact['certificadocumplimiento'],contact['tiemporegistros'],contact['trazabilidad'],contact['attach']]
            change_db("INSERT INTO contact (company,phone,mail,adress,city,country,website,industry,description,transportemedio,transportequimicos,managername,manageremail,managerphone,calidadname,calidademail,calidadphone,finanzasname,finanzasemail,finanzasphone,salename,saleemail,salephone,cuentaname,cuentaswift,cuentaaba,cuentanumber,cuentaaba,cuentaaddress,certificados,certificadoscomentarios,certificadocumplimiento,tiemporegistros,trazabilidad,attach) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",values)
            return redirect(url_for("dashboard"))
    return render_template("index.html")


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def udpate(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("update.html",contact=contact)

        if request.method == "POST":

            print(request.form)
            contact=request.form.to_dict()
            print(contact)
            values=[contact['status'],contact['company'],contact['phone'],contact['mail'],contact['adress'],contact['city'],contact['country'],contact['website'],contact['industry'],contact['description'],contact['transportemedio'],contact['transportequimicos'],contact['managername'],contact['manageremail'],contact['managerphone'],contact['calidadname'],contact['calidademail'],contact['calidadphone'],contact['finanzasname'],contact['finanzasemail'],contact['finanzasphone'],contact['salename'],contact['saleemail'],contact['salephone'],contact['cuentaname'],contact['cuentaswift'],contact['cuentaaba'],contact['cuentanumber'],contact['cuentaaba'],contact['cuentaaddress'],contact['certificados'],contact['certificadoscomentarios'],contact['certificadocumplimiento'],contact['tiemporegistros'],contact['trazabilidad'],contact['attach'],id]
            change_db("UPDATE contact SET status=?,company=?,phone=?,mail=?,adress=?,city=?,country=?,website=?,industry=?,description=?,transportemedio=?,transportequimicos=?,managername=?,manageremail=?,managerphone=?,calidadname=?,calidademail=?,calidadphone=?,finanzasname=?,finanzasemail=?,finanzasphone=?,salename=?,saleemail=?,salephone=?,cuentaname=?,cuentaswift=?,cuentaaba=?,cuentanumber=?,cuentaaba=?,cuentaaddress=?,certificados=?,certificadoscomentarios=?,certificadocumplimiento=?,tiemporegistros=?,trazabilidad=?,attach=? WHERE ID=?",values)
            return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.route('/view/<int:id>', methods=['GET', 'POST'])
def view(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("view.html",contact=contact)


    return render_template("index.html")

@app.route('/view1/<int:id>', methods=['GET', 'POST'])
def view1(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("view1.html",contact=contact)


    return render_template("index.html")

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("delete.html",contact=contact)

        if request.method == "POST":
            change_db("DELETE FROM contact WHERE id = ?",[id])
            return redirect(url_for("dashboard"))
    return render_template("index.html")

#Otros usuarios conta y calidad
@app.route('/todosview')
def todosview():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("todosview.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/revisionconta')
def revisionconta():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("conta/revisionconta.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/revisioncalidad')
def revisioncalidad():
    if "username" in session:
        contact_list=query_db("SELECT * FROM contact")
        return render_template("calidad/revisioncalidad.html",contact_list=contact_list)
    return  render_template("index.html")

@app.route('/update1/<int:id>', methods=['GET', 'POST'])
def update1(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("update1.html",contact=contact)

        if request.method == "POST":

            print(request.form)
            contact=request.form.to_dict()
            print(contact)
            values=[contact['commecalidad'],contact['status'],id]
            change_db("UPDATE contact SET commecalidad=?,status=? WHERE ID=?",values)
            return redirect(url_for("todosview"))
    return  render_template("index.html")


@app.route('/update2/<int:id>', methods=['GET', 'POST'])
def update2(id):
    if "username" in session:
        if request.method == "GET":
            contact=query_db("SELECT * FROM contact WHERE id=?",[id],one=True)
            return render_template("update2.html",contact=contact)

        if request.method == "POST":

            print(request.form)
            contact=request.form.to_dict()
            print(contact)
            values=[contact['commeconta'],contact['status'],id]
            change_db("UPDATE contact SET commeconta=?,status=? WHERE ID=?",values)
            return redirect(url_for("todosview"))
    return  render_template("index.html")


@app.route('/google')
def google():
    return  render_template("data/google.html")

app.secret_key = "12345"


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
