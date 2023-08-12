def check_palindrom(word):
    if word[::-1] == word:
        return True
    else:
        return False
    
print(check_palindrom('лепсспел'))
print('-' * 5)
print(check_palindrom('helloworld'))