# braz

Biblioteca e CLI para geracao, validacao, criptografia, cifras classicas e
manipulacao de strings voltada para desenvolvedores, testadores e profissionais
de seguranca.

## Instalacao

```bash
pip install braz
```

## Uso (CLI)

### Gerar documentos

```bash
braz gerar --cpf
braz gerar --cnpj
braz gerar --rg
braz gerar --cnh
braz gerar --pis
braz gerar --titulo
braz gerar --renavam
braz gerar --cep
braz gerar --telefone
braz gerar --placa
braz gerar --uuid
braz gerar --senha       # padrao 16 caracteres
braz gerar --senha 32    # tamanho personalizado
```

### Validar documentos

```bash
braz validar --cpf 52998224725
braz validar --cnpj 11222333000181
braz validar --rg 123456789
braz validar --cnh 12345678901
braz validar --pis 12345678901
braz validar --cep 12345-678
braz validar --email usuario@exemplo.com
braz validar --telefone "(11) 91234-5678"
```

### Cifrar e decifrar (cifras classicas)

```bash
braz cifrar --cesar 3 "HELLO"
braz cifrar --rot13 "HELLO"
braz cifrar --binario "Hello"
braz cifrar --morse "SOS"
braz cifrar --vigenere CHAVE "TEXTO"
braz cifrar --atbash "HELLO"
braz cifrar --xor CHAVE "TEXTO"

braz decifrar --cesar 3 "KHOOR"
braz decifrar --morse "... --- ..."
braz decifrar --vigenere CHAVE "HIJKY"
```

### Hash e codificacao

```bash
braz criptar --md5 "senha"
braz criptar --sha1 "senha"
braz criptar --sha256 "senha"
braz criptar --sha512 "senha"
braz criptar --sha3 "senha"
braz criptar --blake2 "senha"
braz criptar --bcrypt "senha"
braz criptar --base64 "Hello"
braz criptar --url "hello world"
braz criptar --hex "Hello"

braz decriptar --base64 SGVsbG8=
braz decriptar --url hello%20world
braz decriptar --hex 48656c6c6f
```

### Manipular strings

```bash
braz manipular --upper "texto"
braz manipular --lower "TEXTO"
braz manipular --title "hello world"
braz manipular --capitalize "hello"
braz manipular --camel-case "hello world"
braz manipular --pascal-case "hello world"
braz manipular --snake-case "hello world"
braz manipular --kebab-case "hello world"
braz manipular --remove-accents "cafe"
braz manipular --remove-spaces "a b c"
braz manipular --remove-special-chars "hello@world"
braz manipular --only-digits "abc123"
braz manipular --only-letters "a1b2c3"
braz manipular --slug "Ola Mundo!"
braz manipular --reverse "abc"
braz manipular --count-chars "hello"
braz manipular --count-words "hello world"
braz manipular --truncate 5 "texto longo"
braz manipular --pad 10 . "a"
```

## Uso (Python)

```python
from braz.gerar import cpf
from braz.validar import cpf as validar_cpf

numero = cpf.cpf()
print(numero)                      # 52998224725
print(validar_cpf.cpf(numero))     # True
```

```python
from braz.criptografia import sha256, base64

h = sha256.sha256("minha senha")
print(h)                           # 55a5e9e7...

codificado = base64.encode("Hello")
original = base64.decode(codificado)
```

```python
from braz.cifras import cesar, morse, vigenere

c = cesar.encrypt("HELLO", 3)
d = cesar.decrypt(c, 3)

m = morse.encrypt("SOS")
dm = morse.decrypt(m)
```

```python
from braz.strings import utils, case

slug = utils.slug("Ola Mundo!")        # ola-mundo
camel = case.camel_case("hello world") # helloWorld
```

## Desenvolvimento

```bash
git clone https://github.com/macb/braz
cd braz

# ambiente virtual com hatch
python -m hatch shell

# rodar testes
python -m pytest -v

# lint e format
ruff check src/ tests/
ruff format src/ tests/
```

## Modulos

| Comando | Descricao |
|---------|-----------|
| `gerar` | Geracao de documentos brasileiros validos (CPF, CNPJ, RG, CNH, PIS, Titulo, RENAVAM, CEP, Telefone, Placa, UUID, Senha) |
| `validar` | Validacao de documentos (CPF, CNPJ, RG, CNH, PIS, CEP, Email, Telefone) |
| `cifrar` / `decifrar` | Cifras classicas (Cesar, ROT13, Binario, Morse, Vigenere, Atbash, XOR) |
| `criptar` / `decriptar` | Hash e codificacao (MD5, SHA1/224/256/384/512, SHA3, BLAKE2, bcrypt, Base64, URL, Hex) |
| `manipular` | Manipulacao de strings (case, limpeza, slug, reverse, count, truncate, pad, replace) |

## Licenca

MIT 
