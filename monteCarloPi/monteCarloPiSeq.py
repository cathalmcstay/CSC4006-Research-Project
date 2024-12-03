import sys
import time
import random

def calculate_pi(iterations):
    inside_circle = 0
    for _ in range(iterations):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return (4.0 * inside_circle) / iterations

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <iterations>")
        sys.exit(1)

    try:
        iterations = int(sys.argv[1])
        if iterations <= 0:
            raise ValueError
    except ValueError:
        print("Please provide a positive integer for iterations.")
        sys.exit(1)


    io_start_time = time.time()
    print(f"Starting Monte Carlo Pi computation with {iterations} iterations...")
    io_end_time = time.time()

    compute_start_time = time.time()
    pi = calculate_pi(iterations)
    compute_end_time = time.time()

    io_final_start = time.time()
    print(f"Estimated Pi: {pi:.10f}")
    io_final_end = time.time()

    io_time = (io_end_time - io_start_time) + (io_final_end - io_final_start)
    compute_time = compute_end_time - compute_start_time
    total_time = io_time + compute_time

    print(f"I/O Time: {io_time:.6f} seconds")
    print(f"Compute Time: {compute_time:.6f} seconds")
    print(f"Total Time: {total_time:.6f} seconds")
