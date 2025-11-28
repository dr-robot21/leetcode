def palindromNumber(number):
    if number < 0 :
        return False
    
    reverse = 0
    number_cpy = number
    
    while number > 0:
        reverse = (reverse) * 10 + (number % 10)
        number = number // 10
    
    
    return reverse == number_cpy


