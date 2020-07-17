Groupe Alpashop : 
- BERNARD Mathis
- BOUVEYRON Nicolas

La connexion est codée en brut car pas réussi dans le temps imparti à l'implémenter de manière dynamique avec la DB
- user name : serge
- password : lama

Le projet comporte :
- La connexion (très basique mais présente)
- La liste des animaux (lamas / alpagas) gérée de manière dynamique
- La liste des lamas uniquement gérée de manière dynamique également
- Le détail pour un animal était en cours mais pas finalisé (bugs et soucis rencontrés)
- Page "about"


Petit mot sur notre approche du projet :

Le projet comporte un dossier template où sont stockées toutes nos vues utilisant le moteur de template Jinja
Les routes sont définies au niveau du fichier app.py
Le fichier db.py fait office de couche permettant la communication avec la DB, il possède des méthodes qui sont utilisées depuis la couche de routage (app.py)
Le fichier alpashop.db est notre base de données SQLITE