# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'operations_manager_dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_OpsManagerWindow(object):
    def setupUi(self, OpsManagerWindow):
        if not OpsManagerWindow.objectName():
            OpsManagerWindow.setObjectName(u"OpsManagerWindow")
        OpsManagerWindow.resize(1680, 980)
        self.centralwidget = QWidget(OpsManagerWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.rootLayout = QVBoxLayout(self.centralwidget)
        self.rootLayout.setSpacing(0)
        self.rootLayout.setObjectName(u"rootLayout")
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.topBarFrame = QFrame(self.centralwidget)
        self.topBarFrame.setObjectName(u"topBarFrame")
        self.topBarFrame.setMinimumSize(QSize(0, 64))
        self.topBarFrame.setMaximumSize(QSize(16777215, 64))
        self.topBarLayout = QHBoxLayout(self.topBarFrame)
        self.topBarLayout.setSpacing(10)
        self.topBarLayout.setObjectName(u"topBarLayout")
        self.topBarLayout.setContentsMargins(18, -1, 18, -1)
        self.btnMenuToggle = QPushButton(self.topBarFrame)
        self.btnMenuToggle.setObjectName(u"btnMenuToggle")
        self.btnMenuToggle.setMaximumSize(QSize(38, 38))

        self.topBarLayout.addWidget(self.btnMenuToggle)

        self.appTitleLabel = QLabel(self.topBarFrame)
        self.appTitleLabel.setObjectName(u"appTitleLabel")

        self.topBarLayout.addWidget(self.appTitleLabel)

        self.searchBar = QLineEdit(self.topBarFrame)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setMinimumSize(QSize(360, 36))
        self.searchBar.setMaximumSize(QSize(480, 36))

        self.topBarLayout.addWidget(self.searchBar)

        self.topBarSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.topBarLayout.addItem(self.topBarSpacer)

        self.btnNotifications = QPushButton(self.topBarFrame)
        self.btnNotifications.setObjectName(u"btnNotifications")
        self.btnNotifications.setMinimumSize(QSize(36, 36))
        self.btnNotifications.setMaximumSize(QSize(36, 36))

        self.topBarLayout.addWidget(self.btnNotifications)

        self.btnMessages = QPushButton(self.topBarFrame)
        self.btnMessages.setObjectName(u"btnMessages")
        self.btnMessages.setMinimumSize(QSize(36, 36))
        self.btnMessages.setMaximumSize(QSize(36, 36))

        self.topBarLayout.addWidget(self.btnMessages)

        self.profileFrame = QFrame(self.topBarFrame)
        self.profileFrame.setObjectName(u"profileFrame")
        self.profileLayout = QVBoxLayout(self.profileFrame)
        self.profileLayout.setSpacing(1)
        self.profileLayout.setObjectName(u"profileLayout")
        self.profileLayout.setContentsMargins(10, -1, -1, -1)
        self.profileNameLabel = QLabel(self.profileFrame)
        self.profileNameLabel.setObjectName(u"profileNameLabel")

        self.profileLayout.addWidget(self.profileNameLabel)

        self.profileRoleLabel = QLabel(self.profileFrame)
        self.profileRoleLabel.setObjectName(u"profileRoleLabel")

        self.profileLayout.addWidget(self.profileRoleLabel)


        self.topBarLayout.addWidget(self.profileFrame)


        self.rootLayout.addWidget(self.topBarFrame)

        self.bodyFrame = QFrame(self.centralwidget)
        self.bodyFrame.setObjectName(u"bodyFrame")
        self.bodyLayout = QHBoxLayout(self.bodyFrame)
        self.bodyLayout.setSpacing(0)
        self.bodyLayout.setObjectName(u"bodyLayout")
        self.bodyLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebarFrame = QFrame(self.bodyFrame)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        self.sidebarFrame.setMinimumSize(QSize(250, 0))
        self.sidebarFrame.setMaximumSize(QSize(250, 16777215))
        self.sidebarLayout = QVBoxLayout(self.sidebarFrame)
        self.sidebarLayout.setSpacing(2)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.sidebarLayout.setContentsMargins(14, 20, 14, 16)
        self.logoLabel = QLabel(self.sidebarFrame)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sidebarLayout.addWidget(self.logoLabel)

        self.companyLabel = QLabel(self.sidebarFrame)
        self.companyLabel.setObjectName(u"companyLabel")
        self.companyLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.sidebarLayout.addWidget(self.companyLabel)

        self.sidebarSep0 = QFrame(self.sidebarFrame)
        self.sidebarSep0.setObjectName(u"sidebarSep0")
        self.sidebarSep0.setFrameShape(QFrame.Shape.HLine)
        self.sidebarSep0.setFrameShadow(QFrame.Shadow.Sunken)

        self.sidebarLayout.addWidget(self.sidebarSep0)

        self.sectionOverview = QLabel(self.sidebarFrame)
        self.sectionOverview.setObjectName(u"sectionOverview")

        self.sidebarLayout.addWidget(self.sectionOverview)

        self.btnDashboard = QPushButton(self.sidebarFrame)
        self.btnDashboard.setObjectName(u"btnDashboard")

        self.sidebarLayout.addWidget(self.btnDashboard)

        self.sectionDailyOps = QLabel(self.sidebarFrame)
        self.sectionDailyOps.setObjectName(u"sectionDailyOps")

        self.sidebarLayout.addWidget(self.sectionDailyOps)

        self.btnOfficeCleanliness = QPushButton(self.sidebarFrame)
        self.btnOfficeCleanliness.setObjectName(u"btnOfficeCleanliness")

        self.sidebarLayout.addWidget(self.btnOfficeCleanliness)

        self.btnCompoundManagement = QPushButton(self.sidebarFrame)
        self.btnCompoundManagement.setObjectName(u"btnCompoundManagement")

        self.sidebarLayout.addWidget(self.btnCompoundManagement)

        self.btnFacilityInspections = QPushButton(self.sidebarFrame)
        self.btnFacilityInspections.setObjectName(u"btnFacilityInspections")

        self.sidebarLayout.addWidget(self.btnFacilityInspections)

        self.btnOfficeSafety = QPushButton(self.sidebarFrame)
        self.btnOfficeSafety.setObjectName(u"btnOfficeSafety")

        self.sidebarLayout.addWidget(self.btnOfficeSafety)

        self.sectionVisitors = QLabel(self.sidebarFrame)
        self.sectionVisitors.setObjectName(u"sectionVisitors")

        self.sidebarLayout.addWidget(self.sectionVisitors)

        self.btnVisitorRegistration = QPushButton(self.sidebarFrame)
        self.btnVisitorRegistration.setObjectName(u"btnVisitorRegistration")

        self.sidebarLayout.addWidget(self.btnVisitorRegistration)

        self.sectionMaintenance = QLabel(self.sidebarFrame)
        self.sectionMaintenance.setObjectName(u"sectionMaintenance")

        self.sidebarLayout.addWidget(self.sectionMaintenance)

        self.btnMaintenanceRequests = QPushButton(self.sidebarFrame)
        self.btnMaintenanceRequests.setObjectName(u"btnMaintenanceRequests")

        self.sidebarLayout.addWidget(self.btnMaintenanceRequests)

        self.sidebarSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebarLayout.addItem(self.sidebarSpacer)

        self.sidebarSep1 = QFrame(self.sidebarFrame)
        self.sidebarSep1.setObjectName(u"sidebarSep1")
        self.sidebarSep1.setFrameShape(QFrame.Shape.HLine)
        self.sidebarSep1.setFrameShadow(QFrame.Shadow.Sunken)

        self.sidebarLayout.addWidget(self.sidebarSep1)

        self.btnSettings = QPushButton(self.sidebarFrame)
        self.btnSettings.setObjectName(u"btnSettings")

        self.sidebarLayout.addWidget(self.btnSettings)

        self.btnLogout = QPushButton(self.sidebarFrame)
        self.btnLogout.setObjectName(u"btnLogout")

        self.sidebarLayout.addWidget(self.btnLogout)


        self.bodyLayout.addWidget(self.sidebarFrame)

        self.contentScrollArea = QScrollArea(self.bodyFrame)
        self.contentScrollArea.setObjectName(u"contentScrollArea")
        self.contentScrollArea.setWidgetResizable(True)
        self.contentScrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.contentLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.contentLayout.setSpacing(18)
        self.contentLayout.setObjectName(u"contentLayout")
        self.contentLayout.setContentsMargins(28, 24, 28, 28)
        self.headerFrame = QFrame(self.scrollAreaWidgetContents)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerTopLayout = QHBoxLayout(self.headerFrame)
        self.headerTopLayout.setSpacing(12)
        self.headerTopLayout.setObjectName(u"headerTopLayout")
        self.welcomeTextLayout = QVBoxLayout()
        self.welcomeTextLayout.setSpacing(3)
        self.welcomeTextLayout.setObjectName(u"welcomeTextLayout")
        self.titleLabel = QLabel(self.headerFrame)
        self.titleLabel.setObjectName(u"titleLabel")

        self.welcomeTextLayout.addWidget(self.titleLabel)

        self.metaLabel = QLabel(self.headerFrame)
        self.metaLabel.setObjectName(u"metaLabel")

        self.welcomeTextLayout.addWidget(self.metaLabel)


        self.headerTopLayout.addLayout(self.welcomeTextLayout)

        self.headerSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerTopLayout.addItem(self.headerSpacer)

        self.dateBadge = QLabel(self.headerFrame)
        self.dateBadge.setObjectName(u"dateBadge")

        self.headerTopLayout.addWidget(self.dateBadge)


        self.contentLayout.addWidget(self.headerFrame)

        self.logButtonsFrame = QFrame(self.scrollAreaWidgetContents)
        self.logButtonsFrame.setObjectName(u"logButtonsFrame")
        self.logButtonsLayout = QHBoxLayout(self.logButtonsFrame)
        self.logButtonsLayout.setSpacing(10)
        self.logButtonsLayout.setObjectName(u"logButtonsLayout")
        self.logButtonsSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.logButtonsLayout.addItem(self.logButtonsSpacer)

        self.btnLogMaintenance = QPushButton(self.logButtonsFrame)
        self.btnLogMaintenance.setObjectName(u"btnLogMaintenance")

        self.logButtonsLayout.addWidget(self.btnLogMaintenance)

        self.btnLogInspection = QPushButton(self.logButtonsFrame)
        self.btnLogInspection.setObjectName(u"btnLogInspection")

        self.logButtonsLayout.addWidget(self.btnLogInspection)


        self.contentLayout.addWidget(self.logButtonsFrame)

        self.statsFrame = QFrame(self.scrollAreaWidgetContents)
        self.statsFrame.setObjectName(u"statsFrame")
        self.statsLayout = QHBoxLayout(self.statsFrame)
        self.statsLayout.setSpacing(14)
        self.statsLayout.setObjectName(u"statsLayout")
        self.cardVisitors = QFrame(self.statsFrame)
        self.cardVisitors.setObjectName(u"cardVisitors")
        self.cardVisitorsLayout = QVBoxLayout(self.cardVisitors)
        self.cardVisitorsLayout.setSpacing(4)
        self.cardVisitorsLayout.setObjectName(u"cardVisitorsLayout")
        self.cardVisitorsIcon = QLabel(self.cardVisitors)
        self.cardVisitorsIcon.setObjectName(u"cardVisitorsIcon")

        self.cardVisitorsLayout.addWidget(self.cardVisitorsIcon)

        self.cardVisitorsValue = QLabel(self.cardVisitors)
        self.cardVisitorsValue.setObjectName(u"cardVisitorsValue")

        self.cardVisitorsLayout.addWidget(self.cardVisitorsValue)

        self.cardVisitorsCaption = QLabel(self.cardVisitors)
        self.cardVisitorsCaption.setObjectName(u"cardVisitorsCaption")

        self.cardVisitorsLayout.addWidget(self.cardVisitorsCaption)


        self.statsLayout.addWidget(self.cardVisitors)

        self.cardMaintenance = QFrame(self.statsFrame)
        self.cardMaintenance.setObjectName(u"cardMaintenance")
        self.cardMaintenanceLayout = QVBoxLayout(self.cardMaintenance)
        self.cardMaintenanceLayout.setSpacing(4)
        self.cardMaintenanceLayout.setObjectName(u"cardMaintenanceLayout")
        self.cardMaintenanceIcon = QLabel(self.cardMaintenance)
        self.cardMaintenanceIcon.setObjectName(u"cardMaintenanceIcon")

        self.cardMaintenanceLayout.addWidget(self.cardMaintenanceIcon)

        self.cardMaintenanceValue = QLabel(self.cardMaintenance)
        self.cardMaintenanceValue.setObjectName(u"cardMaintenanceValue")

        self.cardMaintenanceLayout.addWidget(self.cardMaintenanceValue)

        self.cardMaintenanceCaption = QLabel(self.cardMaintenance)
        self.cardMaintenanceCaption.setObjectName(u"cardMaintenanceCaption")

        self.cardMaintenanceLayout.addWidget(self.cardMaintenanceCaption)


        self.statsLayout.addWidget(self.cardMaintenance)

        self.cardInspections = QFrame(self.statsFrame)
        self.cardInspections.setObjectName(u"cardInspections")
        self.cardInspectionsLayout = QVBoxLayout(self.cardInspections)
        self.cardInspectionsLayout.setSpacing(4)
        self.cardInspectionsLayout.setObjectName(u"cardInspectionsLayout")
        self.cardInspectionsIcon = QLabel(self.cardInspections)
        self.cardInspectionsIcon.setObjectName(u"cardInspectionsIcon")

        self.cardInspectionsLayout.addWidget(self.cardInspectionsIcon)

        self.cardInspectionsValue = QLabel(self.cardInspections)
        self.cardInspectionsValue.setObjectName(u"cardInspectionsValue")

        self.cardInspectionsLayout.addWidget(self.cardInspectionsValue)

        self.cardInspectionsCaption = QLabel(self.cardInspections)
        self.cardInspectionsCaption.setObjectName(u"cardInspectionsCaption")

        self.cardInspectionsLayout.addWidget(self.cardInspectionsCaption)


        self.statsLayout.addWidget(self.cardInspections)

        self.cardSafety = QFrame(self.statsFrame)
        self.cardSafety.setObjectName(u"cardSafety")
        self.cardSafetyLayout = QVBoxLayout(self.cardSafety)
        self.cardSafetyLayout.setSpacing(4)
        self.cardSafetyLayout.setObjectName(u"cardSafetyLayout")
        self.cardSafetyIcon = QLabel(self.cardSafety)
        self.cardSafetyIcon.setObjectName(u"cardSafetyIcon")

        self.cardSafetyLayout.addWidget(self.cardSafetyIcon)

        self.cardSafetyValue = QLabel(self.cardSafety)
        self.cardSafetyValue.setObjectName(u"cardSafetyValue")

        self.cardSafetyLayout.addWidget(self.cardSafetyValue)

        self.cardSafetyCaption = QLabel(self.cardSafety)
        self.cardSafetyCaption.setObjectName(u"cardSafetyCaption")

        self.cardSafetyLayout.addWidget(self.cardSafetyCaption)


        self.statsLayout.addWidget(self.cardSafety)

        self.cardCompound = QFrame(self.statsFrame)
        self.cardCompound.setObjectName(u"cardCompound")
        self.cardCompoundLayout = QVBoxLayout(self.cardCompound)
        self.cardCompoundLayout.setSpacing(4)
        self.cardCompoundLayout.setObjectName(u"cardCompoundLayout")
        self.cardCompoundIcon = QLabel(self.cardCompound)
        self.cardCompoundIcon.setObjectName(u"cardCompoundIcon")

        self.cardCompoundLayout.addWidget(self.cardCompoundIcon)

        self.cardCompoundValue = QLabel(self.cardCompound)
        self.cardCompoundValue.setObjectName(u"cardCompoundValue")

        self.cardCompoundLayout.addWidget(self.cardCompoundValue)

        self.cardCompoundCaption = QLabel(self.cardCompound)
        self.cardCompoundCaption.setObjectName(u"cardCompoundCaption")

        self.cardCompoundLayout.addWidget(self.cardCompoundCaption)


        self.statsLayout.addWidget(self.cardCompound)


        self.contentLayout.addWidget(self.statsFrame)

        self.gridFrame1 = QFrame(self.scrollAreaWidgetContents)
        self.gridFrame1.setObjectName(u"gridFrame1")
        self.gridLayout1 = QHBoxLayout(self.gridFrame1)
        self.gridLayout1.setSpacing(14)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.checklistPanel = QFrame(self.gridFrame1)
        self.checklistPanel.setObjectName(u"checklistPanel")
        self.checklistPanelLayout = QVBoxLayout(self.checklistPanel)
        self.checklistPanelLayout.setSpacing(10)
        self.checklistPanelLayout.setObjectName(u"checklistPanelLayout")
        self.checklistHeaderLayout = QHBoxLayout()
        self.checklistHeaderLayout.setObjectName(u"checklistHeaderLayout")
        self.checklistTitle = QLabel(self.checklistPanel)
        self.checklistTitle.setObjectName(u"checklistTitle")

        self.checklistHeaderLayout.addWidget(self.checklistTitle)

        self.checklistHeaderSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.checklistHeaderLayout.addItem(self.checklistHeaderSpacer)

        self.btnViewChecklist = QPushButton(self.checklistPanel)
        self.btnViewChecklist.setObjectName(u"btnViewChecklist")

        self.checklistHeaderLayout.addWidget(self.btnViewChecklist)


        self.checklistPanelLayout.addLayout(self.checklistHeaderLayout)

        self.checklistWidget = QListWidget(self.checklistPanel)
        self.checklistWidget.setObjectName(u"checklistWidget")

        self.checklistPanelLayout.addWidget(self.checklistWidget)


        self.gridLayout1.addWidget(self.checklistPanel)

        self.maintenancePanel = QFrame(self.gridFrame1)
        self.maintenancePanel.setObjectName(u"maintenancePanel")
        self.maintenancePanelLayout = QVBoxLayout(self.maintenancePanel)
        self.maintenancePanelLayout.setSpacing(10)
        self.maintenancePanelLayout.setObjectName(u"maintenancePanelLayout")
        self.maintenanceHeaderLayout = QHBoxLayout()
        self.maintenanceHeaderLayout.setObjectName(u"maintenanceHeaderLayout")
        self.maintenanceTitle = QLabel(self.maintenancePanel)
        self.maintenanceTitle.setObjectName(u"maintenanceTitle")

        self.maintenanceHeaderLayout.addWidget(self.maintenanceTitle)

        self.maintenanceHeaderSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.maintenanceHeaderLayout.addItem(self.maintenanceHeaderSpacer)

        self.btnViewMaintenance = QPushButton(self.maintenancePanel)
        self.btnViewMaintenance.setObjectName(u"btnViewMaintenance")

        self.maintenanceHeaderLayout.addWidget(self.btnViewMaintenance)


        self.maintenancePanelLayout.addLayout(self.maintenanceHeaderLayout)

        self.maintenanceTable = QTableWidget(self.maintenancePanel)
        if (self.maintenanceTable.columnCount() < 3):
            self.maintenanceTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.maintenanceTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.maintenanceTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.maintenanceTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.maintenanceTable.setObjectName(u"maintenanceTable")
        self.maintenanceTable.setColumnCount(3)

        self.maintenancePanelLayout.addWidget(self.maintenanceTable)


        self.gridLayout1.addWidget(self.maintenancePanel)

        self.activityPanel = QFrame(self.gridFrame1)
        self.activityPanel.setObjectName(u"activityPanel")
        self.activityPanelLayout = QVBoxLayout(self.activityPanel)
        self.activityPanelLayout.setSpacing(10)
        self.activityPanelLayout.setObjectName(u"activityPanelLayout")
        self.activityHeaderLayout = QHBoxLayout()
        self.activityHeaderLayout.setObjectName(u"activityHeaderLayout")
        self.activityTitle = QLabel(self.activityPanel)
        self.activityTitle.setObjectName(u"activityTitle")

        self.activityHeaderLayout.addWidget(self.activityTitle)

        self.activityHeaderSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.activityHeaderLayout.addItem(self.activityHeaderSpacer)

        self.btnViewActivity = QPushButton(self.activityPanel)
        self.btnViewActivity.setObjectName(u"btnViewActivity")

        self.activityHeaderLayout.addWidget(self.btnViewActivity)


        self.activityPanelLayout.addLayout(self.activityHeaderLayout)

        self.activityListWidget = QListWidget(self.activityPanel)
        self.activityListWidget.setObjectName(u"activityListWidget")

        self.activityPanelLayout.addWidget(self.activityListWidget)


        self.gridLayout1.addWidget(self.activityPanel)


        self.contentLayout.addWidget(self.gridFrame1)

        self.visitorPanel = QFrame(self.scrollAreaWidgetContents)
        self.visitorPanel.setObjectName(u"visitorPanel")
        self.visitorPanelLayout = QVBoxLayout(self.visitorPanel)
        self.visitorPanelLayout.setSpacing(10)
        self.visitorPanelLayout.setObjectName(u"visitorPanelLayout")
        self.visitorHeaderLayout = QHBoxLayout()
        self.visitorHeaderLayout.setObjectName(u"visitorHeaderLayout")
        self.visitorTitle = QLabel(self.visitorPanel)
        self.visitorTitle.setObjectName(u"visitorTitle")

        self.visitorHeaderLayout.addWidget(self.visitorTitle)

        self.visitorHeaderSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.visitorHeaderLayout.addItem(self.visitorHeaderSpacer)

        self.btnViewVisitorLog = QPushButton(self.visitorPanel)
        self.btnViewVisitorLog.setObjectName(u"btnViewVisitorLog")

        self.visitorHeaderLayout.addWidget(self.btnViewVisitorLog)


        self.visitorPanelLayout.addLayout(self.visitorHeaderLayout)

        self.visitorLogTable = QTableWidget(self.visitorPanel)
        if (self.visitorLogTable.columnCount() < 4):
            self.visitorLogTable.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.visitorLogTable.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.visitorLogTable.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.visitorLogTable.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.visitorLogTable.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        self.visitorLogTable.setObjectName(u"visitorLogTable")
        self.visitorLogTable.setColumnCount(4)

        self.visitorPanelLayout.addWidget(self.visitorLogTable)


        self.contentLayout.addWidget(self.visitorPanel)

        self.quickActionsFrame = QFrame(self.scrollAreaWidgetContents)
        self.quickActionsFrame.setObjectName(u"quickActionsFrame")
        self.quickActionsOuterLayout = QVBoxLayout(self.quickActionsFrame)
        self.quickActionsOuterLayout.setSpacing(12)
        self.quickActionsOuterLayout.setObjectName(u"quickActionsOuterLayout")
        self.quickActionsTitle = QLabel(self.quickActionsFrame)
        self.quickActionsTitle.setObjectName(u"quickActionsTitle")

        self.quickActionsOuterLayout.addWidget(self.quickActionsTitle)

        self.quickActionsLayout = QHBoxLayout()
        self.quickActionsLayout.setSpacing(12)
        self.quickActionsLayout.setObjectName(u"quickActionsLayout")
        self.btnQaReportMaintenance = QPushButton(self.quickActionsFrame)
        self.btnQaReportMaintenance.setObjectName(u"btnQaReportMaintenance")

        self.quickActionsLayout.addWidget(self.btnQaReportMaintenance)

        self.btnQaRegisterVisitor = QPushButton(self.quickActionsFrame)
        self.btnQaRegisterVisitor.setObjectName(u"btnQaRegisterVisitor")

        self.quickActionsLayout.addWidget(self.btnQaRegisterVisitor)

        self.btnQaLogInspection = QPushButton(self.quickActionsFrame)
        self.btnQaLogInspection.setObjectName(u"btnQaLogInspection")

        self.quickActionsLayout.addWidget(self.btnQaLogInspection)


        self.quickActionsOuterLayout.addLayout(self.quickActionsLayout)


        self.contentLayout.addWidget(self.quickActionsFrame)

        self.contentScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.bodyLayout.addWidget(self.contentScrollArea)


        self.rootLayout.addWidget(self.bodyFrame)

        OpsManagerWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OpsManagerWindow)

        QMetaObject.connectSlotsByName(OpsManagerWindow)
    # setupUi

    def retranslateUi(self, OpsManagerWindow):
        OpsManagerWindow.setWindowTitle(QCoreApplication.translate("OpsManagerWindow", u"Operations Management System \u2014 Operations Manager", None))
        self.btnMenuToggle.setText(QCoreApplication.translate("OpsManagerWindow", u"\u2630", None))
        self.appTitleLabel.setText(QCoreApplication.translate("OpsManagerWindow", u"OPERATIONS MANAGEMENT SYSTEM (OMS)", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("OpsManagerWindow", u"Search anything\u2026", None))
        self.btnNotifications.setText(QCoreApplication.translate("OpsManagerWindow", u"\U0001f514", None))
        self.btnMessages.setText(QCoreApplication.translate("OpsManagerWindow", u"\u2709", None))
        self.profileNameLabel.setText(QCoreApplication.translate("OpsManagerWindow", u"Operations Manager", None))
        self.profileRoleLabel.setText(QCoreApplication.translate("OpsManagerWindow", u"Full access", None))
        self.logoLabel.setText(QCoreApplication.translate("OpsManagerWindow", u"OM", None))
        self.companyLabel.setText(QCoreApplication.translate("OpsManagerWindow", u"Mfano Bora Africa\n"
"Operations Manager \u00b7 OMS", None))
        self.sectionOverview.setText(QCoreApplication.translate("OpsManagerWindow", u"OVERVIEW", None))
        self.btnDashboard.setText(QCoreApplication.translate("OpsManagerWindow", u"\U0001f3e0  Dashboard", None))
        self.sectionDailyOps.setText(QCoreApplication.translate("OpsManagerWindow", u"DAILY OPERATIONS", None))
        self.btnOfficeCleanliness.setText(QCoreApplication.translate("OpsManagerWindow", u"\U0001f9f9  Office Cleanliness", None))
        self.btnCompoundManagement.setText(QCoreApplication.translate("OpsManagerWindow", u"\U0001f333  Compound Management", None))
        self.btnFacilityInspections.setText(QCoreApplication.translate("OpsManagerWindow", u"\U0001f50d  Facility Inspections", None))
        self.btnOfficeSafety.setText(QCoreApplication.translate("OpsManagerWindow", u"\U0001f6e1  Office Safety", None))
        self.sectionVisitors.setText(QCoreApplication.translate("OpsManagerWindow", u"VISITORS", None))
        self.btnVisitorRegistration.setText(QCoreApplication.translate("OpsManagerWindow", u"\U0001f9fe  Visitor Registration", None))
        self.sectionMaintenance.setText(QCoreApplication.translate("OpsManagerWindow", u"MAINTENANCE", None))
        self.btnMaintenanceRequests.setText(QCoreApplication.translate("OpsManagerWindow", u"\U0001f527  Maintenance Requests", None))
        self.btnSettings.setText(QCoreApplication.translate("OpsManagerWindow", u"\u2699  Settings", None))
        self.btnLogout.setText(QCoreApplication.translate("OpsManagerWindow", u"\U0001f6aa  Logout", None))
        self.titleLabel.setText(QCoreApplication.translate("OpsManagerWindow", u"Welcome back, Operations Manager! \U0001f44b", None))
        self.metaLabel.setText(QCoreApplication.translate("OpsManagerWindow", u"Here's an overview of today's operations.", None))
        self.dateBadge.setText(QCoreApplication.translate("OpsManagerWindow", u"\U0001f4c5  Thursday, 9 July 2026   10:30 AM", None))
        self.btnLogMaintenance.setText(QCoreApplication.translate("OpsManagerWindow", u"\u270e  Log Maintenance Issue", None))
        self.btnLogInspection.setText(QCoreApplication.translate("OpsManagerWindow", u"\u2713  Log Facility Inspection", None))
        self.cardVisitorsIcon.setText(QCoreApplication.translate("OpsManagerWindow", u"\U0001f464", None))
        self.cardVisitorsValue.setText(QCoreApplication.translate("OpsManagerWindow", u"12", None))
        self.cardVisitorsCaption.setText(QCoreApplication.translate("OpsManagerWindow", u"Visitors Today", None))
        self.cardMaintenanceIcon.setText(QCoreApplication.translate("OpsManagerWindow", u"\U0001f527", None))
        self.cardMaintenanceValue.setText(QCoreApplication.translate("OpsManagerWindow", u"6", None))
        self.cardMaintenanceCaption.setText(QCoreApplication.translate("OpsManagerWindow", u"Open Maintenance Requests", None))
        self.cardInspectionsIcon.setText(QCoreApplication.translate("OpsManagerWindow", u"\U0001f50d", None))
        self.cardInspectionsValue.setText(QCoreApplication.translate("OpsManagerWindow", u"3/5", None))
        self.cardInspectionsCaption.setText(QCoreApplication.translate("OpsManagerWindow", u"Facility Inspections", None))
        self.cardSafetyIcon.setText(QCoreApplication.translate("OpsManagerWindow", u"\U0001f6e1", None))
        self.cardSafetyValue.setText(QCoreApplication.translate("OpsManagerWindow", u"2", None))
        self.cardSafetyCaption.setText(QCoreApplication.translate("OpsManagerWindow", u"Safety Checks Due", None))
        self.cardCompoundIcon.setText(QCoreApplication.translate("OpsManagerWindow", u"\U0001f333", None))
        self.cardCompoundValue.setText(QCoreApplication.translate("OpsManagerWindow", u"Clear", None))
        self.cardCompoundCaption.setText(QCoreApplication.translate("OpsManagerWindow", u"Compound Status", None))
        self.checklistTitle.setText(QCoreApplication.translate("OpsManagerWindow", u"Facility Inspection Checklist", None))
        self.btnViewChecklist.setText(QCoreApplication.translate("OpsManagerWindow", u"View all \u203a", None))
        self.maintenanceTitle.setText(QCoreApplication.translate("OpsManagerWindow", u"Maintenance Requests", None))
        self.btnViewMaintenance.setText(QCoreApplication.translate("OpsManagerWindow", u"View all \u203a", None))
        ___qtablewidgetitem = self.maintenanceTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("OpsManagerWindow", u"Issue", None))
        ___qtablewidgetitem1 = self.maintenanceTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("OpsManagerWindow", u"Location", None))
        ___qtablewidgetitem2 = self.maintenanceTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("OpsManagerWindow", u"Priority", None))
        self.activityTitle.setText(QCoreApplication.translate("OpsManagerWindow", u"Recent Activity", None))
        self.btnViewActivity.setText(QCoreApplication.translate("OpsManagerWindow", u"View all \u203a", None))
        self.visitorTitle.setText(QCoreApplication.translate("OpsManagerWindow", u"Today's Visitor Log", None))
        self.btnViewVisitorLog.setText(QCoreApplication.translate("OpsManagerWindow", u"View all \u203a", None))
        ___qtablewidgetitem3 = self.visitorLogTable.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("OpsManagerWindow", u"Visitor", None))
        ___qtablewidgetitem4 = self.visitorLogTable.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("OpsManagerWindow", u"Host", None))
        ___qtablewidgetitem5 = self.visitorLogTable.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("OpsManagerWindow", u"Time", None))
        ___qtablewidgetitem6 = self.visitorLogTable.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("OpsManagerWindow", u"Status", None))
        self.quickActionsTitle.setText(QCoreApplication.translate("OpsManagerWindow", u"Quick Actions", None))
        self.btnQaReportMaintenance.setText(QCoreApplication.translate("OpsManagerWindow", u"\u270e\n"
"Report Maintenance", None))
        self.btnQaRegisterVisitor.setText(QCoreApplication.translate("OpsManagerWindow", u"\U0001f464\n"
"Register Visitor", None))
        self.btnQaLogInspection.setText(QCoreApplication.translate("OpsManagerWindow", u"\u2713\n"
"Log Inspection", None))
    # retranslateUi

