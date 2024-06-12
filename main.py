import sys
import os
import csv
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox

class DatabaseFinder:
    def __init__(self, folder_path, output_file_path):
        self.folder_path = folder_path
        self.output_file_path = output_file_path

    def find_and_write_db_lines(self):
        try:
            if not os.path.exists(self.folder_path):
                raise FileNotFoundError(f"Error: Directory not found - {self.folder_path}")
            with open(self.output_file_path, 'w', newline='') as csvfile:
                fieldnames = ['Folder Path', 'DB_DATABASE Value']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Write the header
                writer.writeheader()

                for env_file_path, db_value in self._get_database_values():
                    writer.writerow({'Folder Path': env_file_path, 'DB_DATABASE Value': db_value})
        
        except Exception as e:
            print(f"Error: {e}")

    def _get_database_values(self):
        for root, dirs, files in os.walk(self.folder_path):
            # Include hidden files and directories
            for file in files:
                if file.endswith(".env"):
                    env_file_path = os.path.join(root, file)
                    with open(env_file_path, 'r') as env_file:
                        for line in env_file:
                            if line.startswith("DB_DATABASE="):
                                # Extract the value after the '=' sign
                                db_value = line.split('=')[1].strip()
                                yield env_file_path, db_value

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Laravel Database Finder')
        self.setGeometry(100, 100, 600, 200)

        layout = QVBoxLayout()

        self.folderLabel = QLabel('Folder Path:', self)
        layout.addWidget(self.folderLabel)

        self.folderInput = QLineEdit(self)
        layout.addWidget(self.folderInput)

        self.folderButton = QPushButton('Browse...', self)
        self.folderButton.clicked.connect(self.browseFolder)
        layout.addWidget(self.folderButton)

        self.outputLabel = QLabel('Output File Path:', self)
        layout.addWidget(self.outputLabel)

        self.outputInput = QLineEdit(self)
        layout.addWidget(self.outputInput)

        self.outputButton = QPushButton('Browse...', self)
        self.outputButton.clicked.connect(self.browseOutputFile)
        layout.addWidget(self.outputButton)

        self.runButton = QPushButton('Run', self)
        self.runButton.clicked.connect(self.runDatabaseFinder)
        layout.addWidget(self.runButton)

        self.setLayout(layout)

    def browseFolder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folder:
            self.folderInput.setText(folder)

    def browseOutputFile(self):
        output_file, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV Files (*.csv)')
        if output_file:
            self.outputInput.setText(output_file)

    def runDatabaseFinder(self):
        folder_path = self.folderInput.text()
        output_file_path = self.outputInput.text()
        if not folder_path or not output_file_path:
            QMessageBox.warning(self, 'Input Error', 'Please provide both folder and output file paths.')
            return

        try:
            database_finder = DatabaseFinder(folder_path, output_file_path)
            database_finder.find_and_write_db_lines()
            QMessageBox.information(self, 'Success', 'Database paths extracted successfully!')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f"Error: {e}")

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

