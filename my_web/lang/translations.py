from . import en, es, jp, val, cat

translations = {"en": en.texts, "es": es.texts, "jp": jp.texts, "val": val.texts, "cat": cat.texts}

# Devuelve el saludo
def get_greetings(language: str) -> str:
    if language not in translations:
        return ""
    current_texts = translations[language]
    return current_texts["greeting"]
