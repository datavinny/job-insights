# Job Insights

## 📝 Introdução

Este projeto foi feito enquanto estudava na @betrybe.

<img src="/.images/job.png" alt="Logo Aplicação" width="300"/>
  
  Neste projeto você implementei análises a partir de um conjunto de dados sobre empregos. Minhas implementações foram incorporadas a um aplicativo Web desenvolvido com Flask (um framework web muito popular na comunidade Python). Também escrevi testes para a implementação de uma análise de dados.

  Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/) e obtidos através do [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data), uma plataforma disponiblizando conjuntos de dados para cientistas de dados.

<details>
  <summary>
    <strong> :wrench: Técnologias usadas </strong>
  </summary>

Front-end:
  > Desenvolvido usando: Flask
  
Back-end:
  > Desenvolvido usando: Python
 
Tests:
  > Desenvolvido usando: Pytest

</details>

<details>
  <summary>
     <strong> 🎓 Orientações - Rodando o Projeto </strong>
   </summary>

### Desenvolvimento

   <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/test_jobs.py
  ```
  
  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
  ```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).

  <p align="center">
    <img src="/.images/flask-logo.png" alt="Logo Flask" width="200"/>
  </p>

  Além dos testes com o Pytest, você pode (e vai ser bem bacana) rodar a aplicação flask para visualizar no navegador o resultado do desenvolvimento das funções.
  Para isso, digite o comando `flask run`, e acesse o site gerado pelo Flask em `http://localhost:5000`.

  <p align="center">
    <img src="/.images/sistema.png" alt="Tela Aplicação" width="800"/>
  </p>

</details>
 
</details>

## 📌 Credits 
- <p><a href="https://www.linkedin.com/in/davifreitass/">Davi Freitas (back)</a></p>
- Trybe (front)
