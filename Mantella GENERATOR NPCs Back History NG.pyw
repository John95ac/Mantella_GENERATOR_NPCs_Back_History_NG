import json
import tkinter as tk
from tkinter import ttk, messagebox
import random
import os
import re
from tkinter import filedialog, simpledialog, messagebox
import shutil
import zipfile



# Función para cargar datos desde archivos
def load_data(file, default):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return default

# Cargar datos desde archivos
RACES_FILE = 'Stories/races.json'
VOICES_FILE = 'Stories/voices.json'
CHARACTERS_FILE = 'Stories/characters.json'
POSITIVE_TRAITS_FILE = 'Stories/positive_traits.json'
NEGATIVE_TRAITS_FILE = 'Stories/negative_traits.json'


skyrim_races = sorted(load_data(RACES_FILE, [
    "Nord", "Breton", "Imperial", "Redguard", "High Elf", "Dark Elf", "Wood Elf", "Orc",
    "Khajiit", "Argonian", "Nord Vampire", "Breton Vampire", "Imperial Vampire",
    "Redguard Vampire", "High Elf Vampire", "Dark Elf Vampire", "Wood Elf Vampire",
    "Orc Vampire", "Khajiit Vampire", "Argonian Vampire", "Elder", "Dremora"
]))

skyrim_voices = sorted(load_data(VOICES_FILE, [
    "FemaleEvenToned", "MaleEvenToned", "FemaleYoungEager", "MaleYoungEager",
    "FemaleSultry", "MaleBrute", "FemaleCondescending", "MaleCondescending",
    "FemaleCommander", "MaleCommander", "FemaleCoward", "MaleCoward",
    "FemaleDarkElf", "MaleDarkElf", "FemaleNord", "MaleNord",
    "FemaleOrc", "MaleOrc", "FemaleKhajiit", "MaleKhajiit",
    "FemaleArgonian", "MaleArgonian", "FemaleChild", "MaleChild",
    "FemaleOldGrumpy", "MaleOldGrumpy", "FemaleOldKind", "MaleOldKind",
    "FemaleSlyCynical", "MaleSlyCynical", "FemaleCommoner", "MaleCommoner",
    "Adril", "Alduin", "Ancano", "Arngeir", "Astrid", "Brynjolf", "Cicero",
    "Delphine", "Delvin", "Dexion", "Dragon", "Elenwen", "Esbern",
    "FemaleDarkElfCommoner", "FemaleElfHaughty", "FemaleShrill", "FemaleVampire",
    "Florentius", "Frea", "Fura", "Galmar", "Garan", "Gelebor", "Hadvar",
    "Harkon", "Ileril", "Isran", "Karliah", "KodlakWhitemane", "MaleBandit",
    "MaleCommonerAccented", "MaleDarkElfCommoner", "MaleDarkElfCynical",
    "MaleDrunk", "MaleDunmer", "MaleElfHaughty", "MaleEvenTonedAccented",
    "MaleGuard", "MaleNordCommander", "MaleOldKindly", "MaleSoldier",
    "MaleVampire", "MaleWarlock", "Maven", "MercerFrey", "Mirabelle", "Modyn",
    "Nazir", "Neloth", "Odahviing", "Paarthurnax", "Riekling", "Serana",
    "Storn", "Tulius", "Ulfric", "Valerica", "Vex"
]))

characters = load_data(CHARACTERS_FILE, [])

positive_traits = sorted(load_data(POSITIVE_TRAITS_FILE, [
    "Adventurous", "Affable", "Ambitious", "Amiable", "Brave", "Calm",
    "Charming", "Cheerful", "Clever", "Compassionate", "Confident",
    "Courageous", "Courteous", "Creative", "Curious", "Decisive", "Dedicated",
    "Dependable", "Diligent", "Diplomatic", "Disciplined", "Empathetic",
    "Energetic", "Enthusiastic", "Faithful", "Flexible", "Focused", "Generous",
    "Gentle", "Hardworking", "Honest", "Humble", "Idealistic", "Independent",
    "Ingenious", "Insightful", "Intelligent", "Intuitive", "Inventive", "Kind",
    "Logical", "Loyal", "Meticulous", "Modest", "Observant", "Optimistic",
    "Organized", "Patient", "Perceptive", "Persistent", "Philosophical",
    "Practical", "Precise", "Punctual", "Quick-witted", "Rational", "Realistic",
    "Reflective", "Reliable", "Resourceful", "Respectful", "Responsible",
    "Self-disciplined", "Sensible", "Sincere", "Sociable", "Sympathetic",
    "Thoughtful", "Trustworthy", "Understanding", "Versatile", "Warm-hearted",
    "Wise", "Witty"
]))

negative_traits = sorted(load_data(NEGATIVE_TRAITS_FILE, [
    "Abrasive", "Aggressive", "Aloof", "Arrogant", "Bossy", "Calculating",
    "Callous", "Cynical", "Deceitful", "Dishonest", "Egocentric", "Greedy",
    "Impatient", "Impulsive", "Inconsiderate", "Indifferent", "Insecure",
    "Intolerant", "Irresponsible", "Jealous", "Manipulative", "Narcissistic",
    "Obstinate", "Pessimistic", "Reckless", "Rude", "Selfish", "Sneaky",
    "Spiteful", "Stubborn", "Uncooperative", "Unforgiving", "Unreliable",
    "Vain", "Vindictive"
]))

