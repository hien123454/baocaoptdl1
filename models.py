# import os
# from firebase_admin import credentials, firestore, initialize_app
# import pdb
# import firebase_admin
# from firebase_admin import credentials
# import pandas as pd
# cred = credentials.Certificate('key.json')
# default_app = initialize_app(cred)
# db = firestore.client()



# def data_table(self):
#     todo_ref = db.collection('momos_nv')
#     all_todos = [doc.to_dict() for doc in todo_ref.stream()]
#     data = pd.DataFrame(all_todos)
#     return data

# class clomn:
#     def itemName(self):
#          data = data_table(1)  
#          df = data.itemName
#          return list(df)

#     def itemPriceFull (self):
#       data = data_table(1)
#       df = data.itemPriceFull 
#       return list(df)
# print(data_table(1))
# print(clomn.itemPriceFull(1))


