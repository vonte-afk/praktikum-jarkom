# Week 3 HTTP
### Penjelasan
1. Basic HTTP GET/Response Interaction

Basic HTTP GET/Response Interaction
Pada percobaan ini dilakukan proses pengambilan (request) sebuah file HTML sederhana dari server tanpa melibatkan objek tambahan seperti gambar atau script. Tujuannya adalah untuk memahami bagaimana proses komunikasi dasar antara client (browser) dan server menggunakan protokol HTTP, khususnya metode GET dan respon yang diberikan oleh server.

Langkah-langkah Percobaan :
- Jalankan aplikasi web browser (misalnya Chrome atau Firefox).
- Buka aplikasi Wireshark, lalu mulai proses capture pada jaringan yang digunakan (Wi-Fi atau Ethernet).
- Pada kolom filter di Wireshark, ketik http untuk menyaring paket yang berhubungan dengan HTTP.
- Kembali ke browser, kemudian masukkan URL berikut:
  http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html
- Tunggu hingga halaman berhasil dimuat sepenuhnya.
- Setelah itu, kembali ke Wireshark dan hentikan proses capture.

<img width="903" height="506" alt="Screenshot 2026-03-31 114300" src="https://github.com/user-attachments/assets/c9554321-b4fa-4c3d-9dbd-987cc4e2254a" />
<img width="828" height="555" alt="Screenshot 2026-03-31 114315" src="https://github.com/user-attachments/assets/d06bdd2d-bd20-4d8d-aec5-940934c2f8a0" />

Hasil tangkapan Wireshark menunjukkan bahwa:

Berdasarkan hasil tangkapan menggunakan Wireshark, dapat diamati bahwa browser mengirimkan HTTP GET request ke server untuk meminta file yang diinginkan. Selanjutnya, server merespons permintaan tersebut dengan HTTP response yang memiliki status 200 OK, yang menandakan bahwa permintaan berhasil diproses dengan baik.

Hal ini menunjukkan mekanisme dasar HTTP, yaitu:

- Client mengirim permintaan (request) ke server
- Server memberikan balasan (response) terhadap permitaan tersebut

Selain itu, karena ukuran file yang diminta relatif kecil, respon dari server dikirimkan dalam satu paket saja tanpa mengalami proses fragmentasi.

---
 
2. HTTP CONDITIONAL GET/response interaction

Pada percobaan ini dilakukan pengaksesan halaman web yang sama sebanyak dua kali dengan tujuan untuk mengamati mekanisme caching pada protokol HTTP. Dengan melakukan akses berulang, dapat dilihat apakah browser mengambil data dari server kembali atau menggunakan data yang sudah tersimpan sebelumnya (cache).

Langkah-langkah Percobaan :
- Jalankan aplikasi web browser (seperti Chrome atau Firefox).
- Buka aplikasi Wireshark, kemudian mulai proses capture pada jaringan yang digunakan.
- Gunakan filter http pada Wireshark untuk menampilkan paket yang berkaitan dengan HTTP.
- Masukkan URL berikut pada browser:
  http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html
- Akses atau reload halaman tersebut sebanyak dua kali.
- Setelah proses selesai, kembali ke Wireshark dan hentikan capture.

<img width="826" height="459" alt="Screenshot 2026-03-31 114327" src="https://github.com/user-attachments/assets/aa0a9aac-9578-41e4-a59d-f2a80f40ed57" />
<img width="825" height="552" alt="Screenshot 2026-03-31 114335" src="https://github.com/user-attachments/assets/f07858d5-ea81-47ef-b57b-ea37ff4bf364" />

Hasil yang diamati:

- Berdasarkan hasil pengamatan, pada request kedua terlihat adanya header If-Modified-Since yang dikirim oleh browser ke server. Header ini digunakan untuk menanyakan apakah file yang diminta mengalami perubahan sejak waktu terakhir diakses.
- Server kemudian dapat memberikan dua jenis respon, yaitu:
- - 304 Not Modified, jika file tidak mengalami perubahan sejak terakhir diakses
- - 200 OK, jika file telah diperbarui sehingga server mengirimkan ulang data tersebut 

Mekanisme ini digunakan untuk:

- Mengurangi penggunaan bandwidth karena data tidak selalu dikirim ulang
- Mempercepat waktu akses dengan memanfaatkan cache yang tersimpan di sisi client

---

3. Retrieving Long Documents

Pada percobaan ini dilakukan pengambilan dokumen berukuran besar dari server. Tujuan dari percobaan ini adalah untuk mengamati bagaimana proses pengiriman data HTTP ketika ukuran file cukup besar, yang biasanya akan dikirim dalam beberapa bagian (packet) oleh server.

Langkah - langkah Percobaan:
- Jalankan aplikasi web browser (seperti Chrome atau Firefox).
- Buka aplikasi Wireshark, kemudian mulai proses capture pada jaringan yang digunakan.
- Gunakan filter http pada Wireshark untuk menampilkan paket yang berkaitan dengan HTTP.
- Masukkan URL berikut pada browser:
  http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html
- Tunggu hingga halaman berhasil dimuat sepenuhnya.
- Setelah itu, kembali ke Wireshark dan hentikan proses capture.

