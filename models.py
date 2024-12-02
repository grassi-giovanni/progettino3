# Importiamo il modulo SQLAlchemy da Flask per interagire con il database in modo ORM (Object-Relational Mapping)
from flask_sqlalchemy import SQLAlchemy

# Creiamo un'istanza di SQLAlchemy che sarà usata per interagire con il database
db = SQLAlchemy()

# Definiamo il modello ListaSpesa che rappresenta la tabella nel database
class ListaSpesa(db.Model):
    # La colonna 'id' è un intero che sarà la chiave primaria della tabella
    id = db.Column(db.Integer, primary_key=True)
    
    # La colonna 'elemento' è una stringa con una lunghezza massima di 100 caratteri
    # 'nullable=False' significa che il valore per questa colonna non può essere nullo
    elemento = db.Column(db.String(100), nullable=False)
