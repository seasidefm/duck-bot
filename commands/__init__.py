from .help import help_commands
from .translations import translation_commands

def get_commands():
    return {
        **help_commands,
        **translation_commands
    }