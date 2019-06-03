def findBlank(arr):
    # find the blank of triangle
    lstBlankPoint = []
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 0:
                lstBlankPoint.append((i,j))
    return lstBlankPoint

def findCanJumpChess(arr):
    dictJumpPosts = {}
    for row in range(5):
        for col in range(5):
            if arr[row][col] == 1:
                lstJmpPoints = []
                # left
                if col-2 >= 0:
                    lstJmpPoints.append((row, col-2))
                # right
                if col+2 < 5-row:
                    lstJmpPoints.append((row, col+2))

                # up
                if row-2 >= 0:
                    lstJmpPoints.append((row-2, col))
                
                # down
                if row+2 <5- col:
                    lstJmpPoints.append((row+2, col))

                # left-down
                if row+2 < 5 and col-2 >=0 :
                    lstJmpPoints.append((row+2, col-2))

                # right-top
                if row-2 >= 0 and col+2 < 5 :
                    lstJmpPoints.append((row-2, col+2))
            
                dictJumpPosts[(row, col)] = lstJmpPoints

    return dictJumpPosts

if __name__ == "__main__":
    arr = [1]*5
    for i in range(5):
        arr[i] = [1]*5
    
    for i in range(5):
        for j in range(5-i, 5):
            arr[i][j] = -1

    # arr[2][2] = 0    
    for item in arr:
        print(item)

    # print(findBlank(arr))
    itemDict = findCanJumpChess(arr)
    for key in itemDict:
        print(key, itemDict[key])
    # print(findCanJumpChess(arr))