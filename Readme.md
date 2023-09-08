# Mini Sistema de Consulta de Registros de Logon e Logoff

## Índice

- [Introdução](#introdução)
- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Como Usar](#como-usar)
- [Contribuições](#contribuições)
- [Contato](#contato)

## Introdução

Este é um mini sistema desenvolvido em Python que permite a consulta de registros de logon e logoff em arquivos de log. O sistema é projetado para ser executado em sistemas Windows e fornece uma interface de usuário interativa para realizar consultas com base em três critérios principais: IP, Nome do Usuário, e Nome do Computador.

## Funcionalidades

O Mini Sistema de Consulta de Registros de Logon e Logoff oferece as seguintes funcionalidades:

1. **Consulta de Registro por IP:**
   - Consulta e exibe o último registro de logon e logoff associado a um IP específico.

2. **Consulta de Registro por Nome do Usuário:**
   - Consulta e exibe o último registro de logon e logoff associado a um Nome do Usuário que comece com um determinado primeiro nome.

3. **Consulta de Registro por Nome do Computador:**
   - Consulta e exibe o último registro de logon e logoff associado a um Nome do Computador específico.

## Requisitos

Para executar o Mini Sistema de Consulta de Registros de Logon e Logoff, você precisará:

- Python 3.x (recomendado)
- Biblioteca `pywin32` (para sistemas Windows)
- Sistema operacional Windows (para acesso aos registros de eventos)

## Como Usar

1. Clone o repositório em sua máquina local.

2. Abra o arquivo `LogFileSearch.py` em um editor de texto.

3. No início do arquivo, você encontrará a seguinte linha:

   ```python
   diretorio_logs = r'\\caminhoArquivoLog' #Coloque o caminho para seus arquivos de Logs
   Substitua '\\caminhoArquivoLog' pelo caminho completo para o diretório onde estão armazenados seus arquivos de log.

4. Instale a biblioteca `pywin32` usando o seguinte comando em seu terminal: " pip install pywin32 "

5. Execute o arquivo `LogFileSearch.py` em um ambiente Python compatível com as dependências.

6. Siga as instruções apresentadas no menu interativo para realizar consultas com base em IP, Nome do Usuário ou Nome do Computador.

7. Os resultados da consulta serão exibidos na tela, incluindo o último registro de logon e logoff relacionado ao critério escolhido.

## Contribuições

Contribuições são bem-vindas! Se você deseja melhorar ou estender este Mini Sistema de Consulta de Registros de Logon e Logoff, fique à vontade para criar um fork do repositório, fazer suas alterações e enviar um pull request.

## Contato

Se você deseja entrar em contato comigo para discutir sobre o projeto ou qualquer assunto relacionado, sinta-se à vontade para utilizar os seguintes meios de contato:

📞 Telefone: +55 (62) 99850-0635
📧 E-mail: contactstanley.devtech@gmail.com
📷 Instagram: @stanley.devtech

---

Esperamos que este mini sistema seja útil para você e que você aproveite a consulta de registros de logon e logoff de maneira eficiente. Se tiver alguma dúvida ou sugestão, sinta-se à vontade para abrir uma issue neste repositório.

Agradecemos por usar o Mini Sistema de Consulta de Registros de Logon e Logoff!


