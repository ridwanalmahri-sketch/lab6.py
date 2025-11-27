import math

# Latihan 1: Mengubah fungsi menjadi lambda

# Fungsi asli a(x): menghitung kuadrat
a = lambda x: x**2

# Fungsi asli b(x, y): menghitung jarak Euclidean
b = lambda x, y: math.sqrt(x**2 + y**2)

# Fungsi asli c(*args): menghitung rata-rata
c = lambda *args: sum(args)/len(args) if args else 0

# Fungsi asli d(s): menghilangkan duplikat karakter
d = lambda s: "".join(set(s))

# Testing
if __name__ == "__main__":
    print("=== LATIHAN 1: Lambda Functions ===")
    
    print(f"\na(5) = {a(5)}")  # 25
    print(f"a(-3) = {a(-3)}")  # 9
    
    print(f"\nb(3, 4) = {b(3, 4)}")  # 5.0
    print(f"b(5, 12) = {b(5, 12)}")  # 13.0
    
    print(f"\nc(10, 20, 30) = {c(10, 20, 30)}")  # 20.0
    print(f"c(5, 15, 25, 35) = {c(5, 15, 25, 35)}")  # 20.0
    
    print(f"\nd('hello') = {d('hello')}")  # kombinasi: e, h, l, o
    print(f"d('mississippi') = {d('mississippi')}")  # kombinasi: i, m, p, s
