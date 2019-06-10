https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env
gcloud app deploy

CREATE TABLE `contact` (
	`id`,	`company`,`phone`,	`mail`	,	`adress`,	`city`,	`country`,	`website`,	`industry`,	`description`,	`transportemedio`	,	`transportequimicos`,	`managername`,	`manageremail`	,	`managerphone`,`calidadname`	,`calidademail`	,`calidadphone`	,`finanzasname`	,`finanzasemail`	,`finanzasphone`	,`salename`	,`saleemail`	,`salephone`	,`cuentaname`,`cuentaswift`,`cuentaaba`,`cuentanum,`cuentaba,`cuentaaddr,`certificados`	,`certificadoscomentarios`,`certificadocumplimiento`,	`conservarregistros`,`tiemporegistros`,	`trazabilidad`,	`staus`
    contact[`company`],contact[`phone`,contact[`mail`],contact[`adress`],contact[`city`],contact[`country`],contact[`website`],contact[`industry`],contact[`description`],contact[`transportemedio`],contact[`transportequimicos`],contact[`managername`],contact[`manageremail`],contact[`managerphone`],contact[`calidadname`],contact[`calidademail`],contact[`calidadphone`],contact[`finanzasname`],contact[`finanzasemail`],contact[`finanzasphone`],contact[`salename`,contact[`saleemail`],contact[`salephone`],contact[`cuentaname`],contact[`cuentaswift`],contact[`cuentaaba`],contact[`cuentanumber],contact[`cuentaba],contact[`cuentaaddr],contact[`certificados`],contact[`certificadoscomentarios`],contact[`certificadocumplimiento`],	contact[`conservarregistros`],contact[`tiemporegistros`],contact[`trazabilidad`],contact[`staus`]
    
);
CREATE TABLE `contact` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`company`	TEXT NOT NULL,
	`phone`	TEXT NOT NULL,
	`mail`	TEXT NOT NULL,
	`adress`	TEXT NOT NULL,
	`city`	TEXT,
	`country`	TEXT,
	`website`	TEXT,
	`industry`	TEXT,
	`description`	TEXT,
	`transportemedio`	TEXT,
	`transportequimicos`	TEXT,
	`managername`	TEXT,
	`manageremail`	TEXT,
	`managerphone`	TEXT,
	`calidadname`	TEXT,
	`calidademail`	TEXT,
	`calidadphone`	TEXT,
	`finanzasname`	TEXT,
	`finanzasemail`	TEXT,
	`finanzasphone`	TEXT,
	`salename`	TEXT,
	`saleemail`	TEXT,
	`salephone`	TEXT,
	`cuentaname`	TEXT,
	`cuentaswift`	TEXT,
	`cuentaaba`	TEXT,
	`cuentanumber`	TEXT,
	`cuentabanco`	TEXT,
	`cuentaaddress`	TEXT,
	`certificados`	TEXT,
	`certificadoscomentarios`	TEXT,
	`certificadocumplimiento`	TEXT,
	`tiemporegistros`	TEXT,
	`trazabilidad`	TEXT,
	`status`	TEXT DEFAULT "new",
	`attach`	BLOB,
	`attach2`	BLOB,
	`attach3`	BLOB,
	`datevencimiento`	TEXT,
	`commecompras`	TEXT,
	`commeconta`	TEXT,
	`commecalidad`	TEXT
);

https://www.josedomingo.org/pledin/2018/04/flask-plantillas-con-jinja2-4a-parte/
Masterlist-end

#Comandos para ejecutarlo 
$ export FLASK_APP=main.py
$ flask run
 * Running on http://127.0.0.1:5000/

If you are on Windows, the environment variable syntax depends on command line interpreter. On Command Prompt:

C:\path\to\app>set FLASK_APP=hello.py

And on PowerShell:

PS C:\path\to\app> $env:FLASK_APP = "hello.py"

Alternatively you can use python -m flask:

$ export FLASK_APP=hello.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/

#Comando para instalar dependencias
pip install -r requirements.txt


#Activar modo envirinment
En Linux/Mac:

    export FLASK_ENV="development"

En Windows:

    set "FLASK_ENV=development"

#Logger para registrar los errores de la app
app.logger.debug('Mensaje de debug')
app.logger.warning('Una advertencia (%d advertencias)', 55)
app.logger.error('Un error fatal ha ocurrido!')


#Borrar prueba email
@app.route ('/email')
def email():
   msg = Message('Hello', sender = 'pom.pile.of.money@gmail.com', recipients = ['najerarodriguez04@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return render_template('index.html')

#Borrar prueba para subir archivo
@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get['file']
        if file:
            mimetype = file.content_type
            filename = werkzeug.secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename)
            return redirect(url_for('uploaded_file'))
        else:
            return redirect(url_for('upload'))

@app.route ('/subirbg', methods=['POST'])
def upload_file():
    target = os.path.join(APP_ROOT, 'static/attach')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    return render_template('forms/selecionar3.html')

#Link google console
https://console.cloud.google.com/cloudshell/editor?project=masterlist-237220&authuser=5&folder&organizationId



<div class="form-group row">
        <label for="phone" class="col-sm-2 col-form-label">Phone</label>
        <div class="col-sm-10">
            
            <select type="text" class="form-control" name="phone" value={{contact.phone}}>

                    <option>Coche</option>
                    
                    <option>Avión</option>
                    
                    <option>Tren</option>
                    
            </select>
        </div>
    </div>