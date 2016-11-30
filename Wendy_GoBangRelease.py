import copy


#...Define Function...
###...
def CheckCombinationWin(CombinationArrayList):
    RetNumber = 0
    for ArrayNumber in range(572):
        if(CombinationArrayList[ArrayNumber] == 5):
            RetNumber = 1

    return (RetNumber)
            
###...
def CheckCombinationScore(CombinationArrayList):
    RetScore = 0
    for ArrayNumber in range(572):
        if(CombinationArrayList[ArrayNumber] == 5):
            RetScore = RetScore + 100000
        elif (CombinationArrayList[ArrayNumber] == 4):
            RetScore = RetScore + 10000
        elif (CombinationArrayList[ArrayNumber] == 3):
            RetScore = RetScore + 1000
        elif (CombinationArrayList[ArrayNumber] == 2):
            RetScore = RetScore + 10
        elif (CombinationArrayList[ArrayNumber] == 1):
            RetScore = RetScore + 1

    return (RetScore)
            
        
###...
def CheckCombination(WinDatabaseArray, CombinationArray, CoordinatePlacement, master, guest):
    for ArrayNumber in range(572):
        if((WinDatabaseArray[master][CoordinatePlacement[0]][CoordinatePlacement[1]][ArrayNumber] == 1) and (CombinationArray[master][ArrayNumber] < 6)):
            if(CombinationArray[master][ArrayNumber] < 5):
                CombinationArray[master][ArrayNumber] = CombinationArray[master][ArrayNumber] + 1

        if(WinDatabaseArray[guest][CoordinatePlacement[0]][CoordinatePlacement[1]][ArrayNumber]):
            WinDatabaseArray[guest][CoordinatePlacement[0]][CoordinatePlacement[1]][ArrayNumber] = 0;
            CombinationArray[guest][ArrayNumber] = 6
        
    return


###...
def CheckCrossLine(WinDatabaseCheck, CombinationCheck, Client, CoordinateY, CoordinateX):
    RetNumber   = 0
    LineNumber  = 0
    
    CrossNumber = 0
    MaxChess    = 0
    for ArrayNumber in range(0, 165):
        if(WinDatabaseCheck[Client][CoordinateY][CoordinateX][ArrayNumber] and (CombinationCheck[Client][ArrayNumber] > 1) and (CombinationCheck[Client][ArrayNumber] < 6)):
            CrossNumber = 1
            MaxChess    = CombinationCheck[Client][ArrayNumber]
            if(MaxChess > 2):
                break
    if(CrossNumber):
        RetNumber  = RetNumber + 1
    if(MaxChess > 2):
        LineNumber = LineNumber + 1
                    
    CrossNumber = 0
    MaxChess    = 0
    for ArrayNumber in range(165, 330):
        if(WinDatabaseCheck[Client][CoordinateY][CoordinateX][ArrayNumber] and (CombinationCheck[Client][ArrayNumber] > 1) and (CombinationCheck[Client][ArrayNumber] < 6)):
            CrossNumber = 1
            MaxChess    = CombinationCheck[Client][ArrayNumber]
            if(MaxChess > 2):
                break
    if(CrossNumber):
        RetNumber  = RetNumber + 1
    if(MaxChess > 2):
        LineNumber = LineNumber + 1
                    
    CrossNumber = 0
    MaxChess    = 0
    for ArrayNumber in range(330, 451):
        if(WinDatabaseCheck[Client][CoordinateY][CoordinateX][ArrayNumber] and (CombinationCheck[Client][ArrayNumber] > 1) and (CombinationCheck[Client][ArrayNumber] < 6)):
            CrossNumber = 1
            MaxChess    = CombinationCheck[Client][ArrayNumber]
            if(MaxChess > 2):
                break
    if(CrossNumber):
        RetNumber  = RetNumber + 1
    if(MaxChess > 2):
        LineNumber = LineNumber + 1
                    
    CrossNumber = 0
    MaxChess    = 0
    for ArrayNumber in range(451, 572):
        if(WinDatabaseCheck[Client][CoordinateY][CoordinateX][ArrayNumber] and (CombinationCheck[Client][ArrayNumber] > 1) and (CombinationCheck[Client][ArrayNumber] < 6)):
            CrossNumber = 1
            MaxChess    = CombinationCheck[Client][ArrayNumber]
            if(MaxChess > 2):
                break
    if(CrossNumber):
        RetNumber  = RetNumber + 1
    if(MaxChess > 2):
        LineNumber = LineNumber + 1

    if(RetNumber > 1):
        if(LineNumber < 2):
            RetNumber = 1
    
    return (RetNumber)

