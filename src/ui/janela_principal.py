import sys
from PySide6.QtWidgets import (
    QMainWindow, 
    QApplication, 
    QSplitter,    
    QTextEdit,    
    QFileDialog
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction 
from src.core.leitor_pdf import LeitorPDF

class JanelaPrincipal(QMainWindow):
    """
    A classe principal da nossa interface gráfica (GUI).
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MarginNote")
        self.resize(1024, 768)
        
        self.leitor_pdf = None
        self.note_editor = None

        self.configurar_ui()
        self.configurar_menus()

    def configurar_ui(self):
        """Configura os widgets centrais da aplicação."""
        splitter = QSplitter(Qt.Horizontal)

        self.leitor_pdf = LeitorPDF()
        
        self.note_editor = QTextEdit()
        self.note_editor.setPlaceholderText("Suas notas aqui...") 

        splitter.addWidget(self.leitor_pdf)
        splitter.addWidget(self.note_editor)

        splitter.setSizes([600, 400]) 

        self.setCentralWidget(splitter)

    def configurar_menus(self):
        """Cria e configura a barra de menus e suas ações."""
        abrir_action = QAction("Abrir...", self)
        abrir_action.setShortcut("Ctrl+O")
        abrir_action.triggered.connect(self.abrir_pdf)

        menu_bar = self.menuBar()
        menu_arquivo = menu_bar.addMenu("Arquivo")
        menu_arquivo.addAction(abrir_action)

    def abrir_pdf(self):
        """Abre uma caixa de diálogo para o usuário selecionar um arquivo PDF."""
        caminho_arquivo, _ = QFileDialog.getOpenFileName(
            self, 
            "Abrir PDF", 
            "", 
            "Arquivos PDF (*.pdf)"
        )

        if caminho_arquivo:
            self.leitor_pdf.abrir_pdf(caminho_arquivo)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())