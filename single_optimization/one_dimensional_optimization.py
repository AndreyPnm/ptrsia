"""

Одномерная оптимизация.
Написать программу для решения следующей задачи:
Минимизировать функцию f(x) на отрезке a <= x <= b

1. f(x) = x, 0<=x<=10
2. f(x) = (x - 3)^2+4, 0<=x<=10
3. f(x) = ((x - 3)^2 - 4)^2, 0<=x<=10
4. f(x) = ((x - 3)^2 - 4)^2 + 12x, 0<=x<=10

Методы:
1. Перебора по x_i = a + i/n*(b-a), 0<=i<=n
2. Метод дихотомии с фиксированным delta = 10^(-9)
3. Метод золотого сечения
4. Метод Ньютона (знание производной)

"""

import math
import inspect

class Function:
    def __init__(self, function, dfunction):
        self.counter = 0
        self.f = function
        self.df = dfunction

    def __call__(self, x):
        self.counter += 1
        return self.f(x)

    def get_d(self, x):
        return self.df(x)

class Optimizer:
    def __init__(self):
        pass

    def optimize(self, function, a, b):
        x_opt = a
        f_opt = function(x_opt)
        """Здесь пишем код метода оптимизации"""        
        return x_opt, f_opt

class BruteOptimizer(Optimizer):
    def optimize(self, function, a, b):
        steps_num = 3000

        x_opt = a
        f_opt = function(x_opt)

        x = a
        h = (b - a) / steps_num
        for i in range(0, steps_num):
            x += h
            y = function(x)
            if y < f_opt:
                x_opt = x
                f_opt = function(x_opt)

        return x_opt, f_opt


class GoldenSectionOptimizer(Optimizer):
    def optimize(self, function, a, b):
        delta = 1e-9

        invphi = (math.sqrt(5) - 1) / 2
        invphi2 = (3 - math.sqrt(5)) / 2

        h = b - a
        if h <= delta:
            x_opt = (a + b)/2
            f_opt = function(x_opt)
            return x_opt, f_opt

        n = int(math.ceil(math.log(delta / h) / math.log(invphi)))

        c = a + invphi2 * h
        d = a + invphi * h
        yc = function(c)
        yd = function(d)

        for k in range(n-1):
            if yc < yd:
                b = d
                d = c
                yd = yc
                h = invphi * h
                c = a + invphi2 * h
                yc = function(c)
            else:
                a = c
                c = d
                yc = yd
                h = invphi * h
                d = a + invphi * h
                yd = function(d)

        if yc < yd:
            x_opt = (a + d)/2
        else:
            x_opt = (c + b)/2
        f_opt = function(x_opt)
        return x_opt, f_opt


class DichotomyOptimizer(Optimizer):
    def optimize(self, function, a, b):        
        delta = 1e-9

        mid = (a + b) / 2
        while (b - a > delta):

            if function(mid - delta) < function(mid + delta):
                b = mid
                mid = (a + b) / 2
            else:
                a = mid
                mid = (a + b) / 2

        x_opt = mid
        f_opt = function(x_opt)
        return x_opt, f_opt


class NewtonOptimizer(Optimizer):
    def optimize(self, function, a, b):
        delta = 1e-9
        x = (a + b)/2
        dfx = function.get_d(x)

        while abs(function(x)) > delta:
            dfx = function.get_d(x)
            if dfx == 0:
                break
            x = x - function(x)/dfx

        x_opt = x
        f_opt = function(x_opt)
        return x_opt, f_opt

def f1(x):
    return x

def df1(x):
    return 1

def f2(x):
    return (x - 3)**2 + 4

def df2(x):
    return 2 * x -6

def f3(x):
    return ((x - 3)**2 - 4)**2

def df3(x):
    return 4 * (x**3) - 36 * (x**2) + 92 * x - 60

def f4(x):
    return ((x - 3)**2 - 4)**2

def df4(x):
    return 4 * (x**3) - 36 * (x**2) + 92 * x - 48

def main():
    def run_for_all_functions(optimizer_name, optimizer, a, b):
        print(f'--{optimizer_name}')
        run_and_output(optimizer, Function(f1, df1), 'f1', a, b)
        run_and_output(optimizer, Function(f2, df2), 'f2', a, b)
        run_and_output(optimizer, Function(f3, df3), 'f3', a, b)
        run_and_output(optimizer, Function(f4, df4), 'f4', a, b)

    def run_and_output(optimizer, function, function_name, a, b):
        x, f = optimizer.optimize(function, a, b)
        print(f'The minimal value for {function_name} is {f} and is found at x = {x}')
        print(f'Function {function_name} was called {function.counter} times')
        print('--')

    brute_opt = BruteOptimizer()
    dichotomy_opt = DichotomyOptimizer()
    golden_section_opt = GoldenSectionOptimizer()
    newton_opt = NewtonOptimizer()

    a = 0
    b = 10

    run_for_all_functions('Brute force method', brute_opt, a, b)
    run_for_all_functions('Dichotomy method', dichotomy_opt, a, b)
    run_for_all_functions('Golden section method', golden_section_opt, a, b)
    run_for_all_functions('Newton method', newton_opt, a, b)

if __name__ == '__main__':
    main()
