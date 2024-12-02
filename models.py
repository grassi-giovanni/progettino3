from flask_sqlalchemy import SQLAlchemy

# Inizializziamo l'oggetto db
db = SQLAlchemy()

# Definiamo la classe ListaSpesa che rappresenta la tabella nel database
class ListaSpesa(db.Model):
    # La colonna 'id' sarà di tipo intero (Integer) e sarà la chiave primaria della tabella
    id = db.Column(db.Integer, primary_key=True)
    
    # La colonna 'elemento' sarà di tipo stringa (String) con una lunghezza massima di 100 caratteri
    # La proprietà 'nullable=False' garantisce che ogni record abbia un valore per questa colonna
    elemento = db.Column(db.String(100), nullable=False)
