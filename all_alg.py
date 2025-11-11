import time
import timeit
import math

def measure_algorithm_performance(algorithm, a, b, num_iterations=1000):
    """Измеряет среднее время выполнения алгоритма"""
    total_time = 0
    for _ in range(num_iterations):
        start_time = time.perf_counter()
        algorithm(a, b)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)
    return total_time / num_iterations

def performance_by_number_size():
    """Измеряет производительность на числах разного размера с повышенной точностью"""
    
    # Тестовые случаи разных размеров
    test_cases = [
        ("Малые (10²)", 123, 456),
        ("Средние (10¹⁵)", 123456789012345, 987654321098765),
        ("Большие (10³⁰)", 10**30 + 1, 10**30 - 1),
        ("Очень большие (10⁷⁷)", 
         40725696627773368004912890592846967298666712697731713786592659556762005572364289,
         40027659623007905446788056610391701038149964763267432217910966950673451632367023)
    ]
    
    algorithms = [
        ("Усечённые", extended_euclidean_truncated_simple),
        ("Классический", euclidean),
        ("Бинарный", bin_euclidean)
    ]
    
    print("ТАБЛИЦА 3. ДЕТАЛИЗАЦИЯ ПО ТИПАМ ЧИСЕЛ (УЛУЧШЕННЫЕ ИЗМЕРЕНИЯ)")
    print("=" * 100)
    print(f"{'Размер чисел':<25} | {'Усечённые':<15} | {'Классический':<15} | {'Бинарный':<15} | {'Лучший':<10}")
    print("-" * 100)
    
    results = []
    
    for size_name, a, b in test_cases:
        row = [size_name]
        best_time = float('inf')
        best_algo = ""
        algo_times = []
        
        # Определяем количество итераций в зависимости от размера чисел
        if size_name == "Малые (10²)":
            num_runs = 5      # 5 прогонов
            iterations_per_run = 200  # по 200 итераций каждый
        elif size_name == "Средние (10¹⁵)":
            num_runs = 5
            iterations_per_run = 200
        elif size_name == "Большие (10³⁰)":
            num_runs = 5  
            iterations_per_run = 200
        else:  # Очень большие
            num_runs = 3
            iterations_per_run = 200
        
        for algo_name, algorithm in algorithms:
            run_times = []
            
            # Выполняем несколько прогонов и берем медиану
            for run in range(num_runs):
                # Прогреваем кэш перед каждым прогоном
                algorithm(a, b)
                algorithm(a, b)
                
                # Измеряем среднее время для этого прогона
                avg_time = measure_algorithm_performance(algorithm, a, b, iterations_per_run)
                run_times.append(avg_time)
            
            # Берем медиану из всех прогонов (устойчива к выбросам)
            run_times.sort()
            median_time = run_times[len(run_times) // 2]
            
            row.append(f"{median_time:.6f} сек")
            algo_times.append((algo_name, median_time))
            
            if median_time < best_time:
                best_time = median_time
                best_algo = algo_name
        
        row.append(best_algo)
        results.append(row)
        
        # Выводим строку таблицы
        print(f"{size_name:<25} | {row[1]:<15} | {row[2]:<15} | {row[3]:<15} | {best_algo:<10}")
        
        # Дополнительная информация о разнице в производительности
        times_dict = dict(algo_times)
        if "Усечённые" in times_dict and "Классический" in times_dict:
            truncated_time = times_dict["Усечённые"]
            classic_time = times_dict["Классический"]
            if classic_time > 0:
                speedup = classic_time / truncated_time
                if speedup > 1.1:
                    print(f"{'':<25}   (Усечённые быстрее классического в {speedup:.2f} раз)")
                elif speedup < 0.9:
                    print(f"{'':<25}   (Классический быстрее усечённых в {1/speedup:.2f} раз)")
    
    return results
    
def precise_measurement(a, b, num_iterations=10000):
    """Точные измерения с timeit"""
    print(f"\nТОЧНЫЕ ИЗМЕРЕНИЯ ({num_iterations} итераций):")
    print("-" * 50)
    
    # Классический
    classic_time = timeit.timeit(
        lambda: euclidean(a, b), 
        number=num_iterations
    ) / num_iterations
    
    # Бинарный  
    binary_time = timeit.timeit(
        lambda: bin_euclidean(a, b),
        number=num_iterations
    ) / num_iterations
    
    # Усечённые
    truncated_time = timeit.timeit(
        lambda: extended_euclidean_truncated_simple(a, b),
        number=num_iterations
    ) / num_iterations
    
    print(f"Классический:    {classic_time:.8f} сек")
    print(f"Бинарный:        {binary_time:.8f} сек") 
    print(f"Усечённые:       {truncated_time:.8f} сек")
    
    speedup_binary = binary_time / classic_time
    speedup_truncated = truncated_time / classic_time
    
    print(f"\nКлассический быстрее бинарного в: {speedup_binary:.2f}x")
    print(f"Классический быстрее усечённых в: {speedup_truncated:.2f}x")

def improved_measurement(a, b, num_iterations=1000):
    """Улучшенные измерения с устранением погрешностей"""
    
    # Прогреваем кэш
    euclidean(a, b)
    bin_euclidean(a, b) 
    extended_euclidean_truncated_simple(a, b)
    
    # Измеряем несколько раз и берём медиану
    times = []
    for _ in range(5):
        classic_times = []
        binary_times = []
        truncated_times = []
        
        for _ in range(num_iterations // 5):
            classic_times.append(euclidean(a, b))
            binary_times.append(bin_euclidean(a, b))
            truncated_times.append(extended_euclidean_truncated_simple(a, b))
        
        times.append((
            sorted(classic_times)[len(classic_times)//2],  # Медиана
            sorted(binary_times)[len(binary_times)//2],
            sorted(truncated_times)[len(truncated_times)//2]
        ))
    
    # Усредняем медианы
    avg_classic = sum(t[0] for t in times) / len(times)
    avg_binary = sum(t[1] for t in times) / len(times) 
    avg_truncated = sum(t[2] for t in times) / len(times)
    print(f"Классический:    {avg_classic:.8f} сек")
    print(f"Бинарный:        {avg_binary:.8f} сек") 
    print(f"Усечённые:       {avg_truncated:.8f} сек")

def extended_euclidean_truncated_simple(r1, r2):
    start_time = time.perf_counter()
    
    num1, num2 = r1, r2
    r_prev, r_cur = r1, r2
    x_prev, y_prev = 1, 0
    x_cur, y_cur = 0, 1

    while r_cur != 0:
        q = (r_prev + r_cur // 2) // r_cur
        r_next = r_prev - q * r_cur
        x_next = x_prev - q * x_cur
        y_next = y_prev - q * y_cur

        r_prev, r_cur = r_cur, r_next
        x_prev, x_cur = x_cur, x_next
        y_prev, y_cur = y_cur, y_next

    # Гарантируем положительный НОД
    if r_prev < 0:
        r_prev = -r_prev
        x_prev = -x_prev
        y_prev = -y_prev
        
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    #print("Расширенный алгоритм Евклида с усечёнными остатками")
    #print(f"НОД({num1}, {num2}) = {r_prev}")
    #print(f"Коэффициенты Безу: x = {x_prev}, y = {y_prev}")
    #print(f"Проверка: {num1}*{x_prev} + {num2}*{y_prev} = {num1*x_prev + num2*y_prev}")
    #print(f"Время выполнения: {execution_time:.6f} секунд")
    
    return execution_time

def bin_euclidean(a, b):
    start_time = time.perf_counter()
    g = 1
    while not(a & 1 or b & 1):
        a >>= 1 ; b >>= 1 ; g <<= 1
    u, v = a, b
    A, B, C, D = 1, 0, 0, 1
    while u != 0:
        while not(u & 1): 
            u >>= 1
            if not(A & 1 or B & 1):
                A >>= 1
                B >>= 1
            else:
                A = (A + b) >> 1
                B = (B - a) >> 1
        while not(v & 1):
            v >>= 1
            if not(C & 1 or D & 1):
                C >>= 1
                D >>= 1
            else:
                C = (C + b) >> 1
                D = (D - a) >> 1
        if u == 0:
            break
        if u >= v:
            u = u - v ;  A = A - C;   B = B - D
        else:
            v = v - u;  C = C - A;  D = D - B

    # Гарантируем положительный НОД
    gcd_result = g * v
    if gcd_result < 0:
        gcd_result = -gcd_result
        C = -C
        D = -D
        
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    #print("Расширенный Бинарный алгоритм Евклида")
    #print(f"НОД({a}, {b}) = {gcd_result}")
    #print(f"Коэффициенты Безу: x = {C}, y = {D}")
    #print(f"Проверка: {a}*{C} + {b}*{D} = {a*C + b*D}")
    #print(f"Время выполнения: {execution_time:.6f} секунд")
    
    return execution_time

def euclidean(a, b):
    start_time = time.perf_counter()
    
    r_old, r_new = a, b
    x_old, x_new = 1, 0
    y_old, y_new = 0, 1

    while r_new != 0:
        q = r_old // r_new
        r_old, r_new = r_new, r_old - q * r_new
        x_old, x_new = x_new, x_old - q * x_new
        y_old, y_new = y_new, y_old - q * y_new
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    #print("Расширенный алгоритм Евклида")
    #print(f"НОД({a}, {b}) = {r_old}")
    #print(f"Коэффициенты Безу: x = {x_old}, y = {y_old}")
    #print(f"Проверка: {a}*{x_old} + {b}*{y_old} = {a*x_old + b*y_old}")
    #print(f"Время выполнения: {execution_time:.6f} секунд")
    
    return execution_time

def compare_algorithms(a, b):
    print("=" * 80)
    print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ АЛГОРИТМОВ")
    print(f"Числа: a = {a}, b = {b}")
    print("=" * 80)
    
    times = []
    
    print("\n1. КЛАССИЧЕСКИЙ АЛГОРИТМ ЕВКЛИДА:")
    time1 = euclidean(a, b)
    times.append(("Классический", time1))
    
    print("\n" + "=" * 80)
    print("2. БИНАРНЫЙ АЛГОРИТМ ЕВКЛИДА:")
    time2 = bin_euclidean(a, b)
    times.append(("Бинарный", time2))
    
    print("\n" + "=" * 80)
    print("3. АЛГОРИТМ С УСЕЧЁННЫМИ ОСТАТКАМИ:")
    time3 = extended_euclidean_truncated_simple(a, b)
    times.append(("Усечённые остатки", time3))
    
    print("\n" + "=" * 80)
    print("ИТОГИ СРАВНЕНИЯ:")
    print("-" * 80)
    
    times.sort(key=lambda x: x[1])
    
    for i, (name, t) in enumerate(times, 1):
        print(f"{i}. {name}: {t:.6f} сек")
    
    fastest = times[0]
    slowest = times[-1]
    speedup = slowest[1] / fastest[1] if fastest[1] > 0 else 0
    
    print(f"\nСамый быстрый: {fastest[0]} ({fastest[1]:.6f} сек)")
    print(f"Ускорение относительно самого медленного: {speedup:.2f}x")
    
    return times

if __name__ == "__main__":
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))

    if b <= 0 or a <= 0:
        print("Invalid input (b and a must be positive)")
        exit()
    if b > a:
        a, b = b, a
    
    compare_algorithms(a, b)
    precise_measurement(a, b, 1000)
    performance_by_number_size()
    improved_measurement(a, b, 1000)