from flask import Flask, render_template, g, request, make_response, redirect, url_for
import templates, db
from datetime import date
from functools import wraps


app = Flask(__name__)

# Fonction permettant d'autoriser l'accès à certains endpoint uniquement si l'utilisateur est connecté
# Encapsule la fonction d'origine
# Un formulaire basique d'authentification et compare avec les valeurs présentes dans la condition (pas dynamique avec la db)
def auth_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'serge' and auth.password == 'lama':
            return f(*args, **kwargs)
        return make_response("Nous ne parvenons pas à vérifier vos information", 401, {'WWW-Authenticate' : 'Basic realm="Veuillez vous connecter"'})
    return wrap

#Fonction de routage : 
# - réception d'une requête sur localhost:5000/
# - Signature de la méthode "index()"
# - Logique python (traitements à effectuer), et retour de fonctions (dans ce cas affichage d'un template paramétré)
@app.route("/")
def index():
        d = date.today().isoformat()
        return render_template("home.html", la_date = d, lamas = db.findAll("*")) 

@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/produits")
def produits():
    return render_template("produits/index.html", lamas = db.findLama("*")) 

@app.route("/login")
@auth_required
def login():
    return redirect(url_for('index'))

@app.route("/produit/<name>")
def detail_produit(name):
    return render_template("produits/detail.html", produit = db.findLama(name))

if __name__ == "__main__":
    app.run(debug=True)