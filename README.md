# 📌 Projeto – Design Patterns: Strategy

Este projeto tem como objetivo demonstrar a aplicação do Design Pattern Strategy, permitindo que o programa execute a busca de CEP utilizando diferentes estratégias de consulta, escolhidas dinamicamente pelo usuário.

---

## 🧩 Requisitos do Projeto

O programa deve:

- Permitir ao usuário informar um **CEP**
- Permitir a escolha da **estratégia** de busca (API) a ser utilizada
- Buscar e exibir as informações do CEP (logradouro, bairro, cidade, estado, etc.)
- Possibilitar a troca da estratégia **sem alterar a lógica principal do programa**

---

## 🔁 Estratégias de Busca (APIs)

O sistema deve implementar pelo menos duas estratégias diferentes para consulta de CEP:

- Brasil API
Endpoint: https://brasilapi.com.br/api/cep/v1/{cep}

- Via CEP
Endpoint: http://viacep.com.br/ws/{cep}/json/

Cada API deve ser encapsulada em uma estratégia concreta, seguindo o padrão Strategy.


## 🚀 Como rodar o projeto

### 📋 Pré-requisitos

Certifique-se de que você possui:

- ✅ Acesso à internet
- ✅ Docker instalado
- ✅ Sistema operacional **Linux**

---

### 🐳 Subindo o container Python

Execute o comando abaixo no terminal para iniciar um container com Python 3.13:

```bash
docker run -it -v "$PWD":/strategy_design_project -w /strategy_design_project python:3.13 bash
```

### 📦 Instalando o Poetry

```bash
pip install poetry
```

### 📥 Instalando as dependências do projeto

```bash
poetry install --no-root
```

### 🔧 Ativando o ambiente virtual

```bash
source $(poetry env info --path)/bin/activate
```

### ▶️ Executando o projeto

```bash
python main.py
```

### 🛠️ Tecnologias utilizadas

- Python 3.13
- Poetry (gerenciamento de dependências)
- Docker
- API Brasil API e Via CEP

### 📄 Observações
- O projeto foi desenvolvido com fins educacionais, focando na aplicação do padrão Strategy.