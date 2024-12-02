# Importiamo i moduli necessari: Flask per creare l'app web,
# render_template per usare i template HTML, request per gestire i dati inviati tramite form,
# redirect e url_for per fare il reindirizzamento dopo le operazioni.
from flask import Flask, render_template, request, redirect, url_for
# Importiamo il modulo db e il modello ListaSpesa definiti nel file models.py
from models import db, ListaSpesa  

# Creiamo l'istanza dell'app Flask, che rappresenta l'applicazione web.
app = Flask(__name__)

# Configuriamo l'URI del database. In questo caso, stiamo usando SQLite
# con il file 'lista_spesa.db' che viene creato nella stessa cartella dell'app.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'

# Disabilitiamo il monitoraggio delle modifiche per risparmiare risorse
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inizializziamo l'oggetto db con l'app Flask
db.init_app(app)

# Con il contesto dell'app, creiamo tutte le tabelle nel database, 
# se non esistono già (inclusa la tabella ListaSpesa).
with app.app_context():
    db.create_all()

# Route per la pagina principale
@app.route('/')
def home():
    """
    Questa funzione gestisce la route principale ('/') e visualizza gli elementi
    salvati nel database. La lista degli elementi è passata al template HTML per
    la visualizzazione.
    """
    # Recuperiamo tutti gli elementi dalla tabella ListaSpesa nel database
    items = ListaSpesa.query.all()
    # Rendiamo il template 'index.html' passando la lista degli oggetti come variabile 'items'
    return render_template('index.html', items=items)

# Route per aggiungere un nuovo elemento
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    """
    Questa funzione gestisce la route '/aggiungi'. Quando un utente invia un 
    nuovo elemento tramite il form HTML, questo elemento viene aggiunto nel database.
    """
    # Otteniamo il valore dell'elemento dal form (l'input dell'utente)
    elemento = request.form.get('elemento')
    if elemento:  # Se l'utente ha inserito un valore non vuoto
        # Creiamo un nuovo oggetto ListaSpesa con il valore dell'elemento
        nuovo_elemento = ListaSpesa(elemento=elemento)
        # Aggiungiamo il nuovo elemento al database
        db.session.add(nuovo_elemento)
        # Salviamo la modifica nel database
        db.session.commit()
    # Dopo aver aggiunto l'elemento, reindirizziamo l'utente alla home
    return redirect(url_for('home'))

# Route per svuotare la lista (rimuovere tutti gli elementi)
@app.route('/svuota', methods=['POST'])
def svuota():
    """
    Questa funzione gestisce la route '/svuota'. Quando l'utente clicca il pulsante 
    per svuotare la lista, vengono eliminati tutti gli elementi dal database.
    """
    # Eliminiamo tutti gli elementi dalla tabella ListaSpesa
    ListaSpesa.query.delete()
    # Salviamo la modifica nel database
    db.session.commit()
    # Dopo aver svuotato la lista, reindirizziamo l'utente alla home
    return redirect(url_for('home'))

# Route per rimuovere un singolo elemento dalla lista
@app.route('/rimuovi/<int:id>', methods=['POST'])
def rimuovi(id):
    """
    Questa funzione gestisce la rimozione di un singolo elemento dalla lista.
    Quando l'utente clicca "Rimuovi" accanto a un elemento, viene eliminato dal database.
    """
    # Recuperiamo l'elemento da eliminare tramite il suo ID
    elemento = ListaSpesa.query.get(id)
    if elemento:  # Se l'elemento esiste nel database
        # Eliminiamo l'elemento dal database
        db.session.delete(elemento)
        # Salviamo la modifica nel database
        db.session.commit()
    # Dopo aver rimosso l'elemento, reindirizziamo l'utente alla home
    return redirect(url_for('home'))

# Avvio dell'app in modalità debug (utile per lo sviluppo e la risoluzione dei problemi)
if __name__ == "__main__":
    app.run(debug=True)
