def class_monk():
    return {
        "name": 'Monge',
        "level": 1,
        "damage": 25,
        "life": 60
    }

def class_warrior():
    return {
        "name": 'Guerreiro',
        "level": 1,
        "damage": 30,
        "life": 50
    }

def class_barbarian():
    return {
        "name": 'Bárbaro',
        "level": 1,
        "damage": 40,
        "life": 35
    }

def classes():
    return [class_monk(), class_warrior(), class_barbarian()]
