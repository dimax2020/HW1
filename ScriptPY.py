print("Введите числа через пробел")
a = [int(el) for el in input().split()] #Вводим свои числа через пробел.

def bubble_sort(a):
    k = True #Строчка делает так, чтобы цикл выполнился хотя бы один раз.
    while k:
        k =  False
        for i in range(len(a) - 1):
            if a[i] > a[i+1]: # Этот алгоритм меняет числа в нужном порядке.
                a[i],a[i+1] = a[i+1],a[i]
                k = True
bubble_sort(a) #Команда, которая присваивает новое значение переменной a.
print(a)
