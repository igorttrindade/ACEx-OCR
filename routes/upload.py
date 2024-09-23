import os
from flask import Blueprint,render_template,request,current_app, jsonify
from werkzeug.utils import secure_filename
from controller.ocr import leituraOCR

upload_route = Blueprint('upload', __name__)

@upload_route.route('/')
def upload_file():
    """Upload do arquivo"""
    return render_template('upload.html')

@upload_route.route('/process_ocr', methods=['POST'])
def upload_file_post():
    if 'arquivo' not in request.files:
        return 'Nenhum arquivo foi enviado.'
    file = request.files['arquivo']
    if file.filename == '':
        return 'Nenhum arquivo selecionado.'

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath) 
        ocr_result = leituraOCR(filepath)
    return render_template('process_ocr.html',ocr_text=ocr_result)

@upload_route.route('/<int:ocr_id>/edit')
def form_edit_folha(user_id):
    """Edição das informações na folha processada"""
    pass

@upload_route.route('/<int:user_id>/update', methods=['PUT'])
def obter_folhaOCR(user_id):
    """Enviar folha processada"""
    pass
