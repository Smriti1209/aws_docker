
# Python program to illustrate 
# delete, drop and remove
import pymongo
client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.yfk5s.mongodb.net/AWS?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
db = client.AWS
coll = db.Student
  
emp_rec1 = {"univ_id":"1000","first_name":"Smritikana","last_name":"Maity","age":28,"course":"CSE"}
emp_rec2 = {"univ_id":"1001","first_name":"Meshal","last_name":"Shah","age":25,"course":"EE"}
emp_rec3 = {"univ_id":"1002","first_name":"Sounak","last_name":"Bhattacharyya","age":27,"course":"IT"}
  
# Insert Data
rec_id1 = coll.insert_one(emp_rec1)
rec_id2 = coll.insert_one(emp_rec2)
rec_id3 = coll.insert_one(emp_rec3)
print("Data inserted with record ids",rec_id1," ",rec_id2,rec_id3)