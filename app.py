from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "123abc"  # nécessaire pour les messages flash (formulaire)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cv")
def cv():
    return render_template("cv.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        nom = request.form["nom"]
        message = request.form["message"]
        print(f"[CONTACT] Message reçu de {nom} : {message}")
        flash("Message bien reçu. Merci !")
        return redirect("/contact")
    return render_template("contact.html")

@app.route("/objectif")
def objectif():
    return render_template("objectif.html")

@app.route("/projets")
def projets():
    return render_template("projets.html")

# ✅ On déplace ça ici (avant la ligne "run")
@app.route("/lettre")
def lettre():
    return render_template("lettre.html")

# Lancement de l'app
if __name__ == "__main__":
    app.run(debug=True)
