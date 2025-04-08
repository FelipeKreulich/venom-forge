
# VenomForge - Payload Generator

**VenomForge** é uma ferramenta de geração de payloads utilizando o **msfvenom** do **Metasploit Framework**, focada em Windows, Android e Linux. Através desta ferramenta, é possível criar payloads customizados com opções avançadas como codificação (encoder), persistência e compactação com UPX, além de verificar a segurança do payload gerado. A ferramenta também permite a criação de listeners automáticos para facilitar o processo de exploração.

## Funcionalidades

- **Detecção automática do IP local**: A ferramenta detecta o IP da máquina automaticamente, mas o usuário pode optar por fornecer um IP manualmente.
- **Escolha de Encoder**: O usuário pode escolher entre o encoder padrão (`x86/shikata_ga_nai`) ou inserir um encoder personalizado.
- **Payloads customizados**: Suporta payloads para os sistemas **Windows**, **Android** e **Linux**, com opções como `reverse_tcp`, `bind_tcp`, e `shell_reverse_tcp`.
- **Persistência**: O usuário pode optar por adicionar persistência ao payload para garantir que ele se mantenha ativo após reinicializações.
- **Compactação com UPX**: Possibilidade de compactar o payload com UPX para reduzir seu tamanho e dificultar a detecção.
- **Verificação de segurança**: Verifica se o payload é detectável por antivírus.
- **Listener Automático**: A ferramenta pode gerar um listener automático para facilitar o controle do payload.

## Instalação

Para usar a **VenomForge**, você precisa ter o **Metasploit** e o **msfvenom** instalados no seu sistema, além do **Python** e algumas bibliotecas necessárias.

### Pré-requisitos

- Python 3.x
- **Metasploit** (instalação do `msfvenom`): [Metasploit Framework](https://metasploit.help.rapid7.com/docs/installing-the-metasploit-framework)
- Bibliotecas Python:

  ```bash
  pip install pyfiglet colorama tqdm emoji tabulate
  ```

### Passos para instalar

1. Clone o repositório:

   ```bash
   git clone https://github.com/FelipeKreulich/venom-forge.git
   cd venom-forge
   ```

2. Instale as dependências necessárias:

   Execute o seguinte comando para instalar as bibliotecas que o script usa:

   ```bash
   pip install pyfiglet colorama tqdm emoji tabulate
   ```

3. Certifique-se de que o **Metasploit** está instalado e configurado corretamente no seu sistema, com o comando `msfvenom` acessível no terminal.

## Como usar

### Passo 1: Execute o script

Após instalar as dependências e garantir que o **Metasploit** está instalado corretamente, execute o script `venomforge.py`:

```bash
python main.py
```

### Passo 2: Escolher a plataforma e opções

Durante a execução do script, o usuário será solicitado a fornecer as seguintes informações:

1. **Sistema alvo**: Escolha entre **windows**, **android** ou **linux**.
2. **LHOST (IP local)**: O IP local será detectado automaticamente, mas você pode escolher outro.
3. **LPORT (porta)**: Defina a porta para o payload.
4. **Nome do Payload**: Escolha um nome para o arquivo gerado.
5. **Encoder**: Escolha o encoder a ser utilizado.
6. **Persistência**: Defina se deseja adicionar persistência ao payload.
7. **Compactação com UPX**: Se desejar compactar o payload com UPX, escolha sim.
8. **Listener Automático**: Caso deseje gerar um listener automático para o payload.
9. **Verificação de segurança**: Verifique se o payload é detectável por antivírus.

### Passo 3: Geração do Payload

Após inserir as configurações, a ferramenta gerará o payload de acordo com as opções selecionadas. O arquivo gerado será salvo na pasta de downloads do usuário.

### Exemplo de saída

```
==================================================================
 _    __                           ______
| |  / /__  ____  ____  ____ ___  / ____/___  _________ ____ 
| | / / _ \/ __ \/ __ \/ __ `__ \/ /_  / __ \/ ___/ __ `/ _ \
| |/ /  __/ / / / /_/ / / / / / / __/ / /_/ / /  / /_/ /  __/
|___/\___/_/ /_/\____/_/ /_/ /_/_/    \____/_/   \__, /\___/ 
                                                /____/       

==================================================================

Escolha o alvo (windows/android/linux): windows
IP detectado: 192.168.0.10. Deseja usar esse IP? (S/n): s
Digite a porta (LPORT): 4444
Nome do payload (exe/apk/elf): my_payload
Encoder padrão: x86/shikata_ga_nai
Deseja usar o encoder padrão, escolher outro ou nenhum? (1/2/3): 1
==================[ ESCOLHER PERSISTÊNCIA ]==================
Deseja adicionar persistência ao payload? (S/n): n
==================[ COMPACTAR COM UPX? ]==================
Deseja compactar o payload com UPX? (S/n): s
==================[ GERAR LISTENER AUTOMÁTICO? ]==================
Deseja gerar listener automático? (S/n): n
==================[ VERIFICAR SEGURANÇA? ]==================
Deseja verificar se o payload é detectável por antivírus? (S/n): n
===========================================================
[*] Alvo: Windows
[*] IP: 192.168.0.10
[*] Porta: 4444
[*] Nome do Payload: my_payload
[*] Encoder: x86/shikata_ga_nai
[*] Persistência: Não
[*] Compactação com UPX: Sim
[*] Gerar Listener Automático: Não
[*] Verificar Segurança: Não
===========================================================

------------------[ GERANDO PAYLOAD EXE COM MSFVENOM ]------------------
:skull: Gerando payload... :skull:
...
[+] Payload gerado com sucesso: C:\Users\user\Downloads\my_payload.exe
------------------[ COMPACTANDO COM UPX ]------------------
[+] Payload compactado com sucesso com UPX!
===========================================================
```

## Contribuindo

Contribuições são bem-vindas! Caso tenha alguma sugestão ou correção, fique à vontade para abrir uma **issue** ou enviar um **pull request**.

## Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
