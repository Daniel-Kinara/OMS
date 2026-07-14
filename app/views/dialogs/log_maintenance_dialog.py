# pyrefly: ignore [missing-import]
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QPushButton,
    QFrame,
)

# pyrefly: ignore [missing-import]
from PyQt6.QtCore import Qt


class LogMaintenanceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Log Maintenance Issue")
        self.setMinimumWidth(480)
        self.setObjectName("OMSDialog")
        self._build()

    def _build(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(28, 24, 28, 24)
        root.setSpacing(16)

        title = QLabel("Log Maintenance Issue")
        title.setObjectName("dialogTitle")
        root.addWidget(title)

        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setObjectName("dialogSep")
        root.addWidget(sep)

        # Issue title
        root.addWidget(self._field_label("Issue Title *"))
        self.issueTitle = QLineEdit()
        self.issueTitle.setPlaceholderText("e.g. Broken AC unit in Floor 2")
        self.issueTitle.setObjectName("dialogInput")
        root.addWidget(self.issueTitle)

        # Location
        root.addWidget(self._field_label("Location *"))
        self.location = QLineEdit()
        self.location.setPlaceholderText("e.g. Floor 2, Washroom B")
        self.location.setObjectName("dialogInput")
        root.addWidget(self.location)

        # Priority
        root.addWidget(self._field_label("Priority"))
        self.priority = QComboBox()
        self.priority.setObjectName("dialogCombo")
        self.priority.addItems(["Low", "Medium", "High", "Urgent"])
        root.addWidget(self.priority)

        # Description
        root.addWidget(self._field_label("Description"))
        self.description = QTextEdit()
        self.description.setPlaceholderText("Describe the issue in detail…")
        self.description.setObjectName("dialogInput")
        self.description.setMaximumHeight(100)
        root.addWidget(self.description)

        # Buttons
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        self.btnCancel = QPushButton("Cancel")
        self.btnCancel.setObjectName("btnDialogCancel")
        self.btnSubmit = QPushButton("Submit Request")
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
        if not self.issueTitle.text().strip():
            self.issueTitle.setPlaceholderText("⚠ Issue title is required")
            return
        if not self.location.text().strip():
            self.location.setPlaceholderText("⚠ Location is required")
            return
        # TODO: INSERT into maintenance_requests table (MySQL)
        print(
            f"Maintenance request submitted: "
            f"{self.issueTitle.text()} | "
            f"{self.location.text()} | "
            f"{self.priority.currentText()}"
        )
        self.accept()
