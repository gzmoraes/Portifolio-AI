# Portifolio-AI

Portifolio-AI é um projeto de portfólio dinâmico que utiliza inteligência artificial para oferecer uma experiência interativa aos visitantes. O sistema integra um chatbot inteligente alimentado por modelos GPT-4 da OpenAI via GitHub Models API, capaz de responder perguntas sobre o portfólio, projetos, habilidades, serviços e informações de contato do desenvolvedor.

## Funcionalidades

- **Chatbot Inteligente**: Utiliza múltiplos modelos GPT-4 (4.1, 4.1-mini, 4.1-nano, 4o, 4o-mini) com fallback automático
- **Respostas Contextuais**: Sistema de tools/functions que categoriza automaticamente as consultas do usuário
- **Múltiplas Categorias**: Mapeamento inteligente para navegação (sobre, contato, projetos, serviços, habilidades, redes sociais, feedback)
- **Frontend Moderno**: React 19 com Vite para desenvolvimento rápido
- **Backend Robusto**: API REST com Flask e tratamento de erros avançado
- **Interface Responsiva**: Design web adaptável para diferentes dispositivos
- **Configuração Flexível**: Personalização via arquivos `.env` e `aiConfig.md`
- **Sistema de Memória**: Mantém contexto da conversa durante a sessão
- **Rate Limit Handling**: Troca automática entre modelos quando limites são atingidos

## Arquitetura do Sistema

### Backend (Python/Flask)

- **AIBot Class**: Classe principal que herda de OpenAI e gerencia as interações com a API
- **Sistema de Tools**: Função calling para categorização automática das consultas
- **Fallback de Modelos**: Troca automática entre diferentes modelos GPT-4 em caso de rate limit
- **Tratamento de Erros**: Gestão robusta de erros de autenticação, rate limit e bad requests
- **Sistema de Memória**: Armazena histórico da conversa para manter contexto

### Frontend (React/Vite)

- **Componentes Modernos**: Utiliza React 19 com hooks e componentes funcionais
- **Build Otimizado**: Vite para desenvolvimento rápido e builds eficientes
- **Linting**: ESLint configurado para manter qualidade do código

### API Integration

- **GitHub Models API**: Acesso aos modelos GPT-4 através da infraestrutura do GitHub
- **CORS Habilitado**: Permite requisições cross-origin para desenvolvimento
- **JSON REST API**: Endpoint `/prompt` para comunicação cliente-servidor

## Estrutura do Projeto

```
Portifolio-AI/
├── client/                           # Frontend React
│   ├── public/
│   │   └── vite.svg                 # Ícone do Vite
│   ├── src/
│   │   ├── App.jsx                  # Componente principal
│   │   ├── App.css                  # Estilos principais
│   │   ├── main.jsx                 # Ponto de entrada React
│   │   ├── index.css                # Estilos globais
│   │   └── assets/
│   │       └── react.svg            # Logo React
│   ├── index.html                   # Template HTML
│   ├── package.json                 # Dependências Node.js
│   ├── vite.config.js              # Configuração Vite
│   └── eslint.config.js            # Configuração ESLint
├── server/                          # Backend Python
│   ├── env/                        # Ambiente virtual Python
│   ├── app/
│   │   ├── __init__.py             # Configuração Flask e rotas
│   │   └── ai.py                   # Classe AIBot e lógica principal
│   ├── test/                       # Arquivos de teste
│   │   ├── test.py
│   │   └── backup.py
│   ├── main.py                     # Ponto de entrada do servidor
│   ├── createConfig.py             # Script para criar configurações
│   ├── functions_schema.py         # Schema das funções AI
│   ├── functions.py                # Implementação das funções
│   ├── aiConfig.md                 # Configuração do comportamento da IA
│   ├── sampleAiConfig.md           # Template de configuração
│   ├── requirements.txt            # Dependências Python
│   └── example.env                 # Template de variáveis de ambiente
├── temp/                           # Arquivos temporários/legacy
├── LICENSE                         # Licença Apache 2.0
└── README.md                       # Documentação do projeto
```

## Como rodar o projeto

### Pré-requisitos

- **Node.js** (versão 18 ou superior)
- **Python** (versão 3.8 ou superior)
- **npm** ou **yarn**
- **Conta GitHub** com acesso ao GitHub Models API
- **Token de API** para GitHub Models (ou OpenAI API compatível)

### 1. Clone o repositório

```sh
git clone https://github.com/gzmoraes/Portifolio-AI.git
cd Portifolio-AI
```

### 2. Configuração do Backend (Servidor)

```bash
cd server

# Crie e ative o ambiente virtual
python -m venv env
source env/bin/activate  # Linux/Mac
# No Windows: env\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp example.env .env
# Edite o .env e adicione sua AI_API_TOKEN
nano .env  # ou use seu editor preferido
```

**Configuração essencial no arquivo `.env`:**

```env
AI_API_TOKEN=your_github_models_api_token_here
```

### 3. Configuração do Frontend (Cliente)

```bash
cd ../client

# Instale as dependências
npm install

# Ou usando yarn
# yarn install
```

### 4. Execute a aplicação

#### Modo Desenvolvimento:

**Terminal 1 - Backend:**

```bash
cd server
source env/bin/activate  # Linux/Mac
# No Windows: env\Scripts\activate
python main.py
```

_Servidor rodará em: `http://localhost:8080`_

**Terminal 2 - Frontend:**

```bash
cd client
npm run dev
```

_Frontend rodará em: `http://localhost:5173`_

#### Modo Produção:

```bash
# 1. Build do frontend
cd client
npm run build

# 2. Execute o backend (servirá arquivos estáticos se configurado)
cd ../server
source env/bin/activate
python main.py
```

#### Scripts Disponíveis:

