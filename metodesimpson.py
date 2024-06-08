import time
import numpy as np

def f(x):
    return 4 / (1 + x**2)

def simpson_13_integration(a, b, N):
    h = (b - a) / N
    x = np.linspace(a, b, N+1)
    y = f(x)
    integral = h / 3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return integral

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Variasi nilai N
Ns = [10, 100, 1000, 10000]

# Menghitung integral untuk setiap N
errors = []
runtimes = []

for N in Ns:
    start_time = time.time()
    integral = simpson_13_integration(0, 1, N)
    end_time = time.time()
    runtime = end_time - start_time
    error = abs(integral - pi_ref)
    errors.append(error)
    runtimes.append(runtime)

    print(f"N = {N}:")
    print(f"  Integral: {integral}")
    print(f"  Error: {error}")
    print(f"  Runtime: {runtime} seconds\n")

# Menghitung galat RMS
rms_error = np.sqrt(np.mean(np.array(errors)**2))
print(f"Root Mean Square Error: {rms_error}")
