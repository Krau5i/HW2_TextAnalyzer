'''
app specific funcs here

'''
def mainMenu():
    print('\nWelcome to the text analyzer! \n')
    print('To make an inquiry about Alice in Wonderland, press A. Enter Q to exit the program.')
    while True:
        userInput = input('Enter your choice: ')
        if userInput.lower()=='a':
            subMenu()
            break
        elif userInput.lower()=='q':
            break
        else:
            print('Invalid choice - please enter A for inquiry or Q to exit')
    exit

def subMenu():
    print('\nPlease select one of the following options:\n')
    print('1 - Show the number of distinct raw words')
    print('2 - Show the number of standardized words')
    print('3 - Show counts for some of the most frequently used characters, listed in order of decreasing frequency')
    print('4 - Show counts for some of the most frequently used raw or standardized words, listed in order of decreasing frequency')
    print('5 - Show all the standardized words that occur a specified number of times')
    print('6 - Show the longest and shortest raw or standardized words that contain every character in a list, and do not contain any character in another list')
    print('7 - List the frequency counts for a specified number of raw or standardized words that start with a particular string')
    print('9 - Back to main menu\n')
    while True:
        try:
            userInput = int(input('Enter your choice: '))
            if userInput == 1:
                optionOne()
            elif userInput == 2:
                optionTwo()
            elif userInput == 3:
                print('3')
            elif userInput == 4:
                print('4')
            elif userInput == 5:
                print('5')
            elif userInput == 6:
                print('6')
            elif userInput == 7:
                print('7')
            elif userInput == 9:
                break
            else:
                print('Invalid choice - please enter 1 through 8 for inquiry or 9 to exit')
        except ValueError:
            print('Invalid choice - please enter an integer per menu options!')
           
    exit

if __name__ == '__main__':
    mainMenu()
