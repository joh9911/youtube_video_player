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
        self.cursor.execute("CREATE TABLE IF NOT EXISTS playlist (sequence INTEGER PRIMARY KEY,id TEXT, listname TEXT, FOREIGN KEY(id) REFERENCES user(id))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS player (sequence INTEGER PRIMARY KEY, playlistnum INT, url TEXT, name TEXT ,FOREIGN KEY(playlistnum) REFERENCES playlist(sequence))")

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

    def playlistdataDelete(self,id,num):    
        self.conn.execute("PRAGMA foreign_keys = 0")
        data=[id,num]
        self.cursor.execute("DELETE FROM playlist WHERE id=? AND sequence=?",data)
        self.conn.commit()
        self.conn.execute("PRAGMA foreign_keys = 1")
   
    def dataDelete(self, tableName, column, data):
        sql = "DELETE FROM " + tableName
        for index in range(0, len(column)):
            if index == 0:
                sql += " WHERE "
            sql += column[index] + " =?"
            if index < len(column) - 1:
                sql += " AND "
        self.cursor.execute(sql,data)
        self.conn.commit()
            
    def dataRead(self,tableName, column, data): 
        sql = "SELECT * FROM " + tableName
        for index in range(0, len(column)):
            if index==0:
                sql += " WHERE "
            sql += column[index] + "=? "
            if index < len(column)-1:
                sql += " AND "

        self.cursor.execute(sql,data)
        result = self.cursor.fetchall()
        return result


