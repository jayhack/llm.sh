import os
import sys
from gpt3 import GPT3
from colorama import Fore, Back, Style
from halo import Halo

spinner = Halo(text='Querying GPT-3', spinner='dots')


def indent_multiline_string(s: str) -> str:
    """puts a tab before each line of s"""
    return '|  ' + s.replace('\n', '\n|  ')

def print_prompt(prompt: str):
    with open('temp.sh', 'w') as f:
        f.write(prompt)
    os.system('bat temp.sh')
    os.remove('temp.sh')
    # print(Fore.LIGHTBLACK_EX + '\n| Prompt: ')
    # print(Fore.LIGHTBLACK_EX + '------------------------------')
    # print(Fore.CYAN + indent_multiline_string(prompt))
    # print(Fore.LIGHTBLACK_EX + '------------------------------\n')

def run_bash_file_from_string(s: str):
    """Runs a bash script from a string"""
    with open('temp.sh', 'w') as f:
        f.write(s)
    os.system('bash temp.sh')
    os.remove('temp.sh')


@Halo(text='Querying GPT-3', spinner='dots')
def model_query(prompt: str) -> str:
    return GPT3.generate_code(prompt)

def process():
    prompt = ' '.join(sys.argv[1:])
    result = model_query(prompt)
    print_prompt(result)
    # print(Fore.LIGHTBLACK_EX + '\n| Generated Code: ')
    # print(Fore.LIGHTBLACK_EX + '------------------------------')
    # print(Fore.CYAN + indent_multiline_string(result))
    # print(Fore.LIGHTBLACK_EX + '------------------------------\n')

    # =====[ Run it]=====
    # input inline with print statement
    # input('Press enter to run the code...')
    response = input(Fore.RED + '>> Do you want to run this program? [Y/n] ')
    if response == '' or response.lower() == 'y':
        print(Fore.LIGHTBLACK_EX + '\nRunning...\n')
        run_bash_file_from_string(result)
    else:
        print(Fore.LIGHTBLACK_EX + 'Aborted.')


import time
if __name__ == '__main__':
    # os.system('bat results.csv')
    process()