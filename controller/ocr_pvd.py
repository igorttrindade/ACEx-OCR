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

    # Regex para identificar horários no formato "HH:MM" ou "HH.MM"
    time_pattern = re.compile(r'\b(\d{1,2}[:.]\d{2})\b')

    # Dividir o texto extraído em partes
    lines = text.split()

    folha_ponto = []
    current_day = None
    current_record = {}

    def is_valid_time(time_str):
        """Verifica se o horário está no intervalo plausível de 00:00 a 23:59."""
        try:
            # Substitui '.' por ':' se necessário
            time_str = time_str.replace('.', ':')
            hours, minutes = map(int, time_str.split(':'))
            return 0 <= hours < 24 and 0 <= minutes < 60
        except ValueError:
            return False

    for part in lines:
        # Verificar se o valor é uma data
        if date_pattern.fullmatch(part):
            # Se já houver um registro em andamento, salvar antes de iniciar o novo
            if current_day is not None and current_record:
                folha_ponto.append(current_record)

            # Iniciar novo registro para a nova data
            current_day = part
            current_record = {
                "data": current_day,
                "entrada": None,
                "inicio_intervalo": None,
                "fim_intervalo": None,
                "saida": None,
                "hora_extra": None,
            }

        # Verificar se o valor é um horário válido
        elif time_pattern.fullmatch(part):
            # Corrigir formato se necessário e validar
            if is_valid_time(part):
                part = part.replace('.', ':')
                # Preencher os campos de horário sequencialmente
                if current_record["entrada"] is None:
                    current_record["entrada"] = part
                elif current_record["inicio_intervalo"] is None:
                    current_record["inicio_intervalo"] = part
                elif current_record["fim_intervalo"] is None:
                    current_record["fim_intervalo"] = part
                elif current_record["saida"] is None:
                    current_record["saida"] = part
                else:
                    # Preencher hora extra se já houver todos os outros horários
                    current_record["hora_extra"] = part

    # Adicionar o último registro ao final
    if current_day is not None and current_record:
        folha_ponto.append(current_record)

    # Remover registros incompletos (opcional)
    folha_ponto = [record for record in folha_ponto if record["entrada"]]

    # Salvar em arquivo JSON para referência
    json_path = 'folha_ponto.json'
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(folha_ponto, json_file, indent=4, ensure_ascii=False)

    return folha_ponto
