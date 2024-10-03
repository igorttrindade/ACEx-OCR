from pdf2image import convert_from_path
import easyocr, cv2, json, os
import numpy as np
import re


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
        imagem_final_path = f'C:\\Users\\igort\\OneDrive\\Desktop\\ACEx\\OCR\\static\\processadoImage\\imagem_processada_{i}.jpg'
        cv2.imwrite(imagem_final_path, image)
    return " ".join(extracted_texts)

def process_folha_ponto(text):
    # Regex para identificar datas (números de 1 a 31)
    date_pattern = re.compile(r'\b(0?[1-9]|[12][0-9]|3[01])\b')

    # Regex para identificar horários no formato "HH:MM" (inclui variantes com espaços e caracteres não numéricos)
    time_pattern = re.compile(r'\b(\d{1,2}[:;]\d{2})\b')

    # Dividir o texto em partes
    lines = text.split()

    folha_ponto = []
    current_day = None
    current_record = {}

    for part in lines:
        # Verificar se é uma data
        if date_pattern.fullmatch(part):
            # Salvar o registro anterior, se houver
            if current_day is not None and current_record:
                folha_ponto.append(current_record)

            # Iniciar um novo registro
            current_day = part
            current_record = {
                "data": current_day,
                "entrada": None,
                "inicio_intervalo": None,
                "fim_intervalo": None,
                "saida": None,
                "hora_extra": None,
            }

        # Verificar se é um horário
        elif time_pattern.fullmatch(part):
            # Preencher os campos da folha de ponto de forma sequencial
            if current_record["entrada"] is None:
                current_record["entrada"] = part
            elif current_record["inicio_intervalo"] is None:
                current_record["inicio_intervalo"] = part
            elif current_record["fim_intervalo"] is None:
                current_record["fim_intervalo"] = part
            elif current_record["saida"] is None:
                current_record["saida"] = part
            elif current_record["hora_extra"] is None:
                current_record["hora_extra"] = part

    # Salvar o último registro
    if current_day is not None and current_record:
        folha_ponto.append(current_record)

    # Salvar em um arquivo JSON
    json_path = 'folha_ponto.json'
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(folha_ponto, json_file, indent=4, ensure_ascii=False)

    return folha_ponto