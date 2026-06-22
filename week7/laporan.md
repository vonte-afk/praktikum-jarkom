# PENJELASAN TCP

#### Nama : Muhammad Yusuf Ar Rahman
#### NIM : 103072400143
#### Kelas : IF-04-04
# Program Socket dengan TCP
# Client
<img width="692" height="650" alt="image" src="https://github.com/user-attachments/assets/f75e48a6-9b66-46e0-ab0a-cd9283058875" />

1. Inisialisasi TCP Socket

- SOCK_STREAM: Inilah "tanda pengenal" bahwa kita menggunakan protokol TCP. Berbeda dengan UDP yang main kirim saja, TCP bersifat connection-oriented. Artinya, harus ada jabat tangan (handshake) di awal.

- clientSocket.connect((serverName, serverPort)): Ini baris yang paling penting. Sebelum bisa mengirim data, client harus membangun koneksi stabil ke server. Di balik layar, baris ini memicu proses TCP Three-Way Handshake.

---

2. Pengiriman Data yang Lebih Simpel

- clientSocket.send(sentence.encode()): Perhatikan bahwa di sini kita hanya menggunakan .send(), bukan .sendto().

- Kenapa tidak perlu alamat lagi? Karena koneksi sudah terjalin (sudah "nyambung" lewat telepon). Jadi, program sudah tahu persis ke mana data tersebut harus mengalir tanpa perlu dituliskan ulang alamat tujuannya setiap kali mengirim pesan.

---

3. Penerimaan Data

- clientSocket.recv(2048): Sama seperti pengiriman, fungsi terima datanya pun lebih sederhana. Kita tidak perlu menangkap serverAddress lagi karena dalam satu pipe (pipa) koneksi TCP ini, pengirimnya sudah pasti server yang kita connect tadi.

# Server

<img width="696" height="710" alt="image" src="https://github.com/user-attachments/assets/4b63ad97-3c77-4a96-b630-aa3a3cf73762" />

1. Inisialisasi dan Mendengarkan (Listen)

- SOCK_STREAM: Masih konsisten, ini menandakan penggunaan protokol TCP.

- serverSocket.listen(5): Ini bagian baru. Fungsi ini mengubah socket menjadi "pasif". Angka 5 adalah ukuran antrean (backlog). Artinya, server bisa menampung hingga 5 calon client yang mengantre untuk dilayani sebelum server mulai menolak koneksi baru.

---

2. Proses Jabat Tangan (Accept)

- connectionSocket, addr = serverSocket.accept(): Baris ini sangat sakral di TCP.

- - Saat ada client melakukan .connect(), baris ini akan "terbangun" dan menciptakan socket baru khusus untuk client tersebut (connectionSocket).

- - Penting: serverSocket tetap terjaga di pintu depan untuk menunggu tamu lain, sedangkan connectionSocket adalah jalur pribadi untuk mengobrol dengan tamu yang baru masuk.

---

3. Komunikasi Lewat Jalur Pribadi

- connectionSocket.recv(2048): Perhatikan bahwa server menerima data menggunakan connectionSocket, bukan serverSocket. Karena koneksi sudah terjalin secara eksklusif, server tidak perlu memanggil recvfrom untuk tahu siapa pengirimnya.

- connectionSocket.send(...): Begitu juga saat membalas. Server langsung mengirim ke jalur pribadi tersebut. Data otomatis sampai ke client yang tepat.

---

4. Menutup Jalur Pribadi

- connectionSocket.close(): Setelah satu transaksi selesai (terima, ubah jadi kapital, kirim balik), jalur pribadi ini ditutup. Namun, karena ini berada di dalam while True, server akan langsung naik lagi ke atas untuk menunggu accept() berikutnya.

# Output

<img width="1186" height="57" alt="image" src="https://github.com/user-attachments/assets/867871f7-ed20-4c4d-9182-1cb28671a52d" />

---

# PENJELASAN UDP

# Program Socket dengan UDP
# Client
1. Import dan Inisialisasi

<img width="675" height="802" alt="image" src="https://github.com/user-attachments/assets/146a7655-2b77-49b1-9f0d-3b34464a929f" />

Bagian ini adalah tahap persiapan agar program bisa berkomunikasi lewat jaringan.

- from socket import *: Mengimpor modul socket agar kita bisa menggunakan fungsi-fungsi jaringan.

- serverName = "localhost": Menentukan alamat server tujuan. "localhost" berarti server berada di komputer yang sama.

