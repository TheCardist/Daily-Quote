import re
import os
import glob

# I have two sections in my notes that have potential quotes
path = r'path/to/section'
path2 = r'path/to/section2'


def get_quotes():
  """Go through all the files in my Vault looking for quotes and then randomly selecting one to send. All quotes are returned back to the main.py to then selection 1 randomly."""
    quotes = []

    for filename in glob.glob(os.path.join(path, '*.md')):
        # Read through all files in folder
        with open(os.path.join(os.getcwd(), filename), 'r', encoding='UTF8') as file:
            for line in file:
                if '[!quote]' in line:
                    author = re.findall(r'\[\[(.*?)]]', line)
                    author = ' '.join(author)

                    # Read the next line to get the quote
                    next_line = next(file)

                    quote = next_line.strip('> ').strip('\n')

                    # Create dictionary to add to list
                    info = {'author': author, 'quote': quote}

                    quotes.append(info)

    for subdir, dirs, files in os.walk(path2):
        for f in files:
            with open(os.path.join(subdir, f), 'r', encoding='UTF8') as file:
                for line in file:
                    if '[!quote]' in line:
                        author = re.findall(r'\[\[(.*?)]]', line)
                        author = ' '.join(author)

                        # Read the next line to get the quote
                        next_line = next(file)

                        quote = next_line.strip('> ').strip('\n')

                        # create dictionary to add to list
                        info = {'author': author, 'quote': quote}

                        quotes.append(info)

    return quotes
