#konsep array
from collections import deque

import numpy as num


import os

from pip._vendor.distlib.compat import raw_input

#buat def untuk persiapan
def judul():
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print('{:>110}'.format('========== Tugas UAS Semester II ==========='))
    print('{:>111}'.format('| 1 | Array Dimensi 1 , 2 , 3             /| '))
    print('{:>111}'.format('| 2 | Linked List                         \| '))
    print('{:>111}'.format('| 3 | Stack & Queque                      /| '))
    print('{:>111}'.format('| 4 | POhon Biner                         \| '))
    print('{:>111}'.format('| 5 | Graph                               /| '))
    print('{:>110}'.format('|___|______________________________________|'))

def salah():
    print("\n")
    print("\n")
    print('{:>100}'.format('>>> .Yang Anda cari tidak Ada.<<<'))

def array2d():
    no = 1
    for gm in gamepc:
        print("                                                             |",no,".", gm)

        no +=1

def array3d():
    print("                                                                             [  [1, 2, 3, ] [4, 5, 6] ] ")
    print("                                                                             [ [7, 8, 9], [10, 11, 12] ] ")




def linklis():
    print('{:>100}'.format('-----------------------------------'))
    print('{:>86}'.format('1.Tambah '))
    print('{:>85}'.format('2.Cari  '))
    print('{:>85}'.format('3.Hapus '))
    print('{:>88}'.format('4 |< BACK | '))
    print('{:>100}'.format('-----------------------------------'))

def array():
    print("\n")
    print("\n")
    print('{:>100}'.format('-----------------------'))
    print('{:>94}'.format(' 1 > Dimensi 1'))
    print('{:>95}'.format(' 2 > Dimensi 2 '))
    print('{:>95}'.format('3 > Dimensi 3 '))
    print('{:>100}'.format('-----------------------'))



def graphi1():
    print("           Graph 1 :")
    print(" A ______________ B")
    print("  |              |")
    print("  |              |")
    print("  |              |")
    print("  |______________|______________")
    print(" C                D             E")


graph1 = {'A': ['B', 'C'],
          'B': ['A', 'D'],
          'C': ['A', 'D'],
          'D': ['E'],
          'E': ['D']}


def graphi2():
    print("Graph 2 :")
    print("\n")
    print(" A  _____________ D _______________ G")
    print("   |             / \               |")
    print("   |            /   \              |")
    print("   |           /     \             |")
    print("   |__________/       \____________| ")
    print(" B            C        E            F")


graph2 = {'A': ['B', 'D'],
          'B': ['A', 'C'],
          'C': ['B', 'D'],
          'D': ['A', 'C', 'E', 'G'],
          'E': ['D', 'F'],
          'F': ['E', 'G'],
          'G': ['F', 'D']
          }


def graphi3():
    print("A")
    print("          B ")
    print("         /\  ")
    print("        /  \   ")
    print("       /    \   ")
    print("      /      \  ")
    print("     /        \   ")
    print("    /__________\____________ D")
    print("   A          C \          /")
    print("                 \        /")
    print("                  \      /")
    print("                   \    /")
    print("                    \  /")
    print("                     \/")
    print("                     E   ")


graph3 = {'A': ['B', 'C'],
          'B': ['A', 'C'],
          'C': ['A', 'D', 'E'],
          'D': ['C', 'E'],
          'E': ['C', 'D']

          }

