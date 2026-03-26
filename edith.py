import os, socket, subprocess, time, getpass

# --- CONFIGURACIÓN STARK v51.0 ---
PASSWORD = "1234"
C, W, G, N = '\033[1;36m', '\033[1;37m', '\033[0;37m', '\033[0m'
S_OK, S_INFO, S_RAD = f"{C}●{N}", f"{W}○{N}", f"{C}»{N}"

def manage_notes(action, text=""):
    path = os.path.expanduser("~/.stark_vault")
    if action == "add":
        with open(path, "a") as f: f.write(f"- {text}\n")
        return f"{S_OK} {C}Nota guardada en el búnker.{N}"
    if action == "view":
        if not os.path.exists(path): return f"{S_INFO} {W}Búnker vacío.{N}"
        with open(path, "r") as f: return f"\n{C}--- NOTAS SECRETAS ---\n{W}" + f.read() + f"{C}-------------------{N}"
    return ""

def tactical_scan():
    print(f" {S_RAD} {C}Iniciando Reconocimiento de Red...{N}")
    # Escaneo rápido buscando dispositivos activos y resolución de nombres
    res = os.popen("nmap -sP 192.168.1.0/24 | grep 'Nmap scan report for'").read()
    devices = res.strip().split('\n')
    
    if not devices or devices == ['']:
        return f"{S_INFO} {W}No se detectaron intrusos en el sector.{N}"
    
    output = f"\n{C}--- DISPOSITIVOS EN EL SECTOR ---{N}\n"
    for d in devices:
        name = d.replace("Nmap scan report for ", "")
        output += f"{G}  [+] {W}{name}{N}\n"
    return output + f"{C}---------------------------------{N}"

def chat(u):
    u = u.lower().strip()
    if u == "scan": return tactical_scan()
    if u.startswith("note "): return manage_notes("add", u[5:])
    if u == "view": return manage_notes("view")
    if u in ["status", "info"]: return f"{S_OK} {C}SISTEMA MARK 51: RED ACTIVA{N}"
    return f" {S_INFO} {W}Comandos:{N} status, scan, note <txt>, view, exit"

if __name__ == "__main__":
    os.system('clear')
    print(f"\n {C}◢◤ IDENTIDAD REQUERIDA ◢◤{N}")
    if getpass.getpass(" PIN: ") == PASSWORD:
        os.system('clear')
        print(f"\n {C}◢◤ {W}E.D.I.T.H. OS v51.0 {C}◢◤{N}\n {S_OK} {G}Escáner Táctico Instalado.{N}\n")
        while True:
            try:
                p = input(f"{C}stark{N} {G}>>{N} ")
                if p in ['exit', 'salir']: break
                res = chat(p)
                if res: print(f"{res}\n")
            except EOFError: break
