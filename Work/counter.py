from timethis import timethis

@timethis
def countdown(num):
    print(f"{num}...")
    while num>0:
        num= num-1

    print("done")

countdown(1_000_000)
