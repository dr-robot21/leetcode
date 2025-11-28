#include <iostream>

bool plindromNumber(int number) {
    if(number < 0) {
        return false;
    }

    int reverse = 0;
    int number_cpy = number;

    while (number > 0)
    {
        reverse = (reverse*10) + (number % 10);
        number /= 10;
    }
    
    return number_cpy == reverse;
}


int main()
{

    int number = 12621;
    bool isPalindrome = plindromNumber(number);

    std::cout << isPalindrome;
    return 0;
}
