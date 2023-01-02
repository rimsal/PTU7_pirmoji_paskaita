from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/pasisveikinti/<vardas>")
def pasisveikinti(vardas):
    return render_template("pasisveikinimas.html", vardas=vardas)


@app.route("/sveikaspasauli/")
def sveikas_pasauli():
    return render_template("hello_world.html")


@app.route("/skaiciavimai/")
def skaiciavimai():
    return render_template("skaiciavimai.html")


@app.route("/zmones/")
def vardai():
    masyvas = ["Kajus", "Mila", "Nora", "Adamas", "Ieva"]
    return render_template("zmones.html", vardai=masyvas)

@app.route("/login/", methods=['GET', 'POST'])
def prisijungimas():
    if request.method == "GET":
        return render_template('login.html')
    if request.method == "POST":
        vardas = request.form['fname']
        return render_template("greetings.html", vardas=vardas)


if __name__ == "__main__":
    app.run(debug=True)