- serverPort = 12000: Menentukan "pintu" (port) mana yang akan diketuk pada server.

- clientSocket = socket(AF_INET, SOCK_DGRAM):

- - AF_INET: Menandakan kita menggunakan alamat IPv4.

- - SOCK_DGRAM: Menandakan bahwa koneksi ini menggunakan protokol UDP (bukan TCP). UDP bersifat connectionless, artinya data dikirim tanpa perlu membuat koneksi tetap terlebih dahulu.

---

2. Perulangan Utama dan Pengiriman Pesan

<img width="670" height="813" alt="image" src="https://github.com/user-attachments/assets/7d9a7558-301b-4768-ae08-64a908880d55" />

Bagian ini mengatur logika interaksi pengguna dan cara pengiriman datanya.

- while running :: Membuat program terus berjalan agar user bisa mengirim pesan berkali-kali.

- message = input("> "): Mengambil input teks dari keyboard user.

- if message.lower() == "exit" :: Logika untuk keluar. Jika user mengetik "exit", program akan memberi tahu server, lalu mengubah status running menjadi False untuk menghentikan perulangan.

- message.encode(): Sangat penting! Socket hanya bisa mengirim data dalam bentuk bytes (angka biner), bukan teks string biasa. Fungsi ini mengubah teks menjadi format byte agar bisa dikirim lewat kabel jaringan.

- sendto(...): Fungsi khusus UDP untuk mengirim data. Karena UDP tidak punya koneksi tetap, kita harus menyertakan isi pesan dan alamat tujuan (IP & Port) setiap kali mengirim sesuatu.

---

3. Penerimaan Balasan dari Server

<img width="666" height="800" alt="image" src="https://github.com/user-attachments/assets/9b857265-838c-4dd6-82b5-98d1c687ef56" />

Setelah mengirim pesan, client menunggu jawaban kembali dari server.

- clientSocket.recvfrom(2048): Fungsi ini membuat program "menunggu" (blocking) sampai ada data yang masuk.

- - 2048 adalah ukuran buffer, yaitu kapasitas maksimal data yang bisa diterima dalam satu waktu.

- - Fungsi ini mengembalikan dua hal: isi pesan (modifiedMessage) dan alamat pengirimnya (serverAddress).

- modifiedMessage.decode(): Kebalikan dari encode. Data byte yang diterima dari server diubah kembali menjadi teks string agar bisa dibaca manusia di layar monitor.

# Server

1. Menghubungkan (Bind)

<img width="702" height="720" alt="image" src="https://github.com/user-attachments/assets/bef1fc37-0230-4540-b617-7e28cf19e8a6" />

Bagian bind adalah proses mengalokasikan port spesifik untuk program ini.

- serverSocket.bind(('', serverPort)):

-  - Tanda '' (string kosong) berarti server akan mendengarkan koneksi dari semua alamat IP yang tersedia di komputer tersebut (baik itu IP lokal maupun IP publik).

- - serverPort (12000) adalah pintu masuknya. Jika Client mengirim ke port 12000, maka kode inilah yang akan menangkap pesannya.

---

2. Perulangan Utama (Logika Pengolahan Pesan)

<img width="698" height="702" alt="image" src="https://github.com/user-attachments/assets/3385ed52-93e5-401d-b629-c15b14704024" />

Ini adalah "jantung" dari server yang membuatnya terus aktif menunggu kiriman data.

- serverSocket.recvfrom(2048): Server berhenti di baris ini (standby) sampai ada Client yang mengirimkan data. Begitu data sampai, ia menangkap pesannya (message) dan mencatat siapa pengirimnya (clientAddress).

- - .decode() dan .upper():

- - - Pesan yang masuk didekode dari bytes ke teks.

- - - decodedMessage.upper() adalah logika manipulasi teks. Di sini, server diperintahkan untuk mengubah semua huruf menjadi HURUF KAPITAL.

- Logika "Exit": Jika client mengirim kata "exit", server akan mencetak pesan pemberhentian dan mengubah running = False untuk mematikan dirinya sendiri.

- serverSocket.sendto(...): Setelah teks diubah menjadi kapital dan di-encode kembali ke bytes, server mengirimkannya balik ke clientAddress.

- - Inilah alasan mengapa UDP disebut connectionless; server tahu ke mana harus membalas hanya karena ia baru saja menerima informasi clientAddress dari paket yang datang.

# Output

<img width="786" height="63" alt="image" src="https://github.com/user-attachments/assets/af9fd8fd-b496-4666-8aaa-8eb5647b79e7" />