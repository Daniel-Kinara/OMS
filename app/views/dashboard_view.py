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
from PyQt6.QtGui import QPainter, QColor, QFont, QPen, QBrush

# pyrefly: ignore [missing-import]
from PyQt6.QtCharts import (
    QChart,
    QChartView,
    QLineSeries,
    QPieSeries,
    QValueAxis,
    QCategoryAxis
)

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
        container.setAutoFillBackground(True)
        self.setAutoFillBackground(True)

        root = QVBoxLayout(container)
        root.setContentsMargins(28, 24, 28, 28)
        root.setSpacing(18)

        root.addWidget(self._build_header())
        root.addWidget(self._build_log_buttons())
        root.addWidget(self._build_stat_cards())
        root.addWidget(self._build_content_grid())
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
    def _panel_header(self, title: str, btn_name: str, title_name: str) -> tuple:
        hl = QHBoxLayout()
        hl.setContentsMargins(0, 0, 0, 0)
        lbl = QLabel(title)
        lbl.setObjectName(title_name)
        btn = QPushButton("View all ›")
        btn.setObjectName(btn_name)
        hl.addWidget(lbl)
        hl.addStretch()
        hl.addWidget(btn)
        return hl, btn

    # ── Grid Layout (2 Rows x 3 Columns) ─────────────────────────────────
    def _build_content_grid(self):
        outer = QFrame()
        outer.setObjectName("contentGridFrame")
        grid_layout = QVBoxLayout(outer)
        grid_layout.setSpacing(14)
        grid_layout.setContentsMargins(0, 0, 0, 0)

        # ════════════════════════════════════════════════════════════════
        # ROW 1 (TOP) — Operational Overview, Tasks by Status, Recent Activity
        # ════════════════════════════════════════════════════════════════
        row1 = QFrame()
        row1.setObjectName("row1Frame")
        r1_layout = QHBoxLayout(row1)
        r1_layout.setSpacing(14)
        r1_layout.setContentsMargins(0, 0, 0, 0)

        # 1. Operational Overview
        line_panel = QFrame()
        line_panel.setObjectName("lineChartPanel")
        line_layout = QVBoxLayout(line_panel)
        line_layout.setSpacing(0)
        
        line_hdr, self.btnViewLineChart = self._panel_header("Operational Overview", "btnViewLineChart", "lineChartTitle")
        
        line_chart = QChart()
        line_chart.legend().hide()
        line_chart.setBackgroundVisible(False)
        line_chart.layout().setContentsMargins(0, 0, 0, 0)
        
        series = QLineSeries()
        series.append(0, 20)
        series.append(1, 40)
        series.append(2, 35)
        series.append(3, 50)
        series.append(4, 45)
        series.append(5, 75)
        
        pen = QPen(QColor("#c5a880"))
        pen.setWidth(3)
        series.setPen(pen)
        
        line_chart.addSeries(series)
        line_chart.createDefaultAxes()
        
        for axis in line_chart.axes():
            axis.hide()
            
        line_view = QChartView(line_chart)
        line_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        line_view.setStyleSheet("background: transparent;")
        line_view.setMinimumHeight(180)
        
        # Stats container for Operational Overview
        line_body = QHBoxLayout()
        line_body.addWidget(line_view, 2)
        
        line_stats = QVBoxLayout()
        line_stats.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        
        def add_line_stat(color, label, value):
            hl = QHBoxLayout()
            dot = QLabel("●")
            dot.setStyleSheet(f"color: {color}; font-size: 12px;")
            lbl = QLabel(label)
            lbl.setStyleSheet("color: #64748b; font-size: 11px; font-weight: bold;")
            val = QLabel(value)
            val.setStyleSheet("color: #0f172a; font-size: 11px; font-weight: bold;")
            hl.addWidget(dot)
            hl.addWidget(lbl)
            hl.addStretch()
            hl.addWidget(val)
            line_stats.addLayout(hl)
            
        add_line_stat("#c5a880", "Tasks Completed", "72%")
        add_line_stat("#059669", "Maintenance Resolved", "80%")
        add_line_stat("#2563eb", "Visitors Managed", "78%")
        add_line_stat("#dc2626", "Meetings Conducted", "85%")
        
        line_body.addLayout(line_stats, 1)
        
        line_layout.addLayout(line_hdr)
        line_layout.addLayout(line_body)
        r1_layout.addWidget(line_panel, 1)

        # 2. Tasks by Status (Donut Chart)
        donut_panel = QFrame()
        donut_panel.setObjectName("donutChartPanel")
        donut_layout = QVBoxLayout(donut_panel)
        donut_layout.setSpacing(10)
        
        donut_hdr, self.btnViewDonutChart = self._panel_header("Tasks by Status", "btnViewDonutChart", "donutChartTitle")
        
        donut_chart = QChart()
        donut_chart.legend().hide()
        donut_chart.setBackgroundVisible(False)
        donut_chart.layout().setContentsMargins(0, 0, 0, 0)
        
        pie_series = QPieSeries()
        pie_series.setHoleSize(0.45)
        
        slice_completed = pie_series.append("Completed", 54)
        slice_completed.setColor(QColor("#2563eb"))
        slice_in_progress = pie_series.append("In Progress", 38)
        slice_in_progress.setColor(QColor("#c5a880"))
        slice_pending = pie_series.append("Pending", 26)
        slice_pending.setColor(QColor("#059669"))
        slice_overdue = pie_series.append("Overdue", 10)
        slice_overdue.setColor(QColor("#dc2626"))
        
        for s in pie_series.slices():
            s.setBorderWidth(0)
            
        donut_chart.addSeries(pie_series)
        
        donut_view = QChartView(donut_chart)
        donut_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        donut_view.setStyleSheet("background: transparent;")
        donut_view.setMinimumHeight(180)
        
        donut_container = QWidget()
        donut_cl = QVBoxLayout(donut_container)
        donut_cl.setContentsMargins(0, 0, 0, 0)
        donut_cl.addWidget(donut_view)
        
        donut_body = QHBoxLayout()
        donut_body.addWidget(donut_container, 1)
        
        legend_layout = QVBoxLayout()
        legend_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        
        def add_donut_legend(color, label, value, percentage):
            hl = QHBoxLayout()
            dot = QLabel("●")
            dot.setStyleSheet(f"color: {color}; font-size: 16px;")
            lbl = QLabel(label)
            lbl.setStyleSheet("color: #64748b; font-size: 11px; font-weight: bold;")
            val = QLabel(f"{value} ({percentage}%)")
            val.setStyleSheet("color: #0f172a; font-size: 11px; font-weight: bold;")
            hl.addWidget(dot)
            hl.addWidget(lbl)
            hl.addStretch()
            hl.addWidget(val)
            legend_layout.addLayout(hl)
            
        add_donut_legend("#2563eb", "Completed", 54, "42")
        add_donut_legend("#c5a880", "In Progress", 38, "30")
        add_donut_legend("#059669", "Pending", 26, "20")
        add_donut_legend("#dc2626", "Overdue", 10, "8")
        
        donut_body.addLayout(legend_layout, 1)
        
        donut_layout.addLayout(donut_hdr)
        donut_layout.addLayout(donut_body)
        r1_layout.addWidget(donut_panel, 1)

        # 3. Recent Activity
        ap = QFrame()
        ap.setObjectName("activityPanel")
        av = QVBoxLayout(ap)
        av.setSpacing(10)
        hdr_a, self.btnViewActivity = self._panel_header("Recent Activity", "btnViewActivity", "activityTitle")
        av.addLayout(hdr_a)
        
        self.activityListWidget = QListWidget()
        self.activityListWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        for item in [
            "●  Visitor Grace Wanjiru checked in — 9:12 AM",
            "●  Maintenance #41 raised — East wing AC — 9:40 AM",
            "●  Inspection logged — Washrooms, no issues — 10:05 AM",
            "●  Safety flag raised — Parking gate out — 10:52 AM",
            "●  Task 'Restock supplies' in progress — 11:20 AM",
        ]:
            self.activityListWidget.addItem(QListWidgetItem(item))
        av.addWidget(self.activityListWidget)
        ap.setMinimumHeight(240)
        r1_layout.addWidget(ap, 1)

        grid_layout.addWidget(row1)

        # ════════════════════════════════════════════════════════════════
        # ROW 2 (BOTTOM) — Visitor Log, Maintenance, Checklist
        # ════════════════════════════════════════════════════════════════
        row2 = QFrame()
        row2.setObjectName("row2Frame")
        r2_layout = QHBoxLayout(row2)
        r2_layout.setSpacing(14)
        r2_layout.setContentsMargins(0, 0, 0, 0)

        # 1. Visitor Log
        vp = QFrame()
        vp.setObjectName("visitorPanel")
        vpv = QVBoxLayout(vp)
        vpv.setSpacing(10)
        hdr_v, self.btnViewVisitorLog = self._panel_header("Today's Visitor Log", "btnViewVisitorLog", "visitorTitle")
        vpv.addLayout(hdr_v)
        
        self.visitorLogTable = self._make_table(
            ["Visitor", "Host", "Time", "Status"],
            [
                ("Grace Wanjiru", "J. Kamau", "9:12 AM", "Checked in"),
                ("Peter Njoroge", "Ops Mgr", "9:55 AM", "Checked in"),
                ("Amina Hassan", "HR Desk", "8:30 AM", "Checked out"),
                ("Samuel Kiptoo", "Stores", "11:10 AM", "Checked in"),
            ],
            max_height=None,
        )
        vpv.addWidget(self.visitorLogTable)
        vp.setMinimumHeight(240)
        r2_layout.addWidget(vp, 1)

        # 2. Maintenance
        mp = QFrame()
        mp.setObjectName("maintenancePanel")
        mv = QVBoxLayout(mp)
        mv.setSpacing(10)
        hdr_m, self.btnViewMaintenance = self._panel_header("Maintenance Requests", "btnViewMaintenance", "maintenanceTitle")
        mv.addLayout(hdr_m)
        
        self.maintenanceTable = self._make_table(
            ["Issue", "Location", "Priority"],
            [
                ("East wing AC unit", "Floor 2", "Pending"),
                ("Parking gate light", "Parking", "Overdue"),
                ("Leaking tap", "Washroom B", "In progress"),
                ("Broken window latch", "Reception", "Resolved"),
            ],
            max_height=None,
        )
        mv.addWidget(self.maintenanceTable)
        mp.setMinimumHeight(240)
        r2_layout.addWidget(mp, 1)

        # 3. Checklist
        cp = QFrame()
        cp.setObjectName("checklistPanel")
        cv = QVBoxLayout(cp)
        cv.setSpacing(10)
        hdr_c, self.btnViewChecklist = self._panel_header("Facility Inspection Checklist", "btnViewChecklist", "checklistTitle")
        cv.addLayout(hdr_c)
        
        self.checklistWidget = QListWidget()
        self.checklistWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        for item in [
            "01  Reception & Lobby — 100%",
            "02  Compound & Grounds — 100%",
            "03  Washrooms — 100%",
            "04  Parking & Perimeter — 40%",
            "05  Fire & Safety Equipment — Not started",
        ]:
            self.checklistWidget.addItem(QListWidgetItem(item))
        cv.addWidget(self.checklistWidget)
        cp.setMinimumHeight(240)
        r2_layout.addWidget(cp, 1)

        grid_layout.addWidget(row2)

        return outer

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
    def _make_table(
        self, headers: list, rows: list, max_height: int | None = 185
    ) -> QTableWidget:
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
        if max_height is not None:
            t.setMaximumHeight(max_height)
        t.verticalHeader().setDefaultSectionSize(38)
        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                t.setItem(r, c, QTableWidgetItem(val))
        return t
