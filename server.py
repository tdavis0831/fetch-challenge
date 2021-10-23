
#routes

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud

app = Flask(__name__)
app.secret_key = "dev"


#add transaction for specfic player and date
@app.route("/addtransaction", methods=["PUT"] )
def create_user_transaction(payer, points, timestamp):

    user = PayerAccountInfo(payer=payer, points=points, timestamp=timestamp)

    db.session.add(user)
    db.session.commit()

    return user
    return (f"transaction added")


#spend points route
# @app.route("/redeem", methods=["PUT"])
# def redeem_points():
#     points = 


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
