import re

class TurMachine:
    def __init__(self,file,tape=[]):
        self.alphabet
        self.tape = tape
        self.headIndex = 0
        self.states = []
        self.currentState

        nameStates = []
        with open(file, "r") as f:
            lineNumber = 0
            for line in f:
                if lineNumber == 0:
                    #first line in file corresponds to alphabet
                    for char in line:
                        self.alphabet.append(char)
                elif lineNumber == 1:
                    #second line are the names of the states
                    for word in line:
                        nameStates.append(word)
                elif line == "":
                    break
                else:
                    cases = {}
                    state = nameStates[lineNumber-2]
                    for i in re.finditer('/(+/)', line):
                        cases[(line[(i.start()+i.end())/2])] = i.end()
                    for case in cases:
                        startPos = cases[case]+1
                        symbol = line[startPos]
                        i = 0
                        while symbol != '#':
                            if symbol == 'l':
                                pass
                            elif symbol == 'r':
                                pass
                            elif symbol == 'g':
                                pass
                            elif symbol == 'w':
                                pass
                            elif symbol == '$':
                                pass
                            i += 1
                            symbol = line[startPos + i]



                lineNumber += 1
    def headRead(self):
        return self.tape[self.headIndex]
    def headWrite(self, value):
        self.tape[self.headIndex] = value 
    def moveLeft(self, value=1):
        if(self.headIndex - value <= 0):
            raise Exception("Head index cannot be lower than 0")
        else:
            self.headIndex -= value
    def moveRight(self):
        if(self.headIndex >= len(self.tape)-1):
            raise Exception("Head index cannot be larger than tape length")
        else:
            self.headIndex += 1
    def changeState(self, stateName):
        self.currentState = self.states[stateName]
    def translateState(self):
