
def Printf():
    print('1 for add')
    print('2 for printall')
    print('3 for jostejo')
    print('0 for close')


def AddPhoneNumber(phonenumber):
    Name = input('name ra vared konid ')
    Phone = input('name ra vared konid ')
    phonenumber [Name]=Phone
    print('azafe shod shomare')
    print(phonenumber)
def PrintAllPhoneN(phonenumber):
        if phonenumber:
            for k , v in phonenumber.items():
                print(f'{k} and {v}')
        else:
            print('chezy nist')
def JostojoByName(phonenumber):
    serche=input("jostojo by name ")
    if ( serche in phonenumber):
        print(f'shomare {serche} haste {phonenumber[serche]}')
    else:
        print(f'not found {serche}')

    phonenumber = {}
    while True:
        Printf()
        chice=input('choice')
        if chice=='1':
            AddPhoneNumber(phonenumber)
        elif chice=='2':
            PrintAllPhoneN(phonenumber)
        elif chice=='3':
            JostojoByName(phonenumber)
        elif chice=='0':
            break
        else:
            print('ashtah hast choice')


