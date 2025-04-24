import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout,QPushButton, QLabel, QFrame, QListWidget, QAbstractItemView,QHBoxLayout, QFileDialog,QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
import os
from pypdf import PdfWriter



class PDFMerger(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Unir PDFs")
        self.setFixedSize(400,300)

        #Creates the main widget and its layout

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)

        self.pdf_files = []

        # Add pdf button

        self.add_button = QPushButton("Adicionar PDFs")
        self.add_button.setStyleSheet("background-color: #2596be; font-weight: bold; padding: 8px;")
        self.main_layout.addWidget(self.add_button)

        #Frame to show file list

        frame_area = QFrame()
        frame_area.setFrameShape(QFrame.StyledPanel)
        frame_area.setFrameShadow(QFrame.Raised)

        frame_layout = QVBoxLayout(frame_area)
        frame_layout.setContentsMargins(10,10,10,10)

        #Area title
        list_label = QLabel("Ordene os arquivos para juntá-los")
        list_label.setFont(QFont("", weight=QFont.Bold))
        frame_layout.addWidget(list_label)

        #Draggable list
        self.file_list = QListWidget()
        self.file_list.setDragDropMode(QAbstractItemView.InternalMove)
        self.file_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.file_list.setMinimumHeight(200)
        frame_layout.addWidget(self.file_list)

        # Merge PDF & Remove itens buttons

        list_buttons_layout = QHBoxLayout()

        self.remove_button = QPushButton("Remover")
        self.remove_button.setStyleSheet("font-weight: bold; padding: 8px;")
        list_buttons_layout.addWidget(self.remove_button)
    
        self.merge_button = QPushButton("Unir PDFs")
        self.merge_button.setStyleSheet("background-color:#15a457; font-weight: bold; padding: 8px;")
        list_buttons_layout.addWidget(self.merge_button)

        frame_layout.addLayout(list_buttons_layout)

        # Add all widgets to main widget
        self.main_layout.addWidget(frame_area)

        # Connect buttons to functions
        self.add_button.clicked.connect(self.browse_files)
        self.merge_button.clicked.connect(self.merge_pdfs)
        self.remove_button.clicked.connect(self.remove_item)
        


    def browse_files(self):
      files,_ = QFileDialog.getOpenFileNames(
                self,
                "Selecionar arquivos PDF",
                "",
                "Arquivos PDF (*.pdf)"
      ) 
      
      if files:
         for file in files:
            if file not in self.pdf_files:
                self.pdf_files.append(file)
                self.file_list.addItem(os.path.basename(file))

    def merge_pdfs(self):
       if not self.pdf_files:
          QMessageBox.warning(self,"Aviso","Nenhum PDF selecionado")
          return
       
       save_path,_ = QFileDialog.getSaveFileName(
          self,
          "Salvar PDF criado",
          "pdf-criado.pdf",
          "Arquivos PDF (*.pdf)"
       )

       if not save_path:
          return
       

       ordered_files = []

       for i in range(self.file_list.count()):
          item_name = self.file_list.item(i).text()
          for file_name in self.pdf_files:
              if os.path.basename(file_name) == item_name:
                 ordered_files.append(file_name)
                 break        

       merger = PdfWriter()
       for pdf in ordered_files:
          merger.append(pdf)
       merger.write(save_path)
       merger.close()
       QMessageBox.information(self,"Sucesso",f"PDF criado com sucesso em :\n{save_path}")
       os.startfile(save_path) 



    def remove_item(self):
         selected_items = self.file_list.selectedItems()
         if not selected_items:
            return
         for pdf_name in selected_items:
            item_line = self.file_list.row(pdf_name)
            self.file_list.takeItem(item_line)

            item_text = pdf_name.text()
            for path in self.pdf_files:
               if os.path.basename(path) == item_text:
                  self.pdf_files.remove(path)
                  break 
       



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFMerger()
    window.show()
    sys.exit(app.exec())

