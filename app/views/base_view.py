# pyrefly: ignore [missing-import]
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QHBoxLayout

# pyrefly: ignore [missing-import]
from PyQt6.QtCore import Qt


class BaseView(QWidget):
    """Every module screen inherits from this.
    Provides a consistent title bar + content area."""

    def __init__(self, title: str, subtitle: str = "", parent=None):
        super().__init__(parent)
        self._build_layout(title, subtitle)

    def _build_layout(self, title: str, subtitle: str):
        root = QVBoxLayout(self)
        root.setContentsMargins(28, 24, 28, 24)
        root.setSpacing(18)

        # Title bar
        title_frame = QFrame()
        title_frame.setObjectName("viewTitleFrame")
        tl = QVBoxLayout(title_frame)
        tl.setContentsMargins(0, 0, 0, 0)
        tl.setSpacing(3)

        lbl_title = QLabel(title)
        lbl_title.setObjectName("viewTitleLabel")
        tl.addWidget(lbl_title)

        if subtitle:
            lbl_sub = QLabel(subtitle)
            lbl_sub.setObjectName("viewSubtitleLabel")
            tl.addWidget(lbl_sub)

        root.addWidget(title_frame)

        # Content placeholder — subclasses call self._content_layout to add widgets
        self._content_layout = root
