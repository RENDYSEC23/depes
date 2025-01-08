import os
import sys

def check_root():
    if os.geteuid() == 0:
        print("Akses root berhasil! Menjalankan shell...")
        os.system("/bin/bash")  # Membuka shell sebagai root
    else:
        print("Bukan root, mencoba eskalasi hak akses...")

def escalate_privileges():
    try:
        # Menggunakan perintah sudo untuk mencoba mendapatkan akses root
        os.system("sudo /bin/bash -c 'echo root akses berhasil > /tmp/success'")
        with open("/tmp/success", "r") as f:
            print(f.read())
        os.system("rm -f /tmp/success")  # Hapus file setelah ujian
    except Exception as e:
        print(f"Gagal eskalasi: {e}")

if __name__ == "__main__":
    check_root()
    escalate_privileges()
