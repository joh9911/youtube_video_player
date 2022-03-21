import sqlite3
class Database:
    def __init__(self):
        self.conn=None
        self.cursor=None

        self.connectDatabase()
        self.createDatabase()

    def connectDatabase(self):
        self.conn=sqlite3.connect("user.db")
        self.conn.execute("PRAGMA foreign_keys = 1")
        self.cursor=self.conn.cursor()

    def createDatabase(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS user ( id TEXT PRIMARY KEY, pw TEXT, name TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS playlist (sequence INTEGER PRIMARY KEY,id TEXT, name TEXT, FOREIGN KEY(id) REFERENCES user(id))")

    def loginPage_loginCheck(self, id ,pw):
        data=[id,pw]
        self.cursor.execute("SELECT * FROM user WHERE id=? AND pw=?", data)
        result = self.cursor.fetchall()
        return result
    
    def signupPage_idCheck(self, id):
        data = [id]
        self.cursor.execute("SELECT * FROM user WHERE id=?", data)
        result = self.cursor.fetchall()
        return result
    
    def dataCreate(self,tableName,columns,values):
        tmp="INSERT INTO " + tableName + "("
        
        for index in range(0,len(columns)):
            tmp += columns[index]
            if index < len(columns)-1:
                tmp += ","
        
        tmp += ") VALUES("

        for index in range(0,len(values)):
            tmp +="?"
            if index < len(values)-1:
                tmp += ","
        
        tmp += ")"
        self.cursor.execute(tmp,values)
        self.conn.commit()

    def dataDelete(self,name):
        data=[name]
        self.cursor.execute("DELETE FROM playlist WHERE name=?",data)
        self.conn.commit()