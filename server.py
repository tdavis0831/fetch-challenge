
#routes

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db
import crud



#add transaction for specfic player and date
# @app.route("/addtransaction", methods=["PUT"] )
# def add_transaction_for_player_and_date():










app = Flask(__name__)
app.secret_key = "dev"









if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
