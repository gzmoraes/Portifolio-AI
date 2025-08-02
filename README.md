# Portifolio-AI

Portifolio-AI é um projeto de portfólio dinâmico que utiliza inteligência artificial para oferecer uma experiência interativa aos visitantes. O sistema conta com um chatbot alimentado por IA, capaz de responder perguntas sobre o portfólio, projetos, habilidades, serviços e informações de contato do desenvolvedor.

## Funcionalidades

- Chatbot inteligente treinado com informações do portfólio
- Respostas personalizadas e profissionais
- Mapeamento de funções para facilitar a navegação (sobre, contato, projetos, serviços, habilidades, redes sociais, feedback)
- Frontend moderno em React com JavaScript (JSX)
- Backend API REST com Flask
- Interface web responsiva e interativa
- Configuração fácil via arquivos `.env` e `aiConfig.md`

## Estrutura do Projeto

```
.
├── client/                    # Frontend React/JavaScript
│   ├── public/
│   │   └── vite.svg
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── main.jsx
│   │   ├── index.css
│   │   └── assets/
│   │       └── react.svg
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── eslint.config.js
├── server/                    # Backend Python/Flask
│   ├── app/
│   │   ├── __init__.py
│   │   └── ai.py
│   ├── main.py
│   ├── createConfig.py
│   ├── aiConfig.md
│   ├── sampleAiConfig.md
│   ├── requirements.txt
│   └── example.env
├── temp/                      # Arquivos temporários
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   └── templates/
│       └── index.html
├── LICENSE
└── README.md
```

## Como rodar o projeto

### Pré-requisitos

- Node.js (versão 18 ou superior)
- Python 3.8 ou superior
- npm ou yarn

### 1. Clone o repositório

```sh
git clone https://github.com/gzmoraes/Portifolio-AI.git
cd Portifolio-AI
```

### 2. Configuração do Backend (Servidor)

```sh
cd server

# Crie e ative o ambiente virtual
python -m venv env
source env/bin/activate  # No Windows: env\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Configure o arquivo .env
cp example.env .env
# Edite o .env e preencha as variáveis necessárias
```

### 3. Configuração do Frontend (Cliente)

```sh
cd ../client

# Instale as dependências
npm install
```

### 4. Execute a aplicação

#### Para desenvolvimento:

**Terminal 1 - Backend:**

```sh
cd server
source env/bin/activate  # Ative o ambiente virtual
python main.py
```

**Terminal 2 - Frontend:**

```sh
cd client
npm run dev
```

#### Para produção:

```sh
# Build do frontend
cd client
npm run build

# Execute apenas o backend (que servirá os arquivos estáticos)
cd ../server
source env/bin/activate
python main.py
```

### 5. Acesse no navegador

- **Desenvolvimento**: Frontend em `http://localhost:5173` e Backend em `http://localhost:8080`
- **Produção**: `http://localhost:8080`

## Configuração de Variáveis de Ambiente

O projeto utiliza variáveis de ambiente para configurações sensíveis como chaves de API. Siga os passos abaixo:

1. **Copie o arquivo de exemplo:**

   ```sh
   cd server
   cp example.env .env
   ```

2. **Edite o arquivo `.env`** e preencha as variáveis necessárias:

   ```env
   # Exemplo de variáveis que podem estar no .env
   AI_API_TOKEN=your_ai_api_token_here
   ```

3. **Importante:**
   - Nunca commite o arquivo `.env` no repositório
   - O arquivo `.env` deve conter informações sensíveis reais
   - Use o `example.env` como referência para as variáveis necessárias

## Personalização

- Edite o arquivo [`server/aiConfig.md`](server/aiConfig.md) para alterar as informações do portfólio e o comportamento do assistente.
- Use o [`server/createConfig.py`](server/createConfig.py) para gerar configurações personalizadas a partir do template [`server/sampleAiConfig.md`](server/sampleAiConfig.md).
- Personalize o frontend React editando os componentes em `client/src/`.

## Tecnologias Utilizadas

### Frontend

- React 19
- JavaScript (JSX)
- Vite
- ESLint

### Backend

- Python 3
- Flask
- GitHub Models API (GPT-4.1)
- python-dotenv

### Outras

- HTML/CSS

## Licença

Este projeto está licenciado sob a [Licença Apache 2.0](LICENSE).

---

Desenvolvido por Gustavo Moraes & Gabriel Tazz
