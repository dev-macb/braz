import re


def upper(texto: str) -> str:
    """Converte texto para maiusculas."""
    return texto.upper()


def lower(texto: str) -> str:
    """Converte texto para minusculas."""
    return texto.lower()


def title(texto: str) -> str:
    """Converte para title (primeira letra de cada palavra em maiuscula)."""
    return texto.title()


def capitalize(texto: str) -> str:
    """Converte a primeira letra do texto para maiuscula."""
    return texto.capitalize()


def camel_case(texto: str) -> str:
    """Converte texto para camelCase.

    Exemplo: "hello world" -> "helloWorld"
    """
    words = re.split(r"[\s_\-]+", texto)
    return words[0].lower() + "".join(w.capitalize() for w in words[1:])


def pascal_case(texto: str) -> str:
    """Converte texto para PascalCase.

    Exemplo: "hello world" -> "HelloWorld"
    """
    words = re.split(r"[\s_\-]+", texto)
    return "".join(w.capitalize() for w in words)


def snake_case(texto: str) -> str:
    """Converte texto para snake_case.

    Exemplo: "hello world" -> "hello_world"
    """
    words = re.split(r"[\s_\-]+", texto)
    return "_".join(w.lower() for w in words)


def kebab_case(texto: str) -> str:
    """Converte texto para kebab-case.

    Exemplo: "hello world" -> "hello-world"
    """
    words = re.split(r"[\s_\-]+", texto)
    return "-".join(w.lower() for w in words)
