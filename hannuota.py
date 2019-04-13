# def hannuota(arr):
#     print("原：",arr)
#     if len(arr[0]) == 1:
#         print((1, 3), (arr[0][:-1], arr[1], arr[2]+arr[0][-1]))
#     elif len(arr[0]) == 2:
#         newarr = [arr[0][:-1], arr[1]+arr[0][-1], arr[2]]
#         print((1, 2), newarr)
#         hannuota(newarr)
        
#         # print((1, 3), (arr[0][:-1], arr[1], arr[2]+arr[0][-1]))

# def hannuota2(arr, flag = 1):
#     a1 = arr[0]
#     a2 = arr[1]
#     a3 = arr[2]
#     if a1 == "":
#         if a2 == "":
#             print("over!!!")
#             return
#         else:
#             newarr = [a2, a1, a3] #交换第1根柱子和第2根柱子
#             hannuota2(newarr, abs(flag-1))
#     else:
#         if len(a1)%2 == 1: #第一根柱子是奇数，则从第1根柱子移向第3根柱子
#             # if a1[0]<a3[0] or a3=="": #如果第1根可以移动到第3根去
#             if a3 == "" or a1[0] < a3[0]:
#                 newarr = [a1[1:], a2, a1[0]+a3]
#                 if flag == 1:
#                     print((1, 3), newarr)
#                 elif flag == 0:
#                     print((2, 3), [newarr[1], newarr[0], newarr[2]]) #交换第1根柱子和第2根柱子后的正确打印                    
#             else: #否则将第3根向第2根移动
#                 newarr = [a1, a3[0]+a2, a3[1:]]
#                 print((3, 2), newarr)
#         elif len(a1)%2 == 0: #第一根柱子是偶数，则从第1根柱子移向第2根柱子
#             newarr = [a1[1:], a1[0]+a2, a3]
#             if flag == 1:
#                 print((1, 2), newarr)
#             elif flag == 0:
#                 print((2, 1), [newarr[1], newarr[0], newarr[2]])
#         hannuota2(newarr, flag)

    
# def hannuota3(arr, flag = 1):
#     a1 = arr[0]
#     a2 = arr[1]
#     a3 = arr[2]
#     if a1 == "":
#         if a2 == "":
#             print("over!!!")
#             return
#         else:
#             newarr = [a2, a1, a3] #交换第1根柱子和第2根柱子
#             hannuota3(newarr, abs(flag-1))
#     else:
#         if len(a1)%2 == 1: #第一根柱子是奇数，则从第1根柱子移向第3根柱子
#             # if a1[0]<a3[0] or a3=="": #如果第1根可以移动到第3根去
#             if a3 == "" or a1[0] < a3[0]:
#                 newarr = [a1[1:], a2, a1[0]+a3]
#                 printarr(newarr, flag, flag_LR="1-3")
#             else: #否则将第3根向第1根移动
#                 if a3[0]<a1[0]: #第3根可以向第1根移动
#                     newarr = [a3[0]+a1, a2, a3[1:]]
#                     printarr(newarr, flag, flag_LR="3-1")
#                 else: #第3根倒加至第2根
#                     newarr = [a1, a3[0]+a2, a3[1:]]
#                     printarr(newarr, flag, flag_LR="3-2")                   
                    
#         elif len(a1)%2 == 0: #第一根柱子是偶数，则从第1根柱子移向第2根柱子
#             if a2 == "" or a1[0] < a2[0]:
#                 newarr = [a1[1:], a1[0]+a2, a3]
#                 printarr(newarr, flag, flag_LR="1-2")
#             else: #否则将第2根柱子移动到第3根柱子
#                 if a2[0]<a3[0]: #可以移动
#                     newarr = [a1, a2[1:], a2[0]+a3]
#                     printarr(newarr, flag, flag_LR="2-3")
#                 else: #不可以移动，则将第2根柱子移动到第1根柱子上
#                     newarr = [a2[0]+a1, a2[1:], a3]
#                     printarr(newarr, flag, flag_LR="2-1")
                   
#         hannuota3(newarr, flag)

# def printarr(newarr, flag, flag_LR):
#     if flag_LR == "1-2":
#         if flag == 1:
#             print((1, 2), newarr)
#         elif flag == 0:
#             print((2, 1), [newarr[1], newarr[0], newarr[2]])
#     elif flag_LR == "2-1":
#         if flag == 1:
#             print((2, 1), newarr)
#         elif flag == 0:
#             print((1, 2), [newarr[1], newarr[0], newarr[2]])
#     elif flag_LR == "2-3":
#         if flag == 1:
#             print((2, 3), newarr)
#         elif flag == 0:
#             print((1, 3), [newarr[1], newarr[0], newarr[2]])
#     elif flag_LR == "3-1":
#         if flag == 1: #正常顺序
#             print((3, 1), newarr)
#         elif flag == 0:
#             print((3, 2), [newarr[1], newarr[0], newarr[2]])
#     elif flag_LR == "3-2":
#         if flag == 1: #正常顺序
#             print((3, 2), newarr)
#         elif flag == 0:
#             print((3, 1), [newarr[1], newarr[0], newarr[2]])
#     elif flag_LR == "1-3":
#         if flag == 1: #正常顺序
#             print((1, 3), newarr)
#         elif flag == 0:
#             print((2, 3), [newarr[1], newarr[0], newarr[2]])
# # def hannuota4(arr, swap12=0, swap23=0):
# #     a1 = arr[0]
# #     a2 = arr[1]
# #     a3 = arr[2]

# #     if len(a1)==0 and len(a2) == 0:
# #         print("over!")
# #     elif len(a1)==0:
# #         #swap a1 and a2
# #         swap12 = abs(swap12-1)

# #     if len(a1) == 1 and (a3=="" or a1[0] < a3[0]):
# #         newarr = ["", a2, a1[0]+a3]
# #         print((1, 3), newarr)

# #     if len(a1) > 1:


import string
g_sn_arr = []

def gensnarr(arr, flagarr):
    [n1, n2, n3]=arr
    [a,b,c] = flagarr
    if n1==0 and n2==0:
        # print('over')
        return
    else:
        gensnarr([n1-1, n2, n3], [a, c, b])
        # print([a,c])
        g_sn_arr.append([a,c])
        gensnarr([n1-1, n2, n3], [b, a, c])

def hannuota(num=3):
    gensnarr([num,0,0], [1,2,3])
    indx = 0
    somepies = [string.ascii_uppercase[:num], '', '']
    # print(g_sn_arr, somepies)
    print("原来状态：", somepies)
    for item in g_sn_arr:
        [i,j] = item
        i=i-1
        j=j-1
        somepies[j] = somepies[i][0]+somepies[j]
        somepies[i] = somepies[i][1:]
        indx += 1
        print("第%d步"%indx, item, somepies)
        

if __name__ == "__main__":
    hannuota(10)