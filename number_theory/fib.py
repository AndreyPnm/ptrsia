import sys


def fib(n):
    if n < 0:
        raise ValueError('Fibonacci number subscript is negative')

    a, b = 0, 1
    if n == 0:
        return a

    for _ in range(n - 1):
        a, b = b, a + b

    return b

def fib_build_sequence_while(predicate) -> [int]:
    res = []

    i = 0
    _tmp = 0
    while True:
        if (i == 0):
            _tmp = 0
        elif (i == 1):
            _tmp = 1
        else:
            _tmp = res[i-1]+res[i-2]

        if (predicate(_tmp)):
            res.append(_tmp)
            i+=1
        else:
            break

    return (res,i)

def fib_mod(n, m) -> int:
    (fibs_lower_than_m, length) = fib_build_sequence_while(lambda x : x <= m)
    
    traces = [n%2]
    k = n
    while True:
        if (k < length):
            break
        k = int(k/2)
        traces.append(k%2)

    rn = fibs_lower_than_m[k]
    rn_m1 = fibs_lower_than_m[k-1]

    l = len(traces)
    for i in range(1,l):
        r2n = (rn + 2*rn_m1)*rn
        r2n_p1 = (rn + rn_m1)**2 + rn**2
        r2n_m1 = rn**2 + rn_m1**2
        
        if traces[l-1-i] == 0:
            rn = r2n % m
            rn_m1 = r2n_m1 % m
        else:
            rn = r2n_p1 % m
            rn_m1 = r2n % m
    
    return rn
    
def main(argv):
    with open(argv[1], 'r') as input_file:
        for line in input_file:
            if not line.strip():
                continue

            n, m = map(int, line.split())
            print(fib_mod(n, m))

if __name__ == '__main__':
    main(sys.argv)
