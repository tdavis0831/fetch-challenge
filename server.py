
#routes

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud

app = Flask(__name__)
app.secret_key = "dev"


#add transaction for specfic player and date
@app.route("/user", methods=["PUT"] )
def create_user(payer, points, timestamp):

    user = PayerAccountInfo(payer=payer, points=points, timestamp=timestamp)

    db.session.add(user)
    db.session.commit()

    return user

#gets all users
@app.route("/")
def get_all_users():
    all_users = crud.get_all_users()

    return all_users


#gets specific payer
@app.route("/{payer}")
def get_user(payer):
    specific_user = crud.get_user(payer)

    return specific_user





@router.post("/{payer_id}")
def create_transaction(payer, cost):

    payer_transactions =crud.get_all_active_transactions_of_payer(payer=payer)
#check for positive 
    if transaction.points > 0 and ( transaction.points - cost  =>  0):
        
        """ would need to pull the transactions in order and then subtract as much as possible of 
        the cost from the points and then continue to go down the line of transactions until you reach the end
        at that point, you can commit the transaction to the database""" 



@app.route("/transactions")
def get_transactions():
    all_transactions = crud.get_all_transctions()

    return all_transactions













if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
