import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

def f(x):
    return x**2

a = 0  # Нижня межа інтегрування
b = 2  # Верхня межа інтегрування

def monte_carlo(f, a, b, num_samples=10000):
    random_x = np.random.uniform(a, b, num_samples)
    random_y = f(random_x)
    integral_mc = (b - a) * np.mean(random_y)
    return integral_mc

integrals_mc = {}
for n in [100, 1000, 10000, 100000, 1000000]:
    integrals_mc[n] = monte_carlo(f, a, b, n)
    print(f"Monte Carlo інтеграл ({n} точок): {integrals_mc[n]}")

result, error = spi.quad(f, a, b)
print("Інтеграл (quad): ", result)

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')


ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
plt.grid()
plt.show()

# Висновки
print("\nАналіз результатів обчислення інтеграла:")
print(f"Інтеграл (quad): {result}")
for n, integral in integrals_mc.items():
    print(f"Monte Carlo інтеграл ({n} точок): {integral}")
