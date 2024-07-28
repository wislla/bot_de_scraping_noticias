# Bot de Scraping de Notícias

Este projeto é um bot para coleta de notícias de sites utilizando scraping, armazenamento em banco de dados e envio de resumos diários por e-mail.

## Estrutura do Projeto

- `scraping/scraper.py`: Código para scraping de notícias.
- `database/models.py`: Modelos de banco de dados.
- `email/email_sender.py`: Código para envio de e-mails.
- `main.py`: Ponto de entrada do projeto, que integra scraping, armazenamento e envio de e-mails.

## Configuração

1. Instale as dependências usando Poetry:
   ```bash
   poetry install
