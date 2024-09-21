from flask import Blueprint,render_template

upload_route = Blueprint('upload', __name__)

@upload_route.route('/')
def upload_file():
    """Upload do arquivo"""
    return render_template('upload.html')

@upload_route.route('/', methods=['POST'])
def upload_file_post():
    
    return

@upload_route.route('/<int:ocr_id>')
def obter_folha(ocr_id):
    """Obter folha processada"""
    pass

@upload_route.route('/<int:ocr_id>/edit')
def form_edit_folha(user_id):
    """Edição das informações na folha processada"""
    pass

@upload_route.route('/<int:user_id>/update', methods=['PUT'])
def obter_folhaOCR(user_id):
    """Enviar folha processada"""
    pass
