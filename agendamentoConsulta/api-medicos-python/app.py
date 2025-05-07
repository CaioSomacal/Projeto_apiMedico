from flask import Flask
from routes.medicoRoutes import medico_routes  # Importando o blueprint

app = Flask(__name__)
app.register_blueprint(medico_routes, url_prefix='/api')  # Registrando o blueprint com um prefixo de URL

if __name__ == "__main__":
    app.run(debug=True)
