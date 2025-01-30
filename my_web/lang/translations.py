from . import en, es, val

translations_dict = {"en": en.texts, "es": es.texts, "val": val.texts}


# Devuelve el saludo
def get_greetings(language: str) -> str:
    if language not in translations_dict:
        return ""
    current_texts = translations_dict[language]
    return current_texts["greeting"]

# Devuelve el idioma
def get_select_language(language: str) -> str:
    if language not in translations_dict:
        return ""
    current_texts = translations_dict[language]
    return current_texts["select_language"][language]

# Devuelve la traducción del idioma escogido
def get_selected_languages(language: str) -> dict[str]:
    if language not in translations_dict:
        return ""
    current_texts = translations_dict[language]["select_language"]
    return current_texts
