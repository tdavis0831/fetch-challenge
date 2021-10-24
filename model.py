from datetime import datetime #for date information
from flask_sqlalchemy import SQLAlchemy #sqlalchemy import


db = SQLAlchemy()  #sqlalchemy intergration



class PayerAccountInfo(db.Model):
    #creates payer, points and time

    __tablename__ = "payers"
    payer_id = db.Column(db.String, primary_key=True)
    payer = db.Column(db.String)
    points = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)

    #repr function to show us information that is valueable
    def __repr__(self):
        return f"Payer payer_string={self.payer} points={self.points} date ={self.timestamp}"

class Transaction(db.Model):
    __tablename__ = "transactions"
    trans_id = db.Column(db.String, primary_key=True, index=True)
    points = db.Column(db.Integer)
    used_points = db.Column(db.Integer, default=0)
    payer = db.Column(db.String)
    transaction_date = db.Column(db.DateTime)
    fk_payer_id = db.Column(db.String, db.ForeignKey("payers.payer_id"))
    
    user = db.relationship("User", back_populates="transactions")

    def __repr__(self):
        return f"Payer payer={self.payer} points={self.points} date ={self.timestamp}"

    






#this function connects to the database named fetch that was created the rest of this code is used to 
#Initalize the database
def connect_to_db(flask_app, db_uri="postgresql:///fetch", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    #added this to vizualize connection was sucessful
    print("connected")


if __name__ == "__main__":
    from server import app




    connect_to_db(app)

