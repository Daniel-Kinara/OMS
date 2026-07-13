from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QHeaderView,
)


class VisitorManagementWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        # Sub-header actions grouping bar
        hdr = QHBoxLayout()
        title = QLabel("Visitor Registry Information (SRS 5.7)")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #123014;")

        btn_sync = QPushButton("🔄 Sync Database Records")
        btn_sync.setStyleSheet(
            "background-color: #123014; color: white; padding: 6px 14px; border-radius: 4px; font-weight: 600;"
        )
        btn_sync.clicked.connect(self.pull_mysql_records)

        hdr.addWidget(title)
        hdr.addStretch()
        hdr.addWidget(btn_sync)
        layout.addLayout(hdr)

        # Grid Data Matrix View Controller
        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(
            [
                "ID Index",
                "Visitor Full Name",
                "Company/Org Name",
                "ID No/Passport",
                "Purpose of Visit",
            ]
        )
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        layout.addWidget(self.table)

    def pull_mysql_records(self):
        """Fetches and renders visitor data streams mapping cleanly to your PDF schema fields."""
        conn = self.main_window._connect_to_database()
        if not conn:
            return
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT visitor_id, full_name, organization, `ID NO/passport`, visit_purpose FROM visitors ORDER BY visitor_id DESC"
                )
                rows = cursor.fetchall()

                self.table.setRowCount(0)
                for pos, dataset in enumerate(rows):
                    self.table.insertRow(pos)
                    self.table.setItem(
                        pos, 0, QTableWidgetItem(str(dataset["visitor_id"]))
                    )
                    self.table.setItem(pos, 1, QTableWidgetItem(dataset["full_name"]))
                    self.table.setItem(
                        pos, 2, QTableWidgetItem(dataset["organization"])
                    )
                    self.table.setItem(
                        pos, 3, QTableWidgetItem(dataset["ID NO/passport"])
                    )
                    self.table.setItem(
                        pos, 4, QTableWidgetItem(dataset["visit_purpose"])
                    )
        finally:
            conn.close()
