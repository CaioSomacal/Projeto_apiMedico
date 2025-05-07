from flask import Blueprint
from controllers.medicoController import create_medico, get_medicos, get_medico, update_medico, delete_medico

medico_routes = Blueprint('medico_routes', __name__)

# Rotas
medico_routes.route('/medicos', methods=['GET'])(get_medicos)
medico_routes.route('/medico/<int:id>', methods=['GET'])(get_medico)
medico_routes.route('/medicos', methods=['POST'])(create_medico)
medico_routes.route('/medico/<int:id>', methods=['PUT'])(update_medico)
medico_routes.route('/medico/<int:id>', methods=['DELETE'])(delete_medico)
