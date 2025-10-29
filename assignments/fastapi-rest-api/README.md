# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Nesta tarefa, você irá aprender a construir uma API REST moderna usando o framework FastAPI do Python. Você desenvolverá uma API para um sistema de gerenciamento de biblioteca, aplicando conceitos fundamentais de APIs REST e aproveitando os recursos poderosos do FastAPI.

## 📝 Tasks

### 🛠️ Task 1: Configuração do Ambiente e Endpoints Básicos

#### Description
Configure o ambiente de desenvolvimento e crie os endpoints básicos para o sistema de biblioteca.

#### Requirements
O programa completo deve:

- Configurar um ambiente virtual Python e instalar o FastAPI e suas dependências
- Criar um servidor básico FastAPI que rode na porta 8000
- Implementar endpoints GET e POST para gerenciar livros:
  - GET /books: Retorna lista de todos os livros
  - GET /books/{book_id}: Retorna detalhes de um livro específico
  - POST /books: Adiciona um novo livro ao sistema

### 🛠️ Task 2: Modelos de Dados e Validação

#### Description
Defina modelos Pydantic para os dados e implemente validação de dados.

#### Requirements
O programa completo deve:

- Criar um modelo Pydantic para a entidade Book com os campos:
  - id: UUID
  - title: str
  - author: str
  - year: int
  - available: bool
- Implementar validação de dados usando Pydantic
- Adicionar documentação automática usando docstrings do FastAPI

### 🛠️ Task 3: Operações CRUD Completas

#### Description
Complete a API implementando as operações restantes do CRUD.

#### Requirements
O programa completo deve:

- Implementar os seguintes endpoints adicionais:
  - PUT /books/{book_id}: Atualiza informações de um livro
  - DELETE /books/{book_id}: Remove um livro do sistema
- Adicionar tratamento de erros adequado
- Implementar respostas HTTP apropriadas com códigos de status corretos