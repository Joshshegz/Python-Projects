#Continuing Inheritance codde
from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is Already Opened")
        self.opened = True
    
    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is Already Opened")
        self.opened = False    

class FileStream(Stream):       
    def read(self):
        print("Reading data from a file ")

class NetworkStream(Stream):           
    def read(self):
        print("Reading data from a Network ")    


stream = Stream()
stream.open