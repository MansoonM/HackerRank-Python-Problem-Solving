#easy

#convert lowercase to uppercase and vice versa

def swap_case(s):
    # Use the swapcase() method to swap the case of each character
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)