import fitz  # O nome da biblioteca PyMuPDF
from PySide6.QtWidgets import QScrollArea, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt

class LeitorPDF(QScrollArea):
    """
    Este widget é responsável por abrir e exibir as páginas de um arquivo PDF.
    Ele herda de QScrollArea para fornecer barras de rolagem.
    """
    def __init__(self):
        super().__init__()

        self.setWidgetResizable(True) 

        self.container = QWidget()
        self.setWidget(self.container) # Define o container como widget da ScrollArea

        self.layout_container = QVBoxLayout(self.container)
        
        # O QLabel que efetivamente mostrará a imagem da página
        self.label_pagina = QLabel("Abra um arquivo PDF usando o menu 'Arquivo > Abrir...'.")
        self.label_pagina.setAlignment(Qt.AlignCenter) # Centraliza o texto/imagem
        
        self.layout_container.addWidget(self.label_pagina)

        self.doc = None # Onde guardaremos o documento PDF aberto
        self.pagina_atual = 0

    def abrir_pdf(self, caminho_arquivo):
        """Abre um documento PDF e exibe a primeira página."""
        try:
            self.doc = fitz.open(caminho_arquivo)
            print(f"Documento '{caminho_arquivo}' aberto com {self.doc.page_count} páginas.")
            
            self.pagina_atual = 0
            self.mostrar_pagina(self.pagina_atual)
            return True
        
        except Exception as e:
            self.label_pagina.setText(f"Erro ao abrir o PDF: {e}")
            self.doc = None
            return False

    def mostrar_pagina(self, numero_pagina):
        """Renderiza e exibe uma página específica do PDF."""
        if not self.doc or numero_pagina < 0 or numero_pagina >= self.doc.page_count:
            return

        pagina = self.doc.load_page(numero_pagina)
        
        zoom = 2.0 # 200% de zoom
        matriz = fitz.Matrix(zoom, zoom)
        pix = pagina.get_pixmap(matrix=matriz)
        
        imagem = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
        
        qpixmap = QPixmap.fromImage(imagem)

        self.label_pagina.setPixmap(qpixmap)