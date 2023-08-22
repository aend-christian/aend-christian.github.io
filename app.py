import os
from flask import Flask, render_template, request

#Configure
app = Flask(__name__)

#Routes
@app.route("/")
@app.route("/index")
def hello():
    return render_template ('index.html')

@app.route("/book")
def book():
    return render_template ('book.html')

@app.route("/visualiser", methods=["GET", "POST"])
def visualiser():

    # POST METHOD:
    if request.method == "POST":
        body = request.form.get("mybody")
        hexbody = request.form.get("selectBody")
        bodyhex = str((hexbody))

        trim = request.form.get("mytrim")
        hextrim = request.form.get("selectTrim")
        trimhex = str((hextrim))

        frontDoor = request.form.get("myfrontd")
        hexfrontdoor = request.form.get("selectFrontDoor")
        fronthex = str((hexfrontdoor))

        garage = request.form.get("mygarage")
        hexgarage = request.form.get("selectGarage")
        garagehex = str((hexgarage))

        if request.form.get('action') == 'Save':
            return render_template('selection.html', body=body, bodyhex=bodyhex, trim=trim, trimhex=trimhex, frontDoor=frontDoor, fronthex=fronthex, garage=garage, garagehex=garagehex)
        
        elif request.form.get('action') == 'Apply':
            return render_template('apply.html', body=body, bodyhex=bodyhex, trim=trim, trimhex=trimhex, frontDoor=frontDoor, fronthex=fronthex, garage=garage, garagehex=garagehex)

    # GET METHOD:
    else:
        body = request.form.get("mybody")
        trim = request.form.get("mytrim")
        frontDoor = request.form.get("myfrontd")
        garage = request.form.get("mygarage")
        return render_template('visualiser.html')
    
@app.route("/apply")
def apply():
    return render_template('apply.html')

@app.route("/test")
def test():
    return render_template('test.html')