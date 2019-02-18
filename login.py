# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 09:09:40 2019

@author: pythonister
"""



class User(object):
    def __init__(self, username, password):
        """Assumes username and password are strings"""
        self.username = username
        self.password = password
    def getName(self, password):
        if password == self.password:
            return "user name is " + self.username
        else:
            print("sorry, wrong password!!")
    def getPassword(self, username, password):
        if password == self.password:
            return self.password
    def changePass(self, password, newPass):
        if password == self.password:
            self.password = newPass
            print("password succesfully changed :)")
        else:
            print("sorry, wrong password :(")
            
    def login(self, username, password):
        if (username == self.username and password == self.password):
            print(f"Succesfully logged in as {username} :)")
        else:
            print("Wrong username or password :(")
    def __str__(self):
        return "( Username: '" + self.username + "'. Password: ********" + ")"
            

