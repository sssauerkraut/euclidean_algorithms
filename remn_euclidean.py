# Альтернативная версия с более простой логикой
def extended_euclidean_truncated_simple(a, b):
    if b <= 0 or a <= 0:
        print("Invalid input (numbers must be positive)")
        return
    if b > a:
        a, b = b, a
    
    print("Расширенный алгоритм Евклида с усечёнными остатками")
    print(f"Исходные числа: a = {a}, b = {b}")
    print()
    
    r_prev, r_cur = a, b
    num1, num2 = a, b
    x_prev, y_prev = 1, 0
    x_cur, y_cur = 0, 1
    i = 0
    
    print(f"{'Шаг':<4} | {'r_old':<80} | {'q':<10} | {'x':<40} | {'y':<40} | {'Остаток':<10}")
    print("-" * 105)
    print(f"{i:<3} | {r_prev:<80} | {'-':<10} | {x_prev:<40} | {y_prev:<40} | {'-':<10}")
    
    while r_cur != 0:
        i += 1

        # Вычисляем усечённое частное (округление до ближайшего)
        q = (r_prev + r_cur // 2) // r_cur
        r_next = r_prev - q * r_cur
        x_next = x_prev - q * x_cur
        y_next = y_prev - q * y_cur

        print(f"{i:<3} | {r_cur:<80} | {q:<10} | {x_cur:<40} | {y_cur:<40} | {num1}*{x_cur} + {num2}*{y_cur} = {num1*x_cur + num2*y_cur}")

        # Переходим к следующей итерации
        r_prev, r_cur = r_cur, r_next
        x_prev, x_cur = x_cur, x_next
        y_prev, y_cur = y_cur, y_next
    

    if r_prev < 0:
        r_prev = -r_prev
        x_prev = -x_prev
        y_prev = -y_prev
        

    # Финальный результат
    nod = r_prev
    x_final = x_prev
    y_final = y_prev

    print()
    print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
    print(f"НОД({num1}, {num2}) = {nod}")
    print(f"Коэффициенты Безу: x = {x_final}, y = {y_final}")
    print(f"Проверка: {num1}*{x_final} + {num2}*{y_final} = {num1*x_final + num2*y_final}")
    print(f"Корректность: {num1*x_final + num2*y_final == nod}")

# Основная программа
if __name__ == "__main__":
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    
    print("=" * 80)
    extended_euclidean_truncated_simple(a, b)