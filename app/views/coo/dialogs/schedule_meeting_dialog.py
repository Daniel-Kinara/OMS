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


class ScheduleMeetingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Schedule Meeting")
        self.setMinimumWidth(500)
        self.setObjectName("OMSDialog")
        self._build()

    def _build(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(28, 24, 28, 24)
        root.setSpacing(14)

        title = QLabel("Schedule New Meeting")
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

        root.addWidget(self._lbl("Meeting Title *"))
        self.meetingTitle = self._input("e.g. Management Review Meeting")
        root.addWidget(self.meetingTitle)

        root.addLayout(two_col(self._lbl("Date *"), self._lbl("Time *")))
        self.meetingDate = self._input("e.g. 09 Jul 2026")
        self.meetingTime = self._input("e.g. 10:00 AM")
        root.addLayout(two_col(self.meetingDate, self.meetingTime))

        root.addLayout(two_col(self._lbl("Venue *"), self._lbl("Meeting Type")))
        self.venue = self._input("e.g. Board Room")
        self.meetingType = QComboBox()
        self.meetingType.setObjectName("dialogCombo")
        self.meetingType.addItems(
            [
                "Internal Meeting",
                "Department Meeting",
                "Management Meeting",
                "Project Review",
                "Other",
            ]
        )
        root.addLayout(two_col(self.venue, self.meetingType))

        root.addWidget(self._lbl("Agenda / Description"))
        self.agenda = QTextEdit()
        self.agenda.setPlaceholderText("Meeting agenda and key discussion points…")
        self.agenda.setObjectName("dialogInput")
        self.agenda.setMaximumHeight(90)
        root.addWidget(self.agenda)

        sep2 = QFrame()
        sep2.setFrameShape(QFrame.Shape.HLine)
        sep2.setObjectName("dialogSep")
        root.addWidget(sep2)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        self.btnCancel = QPushButton("Cancel")
        self.btnCancel.setObjectName("btnDialogCancel")
        self.btnSchedule = QPushButton("Schedule Meeting")
        self.btnSchedule.setObjectName("btnDialogSubmit")
        btn_row.addWidget(self.btnCancel)
        btn_row.addWidget(self.btnSchedule)
        root.addLayout(btn_row)

        self.btnCancel.clicked.connect(self.reject)
        self.btnSchedule.clicked.connect(self._on_schedule)

    def _lbl(self, text):
        lbl = QLabel(text)
        lbl.setObjectName("dialogFieldLabel")
        return lbl

    def _input(self, placeholder):
        w = QLineEdit()
        w.setPlaceholderText(placeholder)
        w.setObjectName("dialogInput")
        return w

    def _on_schedule(self):
        required = [self.meetingTitle, self.meetingDate, self.meetingTime, self.venue]
        missing = [w for w in required if not w.text().strip()]
        for w in missing:
            w.setStyleSheet("border: 1px solid #ef4444;")
        if missing:
            return
        print(
            f"Meeting scheduled: {self.meetingTitle.text()} | "
            f"{self.meetingDate.text()} {self.meetingTime.text()} | "
            f"{self.venue.text()}"
        )
        self.accept()
