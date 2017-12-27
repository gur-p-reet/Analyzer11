# Condensed Structure is written using single, double and triple bonds
# Each part is separated by single, double and triple bonds called segment
# Each segmant is a self complete with valancy zero by considering bonds from both sides
# if the valncy is not zero Highlinght that segment
# Inside segment the part is called group
# Group may contaons anything inside brackets Therefore bracket valancy is added to group element
# Bracket may contain group or  further segments. But the total valncy of the bracket part must be zero when first
# first bond is also considered. bracket alway attached with a group therefore the bracket valancy is added
# to the corresponding group.
# Segment has to be
# Hellllllll

 # import os
 # os.chdir('/usr/local/WorkSpace/PycharmProjects/nmrShifts/')
 # print (os.getcwd())
 # from ckeckFormula.checkCompound import *
 #
 # from spetralData.hello import *
 #
 # from compounds.checkCompound import *
 # hhhHHHHHHHHHHHHHH
 # Hello111
 # from gui.checkCompound import *

def isGroupExist1(group):

    print("MODULE METHOD")
    if group == "CO" or group == "OH" or group == "(OH)" or group == "NH" or \
                    group == "NH2" or group == "CH" or group == "CH" or \
                    group == "CH2" or group == "CH3" or group == "C2H2":
        return True

    return False


class checkCompounds:
    @classmethod
    def isGroupExist(cls,group):
        print("Hello")
        if group == "CO" or group == "OH" or group == "(OH)" or group == "NH" or \
                        group == "NH2" or group == "CH" or group == "CH" or \
                        group == "CH2" or group == "CH3" or group == "C2H2":
            return True

        return False