**Frontend:**

- `npm run dev` - Servidor de desenvolvimento
- `npm run build` - Build para produção
- `npm run preview` - Preview do build
- `npm run lint` - Verificação de código

**Backend:**

- `python main.py` - Inicia servidor Flask
- `python createConfig.py` - Gera configuração personalizada

### 5. Acesse no navegador

- **Desenvolvimento**: Frontend em `http://localhost:5173` e Backend em `http://localhost:8080`
- **Produção**: `http://localhost:8080`

## Configuração de Variáveis de Ambiente

O projeto utiliza variáveis de ambiente para configurações sensíveis. É essencial configurar corretamente:

### 1. Obtenha um Token de API

- **GitHub Models API**: Acesse [GitHub Models](https://github.com/marketplace/models) e gere um token
- **Ou OpenAI API**: Use sua chave da OpenAI API (ajuste o endpoint no código)

### 2. Configure o arquivo `.env`

```bash
cd server
cp example.env .env
```

### 3. Edite o arquivo `.env`

```env
# Token para GitHub Models API
AI_API_TOKEN=github_pat_your_token_here

# Outras configurações opcionais
# DEBUG=true
# PORT=8080
```

### ⚠️ Importante:

- **Nunca** commite o arquivo `.env` no repositório
- O arquivo `.env` contém informações sensíveis reais
- Use o `example.env` como referência para variáveis necessárias
- Adicione `.env` ao `.gitignore` (já incluído)

## Personalização e Configuração

### Configuração da IA

1. **Personalizar Comportamento**: Edite `server/aiConfig.md` para ajustar:

   - Personalidade e tom do assistente
   - Informações sobre você/empresa
   - Instruções específicas de resposta

2. **Gerar Configuração**: Use o script auxiliar:
   ```bash
   cd server
   python createConfig.py
   ```
3. **Template Base**: Consulte `server/sampleAiConfig.md` para exemplos

### Personalização do Frontend

- **Componentes**: Edite arquivos em `client/src/`
- **Estilos**: Modifique `App.css` e `index.css`
- **Assets**: Substitua imagens em `client/src/assets/`

### Adicionando Novas Funções

1. **Defina a função** em `server/app/ai.py` no array `tools`
2. **Implemente a lógica** se necessário
3. **Teste** a nova funcionalidade

### Functions/Tools Disponíveis

- `about` - Informações pessoais e background
- `contact` - Detalhes de contato
- `projects` - Portfólio de projetos
- `services` - Serviços oferecidos
- `skills` - Habilidades técnicas
- `socialMedia` - Links de redes sociais
- `feedback` - Avaliações e depoimentos

## Tecnologias Utilizadas

### Frontend

- **React** 19.1.0 - Biblioteca principal
- **React DOM** 19.1.0 - Renderização
- **Vite** 7.0.4 - Build tool e dev server
- **ESLint** 9.30.1 - Linting e qualidade de código

### Backend

- **Python** 3.8+ - Linguagem principal
- **Flask** 3.1.1 - Framework web
- **Flask-CORS** 6.0.1 - Suporte CORS
- **OpenAI** 1.97.1 - Cliente para API de IA
- **python-dotenv** 1.1.1 - Gerenciamento de variáveis de ambiente

### IA e Modelos

- **GitHub Models API** - Acesso aos modelos GPT-4
- **GPT-4 Variants**:
  - GPT-4.1 (padrão)
  - GPT-4.1-mini
  - GPT-4.1-nano
  - GPT-4o
  - GPT-4o-mini

### Outras Dependências

- **httpx** 0.28.1 - Cliente HTTP assíncrono
- **pydantic** 2.11.7 - Validação de dados
- **Werkzeug** 3.1.3 - Utilitários WSGI

## Funcionalidades Avançadas

### Sistema de Fallback de Modelos

O sistema automaticamente troca entre diferentes modelos GPT-4 quando rate limits são atingidos:

```python
MODELS = [".1", ".1-mini", ".1-nano", "o", "o-mini"]
```

### Tratamento de Erros Robusto

- **Rate Limit**: Troca automática de modelo
- **Bad Request**: Limpa prompt inválido
- **Auth Error**: Notifica problema de autenticação

### Sistema de Memória Contextual

- Mantém histórico da conversa durante a sessão
- Permite respostas contextualizadas
- Flag de controle para atualização de memória

### Function Calling Inteligente

- Categorização automática das consultas do usuário
- Respostas direcionadas por função específica
- Suporte a múltiplas funções simultâneas

## Troubleshooting

### Problemas Comuns

**1. Erro de Autenticação**

```
AuthenticationError: Incorrect API key provided
```

- Verifique se o `AI_API_TOKEN` está correto no `.env`
- Confirme se o token tem as permissões necessárias

**2. Rate Limit Atingido**

```
RateLimitError: Rate limit exceeded
```

- O sistema automaticamente troca para o próximo modelo
- Se todos os modelos foram esgotados, aguarde e tente novamente

**3. Frontend não conecta com Backend**

- Verifique se o backend está rodando na porta 8080
- Confirme se CORS está habilitado
- Verifique logs de erro no console do navegador

**4. Dependências não encontradas**

```bash
# Para Python
pip install -r requirements.txt

# Para Node.js
npm install
```

### Logs e Debug

Para habilitar logs detalhados, edite `server/app/ai.py`:

```python
logging.basicConfig(level=logging.DEBUG)
```

## Contribuição

1. **Fork** o projeto
2. **Crie** uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. **Push** para a branch (`git push origin feature/MinhaFeature`)
5. **Abra** um Pull Request

## Licença

Este projeto está licenciado sob a [Licença Apache 2.0](LICENSE).

---

Desenvolvido por Gustavo Moraes & Gabriel Tazz
