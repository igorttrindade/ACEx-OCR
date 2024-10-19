import os
from flask import Blueprint,render_template,request,current_app, session, redirect, url_for
from werkzeug.utils import secure_filename
from controller.ocr import leituraOCR, process_folha_ponto

upload_route = Blueprint('upload', __name__)

@upload_route.route('/')
def upload_file():
    
    return render_template('upload.html')

@upload_route.route('/process_ocr', methods=['POST'])
def upload_file_post():
    if 'arquivo' not in request.files:
        return 'Nenhum arquivo foi enviado.', 400
    
    file = request.files['arquivo']
    if file.filename == '':
        return 'Nenhum arquivo selecionado.', 400

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        ocr_result = leituraOCR(filepath)
        folha_ponto = process_folha_ponto(ocr_result)
        return render_template('process_ocr.html', ocr_text=folha_ponto)

    return 'Erro ao processar o arquivo.', 500
