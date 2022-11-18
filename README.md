# LLM.sh

Copilot for your command line. Just type `llm XYZ` and it will generate/run a script for you that does XYZ.

# Installation

Get an OpenAI API Key here: https://beta.openai.com/signup/

Install bat (https://github.com/sharkdp/bat#installation), a better cat alternative
```
~$: port install bat # or brew install bat - 
```


Install LLM.sh via pip
```
~$: pip install --upgrade git+https://github.com/jayhack/llm.sh
```

# Usage

Note that you should expect 10-20s latency for each command.

Type `llm [command]`, like so:
```
~$: llm rename all files in this directory from snake case to camelcase
```

You will receive an output like this:
```
───────┬─────────────────────────────────────────────────────────────────────────────────────
       │ File: temp.sh
───────┼─────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/bin/bash
   2   │
   3   │ # rename all files in this directory from snake case to camelcase
   4   │ for file in *; do
   5   │   mv "$file" "$(echo $file | sed -r 's/(_)([a-z])/\U\2/g')"
   6   │ done
───────┴─────────────────────────────────────────────────────────────────────────────────────
>> Do you want to run this program? [Y/n]
```

Hit Y (or enter) to run the script. That's it!
