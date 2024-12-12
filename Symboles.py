import sys
import tkinter as tk
import pyperclip

class Buttonn(tk.Frame):
    def __init__(self, parent, car, text, max_width):
        super().__init__(parent)
        self.car = car
        
        self.button = tk.Button(self, text=car, command=self.copy_car, width=max_width)
        self.button.grid(row=0, column=0)
        
        self.label = tk.Label(self, text=text)
        self.label.grid(row=0, column=1)

    def copy_car(self):
        pyperclip.copy(self.car)

def resource_path(relative_path):
    # Déterminer le chemin absolu du fichier bg.png
    # Utilisé lorsque le script est exécuté via PyInstaller
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    # Utilisé lorsque le script est exécuté directement
    return os.path.join(os.path.abspath("."), relative_path)


ini_file = resource_path("ini.txt")
# Lecture du contenu du fichier d'init
with open(ini_file, 'r', encoding='utf-8') as ini_file:
    content = [line.strip().split(' ', 1) for line in ini_file]
    
for line in content:
    if 'col_nbr' in line:
        nbr_of_col = int(content[0][1])
    else:
        nbr_of_col = 2

char_list_file = resource_path("char_list.txt")
# Lecture du contenu du fichier des caractères
with open(char_list_file, 'r', encoding='utf-8') as char_list:
    content = [line.strip().split(' ', 1) for line in char_list]

# Détermination du nombre de colonnes en fonction du nombre total de boutons et du nombre maximal de boutons par colonne
total_buttons = len(content)
# max_per_column = 2
# num_columns = -(-total_buttons // max_per_column)  # Division entière avec arrondi à l'entier supérieur
max_per_column = total_buttons // nbr_of_col + 1
num_columns = nbr_of_col

# Détermination de la largeur maximale parmi tous les textes des boutons
max_button_width = max(len(car) for car, _ in content)

# Création de la fenêtre principale
root = tk.Tk()
root.title('Symboles')
icone_file = resource_path('icon.ico')
root.iconbitmap(icone_file)

# Création des boutons à partir des caractères lus dans le fichier
for index, (car, text) in enumerate(content):
    row = index % max_per_column
    column = index // max_per_column * 2  # Multiplier par 2 pour laisser de la place pour le label
    
    button = Buttonn(root, car, text, max_button_width)
    button.grid(row=row, column=column, sticky='w')

# Configuration des colonnes pour qu'elles s'étendent à la taille maximale de leurs composants
for i in range(num_columns * 2):  # Multiplier par 2 pour tenir compte des colonnes de labels
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
