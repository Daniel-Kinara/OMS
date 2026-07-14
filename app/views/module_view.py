# pyrefly: ignore [missing-import]
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView,
)

# pyrefly: ignore [missing-import]
from PyQt6.QtCore import Qt


class ModuleView(QWidget):
    """Generic full-screen module view.
    Used for Office Cleanliness, Compound Management,
    Facility Inspections, Office Safety, Visitor Registration,
    Maintenance Requests — each passes its own title, subtitle,
    columns and placeholder rows."""

    def __init__(
        self,
        title: str,
        subtitle: str,
        columns: list,
        rows: list,
        action_label: str = None,
        parent=None,
    ):
        super().__init__(parent)
        self._title = title
        self._subtitle = subtitle
        self._columns = columns
        self._rows = rows
        self._action_label = action_label
        self._build()

    def _build(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(28, 24, 28, 28)
        root.setSpacing(18)

        # Header
        header = QFrame()
        header.setObjectName("viewTitleFrame")
        hl = QHBoxLayout(header)
        hl.setContentsMargins(0, 0, 0, 0)

        text_vl = QVBoxLayout()
        text_vl.setSpacing(3)
        lbl_title = QLabel(self._title)
        lbl_title.setObjectName("viewTitleLabel")
        lbl_sub = QLabel(self._subtitle)
        lbl_sub.setObjectName("viewSubtitleLabel")
        text_vl.addWidget(lbl_title)
        text_vl.addWidget(lbl_sub)
        hl.addLayout(text_vl)
        hl.addStretch()

        if self._action_label:
            self.actionBtn = QPushButton(self._action_label)
            self.actionBtn.setObjectName("btnLogInspection")
            hl.addWidget(self.actionBtn)

        root.addWidget(header)

        # Table
        panel = QFrame()
        panel.setObjectName("visitorPanel")
        pl = QVBoxLayout(panel)
        pl.setSpacing(10)

        self.table = QTableWidget(len(self._rows), len(self._columns))
        self.table.setHorizontalHeaderLabels(self._columns)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.table.setShowGrid(False)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.verticalHeader().setDefaultSectionSize(40)

        for r, row in enumerate(self._rows):
            for c, val in enumerate(row):
                item = QTableWidgetItem(val)
                self.table.setItem(r, c, item)

        pl.addWidget(self.table)
        root.addWidget(panel)
        root.addStretch()
