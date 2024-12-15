import os
import shutil
import subprocess

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "Data")
    behavior_profile_dir = os.path.join(data_dir, "Behavior profile")
    stories_dir = os.path.join(data_dir, "Stories")
    exe_path = os.path.join(data_dir, "Mantella GENERATOR NPCs Back History NG.exe")
    image_file = os.path.join(data_dir, "background_001.png")
    additional_image_file = os.path.join(data_dir, "MANBH.dds")

    # Verificar si las carpetas ya existen en la carpeta base
    copied_behavior_profile_dir = os.path.join(base_dir, "Behavior profile")
    copied_stories_dir = os.path.join(base_dir, "Stories")

    if not os.path.exists(copied_behavior_profile_dir):
        # Hacer una copia de la carpeta "Behavior profile"
        shutil.copytree(behavior_profile_dir, copied_behavior_profile_dir)

    if not os.path.exists(copied_stories_dir):
        # Hacer una copia de la carpeta "Stories"
        shutil.copytree(stories_dir, copied_stories_dir)

    # Hacer una copia del archivo de imagen "background_001.png" a la carpeta base
    copied_image_file = os.path.join(base_dir, "background_001.png")
    shutil.copy(image_file, copied_image_file)

    # Hacer una copia del archivo de imagen "MANBH.dds" a la carpeta base
    copied_additional_image_file = os.path.join(base_dir, "MANBH.dds")
    shutil.copy(additional_image_file, copied_additional_image_file)

    # Ejecutar el programa "Mantella GENERATOR NPCs Back History NG.exe"
    if os.path.exists(exe_path):
        try:
            subprocess.Popen([exe_path])
        except Exception as e:
            print(f"Error al ejecutar {exe_path}: {e}")
    else:
        print(f"Error: {exe_path} no encontrado.")

if __name__ == "__main__":
    main()






# pyinstaller --onefile --windowed --icon=MantellaHB.ico "Mantella GENERATOR NPCs Back History NG Setup.pyw"




#lo primro este pye tieen al lado tiene una carpta llamada "Data" esta carpate contine dso .ico, llamados "MantellaHB.ico" y "MantellaHBcarpetp.ico"
#tambien tiene dentor de data una carpata llamada "Behavior profile" y un ejecutalbe llamado "Mantella GENERATOR NPCs Back History NG.exe" estos seran
#inportantes para lo qeu ara el pyw,


#lo primero es crear un aseso directo en la misma carpeta donde se ejecuta el pyw, este aseso directo sera de la carpeta "Behavior profile"  y tendra el 
#icono "MantellaHBcarpetp.ico" 

#lo segundo es ejecutar el programa "Mantella GENERATOR NPCs Back History NG.exe" , eso 





#agregaresmo otro acceso directo que se jenere este es de la carpata llamada "Stories" que esta en el interior de "Data", al acceso direco le daremos
#el icono "StoriesHB.ico" que esta en la misma carpta "Data"