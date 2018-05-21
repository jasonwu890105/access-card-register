from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/accesscard'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    tnumber_=db.Column(db.String(120), unique=True)
    fullname_=db.Column(db.String(120), unique=True)

    def __init__(self, email_, tnumber_, fullname_):
        self.email_=email_
        self.tnumber_=tnumber_
        self.fullname_=fullname_

    def __repr__(self):
        return'<Data %r>' %self.email_



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    if request.method=='POST':
        email=request.form["email_name"]
        tnumber=request.form["t_number"]
        fullname=request.form["full_name"]
        print (email, tnumber,fullname)
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data=Data(email, tnumber, fullname)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
    return render_template("index.html", text = "You have already registered your card!")
if __name__ == '__main__':
    app.debug=True
    app.run()
