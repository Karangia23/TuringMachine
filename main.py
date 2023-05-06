import re

class TurMachine:
    def __init__(self,file,tape=[]):
        self.alphabet
        self.tape = tape
        self.head = 0
        self.states
        self.currentState

        with open(file, "r") as f:
            for line in f:
                if line == 1:
                    pass
                elif line == 2:
                    pass
                else:



    def headRead(self):
        return self.tape[self.head]
    def headWrite(self, value):
        self.tape[self.head] = value 
    def moveLeft(self):
        if(self.head <= 0):
            raise Exception("Head index cannot be lower than 0")
        else:
            self.head -= 1
    def moveRight(self):
        if(self.head >= len(self.tape)-1):
            raise Exception("Head index cannot be larger than tape length")
        else:
            self.head += 1
    def changeState(self, stateName):
        self.currentState = self.states[stateName]
    def translateState(self):
