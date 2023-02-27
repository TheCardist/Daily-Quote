import os
import random


def select_note():
  """Process of selecting a note from withint my vault"""

    root_path = r'path/to/vault'
    
    # Randomly selecting the folder within the root, due to how I organize the files
    random_path = random.choice(os.listdir(root_path))
    folder = f'{root_path}/{random_path}'
    
    # Randomly selecting a file to send
    random_file = random.choice(os.listdir(folder))
    new_file = f"{folder}/{random_file}"

    with open(new_file, 'r', encoding='UTF8') as f:
        if 'sharable:' in f.read(): # Sharable tag within the note prevents it from being selected.
            select_note() # Restart process if needed
    return new_file


def read_note():
  """Reading the contents of the file to add into the email."""
    new_file = select_note()
    with open(new_file, 'r', encoding='UTF8') as file:
        for line in file:
            if 'title:' in line:
                title = line.strip('title: ')
                if '# Notes\n' in file:
                    new_note = file.read()
                    new_note = ''.join(new_note)
                    return f'Note Title: {title}\n {new_note}'
                # TODO: Add exception if the note isn't formatted as intended
