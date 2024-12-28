
# Author: Pierce Brooks
# python3 -m pip install -r requirements.txt

import argparse
import fnmatch
import os
import sys
from translate import Translator

parser = argparse.ArgumentParser(prog="RecursiveTranslator", description="Use a shell regex pattern to recursively translate all files within the current working directory of execution and its subdirectories.", epilog="Usage Example: %s -l \"en\" -p \"mymemory\" -r \"\\*.md\" -s \"foo@bar.com\""%sys.executable)
parser.add_argument("-l", "--language")
parser.add_argument("-p", "--provider")
parser.add_argument("-r", "--regex")
parser.add_argument("-s", "--secret")
arguments = parser.parse_args()
print(str(arguments))
language = arguments.language
provider = arguments.provider
regex = arguments.regex.replace("\\*", "*")
secret = arguments.secret
if ((language == None) or (provider == None) or (regex == None) or (secret == None)):
    sys.exit()
translator = None
if (provider == "mymemory"):
    translator = Translator(to_lang=language, from_lang="autodetect", provider=provider, email=secret)
else:
    translator = Translator(to_lang=language, from_lang="autodetect", provider=provider, secret_access_key=secret)

for root, folders, files in os.walk(os.getcwd()):
    for name in files:
        if (fnmatch.fnmatch(name, regex)):
            path = os.path.join(root, name)
            descriptor = open(path, "r")
            content = descriptor.read()
            descriptor.close()
            translation = translator.translate(content)
            descriptor = open(path, "w")
            descriptor.write(translation)
            descriptor.close()

