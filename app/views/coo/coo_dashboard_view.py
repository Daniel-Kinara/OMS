"""
COO Dashboard View — SRS Chapter 4.3
Administration + Industrial Attachment modules
"""

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

# pyrefly: ignore [missing-import]
from PyQt6.QtGui import QPainter, QColor, QPen

# pyrefly: ignore [missing-import]
from PyQt6.QtCharts import (
    QChart,
    QChartView,
    QPieSeries,
    QBarSeries,
    QBarSet,
    QBarCategoryAxis,
    QValueAxis,
)


class COODashboardView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self._build()

    def _build(self):
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setObjectName("dashScroll")

        container = QWidget()
        container.setObjectName("dashContainer")
        container.setAutoFillBackground(True)

        root = QVBoxLayout(container)
        root.setContentsMargins(28, 24, 28, 28)
        root.setSpacing(18)

        root.addWidget(self._build_header())
        root.addWidget(self._build_action_buttons())
        root.addWidget(self._build_stat_cards())
        root.addWidget(self._build_row1())
        root.addWidget(self._build_row2())
        root.addWidget(self._build_quick_actions())

        scroll.setWidget(container)
        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.addWidget(scroll)

    # ── Header ───────────────────────────────────────────────────
    def _build_header(self):
        frame = QFrame()
        frame.setObjectName("headerFrame")
        hl = QHBoxLayout(frame)
        hl.setContentsMargins(0, 0, 0, 0)

        vl = QVBoxLayout()
        vl.setSpacing(3)
        title = QLabel("Chief Operations Officer Dashboard")
        title.setObjectName("titleLabel")
        sub = QLabel("Here's an overview of today's administrative operations.")
        sub.setObjectName("metaLabel")
        vl.addWidget(title)
        vl.addWidget(sub)

        badge = QLabel("📅  Thursday, 9 July 2026   10:30 AM")
        badge.setObjectName("dateBadge")

        hl.addLayout(vl)
        hl.addStretch()
        hl.addWidget(badge)
        return frame

    # ── Action buttons ───────────────────────────────────────────
    def _build_action_buttons(self):
        frame = QFrame()
        frame.setObjectName("logButtonsFrame")
        hl = QHBoxLayout(frame)
        hl.setContentsMargins(0, 0, 0, 0)
        hl.setSpacing(10)
        hl.addStretch()

        self.btnScheduleMeeting = QPushButton("📅  Schedule Meeting")
        self.btnScheduleMeeting.setObjectName("btnLogMaintenance")
        self.btnRegisterApplicant = QPushButton("👤  Register Applicant")
        self.btnRegisterApplicant.setObjectName("btnLogInspection")

        hl.addWidget(self.btnScheduleMeeting)
        hl.addWidget(self.btnRegisterApplicant)
        return frame

    # ── Stat cards ───────────────────────────────────────────────
    def _build_stat_cards(self):
        frame = QFrame()
        frame.setObjectName("statsFrame")
        hl = QHBoxLayout(frame)
        hl.setSpacing(14)
        hl.setContentsMargins(0, 0, 0, 0)

        cards = [
            ("🏢", "2,540", "Company Records", "cardVisitors"),
            ("💬", "18", "Communications", "cardMaintenance"),
            ("📅", "6", "Today's Meetings", "cardInspections"),
            ("📋", "12", "Office Requests", "cardSafety"),
            ("🎓", "24", "Industrial Attachees", "cardCompound"),
            ("📄", "12", "Pending Clearances", "cardPending"),
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

    # ── Row 1: Workload + Donut + Recent Activity ─────────────────
    def _build_row1(self):
        row = QFrame()
        row.setObjectName("gridFrame1")
        hl = QHBoxLayout(row)
        hl.setSpacing(14)
        hl.setContentsMargins(0, 0, 0, 0)

        hl.addWidget(self._build_workload_panel(), 1)
        hl.addWidget(self._build_attachment_donut(), 1)
        hl.addWidget(self._build_activity_panel(), 1)
        return row

    def _build_workload_panel(self):
        panel = QFrame()
        panel.setObjectName("checklistPanel")
        vl = QVBoxLayout(panel)
        vl.setSpacing(10)

        hdr = QHBoxLayout()
        lbl = QLabel("Operational Workload Today")
        lbl.setObjectName("checklistTitle")
        hdr.addWidget(lbl)
        hdr.addStretch()
        vl.addLayout(hdr)

        grid = QFrame()
        gl = QHBoxLayout(grid)
        gl.setSpacing(10)
        gl.setContentsMargins(0, 0, 0, 0)

        workloads = [
            ("📅", "Meetings Today", "6", "2 Upcoming", "#2563eb"),
            ("📋", "Pending Requests", "12", "6 High Priority", "#d97706"),
            ("🎓", "Interviews Today", "5", "3 Scheduled", "#059669"),
            ("📄", "Clearances Due", "12", "4 Overdue", "#dc2626"),
        ]
        for icon, label, value, sub, color in workloads:
            card = QFrame()
            card.setObjectName("cardVisitors")
            cv = QVBoxLayout(card)
            cv.setSpacing(2)

            icon_lbl = QLabel(icon)
            icon_lbl.setObjectName("cardVisitorsIcon")
            icon_lbl.setStyleSheet(f"color: {color};")

            lbl_name = QLabel(label)
            lbl_name.setObjectName("cardVisitorsCaption")

            val_lbl = QLabel(value)
            val_lbl.setObjectName("cardVisitorsValue")
            val_lbl.setStyleSheet(
                f"font-size: 22px; font-weight: bold; color: {color};"
            )

            sub_lbl = QLabel(sub)
            sub_lbl.setObjectName("cardVisitorsCaption")
            sub_lbl.setStyleSheet(f"color: {color}; font-size: 11px;")

            cv.addWidget(icon_lbl)
            cv.addWidget(lbl_name)
            cv.addWidget(val_lbl)
            cv.addWidget(sub_lbl)
            gl.addWidget(card)

        vl.addWidget(grid)
        return panel

    def _build_attachment_donut(self):
        panel = QFrame()
        panel.setObjectName("maintenancePanel")
        vl = QVBoxLayout(panel)
        vl.setSpacing(10)

        hdr = QHBoxLayout()
        lbl = QLabel("Attachment Distribution by Dept")
        lbl.setObjectName("maintenanceTitle")
        self.btnViewAttachment = QPushButton("View all ›")
        self.btnViewAttachment.setObjectName("btnViewMaintenance")
        hdr.addWidget(lbl)
        hdr.addStretch()
        hdr.addWidget(self.btnViewAttachment)
        vl.addLayout(hdr)

        chart = QChart()
        chart.legend().hide()
        chart.setBackgroundVisible(False)
        chart.layout().setContentsMargins(0, 0, 0, 0)

        pie = QPieSeries()
        pie.setHoleSize(0.45)

        data = [
            ("Administration", 6, "#2563eb"),
            ("Finance", 5, "#059669"),
            ("ICT", 4, "#d97706"),
            ("Operations", 5, "#7c3aed"),
            ("Marketing", 4, "#dc2626"),
        ]
        for name, val, color in data:
            s = pie.append(name, val)
            s.setColor(QColor(color))
            s.setBorderWidth(0)

        chart.addSeries(pie)

        view = QChartView(chart)
        view.setRenderHint(QPainter.RenderHint.Antialiasing)
        view.setStyleSheet("background: transparent;")
        view.setMinimumHeight(160)

        body = QHBoxLayout()
        body.addWidget(view, 1)

        legend = QVBoxLayout()
        legend.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        for name, val, color in data:
            row = QHBoxLayout()
            dot = QLabel("●")
            dot.setStyleSheet(f"color: {color}; font-size: 14px;")
            nm = QLabel(name)
            nm.setStyleSheet("color: #64748b; font-size: 11px;")
            vl2 = QLabel(f"{val}  ({int(val / 24 * 100)}%)")
            vl2.setStyleSheet("color: #0f172a; font-size: 11px; font-weight: bold;")
            row.addWidget(dot)
            row.addWidget(nm)
            row.addStretch()
            row.addWidget(vl2)
            legend.addLayout(row)
        body.addLayout(legend, 1)
        vl.addLayout(body)
        return panel

    def _build_activity_panel(self):
        panel = QFrame()
        panel.setObjectName("activityPanel")
        vl = QVBoxLayout(panel)
        vl.setSpacing(10)

        hdr = QHBoxLayout()
        lbl = QLabel("Recent Activity")
        lbl.setObjectName("activityTitle")
        self.btnViewActivity = QPushButton("View all ›")
        self.btnViewActivity.setObjectName("btnViewActivity")
        hdr.addWidget(lbl)
        hdr.addStretch()
        hdr.addWidget(self.btnViewActivity)
        vl.addLayout(hdr)

        self.activityList = QListWidget()
        self.activityList.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        items = [
            "● New applicant registered — Brian Ochieng",
            "● Interview scheduled — Diana Anwour — 9:35 AM",
            "● Office request approved — Board Room booking",
            "● Attachee evaluation submitted — Kevin Onyango",
            "● Meeting minutes uploaded — Management Meeting",
            "● Communication sent — Fire drill notice",
        ]
        for t in items:
            self.activityList.addItem(QListWidgetItem(t))
        vl.addWidget(self.activityList)
        return panel

    # ── Row 2: Pending Approvals + Upcoming Meetings ──────────────
    def _build_row2(self):
        row = QFrame()
        row.setObjectName("gridFrame1")
        hl = QHBoxLayout(row)
        hl.setSpacing(14)
        hl.setContentsMargins(0, 0, 0, 0)

        hl.addWidget(self._build_approvals_panel(), 1)
        hl.addWidget(self._build_meetings_panel(), 1)
        hl.addWidget(self._build_office_requests_donut(), 1)
        return row

    def _build_approvals_panel(self):
        panel = QFrame()
        panel.setObjectName("checklistPanel")
        vl = QVBoxLayout(panel)
        vl.setSpacing(10)

        hdr = QHBoxLayout()
        lbl = QLabel("My Pending Approvals")
        lbl.setObjectName("checklistTitle")
        badge = QLabel("7")
        badge.setObjectName("pendingBadge")
        badge.setStyleSheet(
            "background-color: #dc2626; color: #fff; "
            "border-radius: 10px; padding: 2px 7px; "
            "font-size: 11px; font-weight: bold;"
        )
        self.btnViewApprovals = QPushButton("View all ›")
        self.btnViewApprovals.setObjectName("btnViewChecklist")
        hdr.addWidget(lbl)
        hdr.addWidget(badge)
        hdr.addStretch()
        hdr.addWidget(self.btnViewApprovals)
        vl.addLayout(hdr)

        approvals = [
            ("📋", "Interview Outcomes", "Awaiting approval", "2", "#2563eb"),
            ("🏢", "Department Assignments", "Awaiting approval", "2", "#d97706"),
            ("👤", "Supervisor Allocations", "Awaiting approval", "1", "#059669"),
            ("📄", "Office Requests", "Awaiting your action", "2", "#dc2626"),
        ]
        for icon, title, sub, count, color in approvals:
            item_row = QFrame()
            item_row.setObjectName("visitorPanel")
            item_row.setStyleSheet(
                "QFrame#visitorPanel { border-radius: 8px; "
                "border: 1px solid #e2e8f0; padding: 8px; }"
            )
            il = QHBoxLayout(item_row)
            il.setContentsMargins(8, 6, 8, 6)

            icon_lbl = QLabel(icon)
            icon_lbl.setStyleSheet(f"font-size: 18px; color: {color};")
            text_vl = QVBoxLayout()
            text_vl.setSpacing(1)
            t_lbl = QLabel(title)
            t_lbl.setStyleSheet("font-weight: bold; font-size: 13px;")
            s_lbl = QLabel(sub)
            s_lbl.setStyleSheet("color: #64748b; font-size: 11px;")
            text_vl.addWidget(t_lbl)
            text_vl.addWidget(s_lbl)

            count_lbl = QLabel(count)
            count_lbl.setStyleSheet(
                f"background-color: transparent; "
                f"color: {color}; "
                f"border: 2px solid {color}; "
                f"border-radius: 12px; "
                f"padding: 2px 8px; font-weight: bold;"
            )
            count_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            count_lbl.setFixedSize(28, 28)

            il.addWidget(icon_lbl)
            il.addLayout(text_vl)
            il.addStretch()
            il.addWidget(count_lbl)
            vl.addWidget(item_row)

        return panel

    def _build_meetings_panel(self):
        panel = QFrame()
        panel.setObjectName("maintenancePanel")
        vl = QVBoxLayout(panel)
        vl.setSpacing(10)

        hdr = QHBoxLayout()
        lbl = QLabel("Upcoming Meetings")
        lbl.setObjectName("maintenanceTitle")
        self.btnViewMeetings = QPushButton("View full schedule ›")
        self.btnViewMeetings.setObjectName("btnViewMaintenance")
        hdr.addWidget(lbl)
        hdr.addStretch()
        hdr.addWidget(self.btnViewMeetings)
        vl.addLayout(hdr)

        self.meetingsTable = self._make_table(
            ["Meeting", "Time", "Venue", "Status"],
            [
                ("Management Meeting", "09:00 AM", "Board Room", "Scheduled"),
                ("Project Review Meeting", "11:00 AM", "Meeting Room 2", "Pending"),
                ("Department Briefing", "02:00 PM", "Main Hall", "Confirmed"),
                ("Awards Ceremony Plan", "04:00 PM", "Conference Room", "Scheduled"),
            ],
        )
        vl.addWidget(self.meetingsTable)
        return panel

    def _build_office_requests_donut(self):
        panel = QFrame()
        panel.setObjectName("activityPanel")
        vl = QVBoxLayout(panel)
        vl.setSpacing(10)

        hdr = QHBoxLayout()
        lbl = QLabel("Office Requests by Status")
        lbl.setObjectName("activityTitle")
        self.btnViewRequests = QPushButton("View all ›")
        self.btnViewRequests.setObjectName("btnViewActivity")
        hdr.addWidget(lbl)
        hdr.addStretch()
        hdr.addWidget(self.btnViewRequests)
        vl.addLayout(hdr)

        chart = QChart()
        chart.legend().hide()
        chart.setBackgroundVisible(False)
        chart.layout().setContentsMargins(0, 0, 0, 0)

        pie = QPieSeries()
        pie.setHoleSize(0.45)
        slices = [
            ("Completed", 22, "#059669"),
            ("Pending", 10, "#d97706"),
            ("In Progress", 8, "#2563eb"),
        ]
        for name, val, color in slices:
            s = pie.append(name, val)
            s.setColor(QColor(color))
            s.setBorderWidth(0)

        chart.addSeries(pie)
        view = QChartView(chart)
        view.setRenderHint(QPainter.RenderHint.Antialiasing)
        view.setStyleSheet("background: transparent;")
        view.setMinimumHeight(150)

        body = QHBoxLayout()
        body.addWidget(view, 1)

        legend = QVBoxLayout()
        legend.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        for name, val, color in slices:
            row = QHBoxLayout()
            dot = QLabel("●")
            dot.setStyleSheet(f"color: {color}; font-size: 14px;")
            nm = QLabel(name)
            nm.setStyleSheet("color: #64748b; font-size: 11px;")
            v2 = QLabel(f"{int(val / 40 * 100)}% ({val})")
            v2.setStyleSheet("color: #0f172a; font-size: 11px; font-weight: bold;")
            row.addWidget(dot)
            row.addWidget(nm)
            row.addStretch()
            row.addWidget(v2)
            legend.addLayout(row)
        body.addLayout(legend, 1)
        vl.addLayout(body)
        return panel

    # ── Quick Actions ─────────────────────────────────────────────
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

        actions = [
            ("👤\nRegister Applicant", "btnQaRegisterApplicant"),
            ("📅\nSchedule Interview", "btnQaScheduleInterview"),
            ("🗓\nCreate Meeting", "btnQaCreateMeeting"),
            ("📝\nRecord Minutes", "btnQaRecordMinutes"),
            ("🏢\nProcess Office Req", "btnQaProcessOfficeReq"),
            ("📊\nGenerate Report", "btnQaGenerateReport"),
        ]
        for text, name in actions:
            btn = QPushButton(text)
            btn.setObjectName(name)
            setattr(self, name, btn)
            hl.addWidget(btn)

        vl.addLayout(hl)
        return frame

    # ── Table factory ─────────────────────────────────────────────
    def _make_table(self, headers, rows, max_height=None):
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
        t.verticalHeader().setDefaultSectionSize(38)
        if max_height:
            t.setMaximumHeight(max_height)
        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                t.setItem(r, c, QTableWidgetItem(val))
        return t
