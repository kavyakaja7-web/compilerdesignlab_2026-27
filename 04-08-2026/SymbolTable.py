"""
SymbolTable -- fully implemented.

Declarations write into a SymbolTable during parsing.
"""

from enum import Enum

DataType = Enum('DataType', ['INT'])


class SymbolTableEntry:
    def __init__(self, name, datatype):
        self.name = name
        self.datatype = datatype
        self.offset = None
    # it stores the name and datatype offset #for each single entry like offset as none #first
    def getSymbolName(self):
        return self.name

    def getDataType(self):
        return self.datatype

    def getOffset(self):
        return self.offset

    def setOffset(self, offset):
        self.offset = offset
#to set the offset with some fixed value we use #this set offset function 
    def print(self):
        print(f"{self.name}: {self.datatype.name}, offset = {self.offset}")


class SymbolTable:
    def __init__(self):
        self.table = []
#the above function run whenever you create the #object to the symboltable it is a construction 
    def addSymbol(self, symbol):
        self.table.append(symbol)
#add each symbol entry to the symbol table with #datatype and 0 offset
    def nameInSymbolTable(self, name):
        return any(entry.getSymbolName() == name
                   for entry in self.table)
#this is to check whether the identifier is #already initialise or not 
    def getSymbol(self, name):
        for entry in self.table:
            if entry.getSymbolName() == name:
                return entry
        return None
# this function is to print the name of the #symbol
    def getSizeOfType(self, datatype):
        if datatype == DataType.INT:
            return 4
        raise ValueError(f"Unknown data type: {datatype}")
# this function to assign the value of the #datatype example int 4 float 8 like this

    def assignOffsetsToSymbols(self):
        offset = 0
        for entry in self.table:
            entry.setOffset(offset)
            offset += self.getSizeOfType(entry.getDataType())
#this function to add the correct offset the #every entry in the symbol table 
    def size(self):
        total = 0
        for entry in self.table:
            total += self.getSizeOfType(entry.getDataType())
        return total
# to calculate the total size need to store all #this 

    def printSymbolTable(self):
        for entry in self.table:
            entry.print()
# this used to print the symbol table