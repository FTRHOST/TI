import time

start_time = time.time()

n = 1000

for i in range(n):
    print(i)

end_time = time.time()

waktu_selesai = end_time - start_time

print(f'waktunya adalah {waktu_selesai}')
