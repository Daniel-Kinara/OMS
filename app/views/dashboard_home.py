from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QLineSeries
from PySide6.QtGui import QPainter, QColor


class DashboardHomeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Dashboard Main Title Header
        title = QLabel("Operations Control Center Dashboard")
        title.setStyleSheet("font-size: 22px; font-weight: bold; color: #123014;")
        layout.addWidget(title)

        # Horizontal Splitter for Charts Layout
        charts_box = QHBoxLayout()

        # 1. Generate Doughnut distribution graph
        doughnut_view = self.get_doughnut_chart()
        charts_box.addWidget(doughnut_view)

        # 2. Generate Linear performance tracker graph
        line_view = self.get_line_chart()
        charts_box.addWidget(line_view)

        layout.addLayout(charts_box)

    def get_doughnut_chart(self):
        series = QPieSeries()
        series.setHoleSize(0.50)  # Generates the doughnut style center hole

        series.append("Cleanliness Tasks (45%)", 45).setColor(QColor("#164e21"))
        series.append("Maintenance Issues (35%)", 35).setColor(QColor("#e8a63c"))
        series.append("Pending Safety Audits (20%)", 20).setColor(QColor("#ef4444"))

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Departmental Task Matrix Breakdown")
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        chart.setBackgroundVisible(False)

        view = QChartView(chart)
        view.setRenderHint(QPainter.RenderHint.Antialiasing)
        view.setFrameShape(QFrame.Shape.NoFrame)
        return view

    def get_line_chart(self):
        series = QLineSeries()
        series.append(1, 50)
        series.append(2, 70)
        series.append(3, 64)
        series.append(4, 91)

        line_pen = series.pen()
        line_pen.setWidth(3)
        line_pen.setColor(QColor("#e8a63c"))
        series.setPen(line_pen)

        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setTitle("Weekly Efficiency Performance Output Trend")
        chart.setBackgroundVisible(False)
        chart.legend().setVisible(False)

        view = QChartView(chart)
        view.setRenderHint(QPainter.RenderHint.Antialiasing)
        view.setFrameShape(QFrame.Shape.NoFrame)
        return view
