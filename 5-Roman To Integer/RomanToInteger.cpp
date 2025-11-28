#include <iostream>
#include <unordered_map>
#include <string>

int romanToInteger(const std::string& s) {
    std::unordered_map<char, int> values = {
        {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
        {'C', 100}, {'D', 500}, {'M', 1000}
    };

    int total = 0;
    int n = s.size();

    for (int i = 0; i < n; i++) {
        int current = values[s[i]];
        
        // If next character exists and its value is higher → subtract current
        if (i + 1 < n && current < values[s[i + 1]]) {
            total -= current;
        } else {
            total += current;
        }
    }

    return total;
}

int main() {
    std::string roman = "MCMXCIV";
    std::cout << romanToInteger(roman) << std::endl; // Output: 1994
    return 0;
}
