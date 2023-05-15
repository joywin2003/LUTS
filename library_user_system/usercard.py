import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap


class CredentialsCard(QWidget):
    def __init__(self, name, email, phone, profile_photo):
        super().__init__()
        self.setWindowTitle('Credentials Card')
        self.setGeometry(100, 100, 400, 400)

        # Add profile photo
        self.profile_photo_label = QLabel(self)
        pixmap = QPixmap(profile_photo)
        self.profile_photo_label.setPixmap(pixmap)
        self.profile_photo_label.setGeometry(20, 20, 120, 120)

        # Add name label
        self.name_label = QLabel(self)
        self.name_label.setText(f"<h2>{name}</h2>")
        self.name_label.setGeometry(150, 20, 200, 40)

        # Add email label
        self.email_label = QLabel(self)
        self.email_label.setText(f"<p>{email}</p>")
        self.email_label.setGeometry(150, 70, 200, 40)

        # Add phone label
        self.phone_label = QLabel(self)
        self.phone_label.setText(f"<p>{phone}</p>")
        self.phone_label.setGeometry(150, 120, 200, 40)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CredentialsCard(name='John Doe', email='johndoe@example.com', phone='+1-123-456-7890',
                             profile_photo='profile_photo.png')
    sys.exit(app.exec_())