###...
def AISelectPlacement(ChessboardOrg, WinDatabaseOrg, CombinationOrg, Master, Guest):
    WinDatabaseTemp = [[[[0 for data in range(572)] for x in range(15)] for y in range(15)] for index in range(2)]
    CombinationTemp = [[0 for data in range(572)] for index in range(2)]
    RetCoordinate   = [16, 16]
    ScoreOld        = [0, 0]
    ScoreMaster     = -30000
    ScoreMasterGx   = 0
    ScoreMasterMax  = 0
    MasterCoordinateMax = [16, 16]
    MasterCoordinate    = [16, 16]
    GroupMaster     = 0
    GroupGuest      = 0
    ScoreGuest      = 0
    ScoreGuestMax   = -30000
    ScoreGuestMax2  = -30000
    MasterGuestMax  = -30000
    MasterGuestMax2 = -30000
    CheckMax2       = 0
    GuestCoordinateMax  = [16, 16]
    GuestCoordinateMax2 = [16, 16]
    GuestCoordinate     = [16, 16]


    ScoreOld[Master] = CheckCombinationScore(CombinationOrg[Master])
    ScoreOld[Guest]  = CheckCombinationScore(CombinationOrg[Guest])
    if((ScoreOld[Master] == 0) and (ScoreOld[Guest] == 0)):
        RetCoordinate = [7, 7]
        return (RetCoordinate)
    print("Check guest...")
    for x in range(15):
        print(".")
        for y in range(15):
            if(ChessboardOrg[y][x] == 0):
                WinDatabaseTemp = copy.deepcopy(WinDatabaseOrg)
                CombinationTemp = copy.deepcopy(CombinationOrg)
                GuestCoordinate[0] = y
                GuestCoordinate[1] = x
                CheckCombination(WinDatabaseTemp, CombinationTemp, GuestCoordinate, Guest, Master)
                GroupGuest = CheckCrossLine(WinDatabaseTemp, CombinationTemp, Guest, y, x)
                ScoreGuest = CheckCombinationScore(CombinationTemp[Guest])
                if((ScoreGuest > 10000) and (ScoreGuest < 20000)):
                    ScoreGuest = ScoreGuest - 10000
                    GroupGuest = 1;
                if((ScoreGuest > 1000) and (ScoreGuest < 2000)):
                    ScoreGuest = ScoreGuest - 1000
                    GroupGuest = 1;
                if(ScoreGuest < 10000):
                    ScoreGuest = ScoreGuest * GroupGuest
                    
                if(ScoreGuest > ScoreGuestMax):
                    ScoreGuestMax2        = ScoreGuestMax
                    GuestCoordinateMax2   = copy.deepcopy(GuestCoordinateMax)
                    ScoreGuestMax         = ScoreGuest
                    GuestCoordinateMax[0] = y
                    GuestCoordinateMax[1] = x
    if((ScoreGuestMax2 + (ScoreGuestMax / 100)) > ScoreGuestMax):
        CheckMax2 = 1
    print("Check Master...")
    ScoreMasterMax = -30000
    for x in range(15):
        print(".")
        for y in range(15):
            if(ChessboardOrg[y][x] == 0):
                WinDatabaseTemp = copy.deepcopy(WinDatabaseOrg)
                CombinationTemp = copy.deepcopy(CombinationOrg)
                MasterCoordinate[0] = y
                MasterCoordinate[1] = x
                CheckCombination(WinDatabaseTemp, CombinationTemp, MasterCoordinate, Master, Guest)
                GroupMaster = CheckCrossLine(WinDatabaseTemp, CombinationTemp, Master, y, x)
                ScoreMaster   = CheckCombinationScore(CombinationTemp[Master])
                if(CheckMax2):
                    if((GuestCoordinateMax[0] == y) and (GuestCoordinateMax[1] == x)):
                        MasterGuestMax = ScoreMaster
                    if((GuestCoordinateMax2[0] == y) and (GuestCoordinateMax2[1] == x)):
                        MasterGuestMax2 = ScoreMaster
                        
                ScoreMasterGx = CheckCombinationScore(CombinationTemp[Guest])
                
                if(ScoreMaster > 10000):
                    GroupMaster = 1
                    
                ScoreMaster = ScoreMaster - ScoreMasterGx
                ScoreMaster = ScoreMaster * GroupMaster               
                if(ScoreMaster != 0):
                    if(ScoreMaster > ScoreMasterMax):
                        ScoreMasterMax = ScoreMaster
                        MasterCoordinateMax[0] = y
                        MasterCoordinateMax[1] = x
    if(ScoreMasterMax >= ScoreGuestMax):
        RetCoordinate = copy.deepcopy(MasterCoordinateMax)
    else:
        if(ScoreMasterMax < 100000):
            if(ScoreGuestMax > 3000):
                if(CheckMax2):
                    if((ScoreGuestMax + MasterGuestMax) > (ScoreGuestMax2 + MasterGuestMax2)):
                        RetCoordinate = copy.deepcopy(GuestCoordinateMax)
                    else:
                        RetCoordinate = copy.deepcopy(GuestCoordinateMax2)
                else:
                    RetCoordinate = copy.deepcopy(GuestCoordinateMax)
            else:
                RetCoordinate = copy.deepcopy(MasterCoordinateMax)
        else:
            RetCoordinate = copy.deepcopy(MasterCoordinateMax)



    return (RetCoordinate)


