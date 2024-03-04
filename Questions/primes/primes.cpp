#include <iostream>
#include <chrono>

bool is_prime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int prime = 0;
    int notPrime = 0;
    auto start_time = std::chrono::high_resolution_clock::now();
    for (int i = 1; i <= 1000000; i++) {
        if (is_prime(i)) {
            prime++;
        } else {
            notPrime++;
        }
    }
    auto end_time = std::chrono::high_resolution_clock::now();
    auto elapsed_time = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time);
    std::cout << "Found " << prime << " prime numbers" << std::endl;
    std::cout << "Found " << notPrime << " non prime numbers" << std::endl;
    std::cout << "Took " << elapsed_time.count() << " milliseconds." << std::endl;
    return 0;
}
