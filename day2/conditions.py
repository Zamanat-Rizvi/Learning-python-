age=int(input('enter your age: '))
if age<13:
    print('perfect age buddy')
else:
    print('too old')
    
    
    
    
match(age):
    case 1:
        print('one')
    case 2:
        print('two')
    case _:
        print('i forgot counting')


price= 100 if age<18 else 0.01
print(f'your price:{price}')