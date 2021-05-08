# Read "Problem.txt"

case = dict()


def readbin(txt):
    while True:
        try:
            ok = True
            while ok:
                x = int(input(txt))
                if x == 0 or x == 1:
                    ok = False
                
                elif x != 1 or x != 0:
                    print('Type a number, \033[31m0\033[m to \033[31mOff\033[m or \033[34m1\033[m to \033[34mOn\033[m')
        except:
            print('{}Sorry, invalid command, try again.{}'.format('\033[31m', '\033[m'))
        else:
            return x


print('{}Hello, world.{}'.format('\033[36m', '\033[m'))
while True:
    case["E"] = readbin('"\033[32mE\033[m" is On or Off: ')
    case["G"] = readbin('"\033[32mG\033[m" is On or Off: ')
    case["C"] = readbin('"\033[32mC\033[m" is On or Off: ')
    case["I"] = readbin('"\033[32mI\033[m" is On or Off: ')
    if case["E"] == 0 and case["G"] == 1 and case["C"] == case["I"] == 1 or case ["E"] == 1 and case["G"] == 0 and case["C"] == case["I"] == 1:
        print('{}It is Ok{}'.format('\033[34m', '\033[m'))
    else:
        print('{}Attention! We have a problem.{}'.format('\033[31m', '\033[m'))
    answer = str(input('Do you want to continue [\033[34mY | \033[31mN\033[m]]? ')).title()[0]
    if answer == 'N':
        break
    else:
        print('Another test.')