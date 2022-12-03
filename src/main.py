import os
import sys
from colorama import Fore
from halo import Halo
import requests

spinner = Halo(text='Querying GPT-3', spinner='dots')


def print_prompt(prompt: str):
    """Uses highlighting from your native cat; I use bat, a cat alternative"""
    with open('temp.sh', 'w') as f:
        f.write(prompt)
    os.system('bat temp.sh')
    os.remove('temp.sh')


def run_bash_file_from_string(s: str):
    """Runs a bash script from a string"""
    with open('temp.sh', 'w') as f:
        f.write(s)
    os.system('bash temp.sh')
    os.remove('temp.sh')


@Halo(text='Querying GPT-3', spinner='dots')
def model_query(prompt: str) -> str:
    data = {
        "input": ""
    }
    headers = {"Authorization": "Basic clb76yfe1056trk1al1zq2h0w"}
    response = requests.post(
        "https://dashboard.scale.com/spellbook/api/app/8r493dlh",
        json=data,
        headers=headers
    )
    return response.json()['text']


def process():
    prompt = ' '.join(sys.argv[1:])
    result = model_query(prompt)
    print_prompt(result)
    response = input(Fore.RED + '>> Do you want to run this program? [Y/n] ')
    if response == '' or response.lower() == 'y':
        print(Fore.LIGHTBLACK_EX + '\nRunning...\n')
        run_bash_file_from_string(result)
    else:
        print(Fore.LIGHTBLACK_EX + 'Aborted.')


def main():
    process()


if __name__ == '__main__':
    process()
