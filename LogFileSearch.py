import os
import re
import platform

# Diretório onde estão os arquivos de log
diretorio_logs = r'\\caminhoArquivoLog' #Coloque o caminho para seus arquivos de Logs

# Função para limpar a tela
def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# Função para obter o último registro de LOGIN e LOGOFF por IP
def obter_ultimo_registro_login_logoff_por_ip(ip_pesquisado):
    ultimo_registro_login = None
    ultimo_registro_logoff = None

    # Percorre todos os arquivos .LOG no diretório
    for arquivo in os.listdir(diretorio_logs):
        if arquivo.endswith('.log'):  # Verifica se o arquivo tem extensão .LOG
            with open(os.path.join(diretorio_logs, arquivo), 'r') as f:
                linhas = f.readlines()
                for linha in linhas:
                    # Use expressões regulares para extrair o IP e a data/hora do registro
                    match_ip = re.search(r'(\d+\.\d+\.\d+\.\d+)', linha)  # Extrai o IP
                    match_data_hora = re.search(r'(\d+/\d+/\d+) ; (\d+:\d+:\d+)', linha)  # Extrai a data e horário
                    if match_ip and match_data_hora:
                        ip = match_ip.group(1)
                        data_hora = match_data_hora.group(1) + ' ' + match_data_hora.group(2)
                        
                        # Verifica se o IP coincide com o IP pesquisado
                        if ip == ip_pesquisado:
                            if 'LOGON' in linha.upper():
                                if ultimo_registro_login is None or data_hora > ultimo_registro_login['data_hora']:
                                    ultimo_registro_login = {
                                        'ip': ip,
                                        'data_hora': data_hora,
                                        'linha': linha.strip()
                                    }
                            elif 'LOGOFF' in linha.upper():
                                if ultimo_registro_logoff is None or data_hora > ultimo_registro_logoff['data_hora']:
                                    ultimo_registro_logoff = {
                                        'ip': ip,
                                        'data_hora': data_hora,
                                        'linha': linha.strip()
                                    }

    return ultimo_registro_login, ultimo_registro_logoff

# Função para obter o último registro de LOGIN e LOGOFF por Nome do Usuário (CN)
def obter_ultimo_registro_login_logoff_por_nome_usuario(nome_usuario):
    ultimo_registro_login = None
    ultimo_registro_logoff = None

    # Percorre todos os arquivos .LOG no diretório
    for arquivo in os.listdir(diretorio_logs):
        if arquivo.endswith('.log'):  # Verifica se o arquivo tem extensão .LOG
            with open(os.path.join(diretorio_logs, arquivo), 'r') as f:
                linhas = f.readlines()
                for linha in linhas:
                    # Use expressões regulares para extrair o CN (Nome do Usuário)
                    match_nome_usuario = re.search(r'CN=([^,]+),', linha)  # Extrai o CN (Nome do Usuário)
                    match_data_hora = re.search(r'(\d+/\d+/\d+) ; (\d+:\d+:\d+)', linha)  # Extrai a data e horário
                    if match_nome_usuario and match_data_hora:
                        nome = match_nome_usuario.group(1)
                        data_hora = match_data_hora.group(1) + ' ' + match_data_hora.group(2)
                        
                        # Verifica se o CN (Nome do Usuário) começa com o primeiro nome pesquisado
                        if nome.startswith(nome_usuario):
                            if 'LOGON' in linha.upper():
                                if ultimo_registro_login is None or data_hora > ultimo_registro_login['data_hora']:
                                    ultimo_registro_login = {
                                        'nome_usuario': nome,
                                        'data_hora': data_hora,
                                        'linha': linha.strip()
                                    }
                            elif 'LOGOFF' in linha.upper():
                                if ultimo_registro_logoff is None or data_hora > ultimo_registro_logoff['data_hora']:
                                    ultimo_registro_logoff = {
                                        'nome_usuario': nome,
                                        'data_hora': data_hora,
                                        'linha': linha.strip()
                                    }

    return ultimo_registro_login, ultimo_registro_logoff

# Função para obter o último registro de LOGIN e LOGOFF por Nome do Micro
def obter_ultimo_registro_login_logoff_por_nome_micro(nome_micro):
    ultimo_registro_login = None
    ultimo_registro_logoff = None

    # Percorre todos os arquivos .LOG no diretório
    for arquivo in os.listdir(diretorio_logs):
        if arquivo.endswith('.log'):  # Verifica se o arquivo tem extensão .LOG
            with open(os.path.join(diretorio_logs, arquivo), 'r') as f:
                linhas = f.readlines()
                for linha in linhas:
                    # Use expressões regulares para extrair o nome do micro (por exemplo, 27067-GO)
                    match_nome_micro = re.search(r'(\d+-[A-Z]+)', linha)  # Extrai o nome do micro
                    match_data_hora = re.search(r'(\d+/\d+/\d+) ; (\d+:\d+:\d+)', linha)  # Extrai a data e horário
                    if match_nome_micro and match_data_hora:
                        nome = match_nome_micro.group(1)
                        data_hora = match_data_hora.group(1) + ' ' + match_data_hora.group(2)
                        
                        # Verifica se o nome do micro coincide com o nome pesquisado
                        if nome == nome_micro:
                            if 'LOGON' in linha.upper():
                                if ultimo_registro_login is None or data_hora > ultimo_registro_login['data_hora']:
                                    ultimo_registro_login = {
                                        'nome_micro': nome,
                                        'data_hora': data_hora,
                                        'linha': linha.strip()
                                    }
                            elif 'LOGOFF' in linha.upper():
                                if ultimo_registro_logoff is None or data_hora > ultimo_registro_logoff['data_hora']:
                                    ultimo_registro_logoff = {
                                        'nome_micro': nome,
                                        'data_hora': data_hora,
                                        'linha': linha.strip()
                                    }

    return ultimo_registro_login, ultimo_registro_logoff

