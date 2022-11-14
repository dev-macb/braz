<div id="título" align="center">
    <img width="400px" alt="Braz - Gerador & Validador" src="https://raw.githubusercontent.com/dev-macb/braz/master/.github/assets/images/logo-nome.png"/>
</div>


---


<details>
    <summary>📌 Informações do Projeto</summary>
    <div id="metadados" align="center">
        <sup>Metadados</sup>
        <br/>
        <a href="https://pypi.org/project/braz/">
            <img alt="PyPI" src="https://img.shields.io/pypi/v/braz?label=PyPI&color=blue">
        </a>
        <a href="https://pypi.org/project/braz/">
            <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/braz?color=blue&label=Downloads">
        </a>
        <a href="https://github.com/dev-macb/braz/blob/main/LICENSE">
            <img alt="Licença do Projeto" src="https://img.shields.io/github/license/dev-macb/braz?color=blue&label=License">
        </a>
        <a href="#">
            <img alt="Estrelas do Repositório" src="https://img.shields.io/github/stars/dev-macb/braz?color=blue&label=Stars">
        </a>
    </div>
    <div id="status" align="center">
        <sup>Status</sup>
        <br/>
        <a href="https://pypi.org/project/braz/">
            <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/braz" />
        </a>
        <a href="https://fordev.readthedocs.io/pt_BR/latest/?badge=latest">
            <img alt="Documentation Status" src="https://readthedocs.org/projects/braz/badge/?version=latest" />
        </a>
        <a href="https://github.com/dev-macb/braz/actions/workflows/testes.yml">
            <img alt="Test Status" src="https://github.com/matheusfelipeog/fordev/workflows/Tests/badge.svg" />
        </a>
    </div>
</details>


<details>
    <summary>📌 Índice</summary>
    <ul id="lista-índice" align="left">
        <li><a href="#objetivo">Objetivo</a></li>
        <li><a href="#instalação">Instalação</a></li>
        <li><a href="#demonstração">Demonstração</a></li>
        <li><a href="#funcionalidades">Funcionalidades</a></li>
        <li><a href="#contribuições">Contribuições</a></li>
        <li><a href="#aviso-legal">Aviso Legal</a></li>
        <li><a href="#licença">Licença</a></li>
    </ul>
</details>


---


<h2 id="objetivo" align="left">🎯 Objetivo</h2>
<p id="txt-contribuições" align="left">
    O <strong>Braz</strong> é uma aplicação que disponibiliza diversas funcionalidades com o intuito de auxiliar os desenvolvedores nos projetos que necessitam da geração de dados randômicos válidos dos principais documentos pessoais do Brasil, bem como sua validação. Além do mais, o software trata cifras, criptografias, manipulação de strings e outras peculiaridades. Com o mínimo de configuração, o Braz pode ser utilizado como uma ferramenta de linha de comando para operações simples e rápidas ou sendo implementada diretamente no código-fonte como um módulo Python. 
</p>
<h3 id="divisor" align="center">🔷</h3>


<h2 id="instalação" align="left">🔧 Instalação</h2>
<p id="txt-instalação-pip" align="left">
    Para instalar o pacote braz, certifique-se de que tenha <a href="https://www.python.org/downloads/">Python</a> e o gerenciador de pacotes <a href="https://pypi.org/project/pip/">pip</a> instalados em seu ambiente.
    Instale executando o seguinde comando:
</p>

```shell
$ pip install braz
``` 

<p id="txt-instalação-clone" align="left">
    Para clonar o projeto para sua máquina via <a href="https://git-scm.com/">git</a>, execute os comandos a seguir:
</p>
    
```shell
$ mkdir braz && cd braz
$ git clone https://github.com/dev-macb/braz
$ pip install -r requirements.txt
``` 

<p id="txt-instalação-cli" align="left">
    Caso deseja utilizar o braz como uma <strong>CLI</strong> nativa no seu terminal, baixe a <a href="#">última <em>release</em></a> do projeto e execute o arquivo <code>instalador_cli.py</code> para reazlizar a configuração e a instalação da <em>cli</em> em sua máquina. Para verificar se está funcionando corretamente execute os passos da demonstração abaixo. Caso não funcione corretamente acesse a <a href="#">documentação</a> do braz para mais informações.
