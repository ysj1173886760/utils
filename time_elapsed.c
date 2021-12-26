// this is real time elapsed, can be used in test response time
struct timespec end, start;
clock_gettime(CLOCK_MONOTONIC, &start);
// your code
clock_gettime(CLOCK_MONOTONIC, &end);
double elapsed = (end.tv_sec - start.tv_sec);
elapsed += (end.tv_nsec - start.tv_nsec) / 1000000000.0;
printf("elapsed time %.2fs\n", elapsed);


// this is clock time, do not use it in multi-thread program
clock_t start = clock();
// your code
clock_t end = clock();
double time = ((double)(end - start)) / CLOCKS_PER_SEC;
printf("elapsed time %.2lfs\n", time);