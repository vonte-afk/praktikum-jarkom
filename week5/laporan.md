#### Nama : Muhammad Yusuf Ar Rahman
#### NIM : 103072400143
#### Kelas : IF-04-04

# Pertanyaan
1. Pilih satu paket UDP yang terdapat pada trace Anda. Dari paket tersebut, berapa banyak 
“field” yang terdapat pada header UDP? Sebutkan nama-nama field yang Anda temukan!
2. Perhatikan informasi “content field” pada paket yang Anda pilih di pertanyaan 1. Berapa 
panjang (dalam satuan byte) masing-masing “field” yang terdapat pada header UDP?
3. Nilai yang tertera pada ”Length” menyatakan nilai apa? Verfikasi jawaban Anda melalui 
paket UDP pada trace.
4. Berapa jumlah maksimum byte yang dapat disertakan dalam payload UDP? (Petunjuk: 
jawaban untuk pertanyaan ini dapat ditentukan dari jawaban Anda untuk pertanyaan 2)
5. Berapa nomor port terbesar yang dapat menjadi port sumber? (Petunjuk: lihat petunjuk 
pada pertanyaan 4)
6. Berapa nomor protokol untuk UDP? Berikan jawaban Anda dalam notasi heksadesimal dan 
desimal. Untuk menjawab pertanyaan ini, Anda harus melihat ke bagian ”Protocol” pada 
datagram IP yang mengandung segmen UDP.
7. Periksa pasangan paket UDP di mana host Anda mengirimkan paket UDP pertama dan paket 
UDP kedua merupakan balasan dari paket UDP yang pertama. (Petunjuk: agar paket kedua 
merupakan balasan dari paket pertama, pengirim paket pertama harus menjadi tujuan dari 
paket kedua). Jelaskan hubungan antara nomor port pada kedua paket tersebut!

# Jawaban :

1. Jumlah dan Nama Field pada Header UDP  
Header pada protokol UDP terdiri dari **4 field utama**, yaitu:

- **Source Port** → Menunjukkan nomor port dari pengirim paket  
- **Destination Port** → Menunjukkan nomor port tujuan paket  
- **Length** → Menyatakan panjang keseluruhan segmen UDP  
- **Checksum** → Digunakan untuk proses pengecekan kesalahan pada data

<img width="1267" height="713" alt="image" src="https://github.com/user-attachments/assets/cab70169-ad1b-4cc5-a05b-54a5a5e86991" />

---

2. Panjang Masing-Masing Field  
Setiap field pada header UDP memiliki ukuran **2 byte**. Rinciannya adalah:

- Source Port = 2 byte  
- Destination Port = 2 byte  
- Length = 2 byte  
- Checksum = 2 byte  

Sehingga total ukuran **header UDP adalah 8 byte**.

<img width="1264" height="714" alt="image" src="https://github.com/user-attachments/assets/88191b1a-9874-4159-975f-ccf7fe28ea2d" />

---

3.  
Nilai pada field **Length** menunjukkan **panjang total dari segmen UDP**, yang meliputi bagian header dan payload (data).

Contohnya jika nilai **Length = 58 byte**, maka dapat diuraikan menjadi:

- 8 byte → ukuran header UDP  
- 50 byte → ukuran payload (data)

Dengan demikian dapat disimpulkan bahwa:

**Length = ukuran header UDP + ukuran payload**

<img width="1269" height="715" alt="image" src="https://github.com/user-attachments/assets/2afb2723-d116-4c12-a3af-eb4700e01346" />

---

4.  
**Maksimum Payload UDP**

Diketahui bahwa:

Field **Length** memiliki ukuran **2 byte (16 bit)**  
Sehingga nilai maksimum yang dapat direpresentasikan adalah:

2¹⁶ − 1 = **65.535 byte**

Rumus:

Payload maksimum = 65.535 − 8  

(8 byte merupakan ukuran header UDP)

Hasil:

Payload maksimum = **65.527 byte** (sekitar 64 KB)

<img width="1264" height="710" alt="image" src="https://github.com/user-attachments/assets/6eea8a61-5b23-4826-bd2e-99c5507b8f10" />

---

5. Nomor Port Maksimum  
Karena nomor port direpresentasikan menggunakan **16 bit**, maka nilai maksimum yang dapat digunakan adalah:

2¹⁶ − 1 = **65.535**

---

6. Nomor Protokol UDP  
Pada header IP, protokol UDP memiliki nilai:

- **Desimal : 17**  
- **Heksadesimal : 0x11**

Informasi ini dapat dilihat pada field **Protocol** di dalam datagram IP yang membawa segmen UDP.

<img width="1266" height="656" alt="image" src="https://github.com/user-attachments/assets/76fad434-69ca-4092-ab5d-4e1c7c164489" />

---

7. Hubungan Nomor Port pada Paket UDP  

Pada komunikasi UDP antara dua host, terjadi pertukaran nomor port antara paket permintaan dan balasan.

**Paket pertama (request):**

Source Port = A  
Destination Port = B  

**Paket kedua (reply):**

Source Port = B  
Destination Port = A  

Artinya, port tujuan pada paket pertama akan menjadi port sumber pada paket balasan, dan sebaliknya.

<img width="1268" height="715" alt="image" src="https://github.com/user-attachments/assets/481d3dd8-10c3-4570-8c86-4f90f4db8671" />
<img width="1267" height="716" alt="image" src="https://github.com/user-attachments/assets/939dc0c2-65e1-4b1e-bda5-630037694184" />