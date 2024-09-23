from pdf2image import convert_from_path
import easyocr, cv2, json, os
import numpy as np


def leituraOCR(pdf_path):
    reader = easyocr.Reader(['pt'], gpu=True)
    extracted_texts = []
    image_pdf = convert_from_path(pdf_path, dpi=300)  # dpi=300 para boa qualidade

    for i, page in enumerate(image_pdf):
        image_path = f'C:\\Users\\igort\\OneDrive\\Desktop\\ACEx\\OCR\\static\\preprocessoImage\\imagem_pre_processada_{i}.jpg'
        page.save(image_path, 'JPEG')
        image = cv2.imread(image_path)
        results = reader.readtext(image_path, paragraph=True)
        for (bbox, text) in results:
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = tuple([int(val) for val in top_left])
            bottom_right = tuple([int(val) for val in bottom_right])
            cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 3)
            extracted_texts.append(text)
            print(text)
        imagem_final_path = f'C:\\Users\igort\\OneDrive\\Desktop\\ACEx\\OCR\\static\\processadoImage\\imagem_processada_{i}.jpg'
        cv2.imwrite(imagem_final_path, image)
    return " ".join(extracted_texts)
