text = input('Enter text: ')
def palindrome(arg):
    arg = arg.lower()
    arg =  ''.join(arg.split())
    return arg[::-1] == arg

print(palindrome(text))