species = [
    "Elf", "Argonian", "Khajiit", "Human", "Mer", "Vampire", "Werewolf",
    "Kitsune", "Goblin", "Lich", "Snake Man (Sload)", "Daedric (Dremora)",
    "Atronach", "Fire Atronach", "Storm Atronach", "Ice Atronach", "Spriggan",
    "Snow Maiden", "Snow Banshee", "Giant", "Mountain Giant"
]

def create_npc(name, voice_model, race, gender, species, bio):
    npc = {
        "name": name,
        "voice_model": voice_model,
        "bio": bio,
        "race": race,
        "gender": gender,
        "species": species
    }
    return npc

def save_npc():
    name = name_entry.get()
    voice_model = voice_combobox.get()
    race = race_combobox.get()
    gender = gender_combobox.get()
    species = species_combobox.get()
    bio = bio_text.get("1.0", tk.END).strip()

    npc = create_npc(name, voice_model, race, gender, species, bio)

    with open(f'Stories/{name}.json', 'w') as f:
        json.dump(npc, f, indent=4)

    messagebox.showinfo("Success", f"NPC {name} created and saved in Stories/{name}.json")


def load_npc():
    selected_file = file_combobox.get()
    if selected_file:
        with open(f'Stories/{selected_file}', 'r') as f:
            npc = json.load(f)
            name_entry.delete(0, tk.END)
            name_entry.insert(0, npc.get("name", ""))
            voice_combobox.set(npc.get("voice_model", ""))
            race_combobox.set(npc.get("race", ""))
            gender_combobox.set(npc.get("gender", ""))
            species_combobox.set(npc.get("species", ""))
            bio_text.delete("1.0", tk.END)
            bio_text.insert("1.0", npc.get("bio", ""))
            update_token_progress()


# Función para contar sílabas en una palabra
def count_syllables(word):
    word = word.lower()
    syllables = re.findall(r'[aeiouy]+', word)
    return len(syllables)




#----------------------------------------------------------------------------------------------------------------------------
#
#----------------------------------------------------------------------------------------------------------------------------









# Crear la ventana principal
#root = tk.Tk()
#root.title("Mantella GENERATOR NPCs Back History NG")
#root.configure(bg='#2e2e2e')  # Modo oscuro




from PIL import Image, ImageTk

# Crear la ventana principal
root = tk.Tk()
root.title("Mantella GENERATOR NPCs Back History NG")

# Cargar la imagen de fondo
background_image = Image.open("background_001.png")  # Asegúrate de que "background.png" esté en la misma carpeta que tu script
background_photo = ImageTk.PhotoImage(background_image)

# Crear un widget Label para la imagen de fondo
background_label = tk.Label(root, image=background_photo, bg='black')  # Establecer el fondo negro
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Configurar el modo oscuro para los widgets
root.configure(bg='black')  # Establecer el fondo negro para la ventana principal

# Asegurarse de que los widgets se coloquen sobre la imagen de fondo
background_label.lower()

# Aquí puedes agregar el resto de tu código para los widgets





#----------------------------------------------------------------------------------------------------------------------------
#
#----------------------------------------------------------------------------------------------------------------------------








# Obtener lista de archivos JSON en la carpeta actual
json_files = [f for f in os.listdir() if f.endswith('.json')]

from tkinter import ttk

# Crear widgets de la interfaz

style = ttk.Style()
style.theme_use('clam')  # Usar el tema 'clam' para permitir la personalización

# Configurar el estilo para los Combobox
style.configure("TCombobox",
                fieldbackground='#2e2e2e',  # Fondo del campo de entrada
                background='#2e2e2e',  # Fondo del desplegable
                foreground='white',  # Color del texto
                selectbackground='#2e2e2e',  # Fondo del texto seleccionado
                selectforeground='white')  # Color del texto seleccionado


