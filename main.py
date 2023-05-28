import re
from functools import partial

class TurMachine:
    def __init__(self,file):
        self.turMachineName
        self.alphabet = []
        self.tape = []#[[1,2,3,4],[-,-,-,-,-,-]]
        self.states = {} #{state1:{AZ: [a(),b(),c()]; BZ: doZ}}
        self.currentState
        self.acceptState
        self.head = []
        self.tapeNumber = 0
        self.nameStates = []
        lineNumber = 0
        with open(file, "r") as f:
            myF = iter(f)
            for line in myF:
                if lineNumber == 0:
                    self.turMachineName = line
                elif lineNumber == 1:
                    self.acceptState = line
                elif lineNumber == 2:
                    self.tapeNumber = (int(line))
                    for i in range(int(line)):
                        self.tape.append([])
                        self.head.append(0)
                elif line[0].isalpha():
                    reStateName = re.search("^(\w)[\w]+,", line)
                    stateName = reStateName.group()
                    reWhatToLookUp = re.search("(?<=,).+", line)
                    valuesInTapes = reWhatToLookUp.group()
                    temp = valuesInTapes.split(',')
                    valuesInTapes = "".join(str(x) for x in temp)
                    next(f)
                    reNewState = re.search("^(\w)[\w]+,", line)
                    newState = reNewState.group()
                    temp = re.search("(?<=,).+", line)
                    whatToDo = "".join(str(x) for x in temp)
                    j = []
                    for i in range(len(self.tape)):
                        k = partial(self.headWrite, whatToDo[i], i)
                        j.append(k)
                    for i in range(len(self.tape), len(whatToDo)-1):
                        currentTape = i-len(self.tape)
                        if whatToDo[i] == '<':
                            k= partial(self.moveLeft, currentTape)
                            j.append(k)
                        elif whatToDo[i] == '>':
                            k = partial(self.moveRight, currentTape)
                            j.append(k)
                    k = partial(self.changeState, newState)
                    j.append(k)
                    self.states[stateName][valuesInTapes][j]
                    
                        
                    #sczytac dwie linijki
                    #tu co na pierwszej linijce
                lineNumber += 1

    def headRead(self, tapeNumber = 0):
        tape = self.tape[tapeNumber]
        return tape[self.head[tapeNumber]]
    def headWrite(self, value, tapeNumber = 0):
        try:
            self.tape[tapeNumber][self.head[tapeNumber]] = value
        except:
            self.tape[tapeNumber].append(value)
    def moveLeft(self, tapeNumber=0):
        self.head[tapeNumber] -= 1
        if self.head[tapeNumber] < 0:
            self.tape[tapeNumber]
    def moveRight(self, tapeNumber = 0):
        self.head[tapeNumber] -= 1
    def changeState(self, stateName):
        self.currentState = self.states[stateName]
    def turkMachine(self, input):
        self.tape[0] = input
        l = False
        while self.currentState != self.acceptState:
            buffer = ''
            for i in range(len(self.tape)):
                buffer +=self.headRead(i)
            try:
                self.states[self.currentState][buffer]
            except:
                print("Rejected")
                l = True
                break
        if l is False:
            print("finished without problems")
