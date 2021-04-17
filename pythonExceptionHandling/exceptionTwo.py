try:
    f= open('testException.txt','r')
    f.write('Hello and welcome to exception tutorial')
except TypeError:
    print('Hey there is some type error')
except IOError:
    print('Hey there is some IO Exception')
finally:
    print('from finally block')

def ask_for_int():
    while True:
        try:
            number = int(input('Please enter a number : '))
        except:
            print('There is some error. Please Enter valid number')
            continue
        else:
            print(f'You have entered a valid number {number}')
            break
        finally:
            print('I always run')

ask_for_int()
        

    