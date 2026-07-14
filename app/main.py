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
)

# pyrefly: ignore [missing-import]
from PyQt6.QtCore import Qt

from views.dashboard_view import DashboardView
from views.module_view import ModuleView
from views.dialogs.log_maintenance_dialog import LogMaintenanceDialog
from views.dialogs.log_inspection_dialog import LogInspectionDialog
from views.dialogs.confirm_logout_dialog import ConfirmLogoutDialog

# pyrefly: ignore [missing-import]
from views.dialogs.register_visitor_dialog import RegisterVisitorDialog


class OpsManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operations Management System — Operations Manager")
        self.setMinimumSize(1280, 720)
        self._sidebar_expanded = True
        self._build_ui()
        self._wire_signals()
        self._navigate(0)

    # ── UI construction ──────────────────────────────────────────────
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

    # ── Top bar ──────────────────────────────────────────────────────
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

    # ── Sidebar ──────────────────────────────────────────────────────
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
        logo.setFixedSize(42, 42)

        company = QLabel("Mfano Bora Africa\nOperations Manager · OMS")
        company.setObjectName("companyLabel")
        company.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vl.addWidget(logo)
        vl.addWidget(company)
        vl.addWidget(self._h_line())

        self._nav_items = [
            ("🏠  Dashboard", 0, None),
            ("🧹  Office Cleanliness", 2, "sectionDailyOps"),
            ("🌳  Compound Management", 3, None),
            ("🔍  Facility Inspections", 4, None),
            ("🛡  Office Safety", 5, None),
            ("🧾  Visitor Registration", 6, "sectionVisitors"),
            ("🔧  Maintenance Requests", 7, "sectionMaintenance"),
        ]

        self._nav_buttons = []
        vl.addWidget(self._section_lbl("OVERVIEW", "sectionOverview"))

        for i, (label, page_idx, section) in enumerate(self._nav_items):
            if section:
                vl.addWidget(
                    self._section_lbl(
                        section.replace("section", "")
                        .replace("DailyOps", "DAILY OPERATIONS")
                        .replace("Visitors", "VISITORS")
                        .replace("Maintenance", "MAINTENANCE"),
                        section,
                    )
                )
            btn = QPushButton(label)
            btn.setCheckable(True)
            btn.clicked.connect(
                lambda checked, idx=page_idx, bi=i: self._navigate(idx, bi)
            )
            self._nav_buttons.append(btn)
            vl.addWidget(btn)

        vl.addStretch()
        vl.addWidget(self._h_line())

        self.btnSettings = QPushButton("⚙  Settings")
        self.btnLogout = QPushButton("🚪  Logout")
        vl.addWidget(self.btnSettings)
        vl.addWidget(self.btnLogout)
        return self.sidebarFrame

    # ── Stacked pages ────────────────────────────────────────────────
    def _build_stack(self):
        self.stack = QStackedWidget()
        self.stack.setObjectName("contentStack")

        # Index 0 — Dashboard
        self.dashboardView = DashboardView()
        self.stack.addWidget(self.dashboardView)

        # Index 1 — unused (keeps indices aligned)
        self.stack.addWidget(QWidget())

        # Indices 2–7 — module pages
        module_pages = [
            (
                "🧹  Office Cleanliness",
                "Track and manage daily office cleanliness records.",
                ["Area", "Cleaned By", "Date", "Status"],
                [
                    ("Main Office", "James Otieno", "09 Jul 2026", "Done"),
                    ("Boardroom", "Jane Wambui", "09 Jul 2026", "Done"),
                    ("Washrooms", "James Otieno", "09 Jul 2026", "Pending"),
                    ("Kitchen", "Jane Wambui", "09 Jul 2026", "Done"),
                ],
                None,
            ),
            (
                "🌳  Compound Management",
                "Monitor compound cleanliness, grounds and gate access.",
                ["Zone", "Checked By", "Date", "Condition"],
                [
                    ("Main Gate", "Security", "09 Jul 2026", "Clear"),
                    ("Car Park", "Grounds Team", "09 Jul 2026", "Clear"),
                    ("Back Fence", "Grounds Team", "09 Jul 2026", "Needs attention"),
                    ("Garden", "Grounds Team", "09 Jul 2026", "Clear"),
                ],
                None,
            ),
            (
                "🔍  Facility Inspections",
                "Log and review all facility inspection records.",
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
                "Track safety checks, hazard reports and compliance.",
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
                    ("Smoke Detectors", "Safety Officer", "08 Jul 2026", "OK"),
                ],
                None,
            ),
            (
                "🧾  Visitor Registration",
                "Register new visitors and manage today's visitor log.",
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
            self.stack.addWidget(view)

        return self.stack

    def _action_for_module(self, title: str):
        if "Maintenance" in title:
            return self._open_log_maintenance
        if "Inspection" in title:
            return self._open_log_inspection
        if "Visitor" in title:
            return self._open_register_visitor
        return lambda: None

    # ── Signal wiring ────────────────────────────────────────────────
    def _wire_signals(self):
        self.btnMenuToggle.clicked.connect(self._toggle_sidebar)
        self.btnSettings.clicked.connect(self._open_settings)
        self.btnLogout.clicked.connect(self._confirm_logout)

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

    # ── Navigation ───────────────────────────────────────────────────
    def _navigate(self, page_index: int, nav_btn_index: int = 0):
        self.stack.setCurrentIndex(page_index)
        for i, btn in enumerate(self._nav_buttons):
            btn.setChecked(i == nav_btn_index)

    def _toggle_sidebar(self):
        self._sidebar_expanded = not self._sidebar_expanded
        self.sidebarFrame.setFixedWidth(250 if self._sidebar_expanded else 0)

    # ── Dialogs ──────────────────────────────────────────────────────
    def _open_log_maintenance(self):
        LogMaintenanceDialog(self).exec()

    def _open_log_inspection(self):
        LogInspectionDialog(self).exec()

    def _open_register_visitor(self):
        RegisterVisitorDialog(self).exec()

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

    # ── Helpers ──────────────────────────────────────────────────────
    def _lbl(self, text: str, obj_name: str) -> QLabel:
        lbl = QLabel(text)
        lbl.setObjectName(obj_name)
        return lbl

    def _h_line(self):
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        return line

    def _section_lbl(self, text: str, obj_name: str) -> QLabel:
        lbl = QLabel(text)
        lbl.setObjectName(obj_name)
        return lbl


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
