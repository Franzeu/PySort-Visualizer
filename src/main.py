import matplotlib.pyplot as plt
import random
import copy

#Bubble Sort. Because of the nested for loop. The worst case time complexity is O(n^2)
def bubble(list):
    for i in range(1, len(list)):
        for j in range(0, len(list) - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
                print(list)
    return list

userInput = int(input("How big should the list be?: "))

userList = list(range(1, userInput + 1))
random.shuffle(userList)
convertedList = list(map(str, userList))

plt.bar(convertedList,userList)
plt.title('Bubble Sort')
plt.xlabel('Number')
plt.ylabel('Something')
plt.show()

# print(bubble(userList))