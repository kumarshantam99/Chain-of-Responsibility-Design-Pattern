"""
Template Method design Pattern to avoid super anti pattern

"""

from abc import ABC, abstractmethod

class Logger(ABC):

    def __init__(self, next_logger):
        self.__next_logger=next_logger
    
    @abstractmethod
    def make_entry(self,message):
        pass
    
    def log(self, message):   # Template method to specify at a higher level how an algorithm is carried out.
        self.make_entry(message) # helper method to avoid code duplication
        if (self.__next_logger is None):
            return
        else:
            self.__next_logger.log(message)



class ConsoleLogger(Logger):

    def make_entry(self, message):
        print("**Console**" + message)

class FileLogger(Logger):

    def make_entry(self, message):
        print("**File**" + message)


class DataBaseLogger(Logger):

    def make_entry(self, message):
        print("*DataBase**" + message)

console1=ConsoleLogger(None) # Last object in chain
file1=FileLogger(console1) # next logger object linked to console1
database1= DataBaseLogger(file1) #linked to file1

database1.log("test")


