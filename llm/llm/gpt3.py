import openai

prompt_str = """
Write a bash script with comments that will delete all files in my current directory:
```
#!/bin/bash

rm -f * # removes all files in current directory
```

Write a bash script with comments that deletes all python files from /usr/agarwal/dev:
```
#!/bin/bash

# change to the /usr/agarwal/dev directory
cd /usr/agarwal/dev

# remove all files ending with .py
rm -f *.py
```

Write a bash script that will concatenate all CSVs that start with "test-" in my current directory together into a CSV called 'result.csv'
```
#!/bin/bash

# create a new file called 'result.csv' and concatenate all files starting with 'test-' into it
cat test-*.csv > result.csv
```

create an empty CSV called results.csv with a name and email column
```
#!/bin/bash

# Create a new file called 'result.csv' and add the header
touch results.csv
echo "name,email" > results.csv
```

{prompt}
```"""

test_data = """
#!/bin/bash

# create a directory called test in the current directory
rm -rf test
mkdir test

# change to the test directory
cd test

# create three empty files named 1, 2 and 3
touch 1 2 3
"""


def format_prompt(prompt: str) -> str:
    return prompt_str.format(prompt=prompt)


class GPT3(object):

    def __init__(self, key):
        self.key = key
        openai.api_key = key

    @staticmethod
    def _generate(prompt: str) -> str:
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=prompt,
            temperature=0,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response['choices'][0]['text']

    @classmethod
    def generate_code(cls, prompt: str) -> str:
        prompt_formatted = format_prompt(prompt)
        raw_gen = cls._generate(prompt_formatted)
        code_str = raw_gen.split('```')[0].strip()
        return code_str
