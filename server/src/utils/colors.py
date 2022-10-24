_colors_map = {
    'purple': '\033[95m',
    'blue': '\033[94m',
    'cyan': '\033[96m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'end': '\033[0m',
    'bold': '\033[1m',
    'underline': '\033[4m'
}

def wrap(color, message):
    return _colors_map[color] + str(message) + _colors_map['end']
