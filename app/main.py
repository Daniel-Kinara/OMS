"""
Operations Management System (OMS)
Entry point for the Operations Manager desktop dashboard.

Sidebar modules match SRS Chapter 4.4 exactly:
Office cleanliness, Compound management, Facility inspections,
Visitor registration, Maintenance requests, Office safety,
Daily operational coordination.
(No Meetings/Announcements/Reports — those belong to other roles.)

Run with:  python app/main.py   (from the project root, venv active)
"""

import sys
import os

# pyrefly: ignore [missing-import]
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QListWidgetItem,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView,
)

# pyrefly: ignore [missing-import]
from PyQt6.QtCore import Qt

from generated.ui_operations_manager_dashboard import Ui_OpsManagerWindow


class OpsManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_OpsManagerWindow()
        self.ui.setupUi(self)

        self._sidebar_expanded = True
        self._make_nav_buttons_checkable()
        self._connect_signals()
        self._configure_lists_and_tables()
        self._load_placeholder_data()

    def _toggle_sidebar(self):
        self._sidebar_expanded = not self._sidebar_expanded
        width = 250 if self._sidebar_expanded else 0
        self.ui.sidebarFrame.setMaximumWidth(width)
        self.ui.sidebarFrame.setMinimumWidth(width)

    def _make_nav_buttons_checkable(self):
        self.nav_buttons = [
            self.ui.btnDashboard,
            self.ui.btnOfficeCleanliness,
            self.ui.btnCompoundManagement,
            self.ui.btnFacilityInspections,
            self.ui.btnOfficeSafety,
            self.ui.btnVisitorRegistration,
            self.ui.btnMaintenanceRequests,
        ]
        for btn in self.nav_buttons:
            btn.setCheckable(True)
        self.ui.btnDashboard.setChecked(True)

    def _connect_signals(self):
        for btn in self.nav_buttons:
            btn.clicked.connect(self._on_nav_clicked)

        self.ui.btnLogMaintenance.clicked.connect(self._on_log_maintenance)
        self.ui.btnLogInspection.clicked.connect(self._on_log_inspection)

        self.ui.btnQaReportMaintenance.clicked.connect(self._on_log_maintenance)
        self.ui.btnQaLogInspection.clicked.connect(self._on_log_inspection)
        self.ui.btnQaRegisterVisitor.clicked.connect(self._on_register_visitor)

        self.ui.btnMenuToggle.clicked.connect(self._toggle_sidebar)
        self.ui.btnNotifications.clicked.connect(lambda: print("Notifications clicked"))
        self.ui.btnMessages.clicked.connect(lambda: print("Messages clicked"))

        self.ui.btnViewChecklist.clicked.connect(
            lambda: self._on_view_all("Facility Inspections")
        )
        self.ui.btnViewMaintenance.clicked.connect(
            lambda: self._on_view_all("Maintenance Requests")
        )
        self.ui.btnViewActivity.clicked.connect(
            lambda: self._on_view_all("Recent Activity")
        )
        self.ui.btnViewVisitorLog.clicked.connect(
            lambda: self._on_view_all("Visitor Log")
        )

    def _configure_lists_and_tables(self):
        """Cap panels to 4–5 visible rows. No internal scrollbar —
        the 'View all ›' link handles the rest."""

        for lw in (self.ui.checklistWidget, self.ui.activityListWidget):
            lw.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            lw.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            lw.setMaximumHeight(185)
            lw.setFrameShape(lw.frameShape().NoFrame)

        for table in (self.ui.maintenanceTable, self.ui.visitorLogTable):
            # removes the black corner button
            table.verticalHeader().setVisible(False)
            table.horizontalHeader().setStretchLastSection(True)
            table.horizontalHeader().setSectionResizeMode(
                QHeaderView.ResizeMode.Stretch
            )
            table.setShowGrid(False)
            table.setAlternatingRowColors(True)
            table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
            table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
            table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            table.setMaximumHeight(185)
            table.verticalHeader().setDefaultSectionSize(38)

    def _on_nav_clicked(self):
        sender = self.sender()
        for btn in self.nav_buttons:
            btn.setChecked(btn is sender)
        # TODO: swap QStackedWidget page here

    def _on_view_all(self, module: str):
        # TODO: navigate to the full module screen via the sidebar button
        print(f"View all: {module}")

    def _on_log_maintenance(self):
        print("Log Maintenance Issue clicked")

    def _on_log_inspection(self):
        print("Log Facility Inspection clicked")

    def _on_register_visitor(self):
        print("Register Visitor clicked")

    def _load_placeholder_data(self):
        checklist_items = [
            "01  Reception & Lobby — 100%",
            "02  Compound & Grounds — 100%",
            "03  Washrooms — 100%",
            "04  Parking & Perimeter — 40%",
            "05  Fire & Safety Equipment — Not started",
        ]
        for text in checklist_items:
            self.ui.checklistWidget.addItem(QListWidgetItem(text))

        maintenance_rows = [
            ("East wing AC unit", "Floor 2", "Pending"),
            ("Parking gate light", "Parking", "Overdue"),
            ("Leaking tap", "Washroom B", "In progress"),
            ("Broken window latch", "Reception", "Resolved"),
        ]
        self.ui.maintenanceTable.setRowCount(len(maintenance_rows))
        for row, (issue, location, priority) in enumerate(maintenance_rows):
            self.ui.maintenanceTable.setItem(row, 0, QTableWidgetItem(issue))
            self.ui.maintenanceTable.setItem(row, 1, QTableWidgetItem(location))
            self.ui.maintenanceTable.setItem(row, 2, QTableWidgetItem(priority))

        activity_items = [
            "●  Visitor Grace Wanjiru checked in — 9:12 AM",
            "●  Maintenance request #41 raised — East wing AC — 9:40 AM",
            "●  Inspection logged — Washrooms, no issues — 10:05 AM",
            "●  Safety flag raised — Parking gate light out — 10:52 AM",
            "●  Task 'Restock supplies' marked in progress — 11:20 AM",
        ]
        for text in activity_items:
            self.ui.activityListWidget.addItem(QListWidgetItem(text))

        visitor_rows = [
            ("Grace Wanjiru", "J. Kamau", "9:12 AM", "Checked in"),
            ("Peter Njoroge", "Ops Mgr", "9:55 AM", "Checked in"),
            ("Amina Hassan", "HR Desk", "8:30 AM", "Checked out"),
            ("Samuel Kiptoo", "Stores", "11:10 AM", "Checked in"),
        ]
        self.ui.visitorLogTable.setRowCount(len(visitor_rows))
        for row, (visitor, host, time, status) in enumerate(visitor_rows):
            self.ui.visitorLogTable.setItem(row, 0, QTableWidgetItem(visitor))
            self.ui.visitorLogTable.setItem(row, 1, QTableWidgetItem(host))
            self.ui.visitorLogTable.setItem(row, 2, QTableWidgetItem(time))
            self.ui.visitorLogTable.setItem(row, 3, QTableWidgetItem(status))


def load_stylesheet(app: QApplication):
    style_path = os.path.join(os.path.dirname(__file__), "styles", "style.qss")
    with open(style_path, "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())


def main():
    app = QApplication(sys.argv)
    load_stylesheet(app)
    window = OpsManagerWindow()
    window.showMaximized()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
