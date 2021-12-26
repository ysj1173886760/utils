auto start = std::chrono::steady_clock::now();
// your code
auto end = std::chrono::steady_clock::now();
std::chrono::duration<double> elapsed_seconds = end - start;
std::cout << "elapsed time: " << elapsed_seconds.count() << "s\n";