# 📦 Sistema de Controle de Estoque

Um sistema de controle de estoque desenvolvido em **Python** com **MySQL**, utilizando operações CRUD (Create, Read, Update e Delete).

Este projeto foi desenvolvido com o objetivo de praticar conceitos de programação em Python, manipulação de banco de dados e organização de código em módulos.

---

## 🚀 Tecnologias utilizadas

- Python 3
- MySQL
- MySQL Connector for Python
- Git
- GitHub

---

## 📂 Estrutura do projeto

```
CADASTRO/
│
├── crud.py          # Operações do sistema (CRUD)
├── database.py      # Conexão com o banco de dados
├── main.py          # Menu principal da aplicação
├── README.md
└── .gitignore
```

---

## ⚙️ Funcionalidades

- ✅ Cadastrar produtos
- ✅ Listar todos os produtos
- ✅ Buscar produto por ID
- ✅ Atualizar quantidade
- ✅ Atualizar preço
- ✅ Remover produtos
- ✅ Validação de entradas do usuário
- ✅ Tratamento básico de exceções

---

## 🗄️ Banco de Dados

Tabela utilizada:

```sql
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);
```

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/JacksonJdi/controle-estoque-python.git
```

---

### 2. Entre na pasta

```bash
cd controle-estoque-python
```

---

### 3. Instale a dependência

```bash
pip install mysql-connector-python
```

---

### 4. Configure o banco

Edite o arquivo `database.py` com suas credenciais do MySQL.

Exemplo:

```python
host="localhost"
user="root"
password="SUA_SENHA"
database="estoque"
```

---

### 5. Execute o projeto

```bash
python main.py
```

---

## 📚 Conceitos praticados

- Organização de projetos Python
- Funções
- Estruturas de repetição
- Tratamento de exceções
- Modularização
- MySQL
- CRUD
- SQL parametrizado
- Conexão entre Python e MySQL

---

## 🔒 Segurança

O projeto utiliza consultas parametrizadas (`%s`) para evitar SQL Injection.

Exemplo:

```python
cursor.execute(
    "SELECT * FROM produtos WHERE id = %s",
    (produto_id,)
)
```

---

## 🎯 Próximos passos

Este projeto será evoluído para uma aplicação web utilizando:

- Flask
- HTML
- CSS
- Bootstrap
- Jinja2
- Sistema de Login
- Interface Web
- Dashboard

---

## 👨‍💻 Autor

Desenvolvido por **Jackson Silva** como projeto de estudos em Python e MySQL.