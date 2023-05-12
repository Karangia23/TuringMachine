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
                        a = []
                        i = 0
                        while symbol != '#':
                            if symbol == 'l':
                                temp = ''
                                i+= 1
                                symbol = line[startPos + i]
                                while symbol != ' ':
                                    temp += symbol
                                    i+= 1
                                    symbol = line[startPos + i]
                                k = self.moveLeft(int(temp))
                                a.append(k)

                            elif symbol == 'r':
                                temp = ''
                                i+= 1
                                symbol = line[startPos + i]
                                while symbol != ' ':
                                    temp += symbol
                                    i+= 1
                                    symbol = line[startPos + i]
                                k = self.moveRight(int(temp))
                                a.append(k)

                            elif symbol == 'g':
                                k = self.headRead()
                                a.append(k)

                            elif symbol == 'w':
                                temp = ''
                                i+= 1
                                while symbol != ' ':
                                    symbol = line[startPos + i]
                                    temp += symbol
                                    i+= 1
                                k = self.headWrite(temp)
                                a.append(k)

                            elif symbol == '$':
                                temp = ''
                                i+= 1
                                symbol = line[startPos + i]
                                while symbol != ' ':
                                    temp += symbol
                                    i+= 1
                                    symbol = line[startPos + i]
                                k = self.changeState(temp)
                                a.append(k)                                
                                
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
