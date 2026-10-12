
# Definisi decorator
def my_decorator(func):
    def wrapper():
        print("--- Sebelum fungsi dipanggil ---")
        func()
        print("--- Setelah fungsi dipanggil ---")
    return wrapper

# Menerapkan decorator
@my_decorator
def sapa():
    print("Halo!")

sapa()
