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
)


class RegisterVisitorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Register Visitor")
        self.setMinimumWidth(520)
        self.setObjectName("OMSDialog")
        self._build()

    def _build(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(28, 24, 28, 24)
        root.setSpacing(14)

        title = QLabel("Register New Visitor")
        title.setObjectName("dialogTitle")
        root.addWidget(title)

        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setObjectName("dialogSep")
        root.addWidget(sep)

        def two_col(w1, w2):
            hl = QHBoxLayout()
            hl.setSpacing(14)
            hl.addWidget(w1)
            hl.addWidget(w2)
            return hl

        root.addWidget(self._lbl("Full Name *"))
        self.fullName = self._input("e.g. Grace Wanjiru")
        root.addWidget(self.fullName)

        root.addLayout(
            two_col(self._lbl("ID / Passport No. *"), self._lbl("Phone Number *"))
        )
        self.idNo = self._input("ID or passport number")
        self.phone = self._input("e.g. 0712 345 678")
        root.addLayout(two_col(self.idNo, self.phone))

        root.addLayout(
            two_col(self._lbl("Organisation"), self._lbl("Host / Person to Meet *"))
        )
        self.organisation = self._input("Company or institution")
        self.host = self._input("Name of staff member")
        root.addLayout(two_col(self.organisation, self.host))

        root.addLayout(
            two_col(self._lbl("Purpose of Visit *"), self._lbl("Expected Arrival Time"))
        )
        self.purpose = QComboBox()
        self.purpose.setObjectName("dialogCombo")
        self.purpose.addItems(
            [
                "Meeting",
                "Delivery",
                "Interview",
                "Supplier Visit",
                "Inspection",
                "Other",
            ]
        )
        self.arrivalTime = self._input("e.g. 10:30 AM")
        root.addLayout(two_col(self.purpose, self.arrivalTime))

        root.addWidget(self._lbl("Email Address"))
        self.email = self._input("visitor@example.com")
        root.addWidget(self.email)

        sep2 = QFrame()
        sep2.setFrameShape(QFrame.Shape.HLine)
        sep2.setObjectName("dialogSep")
        root.addWidget(sep2)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        self.btnCancel = QPushButton("Cancel")
        self.btnCancel.setObjectName("btnDialogCancel")
        self.btnRegister = QPushButton("Register Visitor")
        self.btnRegister.setObjectName("btnDialogSubmit")
        btn_row.addWidget(self.btnCancel)
        btn_row.addWidget(self.btnRegister)
        root.addLayout(btn_row)

        self.btnCancel.clicked.connect(self.reject)
        self.btnRegister.clicked.connect(self._on_register)

    def _lbl(self, text):
        lbl = QLabel(text)
        lbl.setObjectName("dialogFieldLabel")
        return lbl

    def _input(self, placeholder):
        w = QLineEdit()
        w.setPlaceholderText(placeholder)
        w.setObjectName("dialogInput")
        return w

    def _on_register(self):
        required = [self.fullName, self.idNo, self.phone, self.host]
        missing = [w for w in required if not w.text().strip()]
        for w in missing:
            w.setStyleSheet("border: 1px solid #ef4444;")
        if missing:
            return
        # TODO: INSERT into visitors table (MySQL)
        print(
            f"Visitor registered: {self.fullName.text()} | "
            f"Host: {self.host.text()} | "
            f"Purpose: {self.purpose.currentText()}"
        )
        self.accept()
