
def isPalindrome( x: int) -> bool:
    if x < 0:
        return False

    reversed_num = 0
    temp = x

    while temp != 0:
        digit = temp % 10
        print(f"digit is currently {digit}")
        reversed_num = reversed_num * 10 + digit
        print(f"reversed_num is currently {reversed_num}")
        temp //= 10
        print(f"temp is currently {temp}")

    return reversed_num == x



isPalindrome(546) 