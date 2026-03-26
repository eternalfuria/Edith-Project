import os, socket, subprocess, time, getpass

# --- CONFIGURACIÓN VISUAL STARK ---
PASSWORD = "1234"
C, W, G, R, N = '\033[1;36m', '\033[1;37m', '\033[0;37m', '\033[1;31m', '\033[0m'

LOGO = f"""
{C}  ______  _____   _____  _______  _     _ 
 {C} |  ____||     \  |   | |__   __| | |   | |
 {C} | |____ |  --  | |   |    | |    | |___| |
 {C} |______||_____/  |___|    |_|    |_____|_|
{W}           S  T  A  R  K    S  Y  S  T  E  M{N}
"""

def tactical_scan():
    print(f" {C}» Escaneando frecuencia local...{N}")
    res = os.popen("arp -a").read()
    if not res: return f" {R}● Error: Sensores bloqueados.{N}"
    output = f"\n{C}--- UNIDADES DETECTADAS ---{N}\n"
    for line in res.split('\n'):
        if "(" in line:
            output += f"{G}  [+] {W}{line}{N}\n"
    return output + f"{C}---------------------------{N}"

def chat(u):
    u = u.lower().strip()
    if u == "scan": return tactical_scan()
    if u.startswith("note "):
        with open(os.path.expanduser("~/.stark_vault"), "a") as f: f.write(f"- {u[5:]}\n")
        return f"{C}● Nota encriptada en el búnker.{N}"
    if u == "view":
        try: 
            with open(os.path.expanduser("~/.stark_vault"), "r") as f: return f"\n{W}{f.read()}{N}"
        except: return f" {R}○ Búnker vacío.{N}"
    if u in ["status", "info"]: return f"{C}● MARK 51.2 | NÚCLEO ESTABLE{N}"
    return f"{G}Comandos: scan, note, view, status, exit{N}"

if __name__ == "__main__":
    os.system('clear')
    print(f"\n {R}◢◤ ACCESO RESTRINGIDO ◢◤{N}")
    if getpass.getpass(" PIN DE SEGURIDAD: ") == PASSWORD:
        os.system('clear')
        print(LOGO)
        print(f" {C}●{N} {W}SISTEMA OPERATIVO v51.2{N}")
        print(f" {C}●{N} {G}BIENVENIDO, ETERNALFURIA.{N}\n")
        while True:
            try:
                p = input(f"{C}stark{N} {G}>>{N} ")
                if p in ['exit', 'salir']: break
                res = chat(p)
                if res: print(f"{res}\n")
            except EOFError: break
:
            try:
                p = input(f"{C}stark{N} {G}>>{N} ")
                if p in ['exit', 'salir']: break
                res = chat(p)
                if res: print(f"{res}\n")
            except EOFError: break
