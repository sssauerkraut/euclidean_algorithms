a = int(input())
b = int(input())

if b <= 0 or a <= 0:
    print("Invalid input (b must be positive)")
    exit()
if b > a:
    a, b = b, a

# Сохраняем исходные числа для проверки
original_a, original_b = a, b

g = 1
i = 1
print(" ШАГ 1: Вынесение общей степени двойки")
print(f"{'Шаг':<4} | {'a':<20} | {'b':<20} | {'g':<10}")
print("-" * 65)
print(f"{i:<4} | {a:<20} | {b:<20} | {g:<10}")
while not(a & 1 or b & 1):
    a >>= 1
    b >>= 1
    g <<= 1
    i += 1
    print(f"{i:<4} | {a:<20} | {b:<20} | {g:<10}")

print("\n ШАГ 2: Основной цикл с вынесением двоек")
print(f"{'Шаг':<4} | {'u':<80} | {'v':<80} | {'x':<70} | {'y':<70} | {'Действие':<15}")
print("-" * 120)

u, v = a, b
A, B, C, D = 1, 0, 0, 1  # Коэффициенты для u и v
i = 1
print(f"{i:<4} | {u:<80} | {v:<80} | {C:<70} | {D:<70} | {'Начало':<15}")
#print(f"      Проверка: {original_a}*{C} + {original_b}*{D} = {original_a*C + original_b*D}")

while u != 0:
    while not(u & 1): 
        u >>= 1
        if not(A & 1 or B & 1):
            A >>= 1
            B >>= 1
        else:
            A = (A + original_b) >> 1
            B = (B - original_a) >> 1
        i += 1
        print(f"{i:<4} | {u:<80} | {v:<80} | {C:<70} | {D:<70} | {'u/2':<15}")
        #print(f"      Проверка: {original_a}*{A} + {original_b}*{B} = {original_a*A + original_b*B} = {u}")

    while not(v & 1):
        v >>= 1
        if not(C & 1 or D & 1):
            C >>= 1
            D >>= 1
        else:
            C = (C + original_b) >> 1
            D = (D - original_a) >> 1
        i += 1
        print(f"{i:<4} | {u:<80} | {v:<80} | {C:<70} | {D:<70} | {'v/2':<15}")
        #print(f"      Проверка: {original_a}*{C} + {original_b}*{D} = {original_a*C + original_b*D} = {v}")
    
    if u == 0:
        break

    if u >= v:
        u = u - v
        A = A - C
        B = B - D
        action = "u = u - v"
    else:
        v = v - u
        C = C - A
        D = D - B
        action = "v = v - u"
    i += 1
    print(f"{i:<4} | {u:<80} | {v:<80} | {C:<70} | {D:<70} | {action:<15}")
    #print(f"      Проверка: {original_a}*{C} + {original_b}*{D} = {original_a*C + original_b*D} = {v}")

print()
print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
gcd_result = g * v
print(f"НОД({original_a}, {original_b}) = {gcd_result}")
print(f"Коэффициенты Безу: x = {C}, y = {D}")
print(f"Проверка: {original_a}*{C} + {original_b}*{D} = {original_a*C + original_b*D}")
print(f"Корректность: {original_a*C + original_b*D == gcd_result}")