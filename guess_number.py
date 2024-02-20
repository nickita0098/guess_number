from random import randint as ri
random_num = ri(1,10)
print('Угадайте число от 1 до 100')
while True:
    user_num = int(input("Введите число"))  
    if user_num < random_num:
        print ("Ваше число меньше того, что загадано")
    if user_num > random_num:
        print ("Ваше число больше того, что загадано")
    if user_num == random_num:
        print ("Отличная интуиция! Вы угадали число :)")
        break
