from flask import Blueprint

Provisional = Blueprint('Provisional', __name__)

@Provisional.route('/blueprint')
def blueprint():
    return "blueprint"
