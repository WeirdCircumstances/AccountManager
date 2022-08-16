Dieses Tool dient dazu neue Accounts bei innovative-students.de für unsere [Akademie](https://www.it-fitness.de/Akademie/Intensivkurse_Gefragte_Jobprofile_und_Skills/2668_Anme) anzulegen.
Es ist im Dezember 2020 aus der Not heraus entstanden, da in sehr kurzer Zeit viele hundert Konten angelegt und Gruppen zugewiesen werden mussten.  
Um den Aufwand zu reduzieren entstand zunächst ein Tool auf der Basis von Selenium mit einfacher grafischer Oberfläche. Da der Prozess mit aber sehr fehleranfällig war, 
wurde Selenium Stück für Stück wieder ausgebaut, bis es zuletzt gar nicht mehr verwendet wurde.
Aktuell werden die Accounts mit Hilfe der Azure CLI verwaltet. Diese sollte also installiert und mit dem Konto von innovative-students.de verbunden sein.

Um das Programm einzurichten, kann wie folgt vorgegangen werden:

Login auf innovative-students.de  
`az login`  
  
Neues virtuelle Umgebung anlegen, mit:  
`python3 -m venv /path/to/new/virtual/environment`  
oder einer anderen Methode.  
  
`pip install -r requirements.txt`  
oder  
alternativ mit poetry  
`cat requirements.txt | xargs poetry add`  
  
Start mit  
`python main.py`  
