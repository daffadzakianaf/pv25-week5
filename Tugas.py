from PyQt6 import QtWidgets, uic
import sys
import re

class Tugas(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design.ui", self)

        self.masukNama = self.findChild(QtWidgets.QLineEdit, "masukNama")
        self.masukEmail = self.findChild(QtWidgets.QLineEdit, "masukEmail")
        self.masukUsia = self.findChild(QtWidgets.QLineEdit, "masukUsia")
        self.noPhone = self.findChild(QtWidgets.QLineEdit, "noPhone")
        self.masukAlamat = self.findChild(QtWidgets.QLineEdit, "masukAlamat")

        self.gender = self.findChild(QtWidgets.QComboBox, "gender")
        self.education = self.findChild(QtWidgets.QComboBox, "education")

        self.simpan = self.findChild(QtWidgets.QPushButton, "simpan")
        self.hapus = self.findChild(QtWidgets.QPushButton, "hapus")

        # Isi default combobox
        self.gender.addItems(["", "Laki-laki", "Perempuan"])
        self.education.addItems(["", "SD", "SMP", "SMA", "Diploma", "S1", "S2", "S3"])

        # No telp default +62
        self.noPhone.setText("+62")

        self.simpan.clicked.connect(self.simpan_data)
        self.hapus.clicked.connect(self.hapus_data)

    def simpan_data(self):
        nama = self.masukNama.text().strip()
        email = self.masukEmail.text().strip()
        usia = self.masukUsia.text().strip()
        phone = self.noPhone.text().strip()
        alamat = self.masukAlamat.text().strip()
        gender = self.gender.currentText()
        education = self.education.currentText()

        if not nama.isalpha():
            self.show_warning("Nama hanya boleh mengandung huruf.")
            return

        if not email.endswith("@gmail.com") or " " in email:
            self.show_warning("isi domain e-mail anda dan tanpa spasi.")
            return

        if not usia.isdigit():
            self.show_warning("isi lah berupa angka saja.")
            return

        if not phone.startswith("+62") or not phone[3:].isdigit() or len(phone[3:]) != 11:
            self.show_warning("isi nomor handphone anda 12 digit")
            return

        if not alamat:
            self.show_warning("Alamat tidak boleh kosong.")
            return

        if gender not in ["Laki-laki", "Perempuan"]:
            self.show_warning("Silakan pilih gender.")
            return

        if education not in ["SD", "SMP", "SMA", "Diploma", "S1", "S2", "S3"]:
            self.show_warning("Silakan pilih pendidikan.")
            return

        QtWidgets.QMessageBox.information(self, "Sukses", "Data berhasil disimpan!")

    def hapus_data(self):
        self.masukNama.clear()
        self.masukEmail.clear()
        self.masukUsia.clear()
        self.noPhone.setText("+62")
        self.masukAlamat.clear()
        self.gender.setCurrentIndex(0)
        self.education.setCurrentIndex(0)

    def show_warning(self, message):
        QtWidgets.QMessageBox.warning(self, "Peringatan", message)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Tugas()
    window.show()
    sys.exit(app.exec())