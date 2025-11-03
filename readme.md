## API Tasks

- Esta API RESTFULL foi desenvolvida para montar um gerenciador de tarefas na linguagem Python com o framework Flask permitindo ler várias ou uma tarefa em específico, salvar uma tarefa, atualizar informações como status da tarefa e deletar uma tarefa tendo que confirmar a remoção.


## Funcionalidades

- **GET /**: Retorna a lista de tarefas armazenada no banco.
- **GET /:sigla**: Retorna as informações de uma tarefa específica, identificado pelo id dela
- **POST /**: Adiciona uma nova tarefa à lista armazenada no banco.
- **PUT /:sigla**: Atualiza as informações de uma tarefa específica, identificado pelo id.
- **DELETE /:sigla**: Remove uma tarefa pelo identificador dela tendo que confirmar a remoção

## Estrutura do Projeto

- **app.py**: Arquivo principal que configura o servidor Flask e as rotas da API
- **db.js**: Arquivo que contém o módulo do banco SQLite integrado com o Flask
- **tasks_models.js**: Contém a entidade que será criada no banco para armazenar tarefas
- **tasks_routes.js**: Contém todos os roteadores da aplicação
- **tasks_controllers.js**: Contém todos os handlers que irá executar uma ação que será executada em uma rota de api
- **tasks.db**: Contém o banco de dados SQLite em memória, podendo visualizar tudo que está armazenado nele relacionado as tarefas

## Endpoints

### 1. **GET /**

Retorna a lista completa de tarefas disponíveis armazenadas.

`GET http://127.0.0.1:5000/tasks`

#### Exemplo de Resposta:

```json
{
    "message": "All tasks retrieved successfully.",
    "data": [
        {
            "id": 1,
            "title": "Assistir a luta entre Jhony x Xamuel",
            "description": "Esta luta de MMA acontecerá no FIGHT Music Show 7",
            "status": "COMPLETED"
        },
        {
            "id": 2,
            "title": "Assistir a luta entre Jhony x Xamuel",
            "description": "Esta luta de MMA acontecerá no FIGHT Music Show 7",
            "status": "PENDING"
        },
        {
            "id": 3,
            "title": "Acompanhar o jogo da final da libertadores de Palmeiras x Flamengo",
            "description": "Na libertadores de 2025, os 2 clubes finalistas que irão se enfrentar em Lima dia 29/11 serão os 2 clubes brasileiros Palmeiras x Flamengo, 2 clubes que se tornaram as 2 maiores potências da américa e no Brasil.",
            "status": "PENDING"
        },
        {
            "id": 4,
            "title": "Acompanhar a semifinal entre Cruzeiro x Corinthians",
            "description": "Na copa do brasil de 2025, já está embargado as semifinais para definir os finalista da copa. Cruzeiro x Corinthians irão se enfrentar dia 12/12 com o jogo de ida na arena MRV e o jogo de volta na Neo Química Arena.",
            "status": "PENDING"
        }
    ]
}
```
### 2. **GET /:sigla**

Retorna as informações de uma taeraf específica, identificado pelo id.

### Exemplo de Requisição:

`GET http://127.0.0.1:5000/task/1`

### Exemplo de Resposta:

```json
{
    "message": "Task founded with success!!",
    "data": {
        "id": 1,
        "title": "Assistir a luta entre Jhony x Xamuel",
        "description": "Esta luta de MMA acontecerá no FIGHT Music Show 7",
        "status": "COMPLETED"
    }
}
```
### 3. **POST /**

Armazenar uma nova tarefa.

#### Exemplo de Requisição:

`POST http://127.0.0.1:5000/post_task`

**Content-Type:** application/json

```json
{
  "title": "Acompanhar a semifinal entre Cruzeiro x Corinthians",
  "status": "PENDING",
  "description": "Na copa do brasil de 2025, já está embargado as semifinais para definir os finalista da copa. Cruzeiro x Corinthians irão se enfrentar dia 12/12 com o jogo de ida na arena MRV e o jogo de volta na Neo Química Arena."
}
```

#### Exemplo de Resposta:

```json
{"message": "Tasks created with success!!.", "data": {"id": 4, "title": "Acompanhar a semifinal entre Cruzeiro x Corinthians", "description": "Na copa do brasil de 2025, já está embargado as semifinais para definir os finalista da copa. Cruzeiro x Corinthians irão se enfrentar dia 12/12 com o jogo de ida na arena MRV e o jogo de volta na Neo Química Arena.", "status": "PENDING"}}
```

### 4. **PUT /:sigla**

Atualiza as informações de uma tarefa específica pelo identificador.

#### Exemplo de Requisição:

`PUT http://127.0.0.1:5000/put_task/2`

**Content-Type:** application/json

```json
{
  "title": "Assistir a luta entre Jhony x Xamuel",
  "status": "COMPLETED",
  "description": "Esta luta de MMA acontecerá no FIGHT Music Show 7"
}
```

#### Exemplo de resposta:

```json
{
    "message": "Tasks updated with success!!.",
    "data": {
        "id": 2,
        "title": "Assistir a luta entre Jhony x Xamuel",
        "description": "Esta luta de MMA acontecerá no FIGHT Music Show 7",
        "status": "COMPLETED"
    }
}
```

### 5. **DELETE /:sigla**

Remove uma tarefa específica pelo identificador e necessidade de confirmação.

#### Exemplo de Requisição:

`DELETE http://127.0.0.1:5000/delete_task/1`
`confirmation=true`

#### Exemplo de Resposta:

```json
{
    "mensagem": "Task successfully deleted!!"
}
```

## Como Rodar o Projeto

1. **Clone este repositório:**

  ```bash
  git clone https://github.com/seu-usuario/nome-do-repositorio.git
  ```

2. **Instale as dependências:**

  Navegue até o diretório do projeto e execute o comando:

  ```bash
  npm install
  ```
3. **Inicie o servidor**
  Após a instalação das dependências, inicie o servidor:

  ```bash
  node ./app.js
  ```
4. **Acesse a API**

A API está disponível em [http://localhost:3000]

## Validações 

Os dados enviados para API são validados com **Joi** para garantir que todos os campos sejam fornecidos corretamente. As validações incluem:

- O nome do carro deve ter pelo menos 3 caracteres.
- A Sigla deve ter exatamente 3 caracteres.
- A potência, velocidade máxima, consumo, aceleração e preço devem ser números válidos.
- Durante a atualização, pelo menos um campo precisa ser fornecido.

Dicas:
https://dillinger.io/ - Para ler a formatação na Web, antes de subir no Git
https://readme.so/pt/editor - Para fazer "Automatico" somente editando

## Autor

Desenvolvido por João Victor Bondaczuk Sousa 2 ano B 