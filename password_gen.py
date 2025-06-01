import random

chars = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXYyZz0123456789!@#$%^&'
password = []

try:
    password_len = int(input('Enter password length: '))
except ValueError or TypeError:
    print('Please enter a number.')
    password_len = int(input('Enter password length: '))

for i in range(0, password_len):
    password += random.choice(chars)

final_pass = ''.join(password)

with open("pass_log.txt", "a") as pass_logs:
    pass_logs.write(final_pass + '\n')

print('Password stored in a log file named pass_log.txt')
print(final_pass)
