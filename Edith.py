import os, socket, subprocess, time, getpass, json
from urllib.request import urlopen

# --- PROTOCOLO DE PRIVACIDAD STARK ---
# La contraseña NO se sube a GitHub. Se guarda localmente.
PIN_PATH = os.path.expanduser("~/.stark_key")

def get_stored_pin():
    if not os.path.exists(PIN_PATH):
        # Si no existe, creamos el de fábrica (CÁMBIALO AL ENTRAR)
        with open(PIN_PATH, "w") as f: f.write("1234")
        return "1234"
    return open(PIN_PATH, "r").read().strip()

C, W, G, R, N = '\033[1;36m', '\033[1;37m', '\033[0;37m', '\033[1;31m', '\033[0m'

LOGO = f"""
{C}  ______  _____   _____  _______  _     _ 
 {C} |  ____||     \  |   | |__   __| | |   | |
 {C} | |____ |  --  | |   |    | |    | |___| |
 {C} |______||_____/  |___|    |_|    |_____|_|
{W}           M  A  R  K    5  3    S  Y  S  T  E  M{N}
"""

def locate_me():
    try:
        data = json.loads(urlopen("http://ip-api.com/json/").read().decode())
        return f"\n{C}--- UBICACIÓN ---{N}\n{G}IP: {W}{data['query']}\n{G}CIUDAD: {W}{data['city']}\n{C}-----------------{N}"
    except: return f" {R}● Error Satelital.{N}"

def chat(u):
    u = u.lower().strip()
    if u == "where": return locate_me()
    if u.startswith("set pin "):
        new_pin = u[8:].strip()
        with open(PIN_PATH, "w") as f: f.write(new_pin)
        return f"{C}● PIN ACTUALIZADO LOCALMENTE.{N}"
    if u == "status": return f"{C}● MARK 53 | REPO PÚBLICO BLINDADO{N}"
    return f"{G}Comandos: where, set pin <nuevo>, status, exit{N}"

if __name__ == "__main__":
    os.system('clear')
    current_pin = get_stored_pin()
    print(f"\n {R}◢◤ ACCESO PRIVADO ◢◤{N}")
    if getpass.getpass(" PIN: ") == current_pin:
        os.system('clear')
        print(LOGO)
        print(f" {C}●{N} {W}MODO: SEGURIDAD DE REPOSITORIO ACTIVA{N}\n")
        while True:
            try:
                p = input(f"{C}stark{N} {G}>>{N} ")
                if p == 'exit': break
                print(chat(p))
            except EOFError: break
        try:
                p = input(f"{C}stark{N} {G}>>{N} ")
                if p in ['exit', 'salir']: break
                res = chat(p)
                if res: print(f"{res}\n")
            except EOFError: break
