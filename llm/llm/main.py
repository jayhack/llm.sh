import os
import sys
from gpt3 import GPT3
from colorama import Fore, Back, Style


def indent_multiline_string(s: str) -> str:
    """puts a tab before each line of s"""
    return '  ' + s.replace('\n', '\n  ')


def run_bash_file_from_string(s: str):
    """Runs a bash script from a string"""
    with open('temp.sh', 'w') as f:
        f.write(s)
    os.system('bash temp.sh')
    os.remove('temp.sh')


def process():
    prompt = ' '.join(sys.argv[1:])
    result = GPT3.generate_code(prompt)
    print(Fore.LIGHTBLACK_EX + '\nGenerated Code: ')
    print(Fore.LIGHTBLACK_EX + '------------------------------')
    print(Fore.CYAN + indent_multiline_string(result))
    print(Fore.LIGHTBLACK_EX + '------------------------------\n')

    # =====[ Run it]=====
    # input inline with print statement
    # input('Press enter to run the code...')
    response = input(Fore.RED + 'Do you want to run this program? [Y/n] ')
    if response == '' or response.lower() == 'y':
        print(Fore.LIGHTBLACK_EX + '\nRunning...\n')
        run_bash_file_from_string(result)
    else:
        print(Fore.LIGHTBLACK_EX + 'Aborted.')


if __name__ == '__main__':
    process()