from flask import Flask
from models import db, ListaSpesa  # Importiamo db e il modello ListaSpesa dal file models.py

# Crea l'app Flask
app = Flask(__name__)

# Configura l'URI del database (in questo caso un database SQLite locale chiamato 'lista_spesa.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'

# Disabilitiamo il monitoraggio delle modifiche per risparmiare risorse
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inizializziamo l'oggetto db con l'app
db.init_app(app)

# Eseguiamo il contesto dell'app per creare le tabelle se non esistono
with app.app_context():
    db.create_all()  # Crea le tabelle del database se non esistono

# Aggiungiamo una route di esempio per testare
@app.route('/')
def home():
    return "Benvenuto nella lista della spesa!"

# Aggiungiamo una route per visualizzare gli elementi nella lista
@app.route('/lista')
def lista():
    # Recupera tutti gli elementi dalla tabella ListaSpesa
    items = ListaSpesa.query.all()
    # Se non ci sono elementi, ritorniamo un messaggio
    if not items:
        return "La lista della spesa è vuota."
    # Altrimenti, mostriamo gli elementi
    return '<br>'.join([item.elemento for item in items])

# Esegui l'app in modalità di debug
if __name__ == "__main__":
    app.run(debug=True)
