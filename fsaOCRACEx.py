from pdf2image import convert_from_path
import easyocr
import cv2

# Caminho do arquivo PDF
pdf_path = 'folhapontoOCR2.pdf'

# Converter o PDF para uma lista de imagens
image_pdf = convert_from_path(pdf_path, dpi=1200)  # dpi=300 para boa qualidade

# Inicializar o leitor EasyOCR
reader = easyocr.Reader(['pt'],gpu=True)  # 'pt' para Português

# Processar cada página
for i, page in enumerate(image_pdf):
    
    image_path = f'imagem_pre_processada{i}.jpg'
    page.save(image_path, 'JPEG')
    
    # Carregar a imagem para o OpenCV
    image = cv2.imread(image_path)
    
    results = reader.readtext(image_path, paragraph=True)
    
    for (bbox, text) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple([int(val) for val in top_left])
        bottom_right = tuple([int(val) for val in bottom_right])
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 3)
        print(text)
    
    imagem_final_path = f'imagem_processada{i}.jpg'
    cv2.imwrite(imagem_final_path, image)