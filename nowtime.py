import time
# storage = 0
storage_limit = 100
def farm(storage):
    while storage < storage_limit:
        storage += 1
        time.sleep(1)
farm(0)