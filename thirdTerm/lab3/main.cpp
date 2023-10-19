#include <iostream>

int main() {
    long long x;
    std::cin >> x;
    for (long long a = 1; a <= x; a *= 3) {
        for (long long b = 1; a * b <= x; b *= 5) {
            for (long long c = 1; a * b * c <= x; c *= 7) {
                std::cout << a * b * c << "\n";
            }
        }
    }
}
