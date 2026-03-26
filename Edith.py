import os, sys, getpass, json, socket, time
from urllib.request import urlopen

# --- CONFIGURACIÓN OMEGA SEALED ---
# Tu PIN Maestro Exclusivo
MASTER_PIN = "9999" 

# Paleta de Colores OMEGA (Rojo, Blanco, Gris)
R, W, G, C, N = '\033[1;31m', '\033[1;37m', '\033[0;37m', '\033[1;36m', '\033[0m'

LOGO = f"""
{R}          ◢◤ Ω ◢◤
{R}      ______  __  __  ______  _____   _____ 
{R}     |     ||  \/  ||  ____||     \ |     |
{R}     |  |  || \  / ||  ____ |  --  ||  -  |
{R}     |_____||_|\/|_||______||_____/ |_____|
{W}               O  M  E  G  A    S  Y  S  T  E  M{N}
"""

def get_sys_info():
    try:
        mem = os.popen("free -m").read().split('\n')[1].split()
        total, used = mem[1], mem[2]
        return f"\n{R}--- ESTADO OMEGA ---{N}\n{G}MEMORIA TOTAL: {W}{total}MB\n{G}EN USO: {R}{used}MB\n{R}---------------------{N}"
    except: return f" {R}● Sensores offline.{N}"

def chat(u):
    u = u.lower().strip()
    if u == "status": return get_sys_info()
    if u == "where":
        try:
            d = json.loads(urlopen("http://ip-api.com/json/").read().decode())
            return f"\n{R}--- UBICACIÓN SELLADA ---{N}\n{G}CIUDAD: {W}{d['city']}\n{G}IP PÚBLICA: {R}{d['query']}{N}"
        except: return f" {R}● Fallo GPS.{N}"
    if u.startswith("note "):
        with open(os.path.expanduser("~/.stark_vault"), "a") as f: f.write(f"- [{time.strftime('%H:%M:%S')] {u[5:]}\n")
        return f"{R}● Nota registrada en el búnker OMEGA.{N}"
    if u == "view":
        try: return f"\n{W}{open(os.path.expanduser('~/.stark_vault'), 'r').read()}{N}"
        except: return f" {R}○ Búnker OMEGA vacío.{N}"
    if u in ["info", "help"]: return f"{G}Comandos: status, where, note, view, exit{N}"
    return f"{R}○ Comando no reconocido.{N}"

if __name__ == "__main__":
    os.system('clear')
    print(f"\n {R}◢◤ INGRESE CREDENCIALES OMEGA ◢◤{N}")
    entry = getpass.getpass(" PIN DE ACCESO: ").strip()
    
    if entry == MASTER_PIN:
        os.system('clear')
        print(LOGO)
        print(f" {R}●{N} {W}PROTOCOLO OMEGA v53.2 {G}SELLADO{N}")
        print(f" {R}●{N} {G}SISTEMA EXCLUSIVO PARA ETERNALFURIA.{N}\n")
        while True:
            try:
                p = input(f"{R}omega{N} {G}>>{N} ")
                if p in ['exit', 'salir']: break
                res = chat(p)
                if res: print(res)
            except EOFError: break
    else:
        print(f"\n {R}!!! ACCESO DENEGADO - PROTOCOLO DE SILENCIO ACTIVADO !!!{N}")
