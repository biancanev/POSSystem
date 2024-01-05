#Basic CRUD Methodologies
import pymongo as pm
import user
import bcrypt

#basic login
def authenticateUser(username:str, password:str)->user.User:
    reqUser = user.User().getUserInfo(username)
    print(reqUser["username"])
    if reqUser is not None:
        bytes = password.encode('utf-8')
        print(bytes)
        print(reqUser["password"])
        if bcrypt.checkpw(bytes, reqUser["password"]):
            return reqUser
        return None
    print("User not found")
    return None

#basic create    
def createAuthUser(username:str, password:str, fname:str, lname:str, phone:int, email:str):
    newUser = user.User()
    hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    newUser.username = username
    newUser.password = hash
    newUser.fname = fname
    newUser.lname = lname
    newUser.phone = phone
    newUser.email = email
    newUser.createUser()
    return

#basic delete
def deleteAuthUser(username:str, password:str):
    if authenticateUser(username, password) is not None:
        user.User().deleteUser(username)
    return

#test casing
#createAuthUser("testUser", "123456", "Test", "User", 1234567890, "test.user@test.com")
uname = input("Enter Username: ")
pwd = input("Enter Password: ")
newUser = authenticateUser(uname, pwd)
if newUser is not None:
    print("Auth Success:", newUser["username"], "has information", newUser["fname"], newUser["lname"])