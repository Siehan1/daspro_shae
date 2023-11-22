import numpy as np

def random_array(low, high, size):
    rng = np.random.default_rng()
    return rng.integers(low=low, high=high,size=size)

def C_to_F(c):
    return c * 9/5 + 32

celcius = random_array(15, 40, 10)

print("Suhu Singapura dalam 10 hari terakhir:")
for x in range(len(celcius)):
    print(f"Hari ke-{x+1}: {celcius[x]} C, {C_to_F(celcius)[x]} F")