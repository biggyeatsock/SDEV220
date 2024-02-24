import multiprocessing
import random
import time
from datetime import datetime

def wait_and_print():
    wait_time = random.random()  # Generate a random number between 0 and 1
    time.sleep(wait_time)
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Current time: {current_time}, Process ID: {multiprocessing.current_process().pid}")

if __name__ == "__main__":
    processes = []
    for _ in range(3):  # Create 3 processes
        p = multiprocessing.Process(target=wait_and_print)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
