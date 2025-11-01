import sys
from PySide6.QtWidgets import (
    QMainWindow, 
    QApplication, 
    QSplitter,    # Importa o divisor
    QTextEdit,    # Importa o campo de texto
    QWidget       # Importa o widget genérico (nosso placeholder)
)
from PySide6.QtCore import Qt

class JanelaPrincipal(QMainWindow):
    """
    A classe principal da nossa interface gráfica (GUI).
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MarginNote")
        self.resize(1024, 768) # Necessária alteração

        splitter = QSplitter(Qt.Horizontal)

        self.pdf_viewer_placeholder = QWidget()
        
        self.note_editor = QTextEdit()
        self.note_editor.setPlaceholderText("Suas notas aqui...") # Um texto de ajuda

        splitter.addWidget(self.pdf_viewer_placeholder)
        splitter.addWidget(self.note_editor)

        splitter.setSizes([600, 400]) # Valores que somam 1000 são fáceis de entender

        self.setCentralWidget(splitter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())