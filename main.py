import re
from functools import partial

class TurMachine:
    def __init__(self,file):
        self.turMachineName = ""
        self.alphabet = []
        self.tape = []#[[1,2,3,4],[-,-,-,-,-,-]]
        self.states = {} #{state1:{AZ: [a(),b(),c()]; BZ: doZ}}
        self.currentState = ""
        self.acceptState = ""
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
                    self.currentState = line.rstrip()
                elif lineNumber == 2:
                    self.tapeNumber = (int(line))
                    for i in range(int(line)):
                        self.tape.append([])
                        self.head.append(0)
                elif lineNumber == 3:
                    self.acceptState = line.rstrip()
                elif line[0].isalpha():
                    line = line.replace(" ", "")
                    reStateName = re.search("^(\w)[\w]+(?=,)", line)
                    stateName = reStateName.group()
                    stateName.replace(" ", "")
                    reWhatToLookUp = re.search("(?<=,).+", line)
                    valuesInTapes = reWhatToLookUp.group()
                    valuesInTapes.replace(" ", "")
                    temp = valuesInTapes.split(',')
                    valuesInTapes = "".join(str(x) for x in temp)
                    valuesInTapes.replace(" ", "")
                    line = next(f)
                    lineNumber += 1
                    reNewState = re.search("^(\w)[\w]+(?=,)", line)
                    newState = reNewState.group()
                    newState.replace(" ", "")
                    temp = re.search("(?<=,).+", line)
                    whatToDo = temp.group().replace(" ", "").split(',')
                    j = []
                    for i in range(len(self.tape)):
                        k = partial(self.headWrite, whatToDo[i], i)
                        j.append(k)
                    for i in range(len(whatToDo)):

                        currentTape = i
                        if currentTape > len(self.tape)-1:
                            currentTape = i - len(self.tape)
                        
                        if whatToDo[i] == '<':
                            k= partial(self.moveLeft, currentTape)
                            j.append(k)
                        elif whatToDo[i] == '>':
                            k = partial(self.moveRight, currentTape)
                            j.append(k)
                        elif whatToDo[i] != '-':
                            k = partial(self.headWrite, whatToDo[i], currentTape)
                    k = partial(self.changeState, newState)
                    j.append(k)
                    try:
                        self.states[stateName][valuesInTapes] = j
                    except:
                        self.states.update({stateName:{valuesInTapes:j}})

                        
                    #sczytac dwie linijki
                    #tu co na pierwszej linijce
                lineNumber += 1

    def headRead(self, tapeNumber = 0):
        try:
            tape = self.tape[tapeNumber]
            return tape[self.head[tapeNumber]]
        except:
            self.tape[tapeNumber].append('_')
            return '_'
    def headWrite(self, value, tapeNumber = 0):
        try:
            self.tape[tapeNumber][self.head[tapeNumber]] = value
        except:
            self.tape[tapeNumber].append(value)
    def moveLeft(self, tapeNumber=0):
        self.head[tapeNumber] -= 1
        if self.head[tapeNumber] < 0:
            self.tape[tapeNumber].insert(0, "_")
            self.head[tapeNumber] = 0 
    def moveRight(self, tapeNumber = 0):
        self.head[tapeNumber] += 1
    def changeState(self, stateName):
        self.currentState = stateName
    def turkMachine(self, input):
        for letter in input:
            self.tape[0].append(letter)
        l = False
        while self.currentState != self.acceptState:
            try:
                buffer = ''
                for i in range(len(self.tape)):
                    try:
                        buffer +=self.headRead(i)
                    except:
                        buffer += '_'
                list = self.states[self.currentState][buffer]
                for i in list:
                    i()
            except:
                l = True
                break
        if l is False:
            print(self.tape)
            print("finished without problems")
        else:
            print("eror")
    def debug(self):
        print(self.states)

arab = TurMachine("nihilizm.txt")
arab.turkMachine("BABA_BAB")
#arab.debug()