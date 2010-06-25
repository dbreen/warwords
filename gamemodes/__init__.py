
class InvalidGameModeException(Exception):
    pass

_game_modes = {}

def register_game_mode(name):
    try:
        module = __import__('gamemodes.%s' % name, globals(), locals(), name)
    except ImportError:
        raise InvalidGameModeException('Could not load game mode: %s' % name)
    _game_modes[name] = getattr(module, "%sGameMode" % name.capitalize())

def get_game_mode(name):
    return _game_modes[name]()

register_game_mode('standard')
