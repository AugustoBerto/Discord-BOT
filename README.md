# 🤖 Discord-BOT

Um bot para Discord desenvolvido com Python utilizando a biblioteca `discord.py`. Este projeto tem como objetivo automatizar tarefas e fornecer comandos personalizados dentro de servidores Discord.

## 📁 Estrutura do Projeto

```
📦 Discord-BOT
├── 📂 commands         # Comandos customizados do bot
├── 📂 tasks            # Tarefas automatizadas (como eventos agendados)
├── main.py             # Arquivo principal para iniciar o bot
├── requirements.txt    # Dependências do projeto
└── token.env           # Token do bot (não deve ser compartilhado publicamente)
```

## 🚀 Como executar

1. **Clone o repositório:**

```bash
git clone https://github.com/AugustoBerto/Discord-BOT.git
cd Discord-BOT
```

2. **Crie um ambiente virtual (opcional, mas recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Configure o arquivo `token.env`:**

```env
TOKEN_ID = token_do_seu_bot
```

5. **Execute o bot:**

```bash
python main.py
```
