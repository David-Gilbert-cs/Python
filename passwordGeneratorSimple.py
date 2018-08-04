'''

author : david gilbert
problem : random password generator simplified

'''
import random as r

length = input("how long do you you want your password ? ")

char = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

password =  "".join(random.sample(s,passlen ))
print password