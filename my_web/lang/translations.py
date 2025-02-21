from . import en, es, val

translations_dict = {"en": en.texts, "es": es.texts, "val": val.texts}

# Devuelve el idioma
def get_select_language(language: str) -> str:
    if language not in translations_dict:
        return ""
    current_texts: str = translations_dict[language]
    return current_texts["select_language"][language]


# Devuelve la traducción del idioma escogido
def get_selected_languages(language: str) -> dict[str]:
    if language not in translations_dict:
        return ""
    current_texts: dict[str] = translations_dict[language]["select_language"]
    return current_texts


# Devuelve el texto traducido solicitado
def get_text(language: str, text: str) -> str:
    if language not in translations_dict:
        return ""
    current_texts: str = translations_dict[language]
    return current_texts[text]


# Devuelve la lista de texto traducido solicitado
def get_list_text(language: str, text: str) -> list[str]:
    if language not in translations_dict:
        return ""
    current_texts: list[str] = translations_dict[language]
    return current_texts[text]
