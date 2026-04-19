#### NAMA : Muhammad Yusuf Ar Rahman
#### NIM : 103072400143
#### Kelas : IF-04-04

# SOAL 1
# Pertanyaan
1. Cari pesan permintaan DNS dan balasannya. Apakah pesan tersebut dikirimkan melalui UDP atau TCP?
2. Apa port tujuan pada pesan permintaan DNS? Apa port sumber pada pesan balasannya?
3. Pada pesan permintaan DNS, apa alamat IP tujuannya? Apa alamat IP server DNS lokal anda (gunakan ipconfig untuk mencari tahu)? Apakah kedua alamat IP tersebut sama?
4. Periksa pesan permintaan DNS. Apa “jenis” atau ”type” dari pesan tersebut? Apakah pesan permintaan tersebut mengandung ”jawaban” atau ”answers”?
5. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau ”answers” yang terdapat di dalamnya? Apa saja isi yang terkandung dalam setiap jawaban tersebut?
6. Perhatikan paket TCP SYN yang selanjutnya dikirimkan oleh host Anda. Apakah alamat IP pada paket tersebut sesuai dengan alamat IP yang tertera pada pesan balasan DNS?
7. Halaman web yang sebelumnya anda akses (http://www.ietf.org) memuat beberapa gambar. Apakah host Anda perlu mengirimkan pesan permintaan DNS baru setiap kali ingin mengakses suatu gambar?

# Jawaban :

1.
<img width="1263" height="720" alt="image" src="https://github.com/user-attachments/assets/7a0aad6c-35f7-4ed9-9c02-ae86f71f7273" />
<img width="1269" height="724" alt="image" src="https://github.com/user-attachments/assets/1042970d-2345-46d7-a253-1f396b5e7fe0" />

**Protokol yang digunakan pada DNS**  
Pesan query (permintaan) dan response (balasan) DNS umumnya dikirim menggunakan protokol UDP (User Datagram Protocol).  
Penggunaan UDP dipilih karena lebih efisien dan memiliki overhead yang kecil dibandingkan TCP, sehingga proses pencarian alamat IP dapat dilakukan dengan lebih cepat.

---

2.
<img width="1267" height="724" alt="image" src="https://github.com/user-attachments/assets/685b75e4-6637-4ebe-9d31-606d35bc4ee4" />
<img width="1271" height="723" alt="image" src="https://github.com/user-attachments/assets/cfde992a-0b44-4d2d-b6ec-debb19590da2" />

**Port yang digunakan**  
Port tujuan pada pesan permintaan DNS adalah **53**.  
Sedangkan port sumber pada pesan balasan DNS juga menggunakan **53**.  
Port 53 merupakan port standar yang digunakan oleh layanan DNS dalam melakukan komunikasi antara client dan server.

---

3.
<img width="1273" height="727" alt="image" src="https://github.com/user-attachments/assets/6cb8dd9a-662f-4198-b4b7-b391c799b192" />
<img width="900" height="557" alt="Screenshot 2026-04-19 113006" src="https://github.com/user-attachments/assets/2d29b2bd-cbc6-4c9f-8a17-e268647ae1a8" />

**Alamat IP tujuan dan DNS lokal**  
Alamat IP tujuan pada pesan permintaan DNS merupakan alamat IP dari server DNS yang digunakan oleh jaringan (biasanya DNS milik ISP atau jaringan lokal).  
Alamat IP DNS lokal dapat diketahui dengan menjalankan perintah **ipconfig** pada komputer.

---

4.
<img width="1266" height="726" alt="image" src="https://github.com/user-attachments/assets/8403aeff-1319-44c0-902a-f227625703ec" />

**Jenis (Type) pesan DNS**  
Jenis pesan pada permintaan DNS adalah **Type A (Host Address)** yang berfungsi untuk menerjemahkan nama domain menjadi alamat IP versi IPv4.  
Pesan permintaan DNS tidak memiliki bagian jawaban (answers), karena hanya berisi permintaan data kepada server DNS.

---

5.
<img width="1273" height="720" alt="image" src="https://github.com/user-attachments/assets/a698a030-ad33-43a0-a5a0-a6ac77a8dd45" />

**Isi pesan balasan DNS**  
Pada pesan balasan DNS terdapat **2 jawaban (answers)**.  
Setiap jawaban biasanya berisi beberapa informasi, antara lain:

- Nama domain yang diminta (misalnya: www.ietf.org)  
- Jenis record (A)  
- Alamat IP hasil dari proses resolusi  
- Nilai **TTL (Time To Live)**

---

6.
**Kesesuaian IP pada paket TCP SYN**  
Alamat IP yang terdapat pada paket **TCP SYN** sesuai dengan alamat IP yang diperoleh dari pesan balasan DNS.  
Hal ini menunjukkan bahwa setelah menerima hasil resolusi DNS, host akan menggunakan alamat IP tersebut untuk memulai koneksi ke server tujuan.

---

7.
**Apakah perlu DNS request untuk setiap gambar?**  
Tidak. Host tidak perlu mengirimkan permintaan DNS baru setiap kali mengambil gambar dari halaman yang sama (misalnya dari situs IETF).  

Hal ini dikarenakan:

- Alamat IP sudah diketahui dari hasil resolusi DNS sebelumnya  
- Browser menyimpan hasil DNS dalam cache  
- Banyak elemen pada halaman web berasal dari domain yang sama

---

# SOAL 2

# Pertanyaan
## Perintah nslookup www.mit.edu

1. Apa port tujuan pada pesan permintaan DNS? Apa port sumber pada pesan balasan DNS?
2. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut merupakan default alamat IP server DNS lokal Anda?
3. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan tersebut mengandung ”jawaban” atau ”answers”?
4. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau “answers” yang terdapat di dalamnya. Apa saja isi yang terkandung dalam setiap jawaban tersebut?

# Jawaban :

1.
<img width="858" height="489" alt="image" src="https://github.com/user-attachments/assets/db46ae1d-f396-4c8a-b65f-0706d1f0ecb4" />
<img width="858" height="488" alt="image" src="https://github.com/user-attachments/assets/05d8524a-a864-4178-9b2f-451ceb37ea93" />

Port tujuan pada permintaan DNS adalah **53**, karena port tersebut merupakan port standar yang digunakan oleh layanan DNS.  
Sementara itu, port sumber pada balasan DNS juga berasal dari **port 53**, yang menandakan bahwa balasan dikirim oleh server DNS.

---

2.
<img width="862" height="492" alt="image" src="https://github.com/user-attachments/assets/84d7832b-33c4-4058-9414-8f59c96f1860" />
<img width="859" height="505" alt="image" src="https://github.com/user-attachments/assets/976a572f-4e23-452d-b590-c36a03ecdb88" />

Pesan permintaan DNS dikirimkan ke alamat IP **10.221.193.2**.  
Alamat tersebut merupakan **server DNS default** yang digunakan oleh perangkat pada jaringan lokal.

---

3.
<img width="863" height="497" alt="image" src="https://github.com/user-attachments/assets/73fd1b86-8c74-42c0-b139-b8d4401746d0" />

Jenis pesan pada permintaan DNS adalah **AAAA**, yang digunakan untuk meminta alamat **IPv6** dari suatu domain.  
Pesan permintaan ini tidak memiliki bagian jawaban (answers) karena hanya berupa permintaan informasi kepada server DNS.

---

4.
<img width="860" height="483" alt="image" src="https://github.com/user-attachments/assets/63b9d1aa-b609-4bce-a99c-59ec5c93bf10" />

Pada pesan balasan DNS terdapat **4 jawaban (answers)**.  
Setiap jawaban memuat:

1. Nama domain yang diminta  
2. Jenis record (**AAAA**)  
3. Alamat **IPv6** dari domain tersebut  
4. Nilai **TTL (Time To Live)**

---

# SOAL 3

# Pertanyaan

Perintah **nslookup –type=NS mit.edu**

1. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut merupakan default alamat IP server DNS lokal Anda?
2. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan tersebut mengandung ”jawaban” atau ”answers”?
3. Periksa pesan balasan DNS. Apa nama server MIT yang diberikan oleh pesan balasan? Apakah pesan balasan ini juga memberikan alamat IP untuk server MIT tersebut?

# Jawaban :

1.
<img width="859" height="480" alt="image" src="https://github.com/user-attachments/assets/3a52f545-9e22-41a5-b3eb-63440f804a6c" />
<img width="862" height="389" alt="image" src="https://github.com/user-attachments/assets/e777dd0a-d126-4671-83cb-a0bf123a9f49" />

Pesan permintaan DNS dikirimkan ke alamat IP **10.221.193.2**, yang merupakan server DNS lokal default pada perangkat.

---

2.
<img width="859" height="491" alt="image" src="https://github.com/user-attachments/assets/90316ab3-e080-4ad3-947e-af3b85ca689b" />

Jenis pesan pada permintaan DNS adalah **A**, yang bertujuan untuk memperoleh alamat **IPv4** dari domain tertentu.  
Pesan permintaan ini tidak mengandung jawaban (answers) karena hanya berupa query.

---

3.
<img width="863" height="488" alt="image" src="https://github.com/user-attachments/assets/695e3ca8-42ed-4b79-8726-19b9ed9ca9af" />

Pada pesan balasan DNS terdapat informasi mengenai server MIT seperti domain **mit.edu** atau subdomain terkait.  
Balasan DNS juga menyertakan alamat **IPv4** dari server tersebut sehingga client dapat melakukan koneksi langsung.

---

# SOAL 4

# Pertanyaan
## Perintah nslookup www.aiit.or.kr bitsy.mit.edu

1. Ke alamat IP manakah pesan permintaan DNS dikirimkan? Apakah alamat IP tersebut merupakan default alamat IP server DNS lokal Anda?
2. Periksa pesan permintaan DNS. Apa ”jenis” atau ”type” dari pesan tersebut? Apakah pesan tersebut mengandung ”jawaban” atau ”answers”?
3. Periksa pesan balasan DNS. Berapa banyak ”jawaban” atau “answers” yang terdapat di dalamnya. Apa saja isi yang terkandung dalam setiap jawaban tersebut?

# Jawaban :

1.
<img width="862" height="488" alt="image" src="https://github.com/user-attachments/assets/ff6c11b6-43d4-431e-b236-aa8f7b0b3f64" />
<img width="863" height="480" alt="image" src="https://github.com/user-attachments/assets/81b94f11-d80a-4d0d-a490-77e23e8ead81" />

Pesan permintaan DNS dikirimkan ke alamat IP **10.221.193.2**, yang merupakan server DNS lokal default pada perangkat.

---

2.
<img width="864" height="488" alt="image" src="https://github.com/user-attachments/assets/5e6140de-4147-46e4-835b-d8993a054c09" />

Jenis pesan pada permintaan DNS adalah **A**, yang digunakan untuk memperoleh alamat **IPv4** dari domain yang diminta.  
Pesan permintaan ini tidak memiliki jawaban (answers) karena hanya berupa query.

---

3.
<img width="856" height="484" alt="image" src="https://github.com/user-attachments/assets/47e6314a-f2eb-4f61-8ff7-c0dad27b6a2b" />

Pada pesan balasan DNS terdapat **1 jawaban (answer)**.  
Jawaban tersebut berisi:

- Nama domain yang diminta  
- Jenis record (**A**)  
- Alamat **IP (IPv4)** dari domain tersebut  
- Nilai **TTL (Time To Live)**
