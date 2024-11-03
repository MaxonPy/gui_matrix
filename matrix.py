import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit,
    QVBoxLayout, QHBoxLayout, QMessageBox, QFileDialog
)
import random


class ArrayReversalApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        input_layout = QHBoxLayout()

        # Поле ввода для массива
        self.array_label = QLabel("Массив(через запятую):")
        self.array_input = QLineEdit()
        input_layout.addWidget(self.array_label)
        input_layout.addWidget(self.array_input)

        # K и L поля ввода
        self.k_label = QLabel("K (начальный индекс)")
        self.k_input = QLineEdit()
        self.l_label = QLabel("L (конечный индекс)")
        self.l_input = QLineEdit()

        k_l_layout = QHBoxLayout()
        k_l_layout.addWidget(self.k_label)
        k_l_layout.addWidget(self.k_input)
        k_l_layout.addWidget(self.l_label)
        k_l_layout.addWidget(self.l_input)

        # Поле вывода
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        # Кнопки
        self.process_button = QPushButton("Выполнить")
        self.load_button = QPushButton("Загрузить из файла")
        self.save_button = QPushButton("Сохранить в файл")
        self.random_button = QPushButton("Рандомный массив")

        # Соединение кнопок с функциями
        self.process_button.clicked.connect(self.alg_matrix)
        self.load_button.clicked.connect(self.load_from_file)
        self.save_button.clicked.connect(self.save_to_file)
        self.random_button.clicked.connect(self.random_array)

        # Добавление виджетов в окно
        layout.addLayout(input_layout)
        layout.addLayout(k_l_layout)
        layout.addWidget(self.output_text)
        layout.addWidget(self.process_button)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.load_button)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.random_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        self.setWindowTitle("Матрица")
        self.setGeometry(300, 300, 600, 400)

    def alg_matrix(self):
        try:
            array = list(map(int, self.array_input.text().split(',')))
            k = int(self.k_input.text()) - 1
            l = int(self.l_input.text()) - 1

            if not (0 <= k < l < len(array)):
                raise ValueError("K и L должны находиться в промежутке 1 ≤ K < L ≤ N")

            array[k:l + 1] = array[k:l + 1][::-1]
            self.output_text.setPlainText(f"{array}")

        except ValueError as e:
            QMessageBox.critical(self, "Ошибка", f"Неверный ввод: {e}")

    def load_from_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Текстовые файлы (*.txt)")
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    data = file.read().splitlines()
                    if len(data) >= 3:
                        self.array_input.setText(data[0])
                        self.k_input.setText(data[1])
                        self.l_input.setText(data[2])
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл: {e}")

    def random_array(self):
        try:
            n = random.randint(5, 20)
            array = [random.randint(1, 100) for _ in range(n)]
            k = random.randint(1, n - 1)
            l = random.randint(k + 1, n)

            self.array_input.setText(",".join(map(str, array)))
            self.k_input.setText(str(k))
            self.l_input.setText(str(l))

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {e}")

    def save_to_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Текстовые файлы (*.txt)")
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    array = self.array_input.text()
                    k = self.k_input.text()
                    l = self.l_input.text()
                    result = self.output_text.toPlainText()
                    file.write(f"{array}\n{k}\n{l}\n{result}")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArrayReversalApp()
    window.show()
    sys.exit(app.exec_())
