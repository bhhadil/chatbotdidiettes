from flask import Flask, request, render_template

app = Flask(__name__)

# --- Fonction pour calculer le prix total ---
def calculer_total(prix_euro, type_article):
    taux_change = 4.5  # 1€ = 4.5 DT
    frais_transport = {
        "sac": 2,
        "chaussure": 2.5,
        "accessoire": 1,
        "vetement_legere": 2,
        "vetement_lourd": 2.5
    }

    prix_dt = prix_euro * taux_change
    frais = frais_transport.get(type_article.lower(), 0)
    total = prix_dt + frais
    return round(total, 2)  # arrondi à 2 chiffres

# --- Page principale ---
@app.route("/", methods=["GET", "POST"])
def index():
    total = None
    if request.method == "POST":
        try:
            prix_euro = float(request.form["prix_euro"])
            type_article = request.form["type_article"]
            total = calculer_total(prix_euro, type_article)
        except ValueError:
            total = "Erreur : prix invalide"
    return render_template("index.html", total=total)

# --- Lancement du serveur ---
if __name__ == "__main__":
    # host=0.0.0.0 pour qu'il soit accessible via ngrok ou Render
    app.run(host="0.0.0.0", port=5000, debug=True)
