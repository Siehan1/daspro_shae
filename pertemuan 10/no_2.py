import numpy as np

def random_array(low, high, size):
    rng = np.random.default_rng()
    return rng.integers(low=low, high=high,size=size)

nilai = random_array(0, 100, 30)
nilai_sorted = np.sort(nilai)[::-1]

print("Nilai 30 orang:")
print(nilai)
print("Nilai 5 orang tertinggi:")
print(nilai_sorted[:5])