</p>
<h3 id="divisor" align="center">🔷</h3>


<h2 id="funcionalidades" align="left">⚙️ Funcionalidades</h2>
<p id="txt-funcionalidades" align="left">
    O <strong>Braz CLI</strong> disponibiliza geradores, validadores, cifradores, decifradores, criptografador, descriptografador e manipulador de strings usando comandos no shell via linha de comando. As operações da <em>cli</em> são realizadas através das funções do módulo <code>braz</code> que pode ser implementado em códigos Python. As classes da <em>lib</em> são:
    <ul id="lista-modulos-pacote" align="left">
        <li><code>braz.gerar</code> O módulo que contém as funções de geração de dados aleatoriamente.</li>
        <li><code>braz.validar</code> O módulo que contém as funções de validação de dados.</li>
        <li><code>braz.cifrar</code> O módulo que contém as funções de cifragem de mensagens.</li>
        <li><code>braz.decifrar</code> O módulo que contém as funções de decifragem de mensagens.</li>
        <li><code>braz.criptografar</code> O módulo que contém as funções de criptografia de mensagens.</li>
        <li><code>braz.descriptografar</code> O módulo que contém as funções de descriptografia de mensagens.</li>
        <li><code>braz.manipular</code> O módulo que contém as funções de manipulação de strings.</li>
    </ul>
    <blockquote>
        Neste documento há apenas uma abresentação breve das funcionalidades do pacote. Para visualizar a documentação oficial com todas as funções e informações adicionais do módulo clique <a href="">aqui</a>.
    </blockquote>
</p>
<h3 id="divisor" align="center">🔷</h3>


<h2 id="demonstração" align="left">💻 Demonstração</h2>
<div id="demonstrações" align="center">
    <img src=".github/assets/images/logo.png" alt="Demonstração do Braz no Python IDLE" width="400px"/>
    <br/>
    <img src=".github/assets/images/logo.png" alt="Demostração do Braz CLI" width="400px"/>
</div>
<h3 id="divisor" align="center">🔷</h3>


<h2 id="contribuições" align="left">✒️ Contribuições</h2>
<p id="txt-contribuições" align="left">
    Toda contribuição será bem-vinda! Caso tenha encontrado algum bug, propor uma nova funcionalidade ou conversar sobre o projeto <a href="https://github.com/dev-macb/braz/issues">Abra uma Issue</a> e descreva seu caso. Se houver uma issue aberta e você deseja resolve-la, adicionar uma nova funcionalidade ou melhorar a documentação, desenvolva suas adições e me envie um <em>Pull Request</em>. Gostou do projeto e ainda não consegue contribuir com ele? Considere deixar uma ⭐ para o <strong>braz</strong>. Desde já agradeço pelo interesse em colaborar de alguma forma com o nosso projeto.
</p>
<h3 id="divisor" align="center">🔷</h3>


<h2 id="aviso-legal" align="left">📜 Aviso Legal</h2>
<p id="txt-aviso-legal" align="left">
    Os dados gerados pelo braz tem por finalidade auxiliar estudantes, programadores, analistas, testadores e hackers no desenvolvimento de softewares que necessitam de dados gerados de forma randômica, respeitando regras/cálculo de criação de cada tipo de dado dos principais documentos pessoais do Brasil. Todo e qualquer risco da utilização dos dados disponibilizados através do módulo e da cli é assumido pelo próprio usuário. Nesse sentido, <strong>NÃO</strong> devem ser considerados completos, atualizados, e não se destinam a ser utilizado no lugar de uma consulta jurídica, médica, financeira, ou de qualquer outro profissional.
</p>
<h3 id="divisor" align="center">🔷</h3>


<h2 id="licença" align="left">📄 Licença</h2>
<p id="txt-licença" align="left">
    O braz utiliza a <strong>licença MIT</strong> em todo seu código, confira suas condições em <a href="https://github.com/dev-macb/braz/blob/main/LICENSE">MIT License</a>.
</p>
