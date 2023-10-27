# #die erste Ubung
# def sortList(list):
#     result = []
#     for nr in list:
#         check = False #pp ca nr nu se repeta
#         for k in result:
#             if k == nr:
#                 check = True
#         if check == False: # not check daaca nu se repeta nr adica daca am avut dreptate la PP
#             result.append(nr)
#
#     return result
#
# def readList(): #diese funktion liest die eingegebenen Zahlen und fuegt sie in eine Liste ein
#     list = input('introdu lista ms: ')
#     list = list.split()
#     result = []
#     for nr in list:
#         result.append(int(nr))
#     return result
#
# def main():
#     list = []
#     list = readList()
#     print(list)
#     list = sortList(list)
#     print(list)
#
# if __name__ == '__main__':
#     main()

#die zweite Ubung

# def symmetrischeZahlen(l):
#     count = 0
#     f=[]
#     for i in l:
#         i_string=str(i) # am pus in i string un nr i din acea lista ca sa fie ma usor de manevrat
#         if int(i_string[::-1]) in l: #daca inversul lui i se afla pe undeva in lista
#             count +=1
#             f.append(i_string)
#     print(f)
#     return count
#
# def main():
#     list = [55, 67, 76, 89, 99]
#
#     count=symmetrischeZahlen(list)
#     print(count)
#
# main()

#die dritte Ubung


def numConcat(num1, num2): #returneaza numerele concatenate
    if num2>num1: #vrem ca num1 sa fie cel mai mare
        num1,num2=num2,num1 #swap
    num1 = str(num1)
    num2 = str(num2) #le convertim into strings
    num1 += num2 #le concartenam ca sa avem cel mai mare numar
    return int(num1)

def largest_number(nums):
    pass


def main():
    numbers = [76, 85, 43, 543, 32]
    result = largest_number(numbers)
    print("The largest number is:", result)

main()

#die v