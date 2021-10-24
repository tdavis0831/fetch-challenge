"""script to seed database"""

import os 
import json
from datetime import datetime

#imported filed that are needed
import crud
import model
import server


#drops any old db, creates a new one
os.system("dropdb fetch")
os.system("createdb fetch")

#creates the data in the table
model.connect_to_db(server.app)
model.db.create_all()

#load user info from JSON file

with open("data/users.json") as f:
    user_data = json.loads(f.read())

#create users and stores in list 

users_in_db=[]

for user in user_data:
    payer, points = (
        user["payer"],
        user["points"]
    )
    
    timestamp=datetime.strptime(user["timestamp"], "%Y-%m-%d")

    db_user = crud.create_user_transaction(payer, points, timestamp)
    users_in_db.append(db_user)