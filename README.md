# Biblioteca
Este é um projeto Django para gerenciar uma biblioteca. O sistema permite cadastrar livros, e categorias.

## Funcionalidades

- **Cadastro de Livros:** Adicione novos livros à biblioteca com informações detalhadas.
- **Categorias:** Organize os livros em diferentes categorias.


## Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd biblioteca
2. **Crie um ambiente virtual**
   ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
4. **Realize as migrações do banco de dados**
   ```bash
    python manage.py migrate
5. **Rode o servidor**
   ```bash
   python manage.py runserver


## Tecnologias Utilizadas
Django: Framework principal para o desenvolvimento web.
SQLite: Banco de dados padrão.
Bootstrap: Usado para estilização da interface.



   

