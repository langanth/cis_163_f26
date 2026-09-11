from time import sleep

for h in range(24):
    for m in range(60):
        for s in range(60):
            print(f'{h:.3f}:{m:03d}:{s:05d}')
            sleep(1)