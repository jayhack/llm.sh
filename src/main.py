import os
import sys
from gpt3 import GPT3
from colorama import Fore
from halo import Halo

spinner = Halo(text='Querying GPT-3', spinner='dots')


def get_dotfile_path():
    return os.path.expanduser('~/.llm.sh')


def get_openai_key():
    """Gets the OpenAI API key from the ~/.llm.sh file"""
    dotfile_path = get_dotfile_path()
    if not os.path.exists(dotfile_path):
        return None
    with open(dotfile_path, 'r') as f:
        for line in f:
            if line.startswith('OPENAI_API_KEY'):
                return line.split('=')[1].strip()
    return None


def set_openai_key():
    """Sets the OpenAI API key in the ~/.llm.sh file"""
    dotfile_path = get_dotfile_path()
    key = input(Fore.RED + '>> Enter your OpenAI key: ')
    with open(dotfile_path, 'w+') as f:
        f.write(f'OPENAI_API_KEY={key}')
    print(Fore.LIGHTBLACK_EX + 'Key saved.')


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
def model_query(openai_key: str, prompt: str) -> str:
    gpt3 = GPT3(openai_key)
    return gpt3.generate_code(prompt)


def process(openai_key: str):
    prompt = ' '.join(sys.argv[1:])
    result = model_query(openai_key, prompt)
    print_prompt(result)
    response = input(Fore.RED + '>> Do you want to run this program? [Y/n] ')
    if response == '' or response.lower() == 'y':
        print(Fore.LIGHTBLACK_EX + '\nRunning...\n')
        run_bash_file_from_string(result)
    else:
        print(Fore.LIGHTBLACK_EX + 'Aborted.')

def main():
    openai_key = get_openai_key()
    if openai_key is None:
        print(Fore.RED + '>> OpenAI API key not found.')
        set_openai_key()
        openai_key = get_openai_key()
    process(openai_key)

if __name__ == '__main__':
    openai_api_key = get_openai_key()
    if not openai_api_key:
        print(Fore.RED + '>> OpenAI API key not found.')
        set_openai_key()
    process(openai_api_key)
