# * işaretiyle isim yazma
# Şekillerin anlaşılabilir olması için boyutu en az 5 girin
boyut=int(input("Boyut giriniz-> "))
#s harfi
for i in range(boyut):
    for j in range(boyut):
        if (i==0 or i==boyut//2 or i==boyut-1 ):
            print("*",end=" ")
        elif (i<boyut/2) and j==0:
            print("*", end=" ")
        elif i>boyut/2 and j==boyut-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\n")
# U harfi
for i in range(1, boyut+1):
    for j in range(1,boyut+1):
        if i==boyut or j==1 or j==boyut :
            print("*", end=" ")
        else:
            print(" ",end=" ")


    print(" ")
print("\n")
# L harfi
for i in range(0, boyut):
    for j in range(0,boyut-1):
        if  i == boyut or i==boyut-1 :
            print("*", end=" ")
    print("*")

print("\n")
# E harfi
for i in range(0,boyut):
    for j in range(boyut-1):
        if i ==0 or i==boyut//2  or j==boyut or i==boyut-1:
            print("*",end=" ")
    print("*")
print("\n")