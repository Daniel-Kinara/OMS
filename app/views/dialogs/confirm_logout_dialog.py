# pyrefly: ignore [missing-import]
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
)


class ConfirmLogoutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Confirm Logout")
        self.setMinimumWidth(360)
        self.setObjectName("OMSDialog")
        self._build()

    def _build(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(28, 24, 28, 24)
        root.setSpacing(16)

        title = QLabel("Log out of OMS?")
        title.setObjectName("dialogTitle")
        root.addWidget(title)

        sep = QFrame()
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setObjectName("dialogSep")
        root.addWidget(sep)

        msg = QLabel(
            "You will be returned to the login screen.\n"
            "Any unsaved changes will be lost."
        )
        msg.setObjectName("dialogFieldLabel")
        msg.setWordWrap(True)
        root.addWidget(msg)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        self.btnCancel = QPushButton("Stay")
        self.btnCancel.setObjectName("btnDialogCancel")
        self.btnLogout = QPushButton("Log out")
        self.btnLogout.setObjectName("btnDialogSubmit")
        btn_row.addWidget(self.btnCancel)
        btn_row.addWidget(self.btnLogout)
        root.addLayout(btn_row)

        self.btnCancel.clicked.connect(self.reject)
        self.btnLogout.clicked.connect(self.accept)
