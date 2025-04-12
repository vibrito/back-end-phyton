# Back-end

**Desenvolvimento Full Stack Básico**<br />
<br />
*Pontifícia Universidade Católica do Rio de Janeiro*<br />
<br />
*Back-end do trabalho do curso de Engenharia de Software*<br />
<br />
*Aluno: Vinicius do Carmo Brito*<br />
<br />
---

<br />
# 🥂 API de Drinks - Flask + Swagger
<br />
Esta é uma API RESTful feita com Flask, que permite gerenciar um menu de drinks. A documentação da API é gerada automaticamente com Swagger usando o Flask-RESTX.
<br />

<br />
## Tecnologias utilizadas
<br />
- Python 3.10+
- Flask
- Flask-RESTX (Swagger)
- Flask-CORS
- Flask-SQLAlchemy
- SQLite (banco local)
<br />

<br />
## Ferramentas usadas:<br />
PyCharm<br />
Postman<br />
Safari<br />
Medium e Stackoverflow para consulta<br />
<br />

<br />
## Como executar<br />
<br />
Primeiro precisamos instalar o pyenv
https://github.com/pyenv/pyenv
<br />
No link acima, exitem as instruções para cada sistema operacional.
<br />
Após a instalação com sucesso, precisa criar um ambiente virtual para rodar o python e suas dependências em versões específicas:
<br />
pyenv install 3.12.3 -> instala o python na versão 3.12.3
<br />
pyenv local 3.12.3   -> seta a versão que a aplicação deve usar
<br />
python3 -m venv .venv -> cria o ambiente virtual, ou seja, as dependências serão instaladas dentro do diretório .venv ao invés de instalar no diretório do pip no sistema operacional
<br />
source .venv/bin/activate -> ativa o ambiente virtual
<br />
python app.py -> roda a aplicação<br />
<br />
OU 
<br />
Para instalar as dependencias com o comando: pip install -r requirements.txt <br />
Execute o arquivo app.py em uma IDE como o PyCharm <br />

