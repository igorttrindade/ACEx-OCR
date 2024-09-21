from pdf2image import convert_from_path
import easyocr, cv2, json, os
import numpy as np

pdf_path = f'C:\\Users\\igort\\OneDrive\\Desktop\\ACEx\\OCR\\controller\\folhapontoOCR2.pdf'

def save_ocr_results_to_json(results, page_number, json_path='output.json'):
    data = {
        "page": page_number,
        "extracted_texts": []
    }

    for (bbox, text) in results:
        entry = {
            "bbox": bbox,
            "text": text
        }
        data["extracted_texts"].append(entry)
    
    if os.path.exists(json_path):
        with open(json_path, 'r') as json_file:
            existing_data = json.load(json_file)
        existing_data.append(data)
    else:
        existing_data = [data]
    
    with open(json_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4, ensure_ascii=False)

image_pdf = convert_from_path(pdf_path, dpi=300)  # dpi=300 para boa qualidade

reader = easyocr.Reader(['pt'], gpu=True)

for i, page in enumerate(image_pdf):
    image_path = f'C:\\Users\\igort\\OneDrive\\Desktop\\ACEx\\OCR\\static\\preprocessoImage\\imagem_pre_processada_{i}.jpg'
    page.save(image_path, 'JPEG')
    image = cv2.imread(image_path)
    results = reader.readtext(image_path, paragraph=True)
    save_ocr_results_to_json(results, page_number=i, json_path='C:\\Users\\igort\\OneDrive\\Desktop\\ACEx\\OCR\\static\\jsonOutput\\ocr_results.json')
    for (bbox, text) in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple([int(val) for val in top_left])
        bottom_right = tuple([int(val) for val in bottom_right])
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 3)
        print(text)
    imagem_final_path = f'C:\\Users\igort\\OneDrive\\Desktop\\ACEx\\OCR\\static\\processadoImage\\imagem_processada_{i}.jpg'
    cv2.imwrite(imagem_final_path, image)
