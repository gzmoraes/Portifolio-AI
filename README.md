# Portifolio-AI

Portifolio-AI é um projeto de portfólio dinâmico que utiliza inteligência artificial para oferecer uma experiência interativa aos visitantes. O sistema conta com um chatbot alimentado por IA, capaz de responder perguntas sobre o portfólio, projetos, habilidades, serviços e informações de contato do desenvolvedor.

## Funcionalidades

- Chatbot inteligente treinado com informações do portfólio
- Respostas personalizadas e profissionais
- Mapeamento de funções para facilitar a navegação (sobre, contato, projetos, serviços, habilidades, redes sociais, feedback)
- Interface web responsiva com Flask
- Configuração fácil via arquivos `.env` e `aiConfig.md`

## Estrutura do Projeto

```
.
├── app/
│   ├── __init__.py
│   ├── AI.py
│   ├── models.py
│   ├── routes.py
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   └── templates/
│       └── index.html
├── main.py
├── createConfig.py
├── aiConfig.md
├── sampleAiConfig.md
├── requirements.txt
├── example.env
└── README.md
```

## Como rodar o projeto

1. **Clone o repositório**
2. **Instale as dependências**
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure o arquivo `.env`**
   - Copie o `example.env` para `.env` e adicione sua chave de API de IA.
4. **Execute a aplicação**
   ```sh
   python main.py
   ```
5. **Acesse no navegador**
   - Abra `http://localhost:5000`

## Personalização

- Edite o arquivo [`aiConfig.md`](aiConfig.md) para alterar as informações do portfólio e o comportamento do assistente.
- Use o [`createConfig.py`](createConfig.py) para gerar configurações personalizadas a partir do template [`sampleAiConfig.md`](sampleAiConfig.md).

## Tecnologias Utilizadas

- Python 3
- Flask
- OpenAI API
- dotenv
- HTML/CSS

## Licença

Este projeto está licenciado sob a [Licença Apache 2.0](LICENSE).

---

Desenvolvido por Gustavo Moraes & Gabriel Tazz