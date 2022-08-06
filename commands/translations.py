import os
from requests import post
from discord import Message

API_HOST = os.environ.get("SEASIDE_API_HOST")


async def get_translation(language, text):
    print("----------------------------------------------------")
    print(f"Target language: {language}")
    print(f"Translating: {text}")
    print("----------------------------------------------------")
    response = post(f"{API_HOST}/translate", json={"text": text, "target": language})
    return response.json()["data"]


def translate_to_language(language_abbr):
    async def _get_translation(message: Message, arg_string):
        if arg_string.strip() == "":
            return "Please provide some text to translate."

        translation = await get_translation(language_abbr, arg_string)
        return f"{message.author.mention} says: {translation}"

    return _get_translation


translation_commands = {
    "?en": translate_to_language("en"),
    "?ja": translate_to_language("ja"),
    "?es": translate_to_language("es"),
    "?fr": translate_to_language("fr"),
    "?pt": translate_to_language("pt"),
    "?de": translate_to_language("de"),
}
