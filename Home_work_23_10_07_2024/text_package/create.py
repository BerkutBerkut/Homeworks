from docx import Document

def create_word_file(text, filename):
    
    doc = Document()
    doc.add_paragraph(text)
    doc.save(filename)
    print(f"Файл {filename} успешно создан!")
