# Importiamo SQLAlchemy dal pacchetto flask_sqlalchemy per interagire con il database
from flask_sqlalchemy import SQLAlchemy

# Configuriamo l'URI del database (in questo caso, un database SQLite locale chiamato 'lista_spesa.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'

# Disabilitiamo il monitoraggio delle modifiche del database, in modo da risparmiare risorse
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inizializziamo l'oggetto SQLAlchemy con l'app Flask. Questo collega l'applicazione Flask al database.
db.init_app(app)

# Eseguiamo il contesto dell'applicazione per assicurarsi che tutte le operazioni vengano eseguite all'interno di un contesto applicativo.
with app.app_context():
    # Creiamo tutte le tabelle del database definite nei modelli. Questo crea il database 'lista_spesa.db' se non esiste.
    db.create_all()
