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
                
                findBlank(arr.copy())
                # print(1)
                # return
                arr[iJumpPoint[0][0]][iJumpPoint[0][1]] = 1
                arr[iJumpPoint[1][0]][iJumpPoint[1][1]] = 1

            arr[iBlankPoint[0]][iBlankPoint[1]] = 0

    

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
            
                dictJumpPoints[(row, col)] = lstJmpPoints

    return dictJumpPoints

if __name__ == "__main__":
    arr = [1]*5
    for i in range(5):
        arr[i] = [1]*5
    
    for i in range(5):
        for j in range(5-i, 5):
            arr[i][j] = -1

    arr[2][2] = 0 

    findBlank(arr)

    # arr[3][1] = 0
    # arr[2][1] = 0
    # for item in arr:
    #     print(item)

    # # print(findBlank(arr))
    # itemDict = findCanJumpChess(arr)
    # for key in itemDict:
    #     print(key, itemDict[key])
    # # print(findCanJumpChess(arr))