# Função para mostrar o menu e executar a ação selecionada
def menu_interativo():
    while True:
        clear_screen()
        print("Menu Interativo:")
        print("--------------------------------------------------------------------------")
        print("1. Consultar último registro de LOGIN e LOGOFF por IP")
        print("2. Consultar último registro de LOGIN e LOGOFF por Nome do Usuário")
        print("3. Consultar último registro de LOGIN e LOGOFF por Nome do Computador")
        print("\n4. Sair")
        print("--------------------------------------------------------------------------")
        
        escolha = input("Digite o número da opção desejada: ")
        clear_screen()
        if escolha == '1':
            ip_pesquisado = input("Digite o IP que deseja consultar: ")
            ultimo_registro_login, ultimo_registro_logoff = obter_ultimo_registro_login_logoff_por_ip(ip_pesquisado)
            
            clear_screen()
            if ultimo_registro_login:
                print("Último LOGON:")
                print(f"\nIP: {ultimo_registro_login['ip']}")
                print(f"Data/Hora: {ultimo_registro_login['data_hora']}")
                print(f"Registro: {ultimo_registro_login['linha']}")
            else:
                print(f"Nenhum registro de LOGON encontrado para o IP: {ip_pesquisado}")

            if ultimo_registro_logoff:
                print("\nÚltimo LOGOFF:")
                print(f"\nIP: {ultimo_registro_logoff['ip']}")
                print(f"Data/Hora: {ultimo_registro_logoff['data_hora']}")
                print(f"Registro: {ultimo_registro_logoff['linha']}")
            else:
                print(f"Nenhum registro de LOGOFF encontrado para o IP: {ip_pesquisado}")
            
            input("\nPressione Enter para continuar...")
            
        elif escolha == '2':
            primeiro_nome_usuario = input("Digite o primeiro Nome do Usuário que deseja consultar: ")
            ultimo_registro_login, ultimo_registro_logoff = obter_ultimo_registro_login_logoff_por_nome_usuario(primeiro_nome_usuario)
            
            clear_screen()
            if ultimo_registro_login:
                print("Último LOGON:")
                print(f"\nNome do Usuário (CN): {ultimo_registro_login['nome_usuario']}")
                print(f"Data/Hora: {ultimo_registro_login['data_hora']}")
                print(f"Registro: {ultimo_registro_login['linha']}")
            else:
                print(f"Nenhum registro de LOGON encontrado para o Nome do Usuário que começa com '{primeiro_nome_usuario}'")

            if ultimo_registro_logoff:
                print("\nÚltimo LOGOFF:")
                print(f"\nNome do Usuário: {ultimo_registro_logoff['nome_usuario']}")
                print(f"Data/Hora: {ultimo_registro_logoff['data_hora']}")
                print(f"Registro: {ultimo_registro_logoff['linha']}")
            else:
                print(f"Nenhum registro de LOGOFF encontrado para o Nome do Usuário que começa com '{primeiro_nome_usuario}'")
            
            input("\nPressione Enter para continuar...")

        elif escolha == '3':
            nome_micro = input("Digite o Nome do Computador que deseja consultar: ")
            ultimo_registro_login, ultimo_registro_logoff = obter_ultimo_registro_login_logoff_por_nome_micro(nome_micro)
            
            clear_screen()
            if ultimo_registro_login:
                print("Último LOGON:")
                print(f"\nNome do Computador: {ultimo_registro_login['nome_micro']}")
                print(f"Data/Hora: {ultimo_registro_login['data_hora']}")
                print(f"Registro: {ultimo_registro_login['linha']}")
            else:
                print(f"Nenhum registro de LOGON encontrado para o Nome do Computador: {nome_micro}")

            if ultimo_registro_logoff:
                print("\nÚltimo LOGOFF:")
                print(f"\nNome do Computador: {ultimo_registro_logoff['nome_micro']}")
                print(f"Data/Hora: {ultimo_registro_logoff['data_hora']}")
                print(f"Registro: {ultimo_registro_logoff['linha']}")
            else:
                print(f"Nenhum registro de LOGOFF encontrado para o Nome do Computador: {nome_micro}")
            
            input("\nPressione Enter para continuar...")

        elif escolha == '4':
            clear_screen()
            break
        else:
            clear_screen()
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    menu_interativo()
