# API de Supermercado

Bem-vindo à **API de Supermercado**! Esta API foi desenvolvida para gerenciar informações de produtos em um supermercado. Ela oferece funcionalidades para cadastrar, listar, visualizar detalhes, atualizar e excluir produtos.

## Estrutura do Projeto

O projeto está organizado da seguinte maneira:

- `entidades.py`: Contém a definição da classe `Mercado`, que representa um produto no supermercado.
- `models.py`: Define o modelo de dados para a tabela do banco de dados que armazenará os produtos.
- `mercado_schemas.py`: Define os esquemas para serialização e desserialização dos objetos `Mercado`.
- `mercado_services.py`: Contém a lógica de negócio para cadastro, listagem, atualização e exclusão de produtos.
- `mercado_views.py`: Define as visões da API usando Flask-RESTful, incluindo endpoints para interagir com os produtos.
- `__init__.py`: Arquivo de inicialização da aplicação Flask e configurações.
- `run.py`: Arquivo para iniciar a aplicação.
- `config.py`: Configurações da aplicação.

## Configuração

Antes de executar a aplicação, é necessário configurar o banco de dados e outras opções. Edite o arquivo `config.py` com as informações apropriadas.

## Como Executar

Siga os passos abaixo para executar a aplicação:

1. Certifique-se de ter o Python instalado.
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # no Windows: venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a aplicação:
   ```bash
   python run.py
   ```
A aplicação estará disponível em [http://localhost:8080](http://localhost:8080).

## Endpoints

### Listar Todos os Produtos

- **URL:** `/mercado`
- **Método:** `GET`
- **Resposta Sucesso:**
  - **Código:** 200
  - **Conteúdo:**
    ```json
    [{"id": 1, "nome": "Produto1", "preco": 10.0}, {"id": 2, "nome": "Produto2", "preco": 20.0}]
    ```

### Cadastrar um Produto

- **URL:** `/mercado`
- **Método:** `POST`
- **Dados de Entrada:**
  ```json
  {"nome": "Produto3", "preco": 15.0}
  ```
- **Resposta Sucesso:**
  - **Código:** 201
  - **Conteúdo:**
    ```json
    {"id": 3, "nome": "Produto3", "preco": 15.0}
    ```

### Visualizar Detalhes de um Produto

- **URL:** `/mercado/<id>`
- **Método:** `GET`
- **Resposta Sucesso:**
  - **Código:** 200
  - **Conteúdo:**
    ```json
    {"id": 1, "nome": "Produto1", "preco": 10.0}
    ```

### Atualizar um Produto

- **URL:** `/mercado/<id>`
- **Método:** `PUT`
- **Dados de Entrada:**
  ```json
  {"nome": "Produto1Atualizado", "preco": 12.0}
  ```
- **Resposta Sucesso:**
  - **Código:** 200
  - **Conteúdo:**
    ```json
    {"id": 1, "nome": "Produto1Atualizado", "preco": 12.0}
    ```

### Excluir um Produto

- **URL:** `/mercado/<id>`
- **Método:** `DELETE`
- **Resposta Sucesso:**
  - **Código:** 204

## Contribuindo

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos. V

## Licença

**Vamos Juntos! 🚀** Seja bem-vindo(a) ao time da API de Supermercado. Sua colaboração é fundamental para tornarmos essa API cada vez melhor!

---

Lembre-se de substituir as informações genéricas pelos valores específicos da sua aplicação. Se precisar de mais alguma coisa ou quiser alguma modificação, é só avisar!
