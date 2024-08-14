import sys
import random
from colorama import Fore, Style

lower_letters = ['a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_letters = ['A','B','C','D','E','F','G','H','I','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['~','`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','/', '\\', '\'', '"', ';', ':', '<', ',', '.', '>', '?', '|', '[',']','{','}']
numbers = ['1','2','3','4','5','6','7','8','9']

def print_ascii():
    ascii_txt = r"""
 $$$$$$\  $$$$$$$$\ $$\   $$\       $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
$$  __$$\ $$  _____|$$$\  $$ |      $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ /  \__|$$ |      $$$$\ $$ |      $$ |  $$ |$$ /  $$ |$$ /  \__|$$ /  \__|
$$ |$$$$\ $$$$$\    $$ $$\$$ |      $$$$$$$  |$$$$$$$$ |\$$$$$$\  \$$$$$$\  
$$ |\_$$ |$$  __|   $$ \$$$$ |      $$  ____/ $$  __$$ | \____$$\  \____$$\ 
$$ |  $$ |$$ |      $$ |\$$$ |      $$ |      $$ |  $$ |$$\   $$ |$$\   $$ |
\$$$$$$  |$$$$$$$$\ $$ | \$$ |      $$ |      $$ |  $$ |\$$$$$$  |\$$$$$$  |
 \______/ \________|\__|  \__|      \__|      \__|  \__| \______/  \______/ """
    print(Fore.LIGHTMAGENTA_EX + ascii_txt + Style.RESET_ALL)

def run_tool():
    args = sys.argv
    if len(args) < 2:
        print(Fore.RED + 'Syntax: python pass_generator.py <pass_length>' + Style.RESET_ALL)
        sys.exit()
    else:
        length = args[1]
        password = ''
        for i in range(0, int(length)):
            j = random.randint(1,4)
            if j == 1:
                x = random.randint(0, len(lower_letters) - 1)
                password += (lower_letters[x])
            elif j == 2:
                x = random.randint(0, len(upper_letters) - 1)
                password += (upper_letters[x])
            elif j == 3:
                x = random.randint(0, len(symbols) - 1)
                password += (symbols[x])
            else:
                x = random.randint(0, len(numbers) - 1)
                password += (numbers[x])
        print(Fore.LIGHTBLACK_EX + "*"*50 + Style.RESET_ALL)
        print(Fore.CYAN + 'Your Password is: ' + Style.RESET_ALL, end='')
        print(Fore.GREEN + password + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + "*"*50 + Style.RESET_ALL)


if __name__ == "__main__":
    try:
        print_ascii()
        run_tool()
    except KeyboardInterrupt:
        print(Fore.RED + 'Ctrl+C Detected! Exiting...' + Style.RESET_ALL)
    except Exception:
        print(Fore.RED + 'Something Strange Happened!' + Style.RESET_ALL)
