# Spaghetti code, pls ignore

from sys import argv
import json

def formatter(filename):
    with open(f'{filename}.json', 'r', encoding='utf-8') as f:
        original = json.load(f)

        with open(f'{filename}_formatted.json', 'w', encoding='utf-8') as formatted:
            formatted.write('')

        with open(f'{filename}_formatted.json', 'a', encoding='utf-8') as appendfile:
            for key, value in original.items():
                player = {
                    'id': int(value),
                    'name': key
                }
                playerformatted = json.dumps(player, indent=4)
                appendfile.write(playerformatted)
                appendfile.write(',\n')


def main():
    try:
        filename = str(argv[1])
    except IndexError:
        return print('You need to input a file name')
    
    formatter(filename)


main()
