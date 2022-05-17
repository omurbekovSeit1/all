'''
problem1
a = input('Add your word: ')
b = input('Add your word: ')
c = input('Add your word: ')
d = []
d.extend([a, b, c])
print(d)

if len(a + b + c) >= 20:
	print(d)
else:
	print('Very shord words')
if len(d) > len(b) and len(a) > len(c):
	d.remove(a)
	print(a.upper())
elif len(b) > len(a) and len(b) > len(c):
	d.remove(b)
	print(b.upper())
else:
	d.remove(c)
	print(c.upper())
print(d)

problem 2
a = input('Add your email adress: ')
if "@mail.ru" in a or a.endswith("@gmail.com"):
	print('Your code is 222222')
else:
	print('Not correct email adress')
b = int(input('Add your code: '))
if b == 222222:
	print('right code')
else:
	print('not correct code')

problem 3

a = 2897607
b = a // 3
c = a%3
d =  b * b
if c == 0:
        print(d)
        print(len(str(d)))

if len(str(d)) > 10:
        print(str(d).replace('3', '0'))
        print(str(d).replace('3', '0')[0:6])

problem 4

a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = ( 11, 12, 13, 14, 15, 45)
c = list(b)
print(c)
a.extend(c)
print(a)
print(a[0], len(a)//2, a[-1])
'''
