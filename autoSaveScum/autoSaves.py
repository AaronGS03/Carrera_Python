

import shutil, psutil, os
from pathlib import Path

for proc in psutil.process_iter():
    if proc.name() == "JumpKing.exe":
        print("Cerrando JumpKing")
        proc.kill()

try:
    print("Cambiando partida guardada")
    shutil.copyfile(str(Path.home())+"\\Desktop\\Nueva carpeta\\combined.sav","C:\\GOG Games\\Jump King\\Content\\Saves\\combined.sav")
    
    try:
        print("Ejecutando JumpKing")
        os.chdir("C:\\GOG Games\\Jump King")
        os.startfile("C:\\GOG Games\\Jump King\\JumpKing.exe")
    except:
        print("Error al ejecutar JumpKing")
        
except IOError as e:
    print("Error al copiar:",e)

