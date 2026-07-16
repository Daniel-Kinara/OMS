"""
OMS — Login Screen
Shown at app startup. Authenticates the user and launches
the correct role dashboard.
"""

import sys
import os

# pyrefly: ignore [missing-import]
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFrame,
    QComboBox,
    QGraphicsDropShadowEffect,
)

# pyrefly: ignore [missing-import]
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRect

# pyrefly: ignore [missing-import]
from PyQt6.QtGui import QColor, QFont


# Role → (window class, avatar initials, avatar color)
ROLE_CONFIG = {
    "Operations Manager": ("OpsManagerWindow", "OM", "#2563eb"),
    "CEO": ("CEOWindow", "CE", "#059669"),
    "Administrator": ("AdminWindow", "AD", "#7c3aed"),
    "HR Manager": ("HRWindow", "HR", "#d97706"),
    "IT Manager": ("ITWindow", "IT", "#0891b2"),
}

# Demo credentials — replace with MySQL auth later
DEMO_USERS = {
    "ops.manager@mfanobora.com": ("password123", "Operations Manager"),
    "ceo@mfanobora.com": ("password123", "CEO"),
    "admin@mfanobora.com": ("password123", "Administrator"),
    "hr@mfanobora.com": ("password123", "HR Manager"),
    "it@mfanobora.com": ("password123", "IT Manager"),
}


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OMS — Login")
        self.setMinimumSize(1100, 680)
        self._build()

    def _build(self):
        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)
        root.addWidget(self._build_left_panel(), 1)
        root.addWidget(self._build_right_panel(), 1)

    # ── Left panel (branding) ────────────────────────────────────
    def _build_left_panel(self):
        panel = QFrame()
        panel.setObjectName("loginLeftPanel")
        vl = QVBoxLayout(panel)
        vl.setContentsMargins(60, 60, 60, 60)
        vl.setSpacing(0)
        vl.addStretch()

        logo_badge = QLabel("OMS")
        logo_badge.setObjectName("loginLogoBadge")
        logo_badge.setFixedSize(72, 72)
        logo_badge.setAlignment(Qt.AlignmentFlag.AlignCenter)

        company = QLabel("Mfano Bora Africa")
        company.setObjectName("loginCompanyLabel")

        tagline = QLabel("Operations Management\nSystem")
        tagline.setObjectName("loginTaglineLabel")

        desc = QLabel(
            "Streamline your operations.\nManage facilities, visitors, maintenance\n"
            "and daily coordination — all in one place."
        )
        desc.setObjectName("loginDescLabel")
        desc.setWordWrap(True)

        vl.addWidget(logo_badge)
        vl.addSpacing(24)
        vl.addWidget(company)
        vl.addSpacing(8)
        vl.addWidget(tagline)
        vl.addSpacing(20)
        vl.addWidget(desc)
        vl.addStretch()

        version = QLabel("v1.0.0 · Mfano Bora Africa Ltd. © 2026")
        version.setObjectName("loginVersionLabel")
        vl.addWidget(version)

        return panel

    # ── Right panel (form) ───────────────────────────────────────
    def _build_right_panel(self):
        panel = QFrame()
        panel.setObjectName("loginRightPanel")
        vl = QVBoxLayout(panel)
        vl.setContentsMargins(60, 0, 60, 0)
        vl.setSpacing(0)
        vl.addStretch()

        title = QLabel("Welcome back")
        title.setObjectName("loginFormTitle")

        subtitle = QLabel("Sign in to your OMS account")
        subtitle.setObjectName("loginFormSubtitle")

        vl.addWidget(title)
        vl.addSpacing(6)
        vl.addWidget(subtitle)
        vl.addSpacing(36)

        # Email
        vl.addWidget(self._field_label("Email address"))
        self.emailInput = self._input("e.g. ops.manager@mfanobora.com", False)
        vl.addWidget(self.emailInput)
        vl.addSpacing(18)

        # Password
        vl.addWidget(self._field_label("Password"))
        self.passwordInput = self._input("Enter your password", True)
        vl.addWidget(self.passwordInput)
        vl.addSpacing(10)

        # Error label
        self.errorLabel = QLabel("")
        self.errorLabel.setObjectName("loginErrorLabel")
        self.errorLabel.setWordWrap(True)
        vl.addWidget(self.errorLabel)
        vl.addSpacing(24)

        # Sign in button
        self.btnSignIn = QPushButton("Sign in")
        self.btnSignIn.setObjectName("loginBtnSignIn")
        self.btnSignIn.setFixedHeight(48)
        self.btnSignIn.clicked.connect(self._on_sign_in)
        vl.addWidget(self.btnSignIn)
        vl.addSpacing(20)

        # Demo hint
        hint = QLabel(
            "Demo: use ops.manager@mfanobora.com / password123\n"
            "or ceo@mfanobora.com / password123"
        )
        hint.setObjectName("loginHintLabel")
        hint.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hint.setWordWrap(True)
        vl.addWidget(hint)

        vl.addStretch()

        # Press Enter to sign in
        self.emailInput.returnPressed.connect(self._on_sign_in)
        self.passwordInput.returnPressed.connect(self._on_sign_in)

        return panel

    def _field_label(self, text: str) -> QLabel:
        lbl = QLabel(text)
        lbl.setObjectName("loginFieldLabel")
        return lbl

    def _input(self, placeholder: str, password: bool) -> QLineEdit:
        w = QLineEdit()
        w.setPlaceholderText(placeholder)
        w.setObjectName("loginInput")
        w.setFixedHeight(44)
        if password:
            w.setEchoMode(QLineEdit.EchoMode.Password)
        return w

    # ── Auth logic ───────────────────────────────────────────────
    def _on_sign_in(self):
        email = self.emailInput.text().strip().lower()
        password = self.passwordInput.text()

        self.errorLabel.setText("")
        self.emailInput.setStyleSheet("")
        self.passwordInput.setStyleSheet("")

        if not email or not password:
            self.errorLabel.setText("⚠  Please enter your email and password.")
            return

        if email not in DEMO_USERS:
            self.emailInput.setStyleSheet("border: 1px solid #ef4444;")
            self.errorLabel.setText("⚠  No account found with that email address.")
            return

        stored_password, role = DEMO_USERS[email]
        if password != stored_password:
            self.passwordInput.setStyleSheet("border: 1px solid #ef4444;")
            self.errorLabel.setText("⚠  Incorrect password. Please try again.")
            return

        # Auth passed — launch the correct dashboard
        self._launch_dashboard(role, email)

    def _launch_dashboard(self, role: str, email: str):
        from main import OpsManagerWindow, load_stylesheet

        initials, color = (
            (ROLE_CONFIG[role][1], ROLE_CONFIG[role][2])
            if role in ROLE_CONFIG
            else ("?", "#64748b")
        )

        # Switch from login.qss to the main dashboard style.qss
        app = QApplication.instance()
        load_stylesheet(app)

        self.dashboard = OpsManagerWindow(
            role=role,
            initials=initials,
            avatar_color=color,
            email=email,
        )
        self.dashboard.showMaximized()
        self.close()


def load_login_stylesheet(app: QApplication):
    style_path = os.path.join(os.path.dirname(__file__), "styles", "login.qss")
    with open(style_path, "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())


def main():
    app = QApplication(sys.argv)
    load_login_stylesheet(app)
    window = LoginWindow()
    window.showMaximized()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
