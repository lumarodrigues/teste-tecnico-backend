
# zapsign-backend

Este repositório contém o backend da aplicação Zapsign, que utiliza Django e PostgreSQL para gerenciamento de dados e recursos.

## 🛠️ Tecnologias Utilizadas
- **Django**: Framework para construção da aplicação web.
- **PostgreSQL**: Banco de dados relacional utilizado para armazenar os dados da aplicação.

## 🔧 Pré-requisitos

Antes de rodar o projeto, você precisa ter o Docker e o Docker Compose instalados na sua máquina.

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## 📦 Configuração e Execução

### 1. Clonar o repositório
Clone o repositório para a sua máquina local:

```bash
git clone git@github.com:lumarodrigues/zapsign-backend.git
```

### 2. Criar o banco de dados
Para criar o banco de dados, basta rodar o seguinte comando para acessar o shell do PostgreSQL:

```bash
docker-compose exec db psql -U ${POSTGRES_USER} -d ${POSTGRES_DB}
```

Isso vai te permitir acessar o banco de dados diretamente.

### 3. Configurar as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto (ou renomeie o arquivo `.env-sample` para `.env`):

```bash
cp .env-sample .env
```

Adicione as seguintes variáveis de ambiente ao seu arquivo `.env`:

```env
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_DB=nome_do_banco
COMPANY_NAME=nome_da_empresa
API_TOKEN=seu_api_token
```

### 4. Rodar o Docker Compose

Agora, para subir a aplicação e o banco de dados, execute o comando:

```bash
docker-compose up --build
```

Isso vai iniciar os containers do Django e do PostgreSQL.

Este comando também irá buscar as variáveis de ambiente `COMPANY_NAME` e `API_TOKEN` e criará uma empresa no banco de dados.

## 🚀 Acessando a Aplicação
A aplicação Django estará disponível em [http://localhost:8001/](http://localhost:8001/).  
A API estará acessível em [http://localhost:8001/api/](http://localhost:8001/api/).

## 🔧 Comandos Úteis

- Rodar o servidor de desenvolvimento:

```bash
docker-compose exec web python manage.py runserver 0.0.0.0:8001
```

- Rodar as migrações do banco de dados:

```bash
docker-compose exec web python manage.py migrate
```

- Criar uma empresa via comando personalizado:

```bash
docker-compose exec web python manage.py create_company
```

## 📄 Licença
Este projeto está sob a licença GNU GENERAL PUBLIC LICENSE. Veja o arquivo LICENSE para mais detalhes.