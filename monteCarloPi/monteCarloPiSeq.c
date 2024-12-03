#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double calculate_pi(long iterations) {
    long inside_circle = 0;
    for (long i = 0; i < iterations; i++) {
        double x = (double)rand() / RAND_MAX;
        double y = (double)rand() / RAND_MAX;
        if ((x * x + y * y) <= 1.0) {
            inside_circle++;
        }
    }
    return (4.0 * inside_circle) / iterations;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <iterations>\n", argv[0]);
        return 1;
    }

    long iterations = atol(argv[1]);
    if (iterations <= 0) {
        printf("Please provide a positive number of iterations.\n");
        return 1;
    }

    clock_t start_io = clock();
    printf("Starting Monte Carlo Pi computation with %ld iterations...\n", iterations);
    clock_t end_io = clock();

    clock_t start_compute = clock();
    double pi = calculate_pi(iterations);
    clock_t end_compute = clock();

    start_io = clock();
    printf("Estimated Pi: %.10f\n", pi);
    printf("I/O Time: %.6f seconds\n", ((double)(end_io - start_io) + (double)(clock() - end_io)) / CLOCKS_PER_SEC);
    printf("Compute Time: %.6f seconds\n", (double)(end_compute - start_compute) / CLOCKS_PER_SEC);
    printf("Total Time: %.6f seconds\n", (double)(clock() - start_io) / CLOCKS_PER_SEC);
    return 0;
}