#run program
i = 'y'
while (i == 'y'):
    judul()
    pilih = int(input('{:>95}'.format('Masukan Pilihan Kamu :')))
    os.system('cls')
    if (pilih == 1):                                    #array
        array()
        pilih = int(input('{:>95}'.format('                                     Ketikan Pilihan Kamu :')))
        os.system('cls')
        if pilih == 1:
                print("\n")
                print("\n")
                print('{:>96}'.format('Latihan Array 1D'))
                print("\n")

                ikan = []

                i = 'y'

                stop = False
                u = 0
                while (not stop):
                    print("\n")
                    print("\n")
                    nikan = input('{:>95}'.format('Sebutkan nama nama Hewan  {} :'.format(u + 1)))
                    ikan.append(nikan)
                    u += 1


                    ulang = input('{:>95}'.format('Tambah Nama Hewan ? [Y/T] :'))
                    os.system('cls')





                    if (ulang == 't'):
                        stop = True
                        print("\n")
                        print("\n")

                        print("                                                     Nama Nama Hewan Yang Kamu Tau")
                        print("                                                     =====================================================")
                        print("                                                     kamu menjawab {} Hewan".format(len(ikan)))
                        for ikn in ikan:
                            print("                                                     - {}".format(ikn))

        elif pilih == 2:
            print("\n")
            print("\n")
            print('{:>100}'.format('Latihan Array 2D'))
            print("\n")

            gamepc = [
                ["harvest moon", "pepsiman", "metal gear", "silent hill"],
                ["bmxxx", "bully scholarship", "resident evil", "most wanted"],
                ["pou", "call of duty", "clas of clans", "head soccer"]

            ]
            array2d()
            cari = raw_input('{:>100}'.format("Masukan Baris Ke :"))
            print('{:>105}'.format('__________________________________________'))
            if (cari == '1'):
                print('{:>100}'.format('Data Dari Baris 1 :'))
                print(                                                              gamepc[0])
                kol = raw_input('{:>100}'.format("Pilih Kolom Ke :"))
                if (kol == '1'):
                    print("                                                             Data yang Kamu Cari :")
                    print(                                                              gamepc[0][0])
                elif (kol == '2'):
                    print("                                                             Data yang Kamu Cari :")
                    print(                                                              gamepc[0][1])
                elif (kol == '3'):
                    print("                                                             Data yang Kamu Cari :")
                    print(                                                              gamepc[0][2])
                elif (kol == '4'):
                    print("                                                             Data yang Kamu Cari :")
                    print(                                                              gamepc[0][3])
            elif (cari == '2'):
                print('{:>100}'.format('Data Dari Baris Ke 2 :'))
                print(                                                              gamepc[1])
                kol = raw_input('{:>100}'.format("Pilih Kolom Ke :"))
                if (kol == '1'):
                    print("                                                             Data yang Kamu Cari :")
                    print(                                                              gamepc[1][0])
                elif (kol == '2'):
                    print("                                                             Data yang Kamu Cari :")
                    print(                                                              gamepc[1][1])
                elif (kol == '3'):
                    print("                                                             Data yang Kamu Cari :")
                    print(                                                              gamepc[1][2])
                elif (kol == '4'):
                    print("                                                             Data yang Kamu Cari :")
                    print(                                                              gamepc[1][3])
            elif (cari == '3'):
                print('{:>100}'.format('Data Dari Baris Ke 3 :'))
                print(                                                              gamepc[2])
                kol = raw_input('{:>100}'.format("Pilih Kolom Ke :"))
                if (kol == '1'):
                    print("                                                             Data yang Kamu Cari :")
                    print(                                                              gamepc[2][0])
                elif (kol == '2'):
                    print("                                                             Data yang Kamu Cari :")
                    print(                                                              gamepc[2][1])
                elif (kol == '3'):
                    print("                                                             Data yang Kamu Cari :")
                    print(                                                              gamepc[2][2])
                elif (kol == '4'):
                    print("                                                             Data yang Kamu Cari :")
                    print(                                                              gamepc[2][3])


        elif pilih == 3:
            print("\n")
            print("\n")
            print('{:>100}'.format('Latihan Array 3D'))
            print("\n")
            angka = num.array([
                [[1, 2, 3, ], [4, 5, 6]],

                [[7, 8, 9], [10, 11, 12]]
            ])
            array3d()
            cari = raw_input('{:>100}'.format("Masukan Baris 1 Ke : "))
            print('{:>105}'.format('__________________________________________'))
            if (cari == '1'):
                print('{:>100}'.format('Data Dari Baris Ke 1 :'))
                print(angka[0])
                bar = raw_input('{:>100}'.format("Masukan Baris 2 Ke : "))
                print('{:>105}'.format('__________________________________________'))
                if (bar == '1'):
                    print('{:>100}'.format('Data Dari Baris 1 Ke 1 :'))
                    print(angka[0][0])
                    kol = raw_input('{:>100}'.format("Pilih Kolom Ke :"))
                    if (kol == '1'):
                        print("                                                             Data yang Kamu Cari :")
                        print(angka[0][0][0])
                    if (kol == '2'):
                        print("                                                             Data yang Kamu Cari :")
                        print(angka[0][0][1])
                    if (kol == '3'):
                        print("                                                             Data yang Kamu Cari :")
                        print(angka[0][0][2])
                if (bar == '2'):
                    print('{:>100}'.format('Data Dari Baris 1 Ke 2 :'))
                    print(angka[0][1])
                    kol = raw_input('{:>100}'.format("Pilih Kolom Ke :"))
                    if (kol == '1'):
                        print("                                                             Data yang Kamu Cari :")
                        print(angka[0][1][0])
                    if (kol == '2'):
                        print("                                                             Data yang Kamu Cari :")
                        print(angka[0][1][1])
                    if (kol == '3'):
                        print("                                                             Data yang Kamu Cari :")
                        print(angka[0][1][2])
            if (cari == '2'):
                print('{:>100}'.format('Data Dari Baris Ke 2 :'))
                print(angka[1])
                bar = raw_input('{:>100}'.format("Masukan Baris 2 Ke : "))
                print('{:>105}'.format('__________________________________________'))
                if (bar == '1'):
                    print('{:>100}'.format('Data Dari Baris 2 Ke 1 :'))
                    print(angka[1][0])
                    kol = raw_input('{:>100}'.format("Pilih Kolom Ke :"))
                    if (kol == '1'):
                        print("                                                             Data yang Kamu Cari :")
                        print(angka[1][0][0])
                    if (kol == '2'):
                        print("                                                             Data yang Kamu Cari :")
                        print(angka[1][0][1])
                    if (kol == '1'):
                        print("                                                             Data yang Kamu Cari :")
                        print(angka[1][0][2])
                if (bar == '2'):
                    print('{:>100}'.format('Data Dari Baris 2 Ke 2 :'))
                    print(angka[1][1])
                    kol = raw_input('{:>100}'.format("Pilih Kolom Ke :"))
                    if (kol == '1'):
                        print("                                                             Data yang Kamu Cari :")
                        print(angka[1][1][0])
                    if (kol == '2'):
                        print("                                                             Data yang Kamu Cari :")
                        print(angka[1][1][1])
                    if (kol == '3'):
                        print("                                                             Data yang Kamu Cari :")
                        print(angka[1][1][2])

        else:
            salah()
            os.system('cls')

    elif (pilih == 2):                             #linked list
        class Node:                             #buat class node
            def __init__(self,data=None):
                self.data=data
                self.next=None
        class Ll:                               #buat class linked list
            def __init__(self):
                self.awal = Node()

            def tambah(self,data):              #def untuk menambah data
                new_node = Node(data)
                list = self.awal
                while list.next!= None:         #apabila list selanjutnya tidak ditemukan, maka buat node baru
                    list = list.next
                list.next = new_node

            def panjang(self):                   #def untuk menghitung panjang list
                list = self.awal
                total = 0
                while list.next!= None:
                    total += 1
                    list = list.next
                return total                    #kembalikan nilai

            def tampil(self):
                elems = []
                list_node = self.awal
                while list_node.next!=None:
                    list_node = list_node.next
                    elems.append(list_node.data)
                print(elems)

            def get(self,index):                            #mencari sebuah data pada list
                if index>=self.panjang():
                    print ("ERROR : tidak ada pilihan itu!")
                    return None
                no_list=0
                list_node = self.awal
                while True:
                    list_node = list_node.next
                    if no_list==index:
                        return list_node.data
                    no_list += 1

            def hapus(self,index):                          #menghapus data list
                if index>=self.panjang():
                    print("Error : tidak dapat menghapus")
                    return None
                no_list = 0
                list_node = self.awal
                while True:
                    pilih_node =list_node
                    list_node = list_node.next
                    if no_list==index:
                        pilih_node.next = list_node.next
                        return
                    no_list +=1
        u=0
        my_list = Ll()
        my_list.tampil()
        stop = False
        while (not stop):
            linklis()
            pilih = raw_input("                                         Kamu pilih Yang mana : ")
            if (pilih == "1"):                                                  #untuk menambah data
                ms = str(input("                                            Masukan angka {}: ".format(u+1)))
                u += 1
                os.system('cls')

                my_list.tambah(ms)
                my_list.tampil()
            elif (pilih == "2"):                                        #untuk mencari data

                ms = int(input("Cari Data Ke : "))
                os.system('cls')
                print("element di index {} adalah : %s ".format(ms) % my_list.get(ms-1),)

                my_list.tampil()
            elif (pilih == "3"):
                ms = int(input("Data Ke berapa yang Akan dihapus : "))
                os.system('cls')
                my_list.hapus(ms-1)
                print("element di index {} Telah dihapus ".format(ms)  )

                my_list.tampil()
            elif (pilih == "4"):
                stop = True
                os.system('cls')

            else :
                salah()

    elif (pilih == 3):   #stack&queue
        stop = False
        while (not stop):

            pilih = int(input('{:>110}'.format("[1]STACK | [2]QUEUE | [3]BACK ,Kamu Memilih :")))
            os.system('cls')
            if (pilih == 1):

                tumpukan = [10, 20, 30, 35]
                print(tumpukan)
                app = int(input("Masukan angka ke dalan STACK :"))
                tumpukan.append(app)
                print("\n")
                print("Data terbaru Adalah : ",tumpukan)

                #kita pop
                keluar = tumpukan.pop()
                print("Data yang keluar adalah : ",keluar)
                print("Data yang kita input saat di POP langsung keluar lagi, karena...")
                print(" Prinsip Dari Stack adalah LIFO last in first Out, sehingga")
                print("Data stack Terbaru setelah di pop : ", tumpukan)
                print("-----------------------------------------------------")
            elif (pilih == 2):
                antrian = deque([1, 2, 3, 5, 9])
                print(antrian)
                app = int(input("Masukan angka ke dalan Queque :"))
                antrian.append(app)
                print("\n")
                print("Data terbaru :", antrian)

                keluar = antrian.popleft()
                print("Data keluar",keluar)
                print("Data yang kita input menjadi antrian akhir,saat di POP data yang ada di awal langsung keluar, karena...")
                print(" Prinsip Dari Queue adalah FIFO First in first Out, sehingga")
                print("Data Antrian setelah di pop : ",antrian)

                print("\n")

                keluar = antrian.popleft()
                print("Data keluar", keluar)
                print("Ketika di Pop lagi, Akan seperti ini...")
                print("Data Antrian setelah di pop : ", antrian)
            elif (pilih == 3):
                stop = True
                os.system('cls')

            else:
                salah()

    elif (pilih == 4):                                #pohon
        class Node(object):  # buat persiapan class nodenya
            def __init__(self, value):
                self.value = value
                self.left = None
                self.right = None


        class pohon(object):  # buat class pohonnya
            def __init__(self, root):
                self.root = Node(root)

            def cetak_pohon(self, jalur):  # inisiasi node
                if jalur == "preorder":
                    return self.kalo_preorder(tree.root, "")
                elif jalur == "inorder":
                    return self.kalo_inorder(tree.root, "")
                elif jalur == "postorder":
                    return self.kalo_postorder(tree.root, "")
                else:
                    print("Tidak Ada Pohon")
                    return False

            def kalo_preorder(self, start, jalur):  # Dephfirstorder
                if start:
                    jalur += (str(start.value) + "-")  # kunjungi ujung akar
                    jalur = self.kalo_preorder(start.left, jalur)  # baru ke cabang kiri
                    jalur = self.kalo_preorder(start.right, jalur)  # lalu ke cabang kanan
                return jalur

            def kalo_inorder(self, start, jalur):  # simetrik order
                if start:
                    jalur = self.kalo_inorder(start.left, jalur)  # kunjungi cabang kiri dulu
                    jalur += (str(start.value) + "-")  # lalu ke ujung akar
                    jalur = self.kalo_inorder(start.right, jalur)  # setelah itu ke cabang kanan
                return jalur

            def kalo_postorder(self, start, jalur):  #
                if start:
                    jalur = self.kalo_postorder(start.left, jalur)  # ke cabang kiri dulu
                    jalur = self.kalo_postorder(start.right, jalur)  # lalu ke cabang kanan
                    jalur += (str(start.value) + "-")  # setelah itu ke ujung akar
                return jalur


        print('{:>28}'.format("Pohon -Pohonan"))

        print("                   50 ")
        print("               /        \  ")
        print("             30          55  ")
        print("            /  \        /  \  ")
        print("           15   40     52   70   ")
        print("          /              \     ")
        print("         10              54    ")
        #buat cabang pohon
        tree = pohon(50)
        tree.root.left = Node(30)
        tree.root.right = Node(55)
        tree.root.left.left = Node(15)
        tree.root.left.right = Node(40)
        tree.root.right.left = Node(52)
        tree.root.right.right = Node(70)
        tree.root.left.left.left = Node(10)
        tree.root.right.left.right = Node(54)
        #buat cetak pohon
        print("Hasil Inordernya :")
        print(tree.cetak_pohon("inorder"))
        print("\n")
        print("Hasil Preordernya :")
        print(tree.cetak_pohon("preorder"))
        print("\n")
        print("Hasil Postordernya :")
        print(tree.cetak_pohon("postorder"))
        print("\n")

    elif (pilih == 5):          #graph
        print("Graph Phyton")
        print("\n")
        print("Pengertian :")
        print("> Graph = Graph adalah salah satu metode pemetaan data dengan memberikan informasi pada kumpulan")
        print("          titik (node) yang dihubungkan dengan segmen garis. ")
        print("verteks = Titik ini atau Node ")
        print("edge = segmen garis disebut dengan ruas ")


        class graph:
            def __init__(self, gdict=None):
                if gdict is None:
                    gdict = []
                self.gdict = gdict

            # buat def untuk ambil vertex dari graph
            def getVertex(self):
                return list(self.gdict.keys())

            # buat def untuk ambil edge dari graph
            def getEdge(self):
                edges = []
                for v in self.gdict:
                    for e in self.gdict[v]:
                        if {e, v} not in edges:
                            edges.append({e, v})
                return edges                        #kembalikan nilai


        # buat dictionary dengan elemen graph

        g = graph(graph1)
        x = graph(graph2)
        z = graph(graph3)
        # tampilkan graph
        print("\n")
        graphi1()
        print("================ Vertexnya ==================")
        print(g.getVertex())
        print("================== Edge ===================")
        print(g.getEdge())

        # tampilkan graph 2
        print("\n")
        graphi2()

        print("================ Vertexnya ==================")
        print(x.getVertex())
        print("================== Edge ===================")
        print(x.getEdge())

        # tampilkan graph 3
        print("\n")
        graphi3()

        print("================ Vertexnya ==================")
        print(z.getVertex())
        print("================== Edge ===================")
        print(z.getEdge())

    else:
        salah()

