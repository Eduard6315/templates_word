from Document_processing.document_processor import DocumentProcessor
from Document_processing.dataset_key import dataset
from settings import template_body_2, template_heading_1, template_heading_2, \
    template_body_1, template_bottom_1, \
    template_bottom_2



if __name__ == '__main__':
    """
     Cоздаем экземпляр класса DocumentProcessor
      и затем загружаем шаблоны документов через различные разделы
    """
    processor = DocumentProcessor()
    processor.load_template(template_heading_1, 0)
    processor.load_template(template_heading_2, 1)
    processor.load_template(template_body_1, 2)
    processor.load_template(template_body_2, 3)
    processor.load_template(template_bottom_1, 4)
    processor.load_template(template_bottom_2, 5)

    processor.process_dataset(dataset)