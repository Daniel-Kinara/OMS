"""
Operations Management System (OMS)
Operations Manager Dashboard — fully wired frontend.

Run with:  python app/main.py
"""

import sys
import os

# pyrefly: ignore [missing-import]
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QLabel,
    QLineEdit,
    QPushButton,
    QStackedWidget,
    QSizePolicy,
)

# pyrefly: ignore [missing-import]
from PyQt6.QtCore import Qt

from views.dashboard_view import DashboardView
from views.module_view import ModuleView
from views.dialogs.log_maintenance_dialog import LogMaintenanceDialog
from views.dialogs.log_inspection_dialog import LogInspectionDialog
from views.dialogs.confirm_logout_dialog import ConfirmLogoutDialog


class OpsManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operations Management System — Operations Manager")
        self.setMinimumSize(1280, 720)
        self._sidebar_expanded = True
        self._build_ui()
        self._wire_signals()
        self._navigate(0)  # start on Dashboard

    # ── UI construction ──────────────────────────────────────────────────
    def _build_ui(self):
        root_widget = QWidget()
        self.setCentralWidget(root_widget)
        root_vl = QVBoxLayout(root_widget)
        root_vl.setContentsMargins(0, 0, 0, 0)
        root_vl.setSpacing(0)

        root_vl.addWidget(self._build_top_bar())

        body = QFrame()
        body.setObjectName("bodyFrame")
        body_hl = QHBoxLayout(body)
        body_hl.setContentsMargins(0, 0, 0, 0)
        body_hl.setSpacing(0)
        body_hl.addWidget(self._build_sidebar())
        body_hl.addWidget(self._build_stack())
        root_vl.addWidget(body)

    # ── Top bar ──────────────────────────────────────────────────────────
    def _build_top_bar(self):
        bar = QFrame()
        bar.setObjectName("topBarFrame")
        bar.setFixedHeight(64)
        hl = QHBoxLayout(bar)
        hl.setContentsMargins(18, 0, 18, 0)
        hl.setSpacing(10)

        self.btnMenuToggle = QPushButton("☰")
        self.btnMenuToggle.setObjectName("btnMenuToggle")
        self.btnMenuToggle.setFixedSize(38, 38)

        self.appTitleLabel = QLabel("OPERATIONS MANAGEMENT SYSTEM (OMS)")
        self.appTitleLabel.setObjectName("appTitleLabel")

        self.searchBar = QLineEdit()
        self.searchBar.setPlaceholderText("Search anything…")
        self.searchBar.setObjectName("searchBar")
        self.searchBar.setFixedSize(380, 36)

        self.btnNotifications = QPushButton("🔔")
        self.btnNotifications.setObjectName("btnNotifications")
        self.btnNotifications.setFixedSize(36, 36)

        self.btnMessages = QPushButton("✉")
        self.btnMessages.setObjectName("btnMessages")
        self.btnMessages.setFixedSize(36, 36)

        profile = QFrame()
        profile.setObjectName("profileFrame")
        pv = QVBoxLayout(profile)
        pv.setContentsMargins(10, 0, 0, 0)
        pv.setSpacing(1)
        pv.addWidget(self._lbl("Operations Manager", "profileNameLabel"))
        pv.addWidget(self._lbl("Full access", "profileRoleLabel"))

        hl.addWidget(self.btnMenuToggle)
        hl.addWidget(self.appTitleLabel)
        hl.addStretch()
        hl.addWidget(self.searchBar)
        hl.addStretch()
        hl.addWidget(self.btnNotifications)
        hl.addWidget(self.btnMessages)
        hl.addWidget(profile)
        return bar

    # ── Sidebar ──────────────────────────────────────────────────────────
    def _build_sidebar(self):
        self.sidebarFrame = QFrame()
        self.sidebarFrame.setObjectName("sidebarFrame")
        self.sidebarFrame.setFixedWidth(250)

        vl = QVBoxLayout(self.sidebarFrame)
        vl.setContentsMargins(14, 20, 14, 16)
        vl.setSpacing(2)

        logo = QLabel("OM")
        logo.setObjectName("logoLabel")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        company = QLabel("Mfano Bora Africa\nOperations Manager · OMS")
        company.setObjectName("companyLabel")
        company.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vl.addWidget(logo)
        vl.addWidget(company)
        vl.addWidget(self._h_line())

        # Nav buttons with page index
        self._nav_items = [
            ("🏠  Dashboard", 0),
            ("🧹  Office Cleanliness", 2),
            ("🌳  Compound Management", 3),
            ("🔍  Facility Inspections", 4),
            ("🛡  Office Safety", 5),
            ("🧾  Visitor Registration", 6),
            ("🔧  Maintenance Requests", 7),
        ]
        self._nav_buttons = []

        sections = {
            0: ("OVERVIEW", "sectionOverview"),
            1: ("DAILY OPERATIONS", "sectionDailyOps"),
            5: ("VISITORS", "sectionVisitors"),
            6: ("MAINTENANCE", "sectionMaintenance"),
        }

        for i, (label, page_idx) in enumerate(self._nav_items):
            if i in sections:
                lbl = QLabel(sections[i][0])
                lbl.setObjectName(sections[i][1])
                vl.addWidget(lbl)
            btn = QPushButton(label)
            btn.setObjectName(f"navBtn_{i}")
            btn.setCheckable(True)
            btn.clicked.connect(
                lambda checked, idx=page_idx, btn_i=i: self._navigate(idx, btn_i)
            )
            self._nav_buttons.append(btn)
            vl.addWidget(btn)

        vl.addStretch()
        vl.addWidget(self._h_line())

        self.btnSettings = QPushButton("⚙  Settings")
        self.btnSettings.setObjectName("sidebarFrame")
        self.btnLogout = QPushButton("🚪  Logout")
        self.btnLogout.setObjectName("sidebarFrame")
        vl.addWidget(self.btnSettings)
        vl.addWidget(self.btnLogout)

        return self.sidebarFrame

    # ── Stacked pages ────────────────────────────────────────────────────
    def _build_stack(self):
        self.stack = QStackedWidget()
        self.stack.setObjectName("contentStack")

        # Page 0: Dashboard
        self.dashboardView = DashboardView()
        self.stack.addWidget(self.dashboardView)  # index 0

        # Page 1: placeholder (unused — keeps index alignment)
        self.stack.addWidget(QWidget())  # index 1

        # Pages 2–7: module views
        module_pages = [
            (
                "🧹  Office Cleanliness",
                "Track and manage daily office cleanliness records.",
                ["Area", "Cleaned By", "Date", "Status"],
                [
                    ("Main Office", "James Otieno", "09 Jul 2026", "Done"),
                    ("Boardroom", "Jane Wambui", "09 Jul 2026", "Done"),
                    ("Washrooms", "James Otieno", "09 Jul 2026", "Pending"),
                ],
                None,
            ),
            (
                "🌳  Compound Management",
                "Monitor compound cleanliness, grounds, and gate access.",
                ["Zone", "Checked By", "Date", "Condition"],
                [
                    ("Main Gate", "Security", "09 Jul 2026", "Clear"),
                    ("Car Park", "Grounds Team", "09 Jul 2026", "Clear"),
                    ("Back Fence", "Grounds Team", "09 Jul 2026", "Needs attention"),
                ],
                None,
            ),
            (
                "🔍  Facility Inspections",
                "Log and review facility inspection records.",
                ["Area", "Inspector", "Date", "Status", "Findings"],
                [
                    (
                        "Reception & Lobby",
                        "P. Njoroge",
                        "09 Jul 2026",
                        "Passed",
                        "No issues",
                    ),
                    (
                        "Compound & Grounds",
                        "P. Njoroge",
                        "09 Jul 2026",
                        "Passed",
                        "No issues",
                    ),
                    ("Washrooms", "P. Njoroge", "09 Jul 2026", "Passed", "No issues"),
                    (
                        "Parking & Perimeter",
                        "P. Njoroge",
                        "09 Jul 2026",
                        "Needs Attention",
                        "Gate light out",
                    ),
                    (
                        "Fire & Safety Equip",
                        "P. Njoroge",
                        "09 Jul 2026",
                        "Not started",
                        "—",
                    ),
                ],
                "✓  Log New Inspection",
            ),
            (
                "🛡  Office Safety",
                "Track safety checks, hazard reports, and compliance.",
                ["Check Item", "Checked By", "Date", "Result"],
                [
                    ("Fire Extinguishers", "Safety Officer", "09 Jul 2026", "OK"),
                    ("Emergency Exits", "Safety Officer", "09 Jul 2026", "OK"),
                    (
                        "First Aid Kits",
                        "Safety Officer",
                        "08 Jul 2026",
                        "Needs restock",
                    ),
                ],
                None,
            ),
            (
                "🧾  Visitor Registration",
                "Register new visitors and view today's visitor log.",
                ["Visitor", "Host", "Purpose", "Check-in", "Check-out", "Status"],
                [
                    (
                        "Grace Wanjiru",
                        "J. Kamau",
                        "Supplier meeting",
                        "9:12 AM",
                        "—",
                        "Checked in",
                    ),
                    (
                        "Peter Njoroge",
                        "Ops Mgr",
                        "Facility audit",
                        "9:55 AM",
                        "—",
                        "Checked in",
                    ),
                    (
                        "Amina Hassan",
                        "HR Desk",
                        "Interview",
                        "8:30 AM",
                        "10:00 AM",
                        "Checked out",
                    ),
                    (
                        "Samuel Kiptoo",
                        "Stores",
                        "Delivery",
                        "11:10 AM",
                        "—",
                        "Checked in",
                    ),
                ],
                "👤  Register Visitor",
            ),
            (
                "🔧  Maintenance Requests",
                "View, manage and track all maintenance requests.",
                ["Issue", "Location", "Reported", "Priority", "Status"],
                [
                    ("East wing AC unit", "Floor 2", "9:40 AM", "High", "Pending"),
                    ("Parking gate light", "Parking", "10:52 AM", "Medium", "Overdue"),
                    ("Leaking tap", "Washroom B", "10:52 AM", "Low", "In progress"),
                    ("Broken window latch", "Reception", "8:15 AM", "Low", "Resolved"),
                ],
                "✎  Log Maintenance Issue",
            ),
        ]

        for title, subtitle, cols, rows, action in module_pages:
            view = ModuleView(title, subtitle, cols, rows, action)
            if action:
                view.actionBtn.clicked.connect(self._action_for_module(title))
            self.stack.addWidget(view)  # indices 2–7

        return self.stack

    def _action_for_module(self, title: str):
        """Return the correct dialog opener for each module's action button."""
        if "Maintenance" in title:
            return self._open_log_maintenance
        if "Inspection" in title:
            return self._open_log_inspection
        if "Visitor" in title:
            return self._open_register_visitor
        return lambda: None

    # ── Signal wiring ────────────────────────────────────────────────────
    def _wire_signals(self):
        # Top bar
        self.btnMenuToggle.clicked.connect(self._toggle_sidebar)

        # Dashboard internal buttons
        dv = self.dashboardView
        dv.btnLogMaintenance.clicked.connect(self._open_log_maintenance)
        dv.btnLogInspection.clicked.connect(self._open_log_inspection)
        dv.btnViewChecklist.clicked.connect(lambda: self._navigate(4, 3))
        dv.btnViewMaintenance.clicked.connect(lambda: self._navigate(7, 6))
        dv.btnViewActivity.clicked.connect(lambda: self._navigate(4, 3))
        dv.btnViewVisitorLog.clicked.connect(lambda: self._navigate(6, 5))
        dv.btnQaReportMaintenance.clicked.connect(self._open_log_maintenance)
        dv.btnQaRegisterVisitor.clicked.connect(self._open_register_visitor)
        dv.btnQaLogInspection.clicked.connect(self._open_log_inspection)

        # Settings / Logout
        self.btnSettings.clicked.connect(self._open_settings)
        self.btnLogout.clicked.connect(self._confirm_logout)

    # ── Navigation ───────────────────────────────────────────────────────
    def _navigate(self, page_index: int, nav_btn_index: int = 0):
        self.stack.setCurrentIndex(page_index)
        for i, btn in enumerate(self._nav_buttons):
            btn.setChecked(i == nav_btn_index)

    def _toggle_sidebar(self):
        self._sidebar_expanded = not self._sidebar_expanded
        self.sidebarFrame.setFixedWidth(250 if self._sidebar_expanded else 0)

    # ── Dialog openers ───────────────────────────────────────────────────
    def _open_log_maintenance(self):
        dlg = LogMaintenanceDialog(self)
        dlg.exec()

    def _open_log_inspection(self):
        dlg = LogInspectionDialog(self)
        dlg.exec()

    def _open_register_visitor(self):
        # Navigates to Visitor Registration module screen
        self._navigate(6, 5)

    def _open_settings(self):
        # pyrefly: ignore [missing-import]
        from PyQt6.QtWidgets import QMessageBox

        QMessageBox.information(
            self,
            "Settings",
            "Settings panel coming soon.\n"
            "User preferences and system configuration will be here.",
        )

    def _confirm_logout(self):
        dlg = ConfirmLogoutDialog(self)
        if dlg.exec():
            QApplication.quit()

    # ── Helpers ──────────────────────────────────────────────────────────
    def _lbl(self, text: str, obj_name: str) -> QLabel:
        lbl = QLabel(text)
        lbl.setObjectName(obj_name)
        return lbl

    def _h_line(self):
        # pyrefly: ignore [missing-import]
        from PyQt6.QtWidgets import QFrame as F

        line = F()
        line.setFrameShape(F.Shape.HLine)
        return line


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
