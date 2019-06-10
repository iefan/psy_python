import sys
sys.setrecursionlimit(1000000) #例如这里设置为一百万

global_arr = []
def findBlank(arr):
    global global_arr
    # find the blank of triangle
    curJumpPoints = findCanJumpChess(arr)
    if len(curJumpPoints) == 14:
        print(global_arr, "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("Over")
        return

    count = 0
    for iBlankPoint in curJumpPoints:
        count += len(curJumpPoints[iBlankPoint])
    if count == 0:
        print("one failure")
        global_arr = []
        return

    for iBlankPoint in curJumpPoints:
        if curJumpPoints[iBlankPoint] != []:
            # copy_arr = arr.copy()

            arr[iBlankPoint[0]][iBlankPoint[1]] = 1
            for iJumpPoint in curJumpPoints[iBlankPoint]:
                arr[iJumpPoint[0][0]][iJumpPoint[0][1]] = 0
                arr[iJumpPoint[1][0]][iJumpPoint[1][1]] = 0
                print("="*30)   
                global_arr.append([iJumpPoint[0], iJumpPoint[1], iBlankPoint])
                print(iJumpPoint[0], iJumpPoint[1], iBlankPoint)
                print("="*30)
                for item in arr:
                    print(item)
                
                findBlank(arr)
                # print(1)
                # return
                arr[iJumpPoint[0][0]][iJumpPoint[0][1]] = 1
                arr[iJumpPoint[1][0]][iJumpPoint[1][1]] = 1

            arr[iBlankPoint[0]][iBlankPoint[1]] = 0

def findBlankEx(arr):
    curJumpPoints = findCanJumpChessEx(arr)
    if arr[0].count(0)+arr[1].count(0)+arr[2].count(0)+arr[3].count(0)+arr[4].count(0) == 14:
        print("Over+++++++++++++++++++++++++++++==========================")
        return True
    
    if len(curJumpPoints) == 0: #没有可以跳的棋子
        return False

    curJumpPoints = curJumpPoints.split("|")
    curThreePoint = curJumpPoints[0].split("-")
    firstPoint = curThreePoint[0]
    secondPoint = curThreePoint[1]
    thirdPoint = curThreePoint[2]

    arr[int(firstPoint[0])][int(firstPoint[1])] = 1
    arr[int(secondPoint[0])][int(secondPoint[1])] = 0
    arr[int(thirdPoint[0])][int(thirdPoint[1])] = 0

    if not findBlankEx(arr): #查找失败
        # print("new finding~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        arr[int(firstPoint[0])][int(firstPoint[1])] = 0
        arr[int(secondPoint[0])][int(secondPoint[1])] = 1
        arr[int(thirdPoint[0])][int(thirdPoint[1])] = 1
        

def findCanJumpChess(arr):
    dictJumpPoints = {}
    for row in range(5):
        for col in range(5):
            if arr[row][col] == 0:
                lstJmpPoints = []
                # left
                if col-2 >= 0:
                    if arr[row][col-1] == 1 and arr[row][col-2] == 1: #中间有棋，左边有棋
                        lstJmpPoints.append([(row, col-2), (row, col-1)]) #要跳的在左
                # right
                if col+2 < 5-row:
                    if arr[row][col+1] == 1 and arr[row][col+2] == 1: #中间有棋，右边有棋
                        lstJmpPoints.append([(row, col+2), (row, col+1)])

                # up
                if row-2 >= 0:
                    if arr[row-1][col] == 1 and arr[row-2][col] == 1: #上边有两棋，可跳
                        lstJmpPoints.append([(row-2, col), (row-1, col)])
                
                # down
                if row+2 <5- col:
                    if arr[row+1][col] == 1 and arr[row+2][col] == 1: #下边有两棋，可跳
                        lstJmpPoints.append([(row+2, col), (row+1, col)])

                # left-down
                if row+2 < 5 and col-2 >=0 :
                    if arr[row+1][col-1] == 1 and arr[row+2][col-2] == 1: #左下有两棋
                        lstJmpPoints.append([(row+2, col-2), (row+1, col-1)])

                # right-top
                if row-2 >= 0 and col+2 < 5 :
                    if arr[row-1][col+1] == 1 and arr[row-2][col+2] == 1: #右上有两棋，可跳
                        lstJmpPoints.append([(row-2, col+2), (row-1, col+1)])
            
                if lstJmpPoints != []:
                    dictJumpPoints[(row, col)] = lstJmpPoints

    return dictJumpPoints

def findCanJumpChessEx(arr):
    strJumpPoints = ""
    for row in range(5):
        for col in range(5):
            if arr[row][col] == 0:
                strTmpJmpPoints = ""
                # left
                if col-2 >= 0:
                    if arr[row][col-1] == 1 and arr[row][col-2] == 1: #中间有棋，左边有棋
                        strTmpJmpPoints += "{}{}-{}{}-{}{}".format(row, col, row, col-1, row, col-2)
                # right
                if col+2 < 5-row:
                    if arr[row][col+1] == 1 and arr[row][col+2] == 1: #中间有棋，右边有棋
                        strTmpJmpPoints += "{}{}-{}{}-{}{}".format(row, col, row, col+1, row, col+2)
                # up
                if row-2 >= 0:
                    if arr[row-1][col] == 1 and arr[row-2][col] == 1: #上边有两棋，可跳
                        strTmpJmpPoints += "{}{}-{}{}-{}{}".format(row, col, row-1, col, row-2, col)
                
                
                # down
                if row+2 <5- col:
                    if arr[row+1][col] == 1 and arr[row+2][col] == 1: #下边有两棋，可跳
                        strTmpJmpPoints += "{}{}-{}{}-{}{}".format(row, col, row+1, col, row+2, col)
                

                # left-down
                if row+2 < 5 and col-2 >=0 :
                    if arr[row+1][col-1] == 1 and arr[row+2][col-2] == 1: #左下有两棋
                        strTmpJmpPoints += "{}{}-{}{}-{}{}".format(row, col, row+1, col-1, row+2, col-2)
                

                # right-top
                if row-2 >= 0 and col+2 < 5 :
                    if arr[row-1][col+1] == 1 and arr[row-2][col+2] == 1: #右上有两棋，可跳
                        strTmpJmpPoints += "{}{}-{}{}-{}{}".format(row, col, row-1, col+1, row-2, col+2)
                
            
                if strTmpJmpPoints != "":
                    strJumpPoints += strTmpJmpPoints + "|"

    return strJumpPoints
# def printTriChess(arr):
#     for i

if __name__ == "__main__":
    arr = [1]*5
    for i in range(5):
        arr[i] = [1]*5
    
    for i in range(5):
        for j in range(5-i, 5):
            arr[i][j] = -1

    arr[2][2] = 0 

    findBlankEx(arr)
    # findBlank(arr)

    # arr[3][1] = 0
    # arr[2][1] = 0
    # for item in arr:
    #     print(item)

    # # print(findBlank(arr))
    # itemDict = findCanJumpChess(arr)
    # for key in itemDict:
    #     print(key, itemDict[key])
    # # print(findCanJumpChess(arr))