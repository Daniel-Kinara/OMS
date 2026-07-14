# pyrefly: ignore [missing-import]
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QFrame,
    QTextEdit,
)

# pyrefly: ignore [missing-import]
from PyQt6.QtCore import Qt


class LogInspectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Log Facility Inspection")
        self.setMinimumWidth(480)
        self.setObjectName("OMSDialog")
        self._build()

    def _build(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(28, 24, 28, 24)
        root.setSpacing(16)

        title = QLabel("Log Facility Inspection")
        title.setObjectName("dialogTitle")
        root.addWidget(title)

        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setObjectName("dialogSep")
        root.addWidget(sep)

        root.addWidget(self._field_label("Area Inspected *"))
        self.area = QLineEdit()
        self.area.setPlaceholderText("e.g. Reception & Lobby")
        self.area.setObjectName("dialogInput")
        root.addWidget(self.area)

        root.addWidget(self._field_label("Inspection Status"))
        self.status = QComboBox()
        self.status.setObjectName("dialogCombo")
        self.status.addItems(["Passed", "Failed", "Needs Attention"])
        root.addWidget(self.status)

        root.addWidget(self._field_label("Inspector Name *"))
        self.inspector = QLineEdit()
        self.inspector.setPlaceholderText("Full name")
        self.inspector.setObjectName("dialogInput")
        root.addWidget(self.inspector)

        root.addWidget(self._field_label("Findings / Notes"))
        self.findings = QTextEdit()
        self.findings.setPlaceholderText("Describe findings…")
        self.findings.setObjectName("dialogInput")
        self.findings.setMaximumHeight(100)
        root.addWidget(self.findings)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        self.btnCancel = QPushButton("Cancel")
        self.btnCancel.setObjectName("btnDialogCancel")
        self.btnSubmit = QPushButton("Log Inspection")
        self.btnSubmit.setObjectName("btnDialogSubmit")
        btn_row.addWidget(self.btnCancel)
        btn_row.addWidget(self.btnSubmit)
        root.addLayout(btn_row)

        self.btnCancel.clicked.connect(self.reject)
        self.btnSubmit.clicked.connect(self._on_submit)

    def _field_label(self, text: str) -> QLabel:
        lbl = QLabel(text)
        lbl.setObjectName("dialogFieldLabel")
        return lbl

    def _on_submit(self):
        if not self.area.text().strip():
            self.area.setPlaceholderText("⚠ Area is required")
            return
        if not self.inspector.text().strip():
            self.inspector.setPlaceholderText("⚠ Inspector name is required")
            return
        # TODO: INSERT into maintenance_inspections table (MySQL)
        print(
            f"Inspection logged: "
            f"{self.area.text()} | "
            f"{self.status.currentText()} | "
            f"{self.inspector.text()}"
        )
        self.accept()
