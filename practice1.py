from random import randint

print("Задание 1")

students = []
fives = 0

for i in range(22):
    students.append(randint(2, 5))
    if students[i] == 5:
        fives += 1

print("Количество пятёрок: ", fives)


print("Задание 2")

def max_row_multiple_of_a(array, a):
    max_row_index = -1

    for i in range(len(array)):
        if all(element % a == 0 for element in array[i]):
            max_row_index = i

    return max_row_index


array = [[2, 4],[3, 9],[1, 2],[10, 20]]
a = 3
print(max_row_multiple_of_a(array, a))


print("Задание 3")
list=[1,2,3,4,4,5,6,7,8,9]
for i in range(len(list)-1):
    if list[i]==list[i+1]:
        print("Первое число: ", list[i],", второе число: ", list[i+1])

print("Задание 4")
print("Введите числа через пробел: ")
sets = input().split(" ")
for i in range(len(sets)):
    isEnded = False
    counter = 0
    if i == 0:
        print("No")
    else:
        while counter < i:
            if sets[i] == sets[counter]:
                print("Yes")
                counter += 1
                break
            else:
                print("No")
                counter += 1
                break

print("Задание 5")
text = input()
def most_frequent_word(text):
    words = text.lower().split()

    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    max_count = max(word_count.values())

    most_frequent = [word for word, count in word_count.items() if count == max_count]

    return min(most_frequent)

print(most_frequent_word(text))