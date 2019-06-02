# g_lastCol, g_lastRow, g_curCol, g_curRow = 0,0,0,0
import sys
sys.setrecursionlimit(1000000) #例如这里设置为一百万

def judge_IsOneLine(point_a,point_b):
    y1, x1 = point_a
    y2, x2 = point_b
    # print(x1, y1, x2, y2, '--')
    # print(x1==x2 , y1==y2 , x1-x2==y1-y2 , x1-x2==y2-y2)
    if x1==x2 or y1==y2 or x1-x2==y1-y2 or x1-x2==y2-y1:
        return 1
    return 0

def GenAllPoints_and_Judge(arr):
    queen_points_lst = []
    for i in range(8):
        for j in range(8):
            if arr[i][j] == 1:
                queen_points_lst.append((i,j))
    # print(queen_points_lst)

    # generate all points-double
    for i in range(len(queen_points_lst)):
        for j in range(i+1, len(queen_points_lst)):
            if judge_IsOneLine(queen_points_lst[i], queen_points_lst[j]): #on one line
                # print(queen_points_lst[i], queen_points_lst[j])
                return [False, queen_points_lst]
    return [True, queen_points_lst]

def eightQueen(arr):
    isRight, pointsArr = GenAllPoints_and_Judge(arr)
    print(pointsArr)
    # if pointsArr[0][1] == 1:
    #     return
    if isRight and len(pointsArr)==8:
        print(pointsArr, 'over')
        return
    else:
        curPoint_col, curPoint_row = pointsArr[-1]
        if len(pointsArr) > 1:
            lastPoint_col, lastPoint_row = pointsArr[-2]
        if len(pointsArr) > 2:
            pre_lastPoint_col, pre_lastPoint_row = pointsArr[-3]
            
        # print(pointsArr)
        if isRight:
            arr[curPoint_col+1][0] = 1
        else:
            arr[curPoint_col][curPoint_row] = 0
            if curPoint_row == 7:
                arr[lastPoint_col][lastPoint_row] = 0
                curPoint_col = lastPoint_col # col back
                if lastPoint_row == 7: # col back again
                    arr[pre_lastPoint_col][pre_lastPoint_row] = 0
                    curPoint_col = pre_lastPoint_col
                    curPoint_row = pre_lastPoint_row+1
                else:
                    curPoint_row = lastPoint_row+1
                print("col back", end="")
            else:
                curPoint_row += 1 # row add
                print("row add", end="")
            print(curPoint_col, curPoint_row)
            arr[curPoint_col][curPoint_row] = 1
        eightQueen(arr)


if __name__ == "__main__":
    # mm = [(0,0), (1,6), (2,4), (3,7), (4,1), (5,3), (6,5),(7,2)]
    arr = [0]*8
    for i in range(8):
        arr[i] = [0]*8
    arr[0][1] = 1
    # for item in mm:
    #     i,j = item
    #     arr[j][i] = 1
    # # print(arr)
    # for i in arr:
    #     print(i)

    # print(GenAllPoints_and_Judge(arr))
    # GenAllPoints_and_Judge(arr)
    eightQueen(arr)
    for i in arr:
        print(i)