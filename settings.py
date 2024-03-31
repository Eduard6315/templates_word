from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# Указываем пути для входных документов
template_heading_1 = BASE_DIR / 'document_ICONICASITE' / 'templates' / 'input' / 'template_heading_1.docx'
template_heading_2 = BASE_DIR / 'document_ICONICASITE' / 'templates' / 'input' / 'template_heading_2.docx'
template_body_1 = BASE_DIR / 'document_ICONICASITE' / 'templates' / 'input' / 'template_body_1.docx'
template_body_2 = BASE_DIR / 'document_ICONICASITE' / 'templates' / 'input' / 'template_body_2.docx'
template_bottom_1 = BASE_DIR / 'document_ICONICASITE' / 'templates' / 'input' / 'template_bottom_1.docx'
template_bottom_2 = BASE_DIR / 'document_ICONICASITE' / 'templates' / 'input' / 'template_bottom_2.docx'

# Указываем путь для выходных документов
output_directory = BASE_DIR / 'document_ICONICASITE' / 'templates' / 'output'