def InitialWinDatabase(WinDatabaseArray):
    WinIndexNumber = 0
    
    for x in range(15):
        for y in range(11):
            for ArrayNumber in range(5):
                WinDatabaseArray[y + ArrayNumber][x][WinIndexNumber] = 1
            WinIndexNumber = WinIndexNumber + 1
            
    for y in range(15):
        for x in range(11):
            for ArrayNumber in range(5):
                WinDatabaseArray[y][x + ArrayNumber][WinIndexNumber] = 1
            WinIndexNumber = WinIndexNumber + 1
            
    for x in range(11):
        for y in range(11):
            for ArrayNumber in range(5):
                WinDatabaseArray[y + ArrayNumber][x + ArrayNumber][WinIndexNumber] = 1
            WinIndexNumber = WinIndexNumber + 1
            
    for x in range(4, 15):
        for y in range(11):
            for ArrayNumber in range(5):
                WinDatabaseArray[y + ArrayNumber][x - ArrayNumber][WinIndexNumber] = 1
            WinIndexNumber = WinIndexNumber + 1
            
    return

def DisplayLine(ChessboardDisplay, LineNUmber):
    LineHead = chr(65 + LineNUmber) + "   "
    for j in range(15):
        if (ChessboardDisplay[LineNUmber][j]):
            if (ChessboardDisplay[LineNUmber][j] == 1):
                LineHead = LineHead + 'X '
            else:
                LineHead = LineHead + 'O '
        else:
            LineHead = LineHead + '+ '

    print(LineHead)
    return
   
def DisplayChessboard(ChessboardDisplay, TurnInformation):
    print("")
    print("")
    print("")
    print("")
    
    if TurnInformation:
        print("Your turn...")
    else:
        print("My turn...")

    print("")
    print("    0 0 0 0 0 0 0 0 0 0 1 1 1 1 1")
    print("    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4")
    
    for i in range(15):
        DisplayLine(ChessboardDisplay, i)
       
    return

def InputPlacement():
    PlacementCoordinate = [16, 16]

    while(1):
        InputString = input("Please input your placement (CNN):")

        if(len(InputString) < 2):
            continue

        if(InputString[1] in "XxUu"):
            PlacementCoordinate = [16, 16]
            print("Exit......")
            break

        if(len(InputString) == 3):
            InputNumber0 = ord(InputString[1]) - 48
            InputNumber1 = ord(InputString[2]) - 48
            ColNumber = InputNumber0 * 10 + InputNumber1
        
            if ((InputString[0] in "ABCDEFGHIJKLMNOabcdefghijklmno") and
                (InputString[1] in "0123456789") and
                (InputString[2] in "0123456789") and
                (ColNumber < 15)):

                RowChar = ord(InputString[0])
                if (InputString[0] >= 'a'):
                    RowNumber = RowChar - 97
                else:
                    RowNumber = RowChar - 65

                PlacementCoordinate[0] = RowNumber
                PlacementCoordinate[1] = ColNumber
                break

        print("")
        print("")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("")
        print("Please input your placement like D08, D is line of D, 08 is col of 08")
        print("")
        print("")
        print("")


    return PlacementCoordinate



Chessboard   = [[0 for y in range(15)] for x in range(15)]
WinDatabase  = [[[[0 for data in range(572)] for x in range(15)] for y in range(15)] for index in range(2)]
Combination  = [[0 for data in range(572)] for index in range(2)]
Coordinate   = [0 for placement in range(2)]

WhosTurn = 0
InitialWinDatabase(WinDatabase[0])
InitialWinDatabase(WinDatabase[1])

while(1):
    DisplayChessboard(Chessboard, WhosTurn);

    if WhosTurn:
        Coordinate = InputPlacement()
        if Coordinate == [16, 16]:
            break
    else:
        Coordinate = AISelectPlacement(Chessboard, WinDatabase, Combination, 0, 1)
        print(Coordinate)

    if(Chessboard[Coordinate[0]][Coordinate[1]] == 0):
        if WhosTurn:
            Chessboard[Coordinate[0]][Coordinate[1]] = 1
            CheckCombination(WinDatabase, Combination, Coordinate, 1, 0)
            WhosTurn = 0
            
            if(CheckCombinationWin(Combination[1])):
                DisplayChessboard(Chessboard, WhosTurn);
                print("You win!")
                break
        else:
            Chessboard[Coordinate[0]][Coordinate[1]] = 2
            CheckCombination(WinDatabase, Combination, Coordinate, 0, 1)
            WhosTurn = 1
            
            if(CheckCombinationWin(Combination[0])):
                DisplayChessboard(Chessboard, WhosTurn);
                print("I win!")
                break

    else:
        print("")
        print("")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("")
        print("This placement alredy has chessman!")
        print("")
        print("")
        print("")
        
    
