from matplotlib_venn import venn3, venn2, venn2_circles, venn3_circles
import matplotlib.pyplot as plt

def vennplot1():
    plt.figure(figsize=(6, 6))
    venn2(subsets=(3,3, 1), set_labels=('A', 'B'))
    venn2_circles(subsets=(3, 3, 1))


    # venn2([set(['A', 'B', 'C', 'D']), set(['D', 'E', 'F'])])
    plt.show()

if __name__ == "__main__":
    vennplot1()


# def int2bin(n):
#     s = bin(n)[2:]
#     return (3-len(s))*'0'+s
#                             # 1 ⇒ '001'
#                             # 2 ⇒ '010'
#                             # 3 ⇒ '011'
#                             # ...
#                             # 7 ⇒ '111'

# v = venn3(subsets=(1, 1, 1, 1, 1, 1, 1))
# for i in range(1, 8):
#     v.get_label_by_id(int2bin(i)).set_text(int2bin(i))
# plt.show()
