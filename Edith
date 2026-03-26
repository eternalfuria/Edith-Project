import subprocess, os, socket, sys

R, Y, W, G, N = '\033[1;31m', '\033[1;33m', '\033[1;37m', '\033[1;32m', '\033[0m'

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except: return "127.0.0.1"

def update_system():
    print(f"{Y}[*] Conectando con el repositorio central...{N}")
    # Verifica si la carpeta es un repositorio Git
    if os.path.exists(".git"):
        st = subprocess.call("git pull origin main", shell=True)
        if st == 0: print(f"{G}[✔] Nanobots actualizados con éxito.{N}")
        else: print(f"{R}[✘] Error de sincronización Git.{N}")
    else:
        print(f"{W}[!] Este directorio no es un repo Git local.{N}")

def chat(text=""):
    text = text.lower().strip()
    if text == "update":
        update_system()
        return "Reinicie E.D.I.T.H. para aplicar cambios."
    if text in ["status", "info"]:
        return f"{Y}IP:{N} {get_ip()} | {Y}REPO:{N} Sincronizado"
    if text == "scan":
        os.system("nmap -sP 192.168.1.0/24 | grep 'Nmap scan report'")
        return f"{G}Escaneo Nmap completado.{N}"
    return "Comandos: status, scan, update, exit"

if __name__ == "__main__":
    print(f"{R}◢◤ E.D.I.T.H. MARK 50 (GIT-ENABLED) ◢◤{N}")
    while True:
        try:
            u = input(f"{Y}Comando > {N}")
            if u.lower() in ['exit', 'salir']: break
            print(chat(u))
        except EOFError: break
