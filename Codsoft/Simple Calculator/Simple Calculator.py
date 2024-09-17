import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QMessageBox

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Simple Calculator')
        self.setGeometry(100, 100, 300, 200)
        
        self.num1_input = QLineEdit(self)
        self.num1_input.setPlaceholderText("Enter first number")
        
        self.num2_input = QLineEdit(self)
        self.num2_input.setPlaceholderText("Enter second number")
        
        self.operation_dropdown = QComboBox(self)
        self.operation_dropdown.addItems(["+", "-", "*", "/"])
        
        self.result_label = QLabel("Result: ", self)
        
        self.calc_button = QPushButton("Calculate", self)
        self.calc_button.clicked.connect(self.perform_calculation)
        
        layout = QVBoxLayout()
        layout.addWidget(self.num1_input)
        layout.addWidget(self.num2_input)
        layout.addWidget(self.operation_dropdown)
        layout.addWidget(self.calc_button)
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)
        
    def perform_calculation(self):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())
            operation = self.operation_dropdown.currentText()
            
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    raise ZeroDivisionError("Cannot divide by zero")
            
            self.result_label.setText(f"Result: {result}")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numbers.")
        except ZeroDivisionError as e:
            QMessageBox.warning(self, "Math Error", str(e))

def main():
    app = QApplication(sys.argv)
    
    calculator = CalculatorApp()
    calculator.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
