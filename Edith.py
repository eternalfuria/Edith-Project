import os, socket, subprocess, time, getpass

# --- CONFIGURACIÓN STARK ---
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

def radar():
    print(f" {S_RAD} {C}Escaneando sector...{N}")
    return f"{S_OK} {W}Radar activo. 1 dispositivo detectado.{N}"

def chat(u):
    u = u.lower().strip()
    if u == "radar": return radar()
    if u.startswith("note "): return manage_notes("add", u[5:])
    if u == "view": return manage_notes("view")
    if u in ["status", "info"]: return f"{S_OK} {C}SISTEMA RECONFIGURADO v50.7{N}"
    return f" {S_INFO} {W}Comandos:{N} status, radar, note <txt>, view, exit"

if __name__ == "__main__":
    os.system('clear')
    print(f"\n {C}◢◤ IDENTIDAD REQUERIDA ◢◤{N}")
    if getpass.getpass(" PIN: ") == PASSWORD:
        os.system('clear')
        print(f"\n {C}◢◤ {W}E.D.I.T.H. OS v50.7 {C}◢◤{N}\n {S_OK} {G}Sincronización Total.{N}\n")
        while True:
            try:
                p = input(f"{C}stark{N} {G}>>{N} ")
                if p in ['exit', 'salir']: break
                res = chat(p)
                if res: print(f"{res}\n")
            except EOFError: break
