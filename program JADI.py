class Orang:
    def __init__(self, nama_depan, nama_belakang, nomer_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nomer_id = nomer_id

class Mahasiswa(Orang):
    SARJANA, MASTER, DOCTOR = range(3)
    gelar_jenjang = {"S1":"SARJANA", "S2":"MASTER", "S3":"DOCTOR"}

    def __init__(self, nama_depan, nama_belakang, nomer_id, jenjang):
        super().__init__(nama_depan, nama_belakang, nomer_id)
        self.jenjang = jenjang
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

    def tampilkan_mhs(self):
        print("Mahasiswa")
        print(f"Nama : {self.nama_depan} {self.nama_belakang}")
        print(f"Nomor ID : {self.nomer_id}")
        if self.jenjang == 0:
            print("Jenjang :", self.gelar_jenjang.get("S1"))
        elif self.jenjang == 1:
            print("Jenjang :", self.gelar_jenjang.get("S2"))
        else:
            print("Jenjang :", self.gelar_jenjang.get("S3"))
        print(f"Mata kuliah yang diambil : {', '.join(self.matkul)}")

class Karyawan(Orang):
    TETAP, TDK_TETAP = range(2)

    def __init__(self, nama_depan, nama_belakang, nomer_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomer_id)
        self.status_karyawan = status_karyawan

class Dosen(Karyawan):
    status_pekerja = {"Tetap":"Karyawan Tetap", "Tidak":"Karyawan Tidak Tetap"}

    def __init__(self, nama_depan, nama_belakang, nomer_id, status_karyawan):
        super().__init__(nama_depan, nama_belakang, nomer_id, status_karyawan)
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah_diajar):
        self.matkul_diajar.append(mata_kuliah_diajar)

    def tampilkan_dosen(self):
        print("Dosen")
        print(f"Nama : {self.nama_depan} {self.nama_belakang}")
        print(f"Nomor ID : {self.nomer_id}")
        if self.status_karyawan == 0:
            print("Status Karyawan :", self.status_pekerja.get("Tetap"))
        else:
            print("Status Karyawan :", self.status_pekerja.get("Tidak"))
        print(f"Mata kuliah yang diajar : {', '.join(self.matkul_diajar)}")

Bowo = Mahasiswa("Bowo", "Nugroho", "987654", Mahasiswa.SARJANA)
Bowo.enrol("Basis Data")

Rizki = Dosen("Rizki", "Setiabudi", "456789", Karyawan.TETAP)
Rizki.mengajar("Statistik")

class Pelajar:
    def __init__(self):
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah_diajar):
        self.matkul_diajar.append(mata_kuliah_diajar)

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, nama_depan, nama_belakang, nomer_id):
        Orang.__init__(self, nama_depan, nama_belakang, nomer_id)
        Pelajar.__init__(self)
        Pengajar.__init__(self)

    def tampilkan_asdos(self):
        print("Asdos")
        print(f"Nama : {self.nama_depan} {self.nama_belakang}")
        print(f"Nomor ID : {self.nomer_id}")
        print(f"Mata kuliah yang diambil : {', '.join(self.matkul)}")
        print(f"Mata kuliah yang diajar : {', '.join(self.matkul_diajar)}")
        
Uswatun = Asdos("Uswatun", "Hasanah", "456456")
Uswatun.enrol("Big Data")
Uswatun.mengajar("Kecerdasan Artifisial")

Mahasiswa.tampilkan_mhs(Bowo)
print()
Dosen.tampilkan_dosen(Rizki)
print()
Asdos.tampilkan_asdos(Uswatun)
