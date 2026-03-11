import time
import random

def waiting_game():
    print("Welcome to the waiting game!")
    random_time = random.randint(2, 4)
    print(f"Your target time is {random_time} seconds.")
    input("---Press Enter to Begin---")
    start_time = time.perf_counter()
    input(f"...Press Enter again after {random_time} seconds...")
    elapsed_time = time.perf_counter() - start_time
    print(f"Elapsed time: {elapsed_time:.3f} seconds")
    if elapsed_time == random_time:
        print("(Congratulations! You hit the target time exactly!)")
    elif elapsed_time < random_time:
        print(f"({random_time - elapsed_time:.3f} seconds too fast)")
    else:
        print(f"({elapsed_time - random_time:.3f} seconds too slow)")

if __name__ == "__main__":
    waiting_game()
