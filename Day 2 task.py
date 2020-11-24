#task A

a = b = c = 10

a //= 10
b  *= 50
c  += 60

print(a,b,c)
#output = 1 500 70

#task B

string = "EABLE"

string = string[:2] + 'G' + string[3:]

print(string)
#output = EAGLE

#task C

a = 1000
b = 100.0
a = float(a)
b = int(b)

print(a,':',type(a),b,':',type(b))
#output = 1000.0 : <class 'float'> 100 : <class 'int'>
