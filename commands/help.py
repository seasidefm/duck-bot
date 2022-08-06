HELP_STRING ="""
```
Available commands:
    ?help - Show this help message
    
    Translations:
        ?en - Translate to English
        ?ja - Translate to Japanese
        ?es - Translate to Spanish
        ?fr - Translate to French
        ?pt - Translate to Portuguese
        ?de - Translate to German
```
"""


async def help_command(_, __):
    return HELP_STRING

help_commands = {
    "?h": help_command,
}