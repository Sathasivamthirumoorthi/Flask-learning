
from crypt import methods
from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(200),nullable = False)
    dep = db.Column(db.String(200),nullable = False)
    phone = db.Column(db.String(200),nullable = False)
    email = db.Column(db.String(200),nullable = False)
    completed = db.Column(db.Integer,default=0,nullable = False)


    def __repr__(self):
        return '<student %r>' % self.name 

def __init__(self,name,dep,phone,email,completed):
    self.name = name    
    self.dep = dep
    self.phone = phone
    self.email = email
    self.completed = completed
       

@app.route('/students',methods=["GET"])
def index():
    students = Student.query.order_by(Student.id).all()

    return render_template("index.html",students = students)


@app.route('/addstudent',methods = ['GET','POST'])

def addStudent():
    if request.method == 'POST':
        name = request.form["name"]
        dep = request.form["dep"]   
        phone = request.form["phone"]
        email = request.form["email"]
        completed = request.form["completed"] 
        
        
        print(name,dep,phone,email,completed) 
        student = Student(name = name,dep = dep,phone =phone,email = email,completed = completed)

        try:
            db.session.add(student)
            db.session.commit()
            return redirect("http://127.0.0.1:5000/students")
        except:
            print("errrrrrrrorrrrrrrrrrrrr")
            return "error"
    else:
        return render_template("addStudent.html")

@app.route('/delete/<int:id>')

def delete(id):
    delete_student = Student.query.get_or_404(id)

    try:
        db.session.delete(delete_student)
        db.session.commit()
        return redirect("http://127.0.0.1:5000/students")
    except:
        return "error deleting student"


@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    student = Student.query.get_or_404(id)
    print(student)
    if request.method == 'POST':
        student.name = request.form["name"]
        student.dep = request.form["dep"]   
        student.phone = request.form["phone"]
        student.email = request.form["email"]
        student.completed = request.form["completed"] 
        try:
            db.session.commit()
            return redirect("http://127.0.0.1:5000/students")
        except:
            print("errrrrrrrorrrrrrrrrrrrr")
            return "error"
        
    else:
        return render_template("edit.html",student = student)




if __name__ == "__main__":
    app.run(debug=True) 