from braz.strings import case


def test_upper():
    assert case.upper("hello") == "HELLO"


def test_lower():
    assert case.lower("HELLO") == "hello"


def test_title():
    assert case.title("hello world") == "Hello World"


def test_capitalize():
    assert case.capitalize("hello") == "Hello"


def test_camel_case():
    assert case.camel_case("hello world") == "helloWorld"


def test_camel_case_com_hifen():
    assert case.camel_case("hello-world") == "helloWorld"


def test_camel_case_com_underscore():
    assert case.camel_case("hello_world") == "helloWorld"


def test_pascal_case():
    assert case.pascal_case("hello world") == "HelloWorld"


def test_snake_case():
    assert case.snake_case("hello world") == "hello_world"


def test_snake_case_com_camel():
    result = case.snake_case("helloWorld")
    # Nota: snake_case nao detecta mudancas de case, apenas separadores
    assert result == "helloworld"


def test_kebab_case():
    assert case.kebab_case("hello world") == "hello-world"


def test_empty_string():
    assert case.upper("") == ""
    assert case.lower("") == ""
    assert case.camel_case("") == ""
