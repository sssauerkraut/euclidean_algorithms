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
i = 1

print(f"Шаг |         r_old         |       x_old       |       y_old       | quotient ")
print("-" * 75)
print(f"{i:3} | {r_old:21} | {x_old:17} | {y_old:17} | --------- ")
   
while (r_new != 0):
    q = r_old // r_new
    print(f"{i:3} | {r_old:21} | {x_old:17} | {y_old:17} | {q:6} ")
    r_old, r_new = r_new, r_old - q * r_new
    x_old, x_new = x_new, x_old - q * x_new
    y_old, y_new = y_new, y_old - q * y_new
    i += 1
    print(r_new)
  
print(f"Результат: НОД({a}, {b}) = {r_old}")
print(f"Коэффициенты Безу: x = {x_old}, y = {y_old}")
print(f"Проверка: {a}*({x_old}) + {b}*({y_old}) = {a*x_old + b*y_old}")