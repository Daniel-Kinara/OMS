"""
OMS — Chief Operations Officer (COO) Dashboard
SRS Chapter 4.3 — Administration + Industrial Attachment modules

Run via login.py (role-based launch)
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
    QMenu,
)

# pyrefly: ignore [missing-import]
from PyQt6.QtCore import Qt

# pyrefly: ignore [missing-import]
from PyQt6.QtGui import QAction

from views.coo.coo_dashboard_view import COODashboardView
from views.module_view import ModuleView
from views.coo.dialogs.schedule_meeting_dialog import ScheduleMeetingDialog
from views.coo.dialogs.register_applicant_dialog import RegisterApplicantDialog
from views.dialogs.confirm_logout_dialog import ConfirmLogoutDialog


class COOWindow(QMainWindow):
    def __init__(
        self,
        role: str = "Administrator / COO",
        initials: str = "CO",
        avatar_color: str = "#059669",
        email: str = "",
    ):
        super().__init__()
        self._role = role
        self._initials = initials
        self._avatar_color = avatar_color
        self._email = email
        self.setWindowTitle(f"OMS — {role}")
        self.setMinimumSize(1280, 720)
        self._sidebar_expanded = True
        self._build_ui()
        self._wire_signals()
        self._navigate(0)

    # ── UI construction ──────────────────────────────────────────
    def _build_ui(self):
        root = QWidget()
        self.setCentralWidget(root)
        rv = QVBoxLayout(root)
        rv.setContentsMargins(0, 0, 0, 0)
        rv.setSpacing(0)
        rv.addWidget(self._build_top_bar())

        body = QFrame()
        body.setObjectName("bodyFrame")
        bh = QHBoxLayout(body)
        bh.setContentsMargins(0, 0, 0, 0)
        bh.setSpacing(0)
        bh.addWidget(self._build_sidebar())
        bh.addWidget(self._build_stack())
        rv.addWidget(body)

    # ── Top bar ──────────────────────────────────────────────────
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
        self.searchBar.setPlaceholderText("Search records, meetings, applicants…")
        self.searchBar.setObjectName("searchBar")
        self.searchBar.setFixedSize(380, 36)

        self.btnNotifications = QPushButton("🔔")
        self.btnNotifications.setObjectName("btnNotifications")
        self.btnNotifications.setFixedSize(36, 36)

        self.btnMessages = QPushButton("✉")
        self.btnMessages.setObjectName("btnMessages")
        self.btnMessages.setFixedSize(36, 36)

        self.avatarBtn = QPushButton(self._initials)
        self.avatarBtn.setObjectName("avatarBtn")
        self.avatarBtn.setFixedSize(38, 38)
        self.avatarBtn.setStyleSheet(
            f"background-color: {self._avatar_color}; "
            f"color: #ffffff; font-weight: bold; font-size: 13px; "
            f"border-radius: 8px; border: none;"
        )

        profile_text = QFrame()
        profile_text.setObjectName("profileFrame")
        pv = QVBoxLayout(profile_text)
        pv.setContentsMargins(6, 0, 0, 0)
        pv.setSpacing(1)
        pv.addWidget(self._lbl(self._role, "profileNameLabel"))
        pv.addWidget(self._lbl("Full access", "profileRoleLabel"))

        self.btnProfileDropdown = QPushButton("▾")
        self.btnProfileDropdown.setObjectName("btnProfileDropdown")
        self.btnProfileDropdown.setFixedSize(24, 38)
        self.btnProfileDropdown.clicked.connect(self._show_profile_menu)

        hl.addWidget(self.btnMenuToggle)
        hl.addWidget(self.appTitleLabel)
        hl.addStretch()
        hl.addWidget(self.searchBar)
        hl.addStretch()
        hl.addWidget(self.btnNotifications)
        hl.addWidget(self.btnMessages)
        hl.addSpacing(10)
        hl.addWidget(self.avatarBtn)
        hl.addWidget(profile_text)
        hl.addWidget(self.btnProfileDropdown)
        return bar

    def _show_profile_menu(self):
        menu = QMenu(self)
        menu.addSection(f"  {self._role}")
        menu.addSection(f"  {self._email}")
        menu.addSeparator()
        menu.addAction(QAction("👤  My Profile", self))
        action_settings = QAction("⚙  Settings", self)
        action_logout = QAction("🚪  Log out", self)
        menu.addAction(action_settings)
        menu.addSeparator()
        menu.addAction(action_logout)
        action_settings.triggered.connect(self._open_settings)
        action_logout.triggered.connect(self._confirm_logout)
        pos = self.btnProfileDropdown.mapToGlobal(
            self.btnProfileDropdown.rect().bottomLeft()
        )
        menu.exec(pos)

    # ── Sidebar — SRS 4.3 modules only ───────────────────────────
    def _build_sidebar(self):
        self.sidebarFrame = QFrame()
        self.sidebarFrame.setObjectName("sidebarFrame")
        self.sidebarFrame.setFixedWidth(250)

        vl = QVBoxLayout(self.sidebarFrame)
        vl.setContentsMargins(14, 20, 14, 16)
        vl.setSpacing(2)

        logo = QLabel("CO")
        logo.setObjectName("logoLabel")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setFixedSize(42, 42)
        logo.setStyleSheet(
            "background-color: #059669; color: #ffffff; "
            "font-weight: bold; border-radius: 10px;"
        )

        company = QLabel("Mfano Bora Africa\nCOO / Administrator · OMS")
        company.setObjectName("companyLabel")
        company.setAlignment(Qt.AlignmentFlag.AlignCenter)

        vl.addWidget(logo)
        vl.addWidget(company)
        vl.addWidget(self._h_line())

        # SRS 4.3 — Administration section
        self._nav_items = [
            ("🏠  Dashboard", 0, "sectionOverview"),
            # Administration
            ("🏢  Company Records", 2, "sectionAdmin"),
            ("💬  Internal Communication", 3, None),
            ("📅  Meeting Scheduling", 4, None),
            ("📝  Meeting Minutes", 5, None),
            ("🖥  Office Administration", 6, None),
            # Industrial Attachment
            ("🎓  Applicant Registration", 7, "sectionAttachment"),
            ("🗓  Interview Scheduling", 8, None),
            ("✅  Interview Outcomes", 9, None),
            ("🏢  Department Assignments", 10, None),
            ("👤  Supervisor Allocation", 11, None),
            ("📊  Attendance Monitoring", 12, None),
            ("📋  Evaluations", 13, None),
            ("📄  Process Clearances", 14, None),
        ]

        self._nav_buttons = []
        for i, (label, page_idx, section) in enumerate(self._nav_items):
            if section:
                section_text = {
                    "sectionOverview": "OVERVIEW",
                    "sectionAdmin": "ADMINISTRATION",
                    "sectionAttachment": "INDUSTRIAL ATTACHMENT",
                }.get(section, section)
                vl.addWidget(self._section_lbl(section_text, section))

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

    # ── Stacked pages ────────────────────────────────────────────
    def _build_stack(self):
        self.stack = QStackedWidget()
        self.stack.setObjectName("contentStack")

        # Index 0: Dashboard
        self.dashboardView = COODashboardView()
        self.stack.addWidget(self.dashboardView)  # 0

        self.stack.addWidget(QWidget())  # 1 unused

        # Indices 2–14: SRS 4.3 modules
        module_pages = [
            # ADMINISTRATION
            (
                "🏢  Company Records",
                "Manage and maintain all company operational records.",
                ["Record ID", "Title", "Category", "Date", "Status"],
                [
                    (
                        "REC-001",
                        "Fire Safety Certificate",
                        "Compliance",
                        "01 Jun 2026",
                        "Active",
                    ),
                    (
                        "REC-002",
                        "Annual Operations Report",
                        "Reports",
                        "31 Dec 2025",
                        "Active",
                    ),
                    ("REC-003", "Staff Policy Handbook", "HR", "01 Jan 2026", "Active"),
                    (
                        "REC-004",
                        "Supplier Agreement — ABC",
                        "Contracts",
                        "15 Mar 2026",
                        "Active",
                    ),
                ],
                None,
            ),
            (
                "💬  Internal Communication",
                "Manage company announcements, messages and notice board.",
                ["Title", "Type", "Posted By", "Date", "Audience"],
                [
                    (
                        "Fire Drill Notice",
                        "Announcement",
                        "COO",
                        "09 Jul 2026",
                        "All Staff",
                    ),
                    (
                        "New Office Policy",
                        "Policy Update",
                        "Admin",
                        "08 Jul 2026",
                        "All Staff",
                    ),
                    (
                        "IT System Maintenance",
                        "Notice",
                        "IT Mgr",
                        "07 Jul 2026",
                        "IT Dept",
                    ),
                    (
                        "Meeting Reminder",
                        "Reminder",
                        "COO",
                        "06 Jul 2026",
                        "Management",
                    ),
                ],
                None,
            ),
            (
                "📅  Meeting Scheduling",
                "Schedule, manage and track all organizational meetings.",
                ["Meeting", "Date", "Time", "Venue", "Status"],
                [
                    (
                        "Management Meeting",
                        "09 Jul 2026",
                        "09:00 AM",
                        "Board Room",
                        "Scheduled",
                    ),
                    (
                        "Project Review Meeting",
                        "09 Jul 2026",
                        "11:00 AM",
                        "Meeting Room 2",
                        "Pending",
                    ),
                    (
                        "Department Briefing",
                        "09 Jul 2026",
                        "02:00 PM",
                        "Main Hall",
                        "Confirmed",
                    ),
                    (
                        "Awards Ceremony Plan",
                        "09 Jul 2026",
                        "04:00 PM",
                        "Conf. Room",
                        "Scheduled",
                    ),
                ],
                "📅  Schedule Meeting",
            ),
            (
                "📝  Meeting Minutes",
                "Record and manage minutes for all organizational meetings.",
                ["Meeting", "Date", "Recorded By", "Key Decisions", "Status"],
                [
                    (
                        "Management Meeting",
                        "02 Jul 2026",
                        "COO",
                        "Budget approved",
                        "Finalized",
                    ),
                    (
                        "Dept Heads Meeting",
                        "01 Jul 2026",
                        "Admin",
                        "New hires confirmed",
                        "Draft",
                    ),
                    (
                        "Strategy Review",
                        "30 Jun 2026",
                        "COO",
                        "Q3 targets set",
                        "Finalized",
                    ),
                ],
                "📝  Record Minutes",
            ),
            (
                "🖥  Office Administration",
                "Manage office requests, supplies and administrative tasks.",
                ["Request", "Requested By", "Date", "Category", "Status"],
                [
                    (
                        "Board Room Booking",
                        "J. Kamau",
                        "09 Jul 2026",
                        "Room Booking",
                        "Approved",
                    ),
                    (
                        "Stationery Restock",
                        "Stores",
                        "08 Jul 2026",
                        "Supplies",
                        "Pending",
                    ),
                    (
                        "AC Repair — Floor 2",
                        "Ops Mgr",
                        "07 Jul 2026",
                        "Maintenance",
                        "In progress",
                    ),
                    (
                        "Printer Cartridge",
                        "IT Dept",
                        "06 Jul 2026",
                        "Supplies",
                        "Approved",
                    ),
                ],
                "🖥  Process Request",
            ),
            # INDUSTRIAL ATTACHMENT
            (
                "🎓  Applicant Registration",
                "Register and manage industrial attachment applicants.",
                ["Name", "University", "Course", "Applied", "Status"],
                [
                    (
                        "Brian Ochieng",
                        "University of Nairobi",
                        "BSc. BIT",
                        "09 Jul 2026",
                        "Pending",
                    ),
                    (
                        "Diana Anwour",
                        "Kenyatta University",
                        "BBA",
                        "08 Jul 2026",
                        "Interview",
                    ),
                    (
                        "Kevin Onyango",
                        "Strathmore University",
                        "BSc. CS",
                        "07 Jul 2026",
                        "Approved",
                    ),
                    (
                        "Mercy Wanjiku",
                        "JKUAT",
                        "BSc. Electrical Eng",
                        "06 Jul 2026",
                        "Pending",
                    ),
                ],
                "🎓  Register Applicant",
            ),
            (
                "🗓  Interview Scheduling",
                "Schedule and manage interviews for attachment applicants.",
                ["Applicant", "Date", "Time", "Interviewer", "Status"],
                [
                    (
                        "Diana Anwour",
                        "10 Jul 2026",
                        "09:30 AM",
                        "HR Manager",
                        "Scheduled",
                    ),
                    ("Brian Ochieng", "11 Jul 2026", "02:00 PM", "COO", "Scheduled"),
                    ("Ann Muthoni", "12 Jul 2026", "10:00 AM", "Dept Head", "Pending"),
                ],
                "🗓  Schedule Interview",
            ),
            (
                "✅  Interview Outcomes",
                "Record and process outcomes for completed interviews.",
                ["Applicant", "Interview Date", "Interviewer", "Decision", "Notes"],
                [
                    (
                        "Kevin Onyango",
                        "01 Jul 2026",
                        "COO",
                        "Approved",
                        "Strong candidate",
                    ),
                    (
                        "Grace Njeri",
                        "30 Jun 2026",
                        "HR Manager",
                        "Rejected",
                        "Not qualified",
                    ),
                    (
                        "James Mwangi",
                        "29 Jun 2026",
                        "Dept Head",
                        "Approved",
                        "Good fit",
                    ),
                ],
                None,
            ),
            (
                "🏢  Department Assignments",
                "Assign accepted attachees to their departments.",
                ["Attachee", "Department", "Start Date", "End Date", "Supervisor"],
                [
                    (
                        "Kevin Onyango",
                        "ICT",
                        "01 Jul 2026",
                        "30 Sep 2026",
                        "IT Manager",
                    ),
                    (
                        "James Mwangi",
                        "Operations",
                        "01 Jul 2026",
                        "30 Sep 2026",
                        "Ops Manager",
                    ),
                    (
                        "Sarah Kimani",
                        "Finance",
                        "01 Jun 2026",
                        "31 Aug 2026",
                        "Finance Head",
                    ),
                ],
                None,
            ),
            (
                "👤  Supervisor Allocation",
                "Allocate supervisors to industrial attachees.",
                ["Attachee", "Department", "Supervisor", "Allocated On", "Status"],
                [
                    ("Kevin Onyango", "ICT", "P. Njoroge", "01 Jul 2026", "Active"),
                    ("James Mwangi", "Operations", "J. Kamau", "01 Jul 2026", "Active"),
                    ("Sarah Kimani", "Finance", "M. Otieno", "01 Jun 2026", "Active"),
                ],
                None,
            ),
            (
                "📊  Attendance Monitoring",
                "Monitor and record attendance for all industrial attachees.",
                ["Attachee", "Department", "Date", "Check-in", "Check-out", "Status"],
                [
                    (
                        "Kevin Onyango",
                        "ICT",
                        "09 Jul 2026",
                        "08:02 AM",
                        "05:01 PM",
                        "Present",
                    ),
                    (
                        "James Mwangi",
                        "Operations",
                        "09 Jul 2026",
                        "08:15 AM",
                        "—",
                        "Present",
                    ),
                    ("Sarah Kimani", "Finance", "09 Jul 2026", "—", "—", "Absent"),
                ],
                None,
            ),
            (
                "📋  Evaluations",
                "Record assessments and evaluations for industrial attachees.",
                ["Attachee", "Department", "Eval Date", "Score", "Remarks"],
                [
                    (
                        "Kevin Onyango",
                        "ICT",
                        "30 Jun 2026",
                        "88%",
                        "Excellent performance",
                    ),
                    (
                        "Sarah Kimani",
                        "Finance",
                        "30 Jun 2026",
                        "75%",
                        "Good, needs improvement",
                    ),
                    ("James Mwangi", "Operations", "30 Jun 2026", "91%", "Outstanding"),
                ],
                None,
            ),
            (
                "📄  Process Clearances",
                "Process and manage clearances for departing attachees.",
                [
                    "Attachee",
                    "Department",
                    "End Date",
                    "Clearance Status",
                    "Processed By",
                ],
                [
                    ("Grace Njeri", "Admin", "30 Jun 2026", "Cleared", "COO"),
                    ("Tom Otieno", "Marketing", "30 Jun 2026", "Pending", "—"),
                    ("Ann Muthoni", "Finance", "31 Aug 2026", "Not due", "—"),
                ],
                "📄  Process Clearance",
            ),
        ]

        for title, subtitle, cols, rows, action in module_pages:
            view = ModuleView(title, subtitle, cols, rows, action)
            if action:
                view.actionBtn.clicked.connect(self._action_for_module(title))
            self.stack.addWidget(view)

        return self.stack

    def _action_for_module(self, title: str):
        if "Meeting" in title and "Minutes" not in title:
            return self._open_schedule_meeting
        if "Applicant" in title or "Register" in title:
            return self._open_register_applicant
        if "Interview Sched" in title:
            return self._open_schedule_meeting
        if "Minutes" in title:
            return lambda: print("Record Minutes clicked")
        if "Request" in title or "Office Admin" in title:
            return lambda: print("Process Office Request clicked")
        if "Clearance" in title:
            return lambda: print("Process Clearance clicked")
        return lambda: None

    # ── Signal wiring ────────────────────────────────────────────
    def _wire_signals(self):
        self.btnMenuToggle.clicked.connect(self._toggle_sidebar)
        self.btnSettings.clicked.connect(self._open_settings)
        self.btnLogout.clicked.connect(self._confirm_logout)

        dv = self.dashboardView
        dv.btnScheduleMeeting.clicked.connect(self._open_schedule_meeting)
        dv.btnRegisterApplicant.clicked.connect(self._open_register_applicant)
        dv.btnViewActivity.clicked.connect(lambda: self._navigate(3, 2))
        dv.btnViewAttachment.clicked.connect(lambda: self._navigate(7, 6))
        dv.btnViewMeetings.clicked.connect(lambda: self._navigate(4, 3))
        dv.btnViewApprovals.clicked.connect(lambda: self._navigate(9, 8))
        dv.btnViewRequests.clicked.connect(lambda: self._navigate(6, 5))

        dv.btnQaRegisterApplicant.clicked.connect(self._open_register_applicant)
        dv.btnQaScheduleInterview.clicked.connect(lambda: self._navigate(8, 7))
        dv.btnQaCreateMeeting.clicked.connect(self._open_schedule_meeting)
        dv.btnQaRecordMinutes.clicked.connect(lambda: self._navigate(5, 4))
        dv.btnQaProcessOfficeReq.clicked.connect(lambda: self._navigate(6, 5))
        dv.btnQaGenerateReport.clicked.connect(lambda: print("Generate Report clicked"))

    # ── Navigation ───────────────────────────────────────────────
    def _navigate(self, page_index: int, nav_btn_index: int = 0):
        self.stack.setCurrentIndex(page_index)
        for i, btn in enumerate(self._nav_buttons):
            btn.setChecked(i == nav_btn_index)

    def _toggle_sidebar(self):
        self._sidebar_expanded = not self._sidebar_expanded
        self.sidebarFrame.setFixedWidth(250 if self._sidebar_expanded else 0)

    # ── Dialogs ──────────────────────────────────────────────────
    def _open_schedule_meeting(self):
        ScheduleMeetingDialog(self).exec()

    def _open_register_applicant(self):
        RegisterApplicantDialog(self).exec()

    def _open_settings(self):
        # pyrefly: ignore [missing-import]
        from PyQt6.QtWidgets import QMessageBox

        QMessageBox.information(self, "Settings", "Settings panel coming soon.")

    def _confirm_logout(self):
        dlg = ConfirmLogoutDialog(self)
        if dlg.exec():
            self._go_to_login()

    def _go_to_login(self):
        from login import LoginWindow, load_login_stylesheet

        app = QApplication.instance()
        load_login_stylesheet(app)
        self.login = LoginWindow()
        self.login.showMaximized()
        self.close()

    # ── Helpers ──────────────────────────────────────────────────
    def _lbl(self, text, obj_name):
        lbl = QLabel(text)
        lbl.setObjectName(obj_name)
        return lbl

    def _h_line(self):
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        return line

    def _section_lbl(self, text, obj_name):
        lbl = QLabel(text)
        lbl.setObjectName(obj_name)
        return lbl


def load_stylesheet(app):
    style_path = os.path.join(os.path.dirname(__file__), "styles", "style.qss")
    with open(style_path, "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())