<img width="827" height="459" alt="Screenshot 2026-03-31 114359" src="https://github.com/user-attachments/assets/51d70889-48fe-467e-abf9-eeaf2eb8d192" />
<img width="829" height="466" alt="Screenshot 2026-03-31 114409" src="https://github.com/user-attachments/assets/58af073c-ee27-48ef-97dc-039b1787eb03" />

Pada percobaan pengambilan file berukuran besar, ditemukan bahwa:

- Pada percobaan pengambilan file dengan ukuran besar, dapat diamati bahwa HTTP response tidak dikirimkan dalam satu paket saja. Data yang dikirim oleh server dipecah menjadi beberapa bagian dalam bentuk segmen TCP.

Di Wireshark ditandai dengan:

- “TCP segment of a reassembled PDU”, yang menunjukkan bahwa data asli telah dibagi menjadi beberapa segmen dan kemudian disusun kembali (reassembly).

Hal ini menunjukkan bahwa:

- Protokol HTTP berjalan di atas protokol TCP
- TCP akan membagi data besar menjadi beberapa segmen agar dapat dikirim melalui jaringan

---

4. HTML Documents dengan Embedded Objects

Pada percobaan ini dilakukan pengaksesan halaman web yang tidak hanya berisi file HTML, tetapi juga mengandung objek tambahan seperti gambar. Tujuan dari percobaan ini adalah untuk mengamati bagaimana browser melakukan beberapa request HTTP untuk mengambil seluruh komponen yang terdapat pada halaman web tersebut.

Langkah - langkah Percobaan:
- Jalankan aplikasi web browser (seperti Chrome atau Firefox).
- Buka aplikasi Wireshark, kemudian mulai proses capture pada jaringan yang digunakan.
- Gunakan filter http pada Wireshark untuk menampilkan paket yang berkaitan dengan HTTP.
- Masukkan URL berikut pada browser:
  http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html
- Tunggu hingga halaman beserta seluruh objek (seperti gambar) berhasil dimuat sepenuhnya.
- Setelah itu, kembali ke Wireshark dan hentikan proses capture.

<img width="825" height="463" alt="Screenshot 2026-03-31 114434" src="https://github.com/user-attachments/assets/9bd41805-f223-456a-bc0a-1ccbd57a2918" />
<img width="831" height="466" alt="Screenshot 2026-03-31 114453" src="https://github.com/user-attachments/assets/4449929a-f5a0-45dd-b3f2-90deb6351a0d" />

Hasil pengamatan menunjukkan:

- Berdasarkan hasil pengamatan, terdapat lebih dari satu HTTP GET request yang dikirimkan oleh browser. Hal ini terjadi karena selain mengambil file HTML utama, browser juga mengirimkan request tambahan untuk setiap objek yang terdapat pada halaman tersebut, seperti gambar.

Kondisi ini terjadi karena:

- File HTML hanya berisi referensi atau tautan ke objek lain
- Browser perlu mengambil setiap objek tersebut secara terpisah melalui request HTTP tambahan

Oleh karena itu, satu halaman web dapat menghasilkan banyak HTTP request untuk memuat seluruh konten secara lengkap.

---

5. HTTP Authentication

Pada percobaan terakhir ini dilakukan pengaksesan terhadap halaman web yang dilindungi oleh mekanisme autentikasi menggunakan username dan password. Tujuan dari percobaan ini adalah untuk memahami bagaimana proses autentikasi bekerja dalam protokol HTTP ketika client mencoba mengakses resource yang terbatas.

<img width="824" height="458" alt="Screenshot 2026-03-31 114509" src="https://github.com/user-attachments/assets/87b86807-3c01-424c-aec7-c4d5fd6bb9b4" />
<img width="822" height="457" alt="Screenshot 2026-03-31 114519" src="https://github.com/user-attachments/assets/de1930c0-de13-4730-a195-355f37316a8d" />
<img width="827" height="466" alt="Screenshot 2026-03-31 114529" src="https://github.com/user-attachments/assets/01da6d87-f519-44cf-8760-e08db8b9510d" />

Hasil Analisis:

Berdasarkan hasil pengamatan, data username dan password yang dikirimkan dalam proses autentikasi HTTP dikodekan menggunakan metode Base64.

Namun, perlu diperhatikan bahwa encoding Base64:

- Bukan merupakan bentuk enkripsi
- Dapat dengan mudah didekode kembali ke bentuk aslinya

Oleh karena itu, dapat disimpulkan bahwa penggunaan HTTP tanpa tambahan keamanan seperti HTTPS tidak aman untuk pertukaran data yang bersifat sensitif, karena informasi penting masih dapat dengan mudah diakses oleh pihak yang tidak berwenang.

---

## Kesimpulan
Pada praktikum ini dapat disimpulkan bahwa HTTP bekerja dengan mekanisme request dan response antara client dan server. Setiap akses web diawali dengan HTTP GET dan direspon server, misalnya dengan status 200 OK.

Satu halaman web dapat menghasilkan banyak request jika terdapat objek tambahan seperti gambar. HTTP juga memiliki fitur seperti caching untuk efisiensi dan menggunakan TCP untuk membagi data besar menjadi beberapa segmen.

Dari sisi keamanan, HTTP Authentication dengan Base64 belum aman karena bukan enkripsi. Oleh karena itu, diperlukan HTTPS untuk melindungi data sensitif.