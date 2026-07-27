<h1 align="center">🔷 Braz 🔷</h1>

<p align="center">
    Gerador, validador, cifras, criptografias e manipulação de strings.
</p>

<p align="center">
    <a href="https://badge.fury.io/py/braz" target="_blank">
        <img alt="GitHub stars" src="https://badge.fury.io/py/braz.svg">
    </a>
    <a href="https://codecov.io/gh/dev-macb/braz" target="_blank">
        <img alt="GitHub forks" src="https://codecov.io/gh/dev-macb/braz/branch/main/graph/badge.svg?token=OVQQF4IQY2">
    </a>
    <a href="https://github.com/dev-macb/braz/blob/main/LICENSE" target="_blank">
        <img alt="GitHub license" src="https://img.shields.io/github/license/dev-macb/braz">
    </a>
</p>


---


### 🎯 Objetivo

O Braz é uma aplicação que disponibiliza diversas funcionalidades com o intuito 
de auxiliar os desenvolvedores nos projetos que necessitam da geração de dados 
randômicos válidos dos principais documentos pessoais do Brasil, bem como sua 
validação. Além do mais, o software trata cifras, criptografias, manipulação de 
strings e outras peculiaridades. Com o mínimo de configuração, o Braz pode ser 
utilizado como uma ferramenta de linha de comando para operações simples e 
rápidas ou sendo implementada diretamente no código-fonte como um módulo Python.

<p align="center">🔷</p>



### 🔧 Instalação

Para clonar o projeto para sua máquina via <a target="_blank" href="https://git-scm.com/">git</a>, execute os comandos a seguir:

```bash
# Instalação via CLI (recomendado para uso no terminal)
py -m pipx install braz

# Instalação como pacote Python (para projetos)
pip install braz

# Desenvolvimento local
git clone https://github.com/dev-macb/braz
cd braz
py -m hatch shell
py -m pytest tests/
```



### 🚀 Modo de Uso

#### CLI (Interface de Linha de Comando)

Ajuda e versão:
```bash
braz -v                       # exibe a versão
braz -h                       # exibe a ajuda geral
```

Gerar documentos:
```bash
braz gerar --cpf              # CPF: 52998224725 (cru)
braz gerar --cpf -f           # CPF: 529.982.247-25 (formatado)
braz gerar --cnpj
braz gerar --rg
braz gerar --cnh
braz gerar --pis
braz gerar --titulo
braz gerar --renavam
braz gerar --cep              # CEP: 12345678
braz gerar --cep -f           # CEP: 12345-678
braz gerar --telefone
braz gerar --placa
braz gerar --uuid
braz gerar --senha            # padrão 16 caracteres
braz gerar --senha 32         # tamanho personalizado
```

Validar documentos:
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

Cifrar e decifrar (cifras clássicas):
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

Hash e codificação:
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

Manipular strings:
```bash
braz manipular --maiusculo "texto"
braz manipular --minusculo "TEXTO"
braz manipular --titulo "hello world"
braz manipular --capitalizar "hello"
braz manipular --camel-case "hello world"
braz manipular --pascal-case "hello world"
braz manipular --snake-case "hello world"
braz manipular --kebab-case "hello world"
braz manipular --remover-acentos "cafe"
braz manipular --remover-espacos "a b c"
braz manipular --remover-especiais "hello@world"
braz manipular --apenas-digitos "abc123"
braz manipular --apenas-letras "a1b2c3"
braz manipular --slugificar "Ola Mundo!"
braz manipular --inverter "abc"
braz manipular --contar-caracteres "hello"
braz manipular --contar-palavras "hello world"
braz manipular --truncar 5 "texto longo"
braz manipular --centralizar 10 . "a"
```



#### Pacote Python
Gerar e validar documentos:
```python
from braz.gerar import cpf
from braz.validar import cpf as validar_cpf

numero = cpf.cpf()
print(numero)                          # 52998224725
print(validar_cpf.cpf(numero))         # True

# Com formatação
print(cpf.cpf(formatar=True))           # 529.982.247-25
```

Criptografia e codificação:
```python
from braz.criptografia import sha256, base64

h = sha256.sha256("minha senha")
print(h)                           # 55a5e9e7...

codificado = base64.codificar("Hello")
original = base64.decodificar(codificado)
```

Cifras clássicas:
```python
from braz.cifras import cesar, morse, vigenere

c = cesar.cifrar("HELLO", 3)
d = cesar.decifrar(c, 3)

m = morse.cifrar("SOS")
dm = morse.decifrar(m)
```

Manipulação de strings:
```python
from braz.strings import utils, case

slug = utils.slug("Ola Mundo!")        # ola-mundo
camel = case.camel_case("hello world") # helloWorld
```

<p align="center">🔷</p>



### ✒️ Contribuições
Toda contribuição será bem-vinda! Caso tenha encontrado algum bug, propor uma nova funcionalidade ou conversar sobre o projeto, <a href="https://github.com/dev-macb/braz/issues">Abra uma Issue</a> e descreva seu caso. Se houver uma issue aberta e você deseja resolvê-la, adicionar uma nova funcionalidade ou melhorar a documentação, desenvolva suas adições e me envie um <em>Pull Request</em>. Gostou do projeto e ainda não consegue contribuir com ele? Considere deixar uma ⭐ para o repositório <strong>Braz</strong>. Desde já agradeço pelo interesse em colaborar de alguma forma com o nosso projeto.

<p align="center">🔷</p>



### 📄 Licença

O repositório <strong>Braz</strong> utiliza a <strong>licença MIT</strong> em 
todo seu código, confira suas condições em <a href="https://github.com/dev-macb/braz/blob/main/LICENSE">LICENSE</a>.

<p align="center">🔷</p>
