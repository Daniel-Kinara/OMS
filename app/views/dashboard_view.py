# pyrefly: ignore [missing-import]
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QListWidget,
    QListWidgetItem,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView,
    QPushButton,
    QScrollArea,
)

# pyrefly: ignore [missing-import]
from PyQt6.QtCore import Qt


class DashboardView(QWidget):
    """The main dashboard — loaded by default when the app starts."""

    # Signals to request navigation from the main window
    view_maintenance_requested = None  # set by main window after init
    view_visitors_requested = None
    view_inspections_requested = None
    log_maintenance_requested = None
    log_inspection_requested = None
    register_visitor_requested = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self._build()

    def _build(self):
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setObjectName("dashScroll")

        container = QWidget()
        container.setObjectName("dashContainer")
        root = QVBoxLayout(container)
        root.setContentsMargins(28, 24, 28, 28)
        root.setSpacing(18)

        root.addWidget(self._build_header())
        root.addWidget(self._build_log_buttons())
        root.addWidget(self._build_stat_cards())
        root.addWidget(self._build_grid_row())
        root.addWidget(self._build_visitor_log())
        root.addWidget(self._build_quick_actions())

        scroll.setWidget(container)
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.addWidget(scroll)

    # ── Header ──────────────────────────────────────────────────────────
    def _build_header(self):
        frame = QFrame()
        frame.setObjectName("headerFrame")
        hl = QHBoxLayout(frame)
        hl.setContentsMargins(0, 0, 0, 0)

        vl = QVBoxLayout()
        vl.setSpacing(3)
        title = QLabel("Welcome back, Operations Manager! 👋")
        title.setObjectName("titleLabel")
        sub = QLabel("Here's an overview of today's operations.")
        sub.setObjectName("metaLabel")
        vl.addWidget(title)
        vl.addWidget(sub)

        badge = QLabel("📅  Thursday, 9 July 2026   10:30 AM")
        badge.setObjectName("dateBadge")

        hl.addLayout(vl)
        hl.addStretch()
        hl.addWidget(badge)
        return frame

    # ── Log buttons ─────────────────────────────────────────────────────
    def _build_log_buttons(self):
        frame = QFrame()
        frame.setObjectName("logButtonsFrame")
        hl = QHBoxLayout(frame)
        hl.setContentsMargins(0, 0, 0, 0)
        hl.setSpacing(10)
        hl.addStretch()

        self.btnLogMaintenance = QPushButton("✎  Log Maintenance Issue")
        self.btnLogMaintenance.setObjectName("btnLogMaintenance")
        self.btnLogInspection = QPushButton("✓  Log Facility Inspection")
        self.btnLogInspection.setObjectName("btnLogInspection")

        hl.addWidget(self.btnLogMaintenance)
        hl.addWidget(self.btnLogInspection)
        return frame

    # ── Stat cards ──────────────────────────────────────────────────────
    def _build_stat_cards(self):
        frame = QFrame()
        frame.setObjectName("statsFrame")
        hl = QHBoxLayout(frame)
        hl.setSpacing(14)
        hl.setContentsMargins(0, 0, 0, 0)

        cards = [
            ("👤", "12", "Visitors Today", "cardVisitors"),
            ("🔧", "6", "Open Maintenance Requests", "cardMaintenance"),
            ("🔍", "3/5", "Facility Inspections", "cardInspections"),
            ("🛡", "2", "Safety Checks Due", "cardSafety"),
            ("🌳", "Clear", "Compound Status", "cardCompound"),
        ]
        for icon, value, caption, name in cards:
            card = QFrame()
            card.setObjectName(name)
            vl = QVBoxLayout(card)
            vl.setSpacing(4)
            lbl_icon = QLabel(icon)
            lbl_icon.setObjectName(f"{name}Icon")
            lbl_val = QLabel(value)
            lbl_val.setObjectName(f"{name}Value")
            lbl_cap = QLabel(caption)
            lbl_cap.setObjectName(f"{name}Caption")
            vl.addWidget(lbl_icon)
            vl.addWidget(lbl_val)
            vl.addWidget(lbl_cap)
            hl.addWidget(card)
        return frame

    # ── Panel header helper ──────────────────────────────────────────────
    def _panel_header(self, title: str, btn_name: str) -> tuple:
        hl = QHBoxLayout()
        hl.setContentsMargins(0, 0, 0, 0)
        lbl = QLabel(title)
        lbl.setObjectName(f"{btn_name.replace('btn', '').lower()}Title")
        btn = QPushButton("View all ›")
        btn.setObjectName(btn_name)
        hl.addWidget(lbl)
        hl.addStretch()
        hl.addWidget(btn)
        return hl, btn

    # ── Content grid row ────────────────────────────────────────────────
    def _build_grid_row(self):
        frame = QFrame()
        frame.setObjectName("gridFrame1")
        hl = QHBoxLayout(frame)
        hl.setSpacing(14)
        hl.setContentsMargins(0, 0, 0, 0)

        # Checklist panel
        cp = QFrame()
        cp.setObjectName("checklistPanel")
        cv = QVBoxLayout(cp)
        cv.setSpacing(10)
        hdr, self.btnViewChecklist = self._panel_header(
            "Facility Inspection Checklist", "btnViewChecklist"
        )
        cv.addLayout(hdr)
        self.checklistWidget = QListWidget()
        self.checklistWidget.setMaximumHeight(185)
        self.checklistWidget.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        items = [
            "01  Reception & Lobby — 100%",
            "02  Compound & Grounds — 100%",
            "03  Washrooms — 100%",
            "04  Parking & Perimeter — 40%",
            "05  Fire & Safety Equipment — Not started",
        ]
        for t in items:
            self.checklistWidget.addItem(QListWidgetItem(t))
        cv.addWidget(self.checklistWidget)
        hl.addWidget(cp)

        # Maintenance panel
        mp = QFrame()
        mp.setObjectName("maintenancePanel")
        mv = QVBoxLayout(mp)
        mv.setSpacing(10)
        hdr2, self.btnViewMaintenance = self._panel_header(
            "Maintenance Requests", "btnViewMaintenance"
        )
        mv.addLayout(hdr2)
        self.maintenanceTable = self._make_table(
            ["Issue", "Location", "Priority"],
            [
                ("East wing AC unit", "Floor 2", "Pending"),
                ("Parking gate light", "Parking", "Overdue"),
                ("Leaking tap", "Washroom B", "In progress"),
                ("Broken window latch", "Reception", "Resolved"),
            ],
        )
        mv.addWidget(self.maintenanceTable)
        hl.addWidget(mp)

        # Activity panel
        ap = QFrame()
        ap.setObjectName("activityPanel")
        av = QVBoxLayout(ap)
        av.setSpacing(10)
        hdr3, self.btnViewActivity = self._panel_header(
            "Recent Activity", "btnViewActivity"
        )
        av.addLayout(hdr3)
        self.activityListWidget = QListWidget()
        self.activityListWidget.setMaximumHeight(185)
        self.activityListWidget.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        for t in [
            "●  Visitor Grace Wanjiru checked in — 9:12 AM",
            "●  Maintenance #41 raised — East wing AC — 9:40 AM",
            "●  Inspection logged — Washrooms, no issues — 10:05 AM",
            "●  Safety flag raised — Parking gate out — 10:52 AM",
            "●  Task 'Restock supplies' in progress — 11:20 AM",
        ]:
            self.activityListWidget.addItem(QListWidgetItem(t))
        av.addWidget(self.activityListWidget)
        hl.addWidget(ap)

        return frame

    # ── Visitor log ─────────────────────────────────────────────────────
    def _build_visitor_log(self):
        frame = QFrame()
        frame.setObjectName("visitorPanel")
        vl = QVBoxLayout(frame)
        vl.setSpacing(10)
        hdr, self.btnViewVisitorLog = self._panel_header(
            "Today's Visitor Log", "btnViewVisitorLog"
        )
        vl.addLayout(hdr)
        self.visitorLogTable = self._make_table(
            ["Visitor", "Host", "Time", "Status"],
            [
                ("Grace Wanjiru", "J. Kamau", "9:12 AM", "Checked in"),
                ("Peter Njoroge", "Ops Mgr", "9:55 AM", "Checked in"),
                ("Amina Hassan", "HR Desk", "8:30 AM", "Checked out"),
                ("Samuel Kiptoo", "Stores", "11:10 AM", "Checked in"),
            ],
        )
        vl.addWidget(self.visitorLogTable)
        return frame

    # ── Quick actions ────────────────────────────────────────────────────
    def _build_quick_actions(self):
        frame = QFrame()
        frame.setObjectName("quickActionsFrame")
        vl = QVBoxLayout(frame)
        vl.setSpacing(12)
        lbl = QLabel("Quick Actions")
        lbl.setObjectName("quickActionsTitle")
        vl.addWidget(lbl)
        hl = QHBoxLayout()
        hl.setSpacing(12)
        hl.setObjectName("quickActionsLayout")

        self.btnQaReportMaintenance = QPushButton("✎\nReport Maintenance")
        self.btnQaRegisterVisitor = QPushButton("👤\nRegister Visitor")
        self.btnQaLogInspection = QPushButton("✓\nLog Inspection")

        for btn in (
            self.btnQaReportMaintenance,
            self.btnQaRegisterVisitor,
            self.btnQaLogInspection,
        ):
            hl.addWidget(btn)
        vl.addLayout(hl)
        return frame

    # ── Table factory ────────────────────────────────────────────────────
    def _make_table(self, headers: list, rows: list) -> QTableWidget:
        t = QTableWidget(len(rows), len(headers))
        t.setHorizontalHeaderLabels(headers)
        t.verticalHeader().setVisible(False)
        t.horizontalHeader().setStretchLastSection(True)
        t.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        t.setShowGrid(False)
        t.setAlternatingRowColors(True)
        t.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        t.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        t.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        t.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        t.setMaximumHeight(185)
        t.verticalHeader().setDefaultSectionSize(38)
        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                t.setItem(r, c, QTableWidgetItem(val))
        return t
