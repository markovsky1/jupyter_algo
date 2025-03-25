import numpy as np
import math
import matplotlib.pyplot as plt


def O_1(n): return np.ones_like(n)  # O(1)
def O_log_n(n): return np.log2(n)  # O(log n)
def O_n(n): return n  # O(n)
def O_n_log_n(n): return n * np.log2(n)  # O(n log n)
def O_n2(n): return n**2  # O(n^2)
def O_2n(n): return 2**n  # O(2^n)
def O_n_fact(n): return [math.factorial(i) for i in n]  # O(n!)


n = np.linspace(1, 20, 100)  # Значения от 1 до 20
n_int = np.arange(1, 11)  # Для факториала (ограничено)


plt.figure(figsize=(10, 6))

# Заливка областей
plt.fill_between(n, O_n(n), O_n_log_n(n), color="yellow", alpha=0.5, label="Приемлемо")
plt.fill_between(n, O_n_log_n(n), O_n2(n), color="lightblue", alpha=0.5, label="Плохо")
plt.fill_between(n, O_n2(n), O_2n(n), color="blue", alpha=0.5, label="Ужас-ужас")

# Линии функций
plt.plot(n, O_1(n), label="O(1)", color="green", linewidth=2)
plt.plot(n, O_log_n(n), label="O(log n)", color="darkgreen", linewidth=2)
plt.plot(n, O_n(n), label="O(n)", color="orange", linewidth=2)
plt.plot(n, O_n_log_n(n), label="O(n log n)", color="red", linewidth=2)
plt.plot(n, O_n2(n), label="O(n^2)", color="purple", linewidth=2)
plt.plot(n, O_2n(n), label="O(2^n)", color="brown", linewidth=2)
plt.plot(n_int, O_n_fact(n_int), label="O(n!)", color="black", linewidth=2)

# Подписи
plt.xlabel("Количество элементов (n)")
plt.ylabel("Количество операций")
plt.legend()
plt.yscale("log")  # Логарифмическая шкала
plt.grid(True, which="both", linestyle="--")

plt.show()