tk.Label(root, text="Name:", bg='#2e2e2e', fg='white', font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(root, font=("Arial", 12), bg='#2e2e2e', fg='white')
name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")


tk.Label(root, text="Voice Model:", bg='#2e2e2e', fg='white', font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
voice_combobox = ttk.Combobox(root, values=skyrim_voices, font=("Arial", 12))
voice_combobox.grid(row=1, column=1, padx=10, pady=5, sticky="we")
voice_combobox['state'] = 'normal'
voice_combobox['values'] = skyrim_voices
voice_combobox['postcommand'] = lambda: voice_combobox.configure(values=skyrim_voices)

tk.Label(root, text="Race:", bg='#2e2e2e', fg='white', font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
race_combobox = ttk.Combobox(root, values=skyrim_races, font=("Arial", 12))
race_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="we")
race_combobox['state'] = 'normal'
race_combobox['values'] = skyrim_races
race_combobox['postcommand'] = lambda: race_combobox.configure(values=skyrim_races)

tk.Label(root, text="Gender:", bg='#2e2e2e', fg='white', font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
gender_combobox = ttk.Combobox(root, values=["Female", "Male"], font=("Arial", 12))
gender_combobox.grid(row=3, column=1, padx=10, pady=5, sticky="we")
gender_combobox['state'] = 'normal'
gender_combobox['values'] = ["Female", "Male"]
gender_combobox['postcommand'] = lambda: gender_combobox.configure(values=["Female", "Male"])

tk.Label(root, text="Species:", bg='#2e2e2e', fg='white', font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=5, sticky="w")
species_combobox = ttk.Combobox(root, values=species, font=("Arial", 12))
species_combobox.grid(row=4, column=1, padx=10, pady=5, sticky="we")
species_combobox['state'] = 'normal'
species_combobox['values'] = species
species_combobox['postcommand'] = lambda: species_combobox.configure(values=species)


#----------------------------------------------------------------------------------------------------------------------------
#
#----------------------------------------------------------------------------------------------------------------------------


tk.Label(root, text="Biography:", bg='#2e2e2e', fg='white', font=("Arial", 12)).grid(row=5, column=0, padx=10, pady=5, sticky="w")

bio_frame = tk.Frame(root, bg='#2e2e2e')
bio_frame.grid(row=5, column=1, padx=10, pady=5, sticky="we")

bio_text = tk.Text(bio_frame, height=15, width=50, font=("Arial", 12), bg='#2e2e2e', fg='white', wrap=tk.WORD)
bio_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(bio_frame, command=bio_text.yview, bg='#2e2e2e')
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

bio_text.config(yscrollcommand=scrollbar.set)


#----------------------------------------------------------------------------------------------------------------------------
#⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⠟⠉⠉⠻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠿⠉⠀⠀⠀⠀⠀⠹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⡿⠛⠉
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⡿⠟⠁⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣷⣶⣶⣦⣤⣤⣄⣤⡀⣀⣩⣾⣿⠿⠋⠀⠀⠀⠀⠀⣠
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⠟⠋⠉⠉⠙⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⢀⡾⠁
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠁⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⡟⠁⠀⠀⠀⢀⣴⣿⣿⣿⣿⡏⠋⠀⠀⠀⠀⠀⠀⠀⡞⠋⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡏⠀⠀⠀⠀⣶⣿⣿⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⢸⡯⠤⣤
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⣿⡏⠀⠀⠀⠀⣼⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣄⣄⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡿⠋⠀⠀⠀⠀⣼⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣄
#⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⣾⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⣠⣶⣶⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻
#⠀⠀⠀⠀⠀⠀⢀⣾⠿⠛⢿⣿⣷⣄⡀⣿⠋⠀⠈⠀⠀⠀⠀⠀⠀⢀⣾⡏⠀⢹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⣠⣤⣦⣼⣿⠀⠀⠀⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⢷⣄⠀⠀⠀⠀⠀⠀⠀
#⠀⣠⣾⡿⠋⠉⠉⠁⠀⠀⠀⠀⠉⢯⡙⠻⣿⣿⣷⣤⡀⠀⠀⠀⠀⢿⣿⣿⣿⣿⡿⠃⢀⡤⠖⠋⣉⣉⣉⣉⠉⠉⠒⠦⣄⠀⠀⠀⢔⡟⡿⠟⠉⣟⣻⣮⣿⠀⠀⠀⠀⠀⠀⠀⠀
#⣾⣿⠋⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠙⢦⣄⠉⠻⢿⣿⣷⣦⡀⠀⠈⠙⠛⠛⠋⠀⢰⠟⠁⠀⠀⠈⠻⡿⠛⠁⠀⠀⠀⠈⠳⣄⠀⠸⣧⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠀⣴⠙⣩⣿⣿⣄⠀⠀⠀⠀⡶⢌⡙⠶⣤⡈⠛⠿⣿⣷⣦⣀⠀⠀⠀⠀⡇⠀⢰⣄⠀⠀⣠⢷⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠻⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⢸⣇⢸⣿⣿⣿⣿⠀⠀⠀⠀⡇⠀⠈⠛⠦⣝⡳⢤⣈⠛⠻⣿⣷⣦⣀⠀⠀⠀⠀⠈⠙⠋⠁⠀⠛⠦⢤⡤⠀⠀⠀⠀⢳⠀⠀⠀⠈⠋⠙⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠈⢿⣄⣿⣿⣿⠏⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠙⠳⢬⣛⠦⠀⠙⢻⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠀⠀⠉⠛⠋⠁⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠈⣿⠉⢻⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠀⠀⠀⣠⣄⠀⠀⢰⠶⠒⠒⢧⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⡇⢸⡟⢿⣷⣦⣴⣶⣶⣶⣶⣤⣔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⣤⠀⠀⠿⠿⠁⢀⡿⠀⠀⠀⡄⠈⠙⡷⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⡇⢸⡇⠀⣿⠙⣿⣿⣉⠉⠙⠿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠙⠷⢤⣀⣠⠴⠛⠁⠀⠀⠀⠇⠀⠀⡇⢸⡏⢹⡷⢦⣄⡀⠀⠀⠀⣿⡀⢸⡇⢸⡇⠀⡟⠀⢸⠀⢹⡷⢦⣄⣘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#----------------------------------------------------------------------------------------------------------------------------



# Barra de progreso para los tokens
tk.Label(root, text="MAX Tokens possible not to pass:", bg='#2e2e2e', fg='white', font=("Arial", 12)).grid(row=6, column=0, padx=10, pady=5, sticky="w")
token_progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", style="orange.Horizontal.TProgressbar")
token_progress.grid(row=6, column=1, padx=10, pady=5, sticky="we")

# Cambiar el color del texto a verde
token_label = tk.Label(root, text="0 Tokens", bg='#D3D3D3', fg='green', font=("Arial", 12), width=10)  # Aumenta el ancho del label
token_label.place(x=115, y=335)  # Ajusta las coordenadas para desplazar a la derecha y hacia abajo

# Mensaje que se mostrará cuando se alcance el límite
limit_message = tk.Label(root, text="", bg='#D3D3D3', fg='red', font=("Arial", 12))
limit_message.place(x=115, y=335)  # Ajusta las coordenadas para que se superponga al token_label

def update_token_progress():
    bio_content = bio_text.get("1.0", tk.END).strip()
    token_count = sum(count_syllables(word) for word in bio_content.split())
    
    if token_count >= 1500:
        token_progress.grid_forget()  # Oculta la barra de progreso
        limit_message.config(text="It's too much for the AI")  # Muestra el mensaje en inglés
        token_label.config(text=f"{token_count} Tokens")  # Actualiza el texto del label
        token_label.config(fg='black')  # Cambia el color a negro
    else:
        token_progress['value'] = (token_count / 1500) * 100
        token_label.config(text=f"{token_count} Tokens")  # Actualiza el texto del label

        # Cambiar el color del texto según el número de tokens
        if token_count < 300:
            token_label.config(fg='green')  # Verde
        elif token_count < 900:
            token_label.config(fg='yellow')  # Amarillo
        elif token_count < 1200:
            token_label.config(fg='orange')  # Naranja
        elif token_count < 1500:
            token_label.config(fg='red')  # Rojo

        limit_message.config(text="")  # Limpia el mensaje si no se ha alcanzado el límite

    # Actualizar el estilo de la barra de progreso
    style = ttk.Style()
    style.configure("orange.Horizontal.TProgressbar", background='orange')  # Color de la barra en naranja

    # Programar la próxima actualización
    root.after(100, update_token_progress)  # Actualiza cada 100 ms

# Iniciar la actualización continua
update_token_progress()

bio_text.bind("<KeyRelease>", lambda event: update_token_progress())
#----------------------------------------------------------------------------------------------------------------------------
#⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⠟⠉⠉⠻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠿⠉⠀⠀⠀⠀⠀⠹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⡿⠛⠉
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⡿⠟⠁⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣷⣶⣶⣦⣤⣤⣄⣤⡀⣀⣩⣾⣿⠿⠋⠀⠀⠀⠀⠀⣠
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⠟⠋⠉⠉⠙⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⢀⡾⠁
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠁⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⡟⠁⠀⠀⠀⢀⣴⣿⣿⣿⣿⡏⠋⠀⠀⠀⠀⠀⠀⠀⡞⠋⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡏⠀⠀⠀⠀⣶⣿⣿⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⢸⡯⠤⣤
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⣿⡏⠀⠀⠀⠀⣼⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣄⣄⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡿⠋⠀⠀⠀⠀⣼⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣄
#⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⣾⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⣠⣶⣶⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻
#⠀⠀⠀⠀⠀⠀⢀⣾⠿⠛⢿⣿⣷⣄⡀⣿⠋⠀⠈⠀⠀⠀⠀⠀⠀⢀⣾⡏⠀⢹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⣠⣤⣦⣼⣿⠀⠀⠀⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⢷⣄⠀⠀⠀⠀⠀⠀⠀
#⠀⣠⣾⡿⠋⠉⠉⠁⠀⠀⠀⠀⠉⢯⡙⠻⣿⣿⣷⣤⡀⠀⠀⠀⠀⢿⣿⣿⣿⣿⡿⠃⢀⡤⠖⠋⣉⣉⣉⣉⠉⠉⠒⠦⣄⠀⠀⠀⢔⡟⡿⠟⠉⣟⣻⣮⣿⠀⠀⠀⠀⠀⠀⠀⠀
#⣾⣿⠋⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠙⢦⣄⠉⠻⢿⣿⣷⣦⡀⠀⠈⠙⠛⠛⠋⠀⢰⠟⠁⠀⠀⠈⠻⡿⠛⠁⠀⠀⠀⠈⠳⣄⠀⠸⣧⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠀⣴⠙⣩⣿⣿⣄⠀⠀⠀⠀⡶⢌⡙⠶⣤⡈⠛⠿⣿⣷⣦⣀⠀⠀⠀⠀⡇⠀⢰⣄⠀⠀⣠⢷⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠻⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⢸⣇⢸⣿⣿⣿⣿⠀⠀⠀⠀⡇⠀⠈⠛⠦⣝⡳⢤⣈⠛⠻⣿⣷⣦⣀⠀⠀⠀⠀⠈⠙⠋⠁⠀⠛⠦⢤⡤⠀⠀⠀⠀⢳⠀⠀⠀⠈⠋⠙⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠈⢿⣄⣿⣿⣿⠏⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠙⠳⢬⣛⠦⠀⠙⢻⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠀⠀⠉⠛⠋⠁⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠈⣿⠉⢻⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠀⠀⠀⣠⣄⠀⠀⢰⠶⠒⠒⢧⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⡇⢸⡟⢿⣷⣦⣴⣶⣶⣶⣶⣤⣔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⣤⠀⠀⠿⠿⠁⢀⡿⠀⠀⠀⡄⠈⠙⡷⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⡇⢸⡇⠀⣿⠙⣿⣿⣉⠉⠙⠿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠙⠷⢤⣀⣠⠴⠛⠁⠀⠀⠀⠇⠀⠀⡇⢸⡏⢹⡷⢦⣄⡀⠀⠀⠀⣿⡀⢸⡇⢸⡇⠀⡟⠀⢸⠀⢹⡷⢦⣄⣘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#----------------------------------------------------------------------------------------------------------------------------




tk.Label(root, text="Positive Traits (number):", bg='#2e2e2e', fg='white', font=("Arial", 12)).grid(row=7, column=0, padx=10, pady=5, sticky="w")
positive_traits_spinbox = tk.Spinbox(root, from_=0, to=len(positive_traits), font=("Arial", 12), bg='#2e2e2e', fg='white')
positive_traits_spinbox.grid(row=7, column=1, padx=10, pady=5, sticky="we")

tk.Label(root, text="Negative Traits (number):", bg='#2e2e2e', fg='white', font=("Arial", 12)).grid(row=8, column=0, padx=10, pady=5, sticky="w")
negative_traits_spinbox = tk.Spinbox(root, from_=0, to=len(negative_traits), font=("Arial", 12), bg='#2e2e2e', fg='white')
negative_traits_spinbox.grid(row=8, column=1, padx=10, pady=5, sticky="we")


def add_traits_to_bio():
    positive_traits_count = int(positive_traits_spinbox.get())
    negative_traits_count = int(negative_traits_spinbox.get())

    selected_positive_traits = random.sample(positive_traits, positive_traits_count)
    selected_negative_traits = random.sample(negative_traits, negative_traits_count)

    bio_text_content = bio_text.get("1.0", tk.END)
    if "Personality:" in bio_text_content:
        bio_text_content = bio_text_content.split("Personality:")[0].strip()
        bio_text.delete("1.0", tk.END)
        bio_text.insert(tk.END, bio_text_content)

    bio_text.insert(tk.END, f"\n\nPersonality: {', '.join(selected_positive_traits + selected_negative_traits)}")
    update_token_progress()






#----------------------------------------------------------------------------------------------------------------------------
#
#----------------------------------------------------------------------------------------------------------------------------


# Obtener lista de archivos JSON en la carpeta "Stories"
json_files = [f for f in os.listdir('Stories') if f.endswith('.json')]

tk.Label(root, text="Select JSON File:", bg='#2e2e2e', fg='white', font=("Arial", 12)).grid(row=13, column=0, padx=10, pady=5, sticky="w")
file_combobox = ttk.Combobox(root, values=json_files, font=("Arial", 12))
file_combobox.grid(row=13, column=1, padx=10, pady=5, sticky="we")
file_combobox['state'] = 'normal'
file_combobox['values'] = json_files
file_combobox['postcommand'] = lambda: file_combobox.configure(values=json_files)

def on_file_select(event):
    selected_file = file_combobox.get()
    if selected_file:
        with open(f'Stories/{selected_file}', 'r') as f:
            npc = json.load(f)
            name_entry.delete(0, tk.END)
            name_entry.insert(0, npc.get("name", ""))
            voice_combobox.set(npc.get("voice_model", ""))
            race_combobox.set(npc.get("race", ""))
            gender_combobox.set(npc.get("gender", ""))
            species_combobox.set(npc.get("species", ""))
            bio_text.delete("1.0", tk.END)
            bio_text.insert("1.0", npc.get("bio", ""))
            update_token_progress()

file_combobox.bind("<<ComboboxSelected>>", on_file_select)


# Texto para selección de historias
tk.Label(root, text="Stories to read or modify", bg='#2e2e2e', fg='white', font=("Arial", 12)).grid(row=12, column=0, padx=10, pady=5, sticky="w")

# Botón para entrar en la carpeta "Stories"
def open_stories_folder():
    os.startfile("Stories")  # Abre la carpeta "Stories" en el mismo lugar donde se ejecuta el programa

tk.Button(root, text="Open Stories Folder", command=open_stories_folder, bg='#4CAF50', fg='white', font=("Arial", 12)).grid(row=14, column=0, padx=10, pady=5, sticky="w")


#----------------------------------------------------------------------------------------------------------------------------
#
#----------------------------------------------------------------------------------------------------------------------------














#----------------------------------------------------------------------------------------------------------------------------
#⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⠟⠉⠉⠻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠿⠉⠀⠀⠀⠀⠀⠹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⡿⠛⠉
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⡿⠟⠁⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣷⣶⣶⣦⣤⣤⣄⣤⡀⣀⣩⣾⣿⠿⠋⠀⠀⠀⠀⠀⣠
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⠟⠋⠉⠉⠙⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⢀⡾⠁
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠁⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⡟⠁⠀⠀⠀⢀⣴⣿⣿⣿⣿⡏⠋⠀⠀⠀⠀⠀⠀⠀⡞⠋⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡏⠀⠀⠀⠀⣶⣿⣿⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⢸⡯⠤⣤
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⣿⡏⠀⠀⠀⠀⣼⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣄⣄⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡿⠋⠀⠀⠀⠀⣼⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣄
#⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⣾⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⣠⣶⣶⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻
#⠀⠀⠀⠀⠀⠀⢀⣾⠿⠛⢿⣿⣷⣄⡀⣿⠋⠀⠈⠀⠀⠀⠀⠀⠀⢀⣾⡏⠀⢹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⣠⣤⣦⣼⣿⠀⠀⠀⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⢷⣄⠀⠀⠀⠀⠀⠀⠀
#⠀⣠⣾⡿⠋⠉⠉⠁⠀⠀⠀⠀⠉⢯⡙⠻⣿⣿⣷⣤⡀⠀⠀⠀⠀⢿⣿⣿⣿⣿⡿⠃⢀⡤⠖⠋⣉⣉⣉⣉⠉⠉⠒⠦⣄⠀⠀⠀⢔⡟⡿⠟⠉⣟⣻⣮⣿⠀⠀⠀⠀⠀⠀⠀⠀
#⣾⣿⠋⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠙⢦⣄⠉⠻⢿⣿⣷⣦⡀⠀⠈⠙⠛⠛⠋⠀⢰⠟⠁⠀⠀⠈⠻⡿⠛⠁⠀⠀⠀⠈⠳⣄⠀⠸⣧⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠀⣴⠙⣩⣿⣿⣄⠀⠀⠀⠀⡶⢌⡙⠶⣤⡈⠛⠿⣿⣷⣦⣀⠀⠀⠀⠀⡇⠀⢰⣄⠀⠀⣠⢷⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠻⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⢸⣇⢸⣿⣿⣿⣿⠀⠀⠀⠀⡇⠀⠈⠛⠦⣝⡳⢤⣈⠛⠻⣿⣷⣦⣀⠀⠀⠀⠀⠈⠙⠋⠁⠀⠛⠦⢤⡤⠀⠀⠀⠀⢳⠀⠀⠀⠈⠋⠙⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠈⢿⣄⣿⣿⣿⠏⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠙⠳⢬⣛⠦⠀⠙⢻⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠀⠀⠉⠛⠋⠁⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠈⣿⠉⢻⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠀⠀⠀⣠⣄⠀⠀⢰⠶⠒⠒⢧⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⡇⢸⡟⢿⣷⣦⣴⣶⣶⣶⣶⣤⣔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⣤⠀⠀⠿⠿⠁⢀⡿⠀⠀⠀⡄⠈⠙⡷⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⡇⢸⡇⠀⣿⠙⣿⣿⣉⠉⠙⠿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠙⠷⢤⣀⣠⠴⠛⠁⠀⠀⠀⠇⠀⠀⡇⢸⡏⢹⡷⢦⣄⡀⠀⠀⠀⣿⡀⢸⡇⢸⡇⠀⡟⠀⢸⠀⢹⡷⢦⣄⣘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#----------------------------------------------------------------------------------------------------------------------------


import os
import tkinter as tk
from tkinter import messagebox

def open_behavior_folder():
    behavior_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Behavior profile")
    if os.path.exists(behavior_folder):
        os.startfile(behavior_folder)
    else:
        messagebox.showerror("Error", "La carpeta 'Behavior profile' no existe.")

# Botones de creación (en la fila 9)
add_traits_button = tk.Button(root, text="Add Traits to Biography", command=add_traits_to_bio, bg='#4CAF50', fg='white', font=("Arial", 12))
add_traits_button.grid(row=9, column=0, padx=10, pady=10)

save_button = tk.Button(root, text="Save NPC", command=save_npc, bg='#4CAF50', fg='white', font=("Arial", 12))
save_button.grid(row=9, column=1, padx=10, pady=10)

# Crear un marco para el perfil de comportamiento (en la fila 11)
behavior_frame = tk.Frame(root, bg='#2e2e2e')
behavior_frame.grid(row=11, column=0, columnspan=2, padx=10, pady=5, sticky="we")  # Cambiado a fila 11

tk.Label(behavior_frame, text="Behavior Profile:", bg='#2e2e2e', fg='white', font=("Arial", 12)).pack(pady=5)

# Listbox para mostrar los archivos de comportamiento
behavior_listbox = tk.Listbox(
    behavior_frame,
    font=("Arial", 12),
    bg='#2e2e2e',  # Fondo oscuro
    fg='white',  # Letras blancas
    selectmode=tk.SINGLE,
    height=5,  # Ajusta la altura (número de líneas visibles)
    width=30   # Ajusta el ancho (número de caracteres)
)
behavior_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar para el Listbox
behavior_scrollbar = tk.Scrollbar(behavior_frame, command=behavior_listbox.yview, bg='#2e2e2e')
behavior_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
behavior_listbox.config(yscrollcommand=behavior_scrollbar.set)

# Cargar archivos de texto de la carpeta "Behavior profile"
def load_behavior_files():
    behavior_folder = "Behavior profile"
    if os.path.exists(behavior_folder):
        for filename in os.listdir(behavior_folder):
            if filename.endswith('.txt'):
                behavior_listbox.insert(tk.END, filename)

load_behavior_files()

# Función para agregar el contenido del archivo seleccionado a la biografía
def add_behavior_to_bio():
    selected_file_index = behavior_listbox.curselection()
    if selected_file_index:
        selected_file = behavior_listbox.get(selected_file_index)
        behavior_folder = "Behavior profile"
        file_path = os.path.join(behavior_folder, selected_file)
        
        with open(file_path, 'r') as f:
            behavior_content = f.read()
            bio_text.insert(tk.END, f"\n\n{behavior_content}")  # Agregar el contenido al final de la biografía

# Botón para agregar el comportamiento a la biografía
add_behavior_button = tk.Button(
    behavior_frame,
    text="Add Behavior to Biography",
    command=add_behavior_to_bio,
    bg='#4CAF50',
    fg='white',
    font=("Arial", 12),
    width=35,  # Ajusta el ancho del botón
    height=2   # Ajusta la altura del botón
)
add_behavior_button.pack(pady=(20, 0))  # Agrega un espacio considerable entre la scrollbar y el botón

# Botón para acceder a la carpeta "Behavior profile"
access_behavior_button = tk.Button(
    behavior_frame,
    text="Access Behavior Folder",
    command=open_behavior_folder,
    bg='#4CAF50',
    fg='white',
    font=("Arial", 12),
    width=20,  # Ajusta el ancho del botón
    height=0   # Ajusta la altura del botón
)
access_behavior_button.pack(pady=(20, 0))  # Agrega un espacio considerable entre la scrollbar y el botón




#----------------------------------------------------------------------------------------------------------------------------
#⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⠟⠉⠉⠻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠿⠉⠀⠀⠀⠀⠀⠹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⡿⠛⠉
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⡿⠟⠁⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣷⣶⣶⣦⣤⣤⣄⣤⡀⣀⣩⣾⣿⠿⠋⠀⠀⠀⠀⠀⣠
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⠟⠋⠉⠉⠙⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⢀⡾⠁
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠁⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⡟⠁⠀⠀⠀⢀⣴⣿⣿⣿⣿⡏⠋⠀⠀⠀⠀⠀⠀⠀⡞⠋⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡏⠀⠀⠀⠀⣶⣿⣿⣿⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⢸⡯⠤⣤
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⣿⡏⠀⠀⠀⠀⣼⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣄⣄⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡿⠋⠀⠀⠀⠀⣼⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣄
#⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⣾⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⣠⣶⣶⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻
#⠀⠀⠀⠀⠀⠀⢀⣾⠿⠛⢿⣿⣷⣄⡀⣿⠋⠀⠈⠀⠀⠀⠀⠀⠀⢀⣾⡏⠀⢹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⣠⣤⣦⣼⣿⠀⠀⠀⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⢷⣄⠀⠀⠀⠀⠀⠀⠀
#⠀⣠⣾⡿⠋⠉⠉⠁⠀⠀⠀⠀⠉⢯⡙⠻⣿⣿⣷⣤⡀⠀⠀⠀⠀⢿⣿⣿⣿⣿⡿⠃⢀⡤⠖⠋⣉⣉⣉⣉⠉⠉⠒⠦⣄⠀⠀⠀⢔⡟⡿⠟⠉⣟⣻⣮⣿⠀⠀⠀⠀⠀⠀⠀⠀
#⣾⣿⠋⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠙⢦⣄⠉⠻⢿⣿⣷⣦⡀⠀⠈⠙⠛⠛⠋⠀⢰⠟⠁⠀⠀⠈⠻⡿⠛⠁⠀⠀⠀⠈⠳⣄⠀⠸⣧⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠀⣴⠙⣩⣿⣿⣄⠀⠀⠀⠀⡶⢌⡙⠶⣤⡈⠛⠿⣿⣷⣦⣀⠀⠀⠀⠀⡇⠀⢰⣄⠀⠀⣠⢷⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠻⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⢸⣇⢸⣿⣿⣿⣿⠀⠀⠀⠀⡇⠀⠈⠛⠦⣝⡳⢤⣈⠛⠻⣿⣷⣦⣀⠀⠀⠀⠀⠈⠙⠋⠁⠀⠛⠦⢤⡤⠀⠀⠀⠀⢳⠀⠀⠀⠈⠋⠙⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠈⢿⣄⣿⣿⣿⠏⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠙⠳⢬⣛⠦⠀⠙⢻⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠀⠀⠉⠛⠋⠁⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠈⣿⠉⢻⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠀⠀⠀⣠⣄⠀⠀⢰⠶⠒⠒⢧⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⡇⢸⡟⢿⣷⣦⣴⣶⣶⣶⣶⣤⣔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⣤⠀⠀⠿⠿⠁⢀⡿⠀⠀⠀⡄⠈⠙⡷⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⡇⢸⡇⠀⣿⠙⣿⣿⣉⠉⠙⠿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⣿⡇⠀⠀⠙⠷⢤⣀⣠⠴⠛⠁⠀⠀⠀⠇⠀⠀⡇⢸⡏⢹⡷⢦⣄⡀⠀⠀⠀⣿⡀⢸⡇⢸⡇⠀⡟⠀⢸⠀⢹⡷⢦⣄⣘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#----------------------------------------------------------------------------------------------------------------------------


# Ajustar el tamaño de las columnas
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)





#----------------------------------------------------------------------------------------------------------------------------
#
#----------------------------------------------------------------------------------------------------------------------------





class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x = event.x_root + 20
        y = event.y_root + 10
        self.tooltip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, background="#696969", fg="white", relief="solid", borderwidth=1, font=("Arial", 14))
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

# Botón para agregar rasgos a la biografía
add_traits_button = tk.Button(
    root,
    text="Add Traits to Biography",
    command=add_traits_to_bio,
    bg='#4CAF50',
    fg='white',
    font=("Arial", 12)
)
add_traits_button.grid(row=9, column=0, padx=10, pady=10)  # Coloca el botón en la fila 9, columna 0

tooltip = ToolTip(add_traits_button, "Just press the button once you have selected the Traits (you can choose 0, that's fine)\nand have your entire story written and ready.\nThis should go at the end of the text, then you can select the Blue button to save or modify the character 🐱.")

# Botón para guardar el NPC
save_button = tk.Button(
    root,
    text="Save NPC",
    command=save_npc,
    bg='#00008B',  # Azul oscuro
    fg='white',
    font=("Arial", 12)
)
save_button.grid(row=9, column=1, padx=10, pady=10)  # Coloca el botón en la fila 9, columna 1

tooltip_save = ToolTip(save_button, "Press this button to save the NPC Back History.\nMake sure all details are correct\nbefore saving 🐱.")



#----------------------------------------------------------------------------------------------------------------------------
#
#----------------------------------------------------------------------------------------------------------------------------

tooltip_behavior = ToolTip(add_behavior_button, "First select the behavior in the window on the side, and press \nthe button to add it to the story. Make sure it is below the text,\nand it cannot go after the Traits (you can select as many as you want,\n but make sure they make sense and don't exceed the token limit) 🐱.")

tooltip_behavior = ToolTip(access_behavior_button, "With this button, you can access the folder that contains the behaviors. You can create your own \nby simply creating a .txt file and writing in it, or by using those shared by the community.")



tooltip_behavior = ToolTip(access_behavior_button, "With this button, you can access the folder that contains the behaviors. You can create your own \nby simply creating a .txt file and writing in it, or by using those shared by the community.")

tooltip_behavior = ToolTip(access_behavior_button, "With this button, you can access the folder that contains the behaviors. You can create your own \nby simply creating a .txt file and writing in it, or by using those shared by the community.")

#tooltip_behavior = ToolTip(open_stories_folder, "With this button, you can access the folder that contains the behaviors. You can create your own \nby simply creating a .txt file and writing in it, or by using those shared by the community.")



#----------------------------------------------------------------------------------------------------------------------------
#
#----------------------------------------------------------------------------------------------------------------------------



# Función para abrir la carpeta "Stories"
def open_stories_folder():
    os.startfile("Stories")  # Abre la carpeta "Stories" en el mismo lugar donde se ejecuta el programa

# Función para crear el mod para instalación
def create_mod():
    # Solicitar el nombre del paquete de historia
    package_name = simpledialog.askstring("Input", "Enter the name of the story package:", parent=root)
    if not package_name:
        return

    # Seleccionar archivos de la carpeta "Stories"
    file_paths = filedialog.askopenfilenames(initialdir="Stories", title="Select JSON files", filetypes=(("JSON files", "*.json"), ("All files", "*.*")), parent=root)
    if not file_paths:
        return

    # Crear la estructura de carpetas
    mod_dir = os.path.join("Stories", package_name)
    os.makedirs(os.path.join(mod_dir, "Mantella BackHistory"), exist_ok=True)
    os.makedirs(os.path.join(mod_dir, "textures", "Mantella-BH"), exist_ok=True)

    # Copiar los archivos seleccionados
    for file_path in file_paths:
        shutil.copy(file_path, os.path.join(mod_dir, "Mantella BackHistory"))

    # Copiar el archivo MANBH.dds con el nuevo nombre
    shutil.copy("MANBH.dds", os.path.join(mod_dir, "textures", "Mantella-BH", f"{package_name}.dds"))

    # Crear el archivo comprimido
    zip_path = os.path.join("Stories", f"{package_name}.zip")
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root_dir, dirs, files in os.walk(mod_dir):
            for file in files:
                file_path = os.path.join(root_dir, file)
                zipf.write(file_path, os.path.relpath(file_path, mod_dir))

    # Eliminar la estructura de carpetas temporal
    shutil.rmtree(mod_dir)

    # Notificar que el proceso ha terminado
    messagebox.showinfo("Success", "The mod package has been created successfully!", parent=root)

# Botón para crear el mod para instalación
tk.Button(root, text="Create Mod for Installation", command=create_mod, bg='#4CAF50', fg='white', font=("Arial", 12)).grid(row=14, column=1, padx=10, pady=5, sticky="w")





#----------------------------------------------------------------------------------------------------------------------------
#
#----------------------------------------------------------------------------------------------------------------------------




# Ejecutar la aplicación
root.mainloop()



