from datetime import datetime #for date information
from flask_sqlachemy import SQLAlchemy #sqlalchemy import


db=SQLALCHEMY()  #sqlalchemy intergration



class PayerAccountInfo(db.model):
    #creates payer, points and time

    payer = db.Column(db.String)
    points = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    #repr function to show us information that is valueable
    def __repr__(self):
        return f"Payer payer_string={self.payer} points={self.points} date ={self.date}"

        