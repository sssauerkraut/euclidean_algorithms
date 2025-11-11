a = int(input())
b = int(input())

if b <= 0 or a <= 0:
    print("Invalid input (b must be positive)")
    exit()
if b > a:
    a, b = b, a

r_old, r_new = a, b
x_old, x_new = 1, 0
y_old, y_new = 0, 1
i = 0

print(f"Шаг |{'r_i':^22}|{'x_i':^12}|{'y_i':^12}|{'q_i':^10}")
print("-" * 210)

# Выводим начальное состояние (r₀ = a)
print(f"{i:3} | {r_old:20} | {x_old:10} | {y_old:10} | {'-':<9}")

i = 1
while r_new != 0:
    # Вычисляем частное qᵢ = rᵢ₋₁ // rᵢ
    q = r_old // r_new
    
    # Выводим текущий шаг с rᵢ и qᵢ
    print(f"{i:3} | {r_new:20} | {x_new:10} | {y_new:10} | {q:9}")
    
    # Обновляем переменные для следующей итерации
    r_old, r_new = r_new, r_old - q * r_new
    x_old, x_new = x_new, x_old - q * x_new
    y_old, y_new = y_new, y_old - q * y_new
    
    i += 1

print(f"Результат: НОД({a}, {b}) = {r_old}")
print(f"Коэффициенты Безу: x = {x_old}, y = {y_old}")
print(f"Проверка: {a}*({x_old}) + {b}*({y_old}) = {a*x_old + b*y_old}")