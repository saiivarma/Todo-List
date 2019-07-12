from flask import Flask,render_template,jsonify,request,redirect
import pyrebase

app = Flask("__main__")

config = {
    "apiKey": "AIzaSyDagDom_feyHDXyXkhcCEc_iCn15rzed8A",
    "authDomain": "firebasic-68b4b.firebaseapp.com",
    "databaseURL": "https://firebasic-68b4b.firebaseio.com",
    "projectId": "firebasic-68b4b",
    "storageBucket": "",
    "messagingSenderId": "141020598185",
    "appId": "1:141020598185:web:5c3c9e92d63f0585"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

@app.route("/",methods = ["GET","POST"])
def func():
    if request.method == "POST":
        if request.form["submit"] == "add":
            name = request.form["name"]
            db.child("todo").child(name).push(name)
            todo = db.child("todo").get().val()
            lis = []
            for i in todo.values():
                m = list(i.values())
                lis.append(m[0])
            return render_template("index.html", to = lis)
        elif request.form["submit"] == "del":
            name = request.form["name"]
            db.child("todo").child(name).remove()
            todo = db.child("todo").get().val()
            if todo == None:
                return render_template("index.html")
            else:

                lis = []
                for i in todo.values():
                    m = list(i.values())
                    print(m)
                    lis.append(m[0])
                return render_template("index.html", to = lis)
    elif request.method == 'GET':
        todo = db.child("todo").get().val()
        if todo == None:
                return render_template("index.html")
        else:
            lis = []
            for i in todo.values():
                m = list(i.values())
                lis.append(m[0])
            return render_template("index.html", to = lis)      
    return render_template("index.html")


@app.route('/delete/<id>')
def delete_task(id):
    db.child("todo").child(id).remove()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)