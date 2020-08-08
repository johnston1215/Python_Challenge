
something =[0,1,2,3]

print(something[2])

somethingElse = {'one':12,'two':13,'zero':8,'blah':10}

print(somethingElse)

somethingElse['zero'] = somethingElse['zero'] + 5
#somethingElse['zero'] += 5

print(somethingElse)

somethingElse['soemthing'] = "6"

print(somethingElse)

if 'onet' in somethingElse:
    print('yes')
else:
    print('nope')