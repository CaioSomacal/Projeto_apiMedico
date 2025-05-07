class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/medicos_db'  # Altere conforme seu banco de dados
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'mysecretkey'
