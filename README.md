<div id="título" align="center">
    <img width="400px" alt="Braz - Gerador & Validador" src="https://raw.githubusercontent.com/dev-macb/braz/master/.github/assets/images/logo-nome.png"/>
</div>


<details>
    <summary>📌 Informações do Projeto</summary>
    <div id="metadados" align="center">
        <sup>Metadados</sup>
        <br/>
        <a href="https://pypi.org/project/braz/">
            <img alt="Versão no PyPI" src="https://img.shields.io/pypi/v/braz?label=PyPI&color=blue">
        </a>
        <a href="https://pepy.tech/project/braz">
            <img alt="Total de Downloads" src="https://static.pepy.tech/personalized-badge/braz?period=month&units=international_system&left_color=grey&right_color=blue&left_text=Downloads" />
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
            <img alt="Status do PyPI" src="https://img.shields.io/pypi/status/braz?label=PyPI%20Status">
        </a>
        <a href='https://braz.readthedocs.io/pt_BR/latest/?badge=latest'>
            <img alt='Status da Documentação' src='https://readthedocs.org/projects/braz/badge/?version=latest'/>
        </a>
        <a href="https://github.com/dev-macb/braz/actions/workflows/testes.yml">
            <img alt="Status dos Testes" src="https://github.com/dev-macb/braz/workflows/Tests/badge.svg" />
        </a>
    </div>
</details>


<details>
    <summary>📌 Índice</summary>
    <ul id="lista-índice">
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

<h2 id="objetivo">🎯 Objetivo</h2>
<p>
    O <strong>Braz</strong> é uma aplicação que disponibiliza diversas funcionalidades com o intuito de auxiliar os desenvolvedores nos projetos que necessitam da geração de dados randômicos válidos dos principais documentos pessoais do Brasil, bem como sua validação. Além do mais, o software trata cifras, criptografias, manipulação de strings e outras peculiaridades. Com o mínimo de configuração, o Braz pode ser utilizado como uma ferramenta de linha de comando para operações simples e rápidas ou sendo implementada diretamente no código-fonte como um módulo Python. 
</p>
<p align="center">🔷</p>


<h2 id="instalação">🔧 Instalação</h2>
<p>
    Para instalar o pacote braz, certifique-se de que tenha <a target="_blank" href="https://www.python.org/downloads/">Python</a> e o gerenciador de pacotes <a target="_blank" href="https://pypi.org/project/pip/">pip</a> instalados em seu ambiente.
    Instale executando o seguinde comando:
</p>

```bash
$ pip install braz
``` 
<p>
    Para clonar o projeto para sua máquina via <a target="_blank" href="https://git-scm.com/">git</a>, execute os comandos a seguir:
</p>
    
```bash
$ mkdir braz && cd braz
$ git clone https://github.com/dev-macb/braz
$ pip install -r requirements.txt
``` 
<p>
    Caso deseja utilizar o braz como uma <strong>CLI</strong> nativa no seu terminal, baixe a <a href="#">última <em>release</em></a> do projeto e execute o arquivo <code>instalador_cli.py</code> para reazlizar a configuração e a instalação da <em>cli</em> em sua máquina. Para verificar se está funcionando corretamente execute os passos da demonstração abaixo. Caso não funcione corretamente acesse a <a target="_blank" href="#">documentação</a> do braz para mais informações.
</p>
<p align="center">🔷</p>


<h2 id="funcionalidades">⚙️ Funcionalidades</h2>
<p>
    O <strong>Braz CLI</strong> disponibiliza geradores, validadores, cifradores, decifradores, criptografador, descriptografador e manipulador de strings usando comandos no shell via linha de comando. As operações da <em>cli</em> são realizadas através das funções do módulo <code>braz</code> que pode ser implementado em códigos Python. As classes da <em>lib</em> são:
    <ul>
        <li><code>braz.gerar</code> O módulo que contém as funções de geração de dados aleatoriamente.</li>
        <li><code>braz.validar</code> O módulo que contém as funções de validação de dados.</li>
        <li><code>braz.cifrar</code> O módulo que contém as funções de cifragem de mensagens.</li>
        <li><code>braz.decifrar</code> O módulo que contém as funções de decifragem de mensagens.</li>
        <li><code>braz.criptografar</code> O módulo que contém as funções de criptografia de mensagens.</li>
        <li><code>braz.descriptografar</code> O módulo que contém as funções de descriptografia de mensagens.</li>
        <li><code>braz.manipular</code> O módulo que contém as funções de manipulação de strings.</li>
    </ul>
    <blockquote>
        Neste documento há apenas uma abresentação breve das funcionalidades do pacote. Para visualizar a documentação oficial com todas as funções e informações adicionais do módulo clique <a target="_blank" href="https://braz.readthedocs.io/pt_BR/latest/?badge=latest">aqui</a>.
    </blockquote>
</p>
<p align="center">🔷</p>


<h2 id="demonstração">💻 Demonstração</h2>
<div align="center">
    <img src=".github/assets/images/logo.png" alt="Demonstração do Braz no Python IDLE" width="300px"/>
    <br/>
    <img src=".github/assets/images/logo.png" alt="Demostração do Braz CLI" width="300px"/>
</div>
<p align="center">🔷</p>


<h2 id="contribuições">✒️ Contribuições</h2>
<p>
    Toda contribuição será bem-vinda!🎉 Caso tenha encontrado algum bug, propor uma nova funcionalidade ou conversar sobre o projeto <a href="https://github.com/dev-macb/braz/issues">Abra uma Issue</a> e descreva seu caso. Se houver uma issue aberta e você deseja resolve-la, adicionar uma nova funcionalidade ou melhorar a documentação, desenvolva suas adições e me envie um <em>Pull Request</em>. Gostou do projeto e ainda não consegue contribuir com ele? Considere deixar uma ⭐ para o <strong>Braz</strong>. Desde já agradeço pelo interesse em colaborar de alguma forma com o nosso projeto. Para obter maiores informações sobre as contribuições do projeto, acesse o documento <a href="">CONTRIBUTING</a>.
</p>
<p align="center">🔷</p>


<h2 id="aviso-legal">📜 Aviso Legal</h2>
<p>
    Os dados gerados pelo braz tem por finalidade auxiliar estudantes, programadores, analistas, testadores e hackers no desenvolvimento de softewares que necessitam de dados gerados de forma randômica, respeitando regras/cálculo de criação de cada tipo de dado dos principais documentos pessoais do Brasil. Todo e qualquer risco da utilização dos dados disponibilizados através do módulo e da cli é assumido pelo próprio usuário. Nesse sentido, <strong>NÃO</strong> devem ser considerados completos, atualizados, e não se destinam a ser utilizado no lugar de uma consulta jurídica, médica, financeira, ou de qualquer outro profissional.
</p>
<p align="center">🔷</p>


<h2 id="licença">📄 Licença</h2>
<p>
    O Braz utiliza a <strong>licença MIT</strong> em todo seu código, confira suas condições em <a href="https://github.com/dev-macb/braz/blob/dev/LICENSE.md">LICENSE</a>.
</p>
<p align="center">🔷</p>
