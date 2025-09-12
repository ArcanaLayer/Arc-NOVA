from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
import random

app = QApplication([])

# Main container
window = QWidget()
window.setWindowTitle("ARC-Nova Notification")

layout = QVBoxLayout(window)

# Label that updates
label = QLabel("ARC-Nova event incoming...stand by")
layout.addWidget(label)

# Button to randomize the message
def update_message():
    messages = [
        "ARC-Nova initializing sequence...",
        "NOVA layer calibration complete.",
        "ARC-Nova signal detected — preparing...",
        "NOVA protocols engaged.",
        "Awaiting ARC-Nova confirmation..."
    ]
    label.setText(random.choice(messages))

button = QPushButton("Update ARC-Nova Status")
button.clicked.connect(update_message)
layout.addWidget(button)

window.setLayout(layout)
window.show()

app.exec()