class checkFromula:

    def __init__(self):
        pass

    @staticmethod
    def isGroupExist(group):
        if group == "CO" or group == "OH" or group == "(OH)" or group == "NH" or \
                        group == "NH2" or group == "CH" or group == "CH" or \
                        group == "CH2" or group == "CH3" or group == "C2H2":
            return True

        return False

    @staticmethod
    def checkBr(condensedName):
        global countCloseBr, countOpenBr
        countOpenBr = 0
        countCloseBr = 0
        for b in range(0, condensedName.__len__()):
            c = condensedName[b]
            if c == '(':
                countOpenBr = countOpenBr + 1
                if condensedName[b - 1] == '-':
                    print("Unnecessary Brackets")
                    return False
            elif c == ')':
                countCloseBr = countCloseBr + 1
        # print (countCloseBr, "  ", countOpenBr)
        if countCloseBr == countOpenBr:
            return True
        return False

    @staticmethod
    def elementBonds(name):
        if name == "C":
            return 4
        elif name == "O":
            return 2
        elif name == "N":
            return 3
        elif name == "H":
            return 1
        return 0

    @staticmethod
    def getBondsNumber(bond):
        if bond == "-":
            return 1
        elif bond == "=":
            return 2
        elif bond == "-=":
            return 3
        else:
            return 1

    @staticmethod
    def groupBonds(name):
        if name == "CO":
            return 2
        elif name == "OH" or name == "(OH)":
            return 1
        elif name == "NH":
            return 2
        elif name == "NH2":
            return 2
        elif name == "CH":
            return 2
        elif name == "CH":
            return 3
        elif name == "CH2":
            return 2
        elif name == "CH3":
            return 1
        elif name == "C2H2":
            return 3
        return 0

    @staticmethod
    def getGroupValancy(self,groupName):
        global times
        times = 0
        grouplength = groupName.__len__()
        valancyList = []
        if self.groupBonds(groupName) != 0:
            groupValancy = self.groupBonds(groupName)
        else:
            i = 0
            char1 = groupName[0]
            groupValancy = self.elementBonds(char1)

            while i in range(1, grouplength - 1):
                char = groupName[i]
                if groupName[i].isalpha():
                    bonds = self.elementBonds(char)
                    st = i
                    while groupName[i + 1].isdigit():
                        i = i + 1
                    ed = i
                    times = ed - st
                    totalBonds = times * bonds
                    groupValancy = groupValancy - totalBonds
        return groupValancy


    bracketPart = ""

    @staticmethod
    def bracket(groupName, startBr2):
        global bracketPart
        global times
        length = groupName.__len__()
        # print(length)
        countBr = 1
        start11 = startBr2

        for j in range(start11 + 1, length):
            # print(groupName[j])
            if groupName[j] == '(':
                countBr = countBr + 1
                # print("countBr=", countBr)
            elif groupName[j] == ')':
                countBr = countBr - 1
                # print("countBr=1", countBr)
                if countBr == 0:
                    bracketPart = groupName[start11 + 1:j]
                    break
        return bracketPart


    startGrp = ""
    valency = 0
    skip = 0
    startGrp = 0
    valancy = 0
    char1 = ''
    char = ''
    i = 0
    startGrp1 = 0

    @staticmethod
    def isBondPresent(groupName):
        groupLength = groupName.__len__()
        for i in range(0, groupLength):
            c = groupName[i]
            if c == '-' or c == '=' or c == '(' or c == '-=':
                return False
        return True

    @staticmethod
    def getBracketsParts(segmentName, startGrp, startBr, level, option):
        # levelSp = "    "
        # for s in range(0,level):
        #     levelSp=levelSp+"    "
        # print("Level=", level)
        countBr = 0
        char2 = ''
        end = 0
        start = 0
        startGrp3 = startGrp
        startBr3 = startBr
        groupLength = startBr
        char2 = segmentName[groupLength]
        CF = checkFromula
        while char2 == '(' and groupLength <= segmentName.__len__() - 1:
            groupName = CF.bracket(segmentName, groupLength)
            # print(levelSp,"groupName= ", groupName)
            groupLength = groupLength + groupName.__len__() + 2
            if groupLength <= segmentName.__len__() - 1:
                char2 = segmentName[groupLength]
                start = groupLength
                while char2.isdigit() and groupLength <= segmentName.__len__() - 1:
                    groupLength = groupLength + 1
                    if groupLength <= segmentName.__len__() - 1:
                        char2 = segmentName[groupLength]
                    end = groupLength
                times = segmentName[start:end]
            else:
                times = 1

            if times == "":
                times = 1
            else:
                times = times
            # print(levelSp,"times =", times)

            CF.getStructure(groupName, times, level + 1, option)
            # print(levelSp,"groupName= ", groupName,"times =",times)
            countBr = countBr + 1
        startGrp = startGrp3
        startBr = startBr3
        segName = segmentName[startGrp:groupLength]
        # print (levelSp,"seg11=",segName , "seg11Length=",groupLength)

        return segName

    @staticmethod
    def getStructure(condensedName, times, level, option):
        nameLength = condensedName.__len__()
        levelSp = "    "
        for s in range(0, level):
            levelSp = levelSp + "    "

        char = ''
        char1 = ''
        i = 0
        startGrp1 = 0
        valancyGrp = 0
        if option != "segmentName":
            print("Level= ", level, levelSp, " Structure Formula= ", condensedName, "Times= ", times)
        CF=checkFromula
        if CF.isGroupExist(condensedName):
            if option == "getValancy":
                valancyGrp = CF.groupBonds(condensedName)
                print(levelSp, "Segment Name= ", condensedName, "GroupBonds= ", valancyGrp)
            return valancyGrp

        else:
            while i <= nameLength - 1:
                char = condensedName[i]
                if char == '-' or i == 0 or char == '=' or char == '-=':
                    if i == 0:
                        startGrp = i
                    else:
                        startGrp = i + 1
                    startGrp1 = startGrp
                    char1 = condensedName[startGrp]
                    while char1 != '(' and char1 != '-' and char1 != '=' and char1 != '-=' and i != nameLength:
                        i = i + 1
                        if i <= nameLength - 1:
                            char1 = condensedName[i]
                    if char1 == '(':

                        segmentName = CF.getBracketsParts(condensedName, startGrp, i, level, "segmentName")

                        if CF.isGroupExist(segmentName):
                            if option == "getValancy":
                                valancyGrp = CF.groupBonds(segmentName)
                                print(levelSp, "Segment Name= ", segmentName, "Group Bonds= ", valancyGrp)
                        else:
                            segmentName = CF.getBracketsParts(condensedName, startGrp, i, level, option)
                        i = startGrp + segmentName.__len__() - 1

                    else:

                        end1 = i
                        segmentName = condensedName[startGrp:end1]
                        if option != "segmentName":
                            print("Level= ", level, levelSp, " Segment Name = ", segmentName)
                            CF.getStructure(segmentName, 1, level + 1, option)
                        startGrp = startGrp1
                        i = end1 - 1

                i = i + 1



def main():
    #  CH(CH2-CH(CH2=CH2)-OH)2-CH(CH2-CH2=CH-OH)5
    # CH(CH(CH2-CH(CH2=CH2)23(OH)2(C2H2)2)3-OH)4-NH2
    print('Enter Condensed Structural Formula (use bonds to separate groups)')
    condensedName = input("Enter Name")
    # hh=checkCompounds1
    # gg=checkCompounds1
    # hh.isGroupExist("AA")
    # gg.isGroupExist("AA")

    cf=checkFromula
    global level
    level = 1
    if cf.checkBr(condensedName):
        cf.getStructure(condensedName, 1, level, "Check")
    else:
        print("Enter The Right Formula")

     # Hello
if __name__ == "__main__":
    main()

