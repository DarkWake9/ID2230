'''Program to store the usernames and passwors in a hash table (with chaining) 
and check for correct login credentials when user enters the Username and password'''

import pandas as pd
import numpy as np

### Node class
class Node:
    
    def __init__(self,keyvalue):
        self.keyvalue = keyvalue
        self.next = None

### Linked list class
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    #customized insert function
    def insert(self, keyvalue):
        if not self.head:
            self.head = Node(keyvalue)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(keyvalue)
        
    def search(self,keyvalue):
        temp = self.head
        while temp:
            if temp.keyvalue[0] == keyvalue:
                return [True, temp.keyvalue]
            temp = temp.next
        return [False,0]
    

### hash table class
class HashTable:
    
    def __init__(self,size):
        self.size  = size
        self.h_table = np.array([None]*self.size)
        for x in range(self.size) :
            self.h_table[x] = LinkedList()

    '''hash function: sums up the ascii values of all the characters in the user name
    # and returns the remainder on dividing by 36 '''
    def h_function(self, keyvalue):
        self.keyvalue = keyvalue
        i=0
        total=0
        while i<len(keyvalue):
             total = total+ord(keyvalue[i])
             i=i+1
        return i % 36
    
    #Insert key function customized for this case
    def insert_key(self, keyvalue):
        self.h_table[self.h_function(keyvalue[0])].insert(keyvalue)
        return 0

    #Searches for the username in the hash tbale and if found,
    #returns a list containing True aand the username password pair for later use
    def search_key(self,keyvalue) :
        index = self.h_function(keyvalue)
        found = self.h_table[index].search(keyvalue)
        if found[0]:
            return [True,found[1]]
        else:
            return [False,0]
  
#initializing the hashtable
HT = HashTable(36)

#reading the data from the .csv file
data = np.array(pd.read_csv("userInfo.csv", names = ["Username", "Password"]))

#Storing the data in hash table
for keyvalue in data:
    HT.insert_key(keyvalue)

'''Prompting the user to enter the username then check it's validity, if valid,
   then accept the password and if correct, display that login is succesful'''
username = input("Please Enter the Username: ")
valid_user = HT.search_key(username)
if not valid_user[0]:
    print("Name Not Found")
    
else:
    password = input("Please enter your password: ")
    if password == valid_user[1][1]:
        print("\nLogin Successful")
    else:
        print("Incorrect password")