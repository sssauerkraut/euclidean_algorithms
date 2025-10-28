a = int(input())
b = int(input())

if b <= 0 or a <= 0:
    print("Invalid input (b must be positive)")
    exit()
if b > a:
    a, b = b, a

g = 1
i = 1
print("ШАГ 1: Вынесение общей степени двойки")
print(f"{'Шаг':<4} | {'a':<20} | {'b':<20} | {'g':<10}")
print("-" * 65)
print(f"{i:<4} | {a:<20} | {b:<20} | {g:<10}")
while (a % 2 == 0 and b % 2 == 0):
    a = a // 2
    b = b // 2
    g *= 2
    i += 1
    print(f"{i:<4} | {a:<20} | {b:<20} | {g:<10}")

print()
print("ШАГ 2: Основной цикл с вынесением двоек")
print(f"{'Шаг':<4} | {'u':<20} | {'v':<20} | {'Действие':<15}")
print("-" * 65)

u, v = a, b
while ( u != 0 ):
    while ( u % 2 == 0): u = u // 2
    while ( v % 2 == 0): v = v // 2
    if ( u >= v ): u = u - v
    else : v = v - u


  
print(f"Результат: НОД({a}, {b}) = {g * v}")