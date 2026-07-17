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


class RegisterApplicantDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Register Attachment Applicant")
        self.setMinimumWidth(520)
        self.setObjectName("OMSDialog")
        self._build()

    def _build(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(28, 24, 28, 24)
        root.setSpacing(14)

        title = QLabel("Register New Applicant")
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
        self.fullName = self._input("e.g. Brian Ochieng")
        root.addWidget(self.fullName)

        root.addLayout(
            two_col(self._lbl("Email Address *"), self._lbl("Phone Number *"))
        )
        self.email = self._input("applicant@university.ac.ke")
        self.phone = self._input("e.g. 0712 345 678")
        root.addLayout(two_col(self.email, self.phone))

        root.addLayout(
            two_col(self._lbl("University / Institution *"), self._lbl("Course *"))
        )
        self.university = self._input("e.g. University of Nairobi")
        self.course = self._input("e.g. BSc. Business Information Technology")
        root.addLayout(two_col(self.university, self.course))

        root.addLayout(
            two_col(self._lbl("Year of Study"), self._lbl("Preferred Department"))
        )
        self.studyYear = QComboBox()
        self.studyYear.setObjectName("dialogCombo")
        self.studyYear.addItems(["Year 1", "Year 2", "Year 3", "Year 4"])
        self.department = QComboBox()
        self.department.setObjectName("dialogCombo")
        self.department.addItems(
            [
                "Administration",
                "Finance",
                "ICT",
                "Operations",
                "Marketing",
            ]
        )
        root.addLayout(two_col(self.studyYear, self.department))

        root.addLayout(
            two_col(self._lbl("Attachment Period *"), self._lbl("Application Date"))
        )
        self.period = self._input("e.g. Jun 2026 – Aug 2026")
        self.appDate = self._input("e.g. 09 Jul 2026")
        root.addLayout(two_col(self.period, self.appDate))

        sep2 = QFrame()
        sep2.setFrameShape(QFrame.Shape.HLine)
        sep2.setObjectName("dialogSep")
        root.addWidget(sep2)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        self.btnCancel = QPushButton("Cancel")
        self.btnCancel.setObjectName("btnDialogCancel")
        self.btnRegister = QPushButton("Register Applicant")
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
        required = [
            self.fullName,
            self.email,
            self.phone,
            self.university,
            self.course,
            self.period,
        ]
        missing = [w for w in required if not w.text().strip()]
        for w in missing:
            w.setStyleSheet("border: 1px solid #ef4444;")
        if missing:
            return
        print(
            f"Applicant registered: {self.fullName.text()} | "
            f"{self.university.text()} | "
            f"Dept: {self.department.currentText()}"
        )
        self.accept()
