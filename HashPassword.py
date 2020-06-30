import uuid
import hashlib

string = 'Hello World'
print(string)
bstring = str.encode(string, 'utf-8')
print(bstring)
new_string = bstring.decode('utf-8')
print(new_string)

#SHA224
hash_object = hashlib.sha224(bstring)
hex_dig = hash_object.hexdigest()
print(hex_dig)

#SHA256
hash_object = hashlib.sha256(bstring)
hex_dig = hash_object.hexdigest()
print(hex_dig)



def hash_password(password):
    # uuid используется для генерации случайного числа
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


new_pass = input('Введите пароль: ')
hashed_password = hash_password(new_pass)
print('Строка для хранения в базе данных: ' + hashed_password)
old_pass = input('Введите пароль еще раз для проверки: ')

if check_password(hashed_password, old_pass):
    print('Вы ввели правильный пароль')
else:
    print('Извините, но пароли не совпадают')
