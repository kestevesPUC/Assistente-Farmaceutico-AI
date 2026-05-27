# Assistente IA de Conformidade Farmacêutica

Este projeto consiste em um agente de Inteligência Artificial especializado em conformidade farmacêutica, desenvolvido com Python, Streamlit e CrewAI.

A aplicação foi criada para auxiliar profissionais da área farmacêutica a consultarem rapidamente regulamentações da ANVISA e diretrizes GMP através de perguntas em linguagem natural.

## Como funciona

O sistema possui uma pasta chamada `knowledge`, responsável por armazenar os arquivos PDF utilizados como base de conhecimento da IA.

Dentro dessa pasta estão documentos regulatórios como:

* RDC 301
* RDC 658
* BPF (Boas Práticas de Fabricação)
* Diretrizes GMP

Quando o usuário realiza uma pergunta, o agente de IA interpreta a solicitação, consulta os documentos presentes na pasta `knowledge` e retorna uma resposta contextualizada com base nas regulamentações encontradas.

A IA pode:

* Responder perguntas sobre conformidade farmacêutica
* Auxiliar na interpretação de regulamentações da ANVISA
* Indicar possíveis ações corretivas
* Resumir trechos importantes dos documentos
* Referenciar regulamentações relevantes

## Tecnologias utilizadas

* Python 3.11.0
* Streamlit
* CrewAI
* OpenAI API
* Processamento de PDFs
* YAML para configuração de agentes e tarefas

## Configuração do ambiente

Antes de executar o projeto, é necessário criar um arquivo `.env` na raiz do projeto contendo sua chave de API da OpenAI.

Exemplo:

```env
OPENAI_API_KEY=sua_chave_aqui
```

A chave da API pode ser obtida em:

https://platform.openai.com/home

## Executando o projeto

Instale as dependências:

```bash
pip install streamlit crewai
```

Execute a aplicação:

```bash
streamlit run app.py
```

## Estrutura do projeto

```bash
📂 knowledge/       -> PDFs com regulamentações farmacêuticas
📂 config/          -> Configurações dos agentes e tarefas
📄 agents.yaml      -> Definição dos agentes
📄 tasks.yaml       -> Definição das tarefas
📄 app.py           -> Interface Streamlit
📄 main.py          -> Execução principal do agente
```
