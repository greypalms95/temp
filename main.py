from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == "GET":
    return render_template("index.html")
  else:
    name = request.form.get('name')
    classs = request.form.get('classs')
    temperature = request.form.get('temperature')
    fout = open("Temperature.txt", 'a')
    fout.write(name + ' | ' + classs + ' | ' + temperature + '\n' )
    fout.close()
    return render_template('index.html')




    
app.run(host='0.0.0.0', port=8080)
