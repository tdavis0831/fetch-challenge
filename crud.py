from model import db, PayerAccountInfo, connect_to_db

#add user to database, will add individual transactions

def create_user_transaction(payer, points, timestamp):

    user = PayerAccountInfo(payer=payer, points=points, timestamp=timestamp)

    db.session.add(user)
    db.session.commit()

    return user

def get_user(payer): 
    #get user by payer
    return db.query(PayerAccountInfo).filter(PayerAccountInfo.payer==payer).first()

def get_all_users(): 
    #get user by payer
    return db.query(PayerAccountInfo).all()



def get_transaction(id):
    #get single transaction
    return db.query(Transaction).filter(Transaction.id == id).first()


def get_all_transactions():

    return db.query(Transaction).all()


def get_positive_transactions(payer):

    return db.query(Transaction).filter(Transaction.payer == payer and Transaction.points > 0).order_by("timestamp").all()


def get_positive_by_payer(payer):

    return db.query(Transaction).filter(Transaction.payer == payer and Transaction.points > 0).all()


    





















# def spend_points (payer, owed_points):
#     #gets all of user transatctions from oldest to newest
#     user_info = db.session.query(PayerAccountInfo).filter(PayerAccountInfo.payer == payer).order_by("timestamp").all()
#     total_points=0
    
    
#     #get total points that user has
#     for i in range(len(user_info)):
#         total_points += user_info[i].points
#         difference = total_points - owed_points

#     return total_points

  

#     if owed_points = 0:
#         break;
#         else if (user_info[0] < owed_points):
#             owed_points -= user_info[0]


#     #get total points that user has
#     for i in range(len(user_info)):
#         total_points += user_info[i].points
#         difference = total_points - owed_points

#     return difference




    # if (total_points > 0) and (owed_points <= total_points):

    #     new_total = total_points - owed_points
    # return new_total #take new total to create transaction

    # else:
    #     difference = (owed_points - user_info[i].points)

        

if __name__ == "__main__":
    from server import app

    connect_to_db(app)