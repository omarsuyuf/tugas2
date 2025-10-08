======= TUGAS 6 ========

- Apa perbedaan antara synchronous request dan asynchronous request?
Synchronous = Alurnya kurang lebih browser mengirim request, page menunggu respons dengan catatan UI terblokir sampai server selesai, lalu seluruh page biasanya di-render ulang.

Asynchronous = Alurnya browser mengirim request di belakang layar (AJAX/fetch), namun berbeda dengan synchronous, ini UI tetap responsif, ketika respons tiba hanya bagian tertentu DOM yang diperbarui, tidak perlu reload penuh halaman, efisien dan terasa cepat.


- Bagaimana AJAX bekerja di Django (alur request–response)?
1. Event di client - seperti user klik tombol/submit form via JS
2. Kirim request - JavaScript (fetch/XMLHttpRequest) mengirim HTTP request ke URL Django (view) dengan header, method (GET/POST), payload (JSON/FormData), dan CSRF token untuk POST
3. Django view memproses - Validasi input, akses DB, jalankan logic
4. Kirim respons - View mengembalikan JSON (JsonResponse) atau fragmen HTML
5. Update UI - JS di client membaca respons dan memodifikasi DOM


- Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
1. UX lebih cepat, tidak reload penuh
3. Bandwidth efisien, kirim dan terima data seperlunya (JSON/HTML kecil).
3. Interaktivitas tinggi (form validasi dinamis, live search, infinite scroll)
4. Arsitektur rapi, pisahkan data (JSON API) dan presentasi (JS/HTML), mudah direuse untuk mobile.


- Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?

1. Sertakan CSRF token pada POST
2. Selalu pakai TLS agar kredensial tidak disadap
3. Validasi & sanitasi server-side, jangan percaya validasi JS. Gunakan Django Forms/Serializer untuk validasi, bersihkan input, agar mencegah XSS/SQLi
4. Session/Cookie amankan = SESSION_COOKIE_SECURE=True, CSRF_COOKIE_SECURE=True, SESSION_COOKIE_HTTPONLY=True, CSRF_COOKIE_HTTPONLY=False (agar JS bisa baca via cookie-to-header pattern), SESSION_COOKIE_SAMESITE='Lax' atau 'Strict'.
5. Rate limiting & anti-bruteforce, seperti captcha setelah beberapa gagal
6. Pesan error generik dengan respons yang seragam agar ga bocor informasi username
7. Log attempt login/register, IP, user agent untuk deteksi jika ada yang janggal


- Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
1. Responsif, jadi kerasa hanya bagian relevan yang berubah
2. Scroll/posisi pengguna tidak kereset karna reload
3. Feedback real time
4. Performa lebih enak karna beban render dan transfer data lebih ringan di mata pengguna



======= TUGAS 5 ========

- Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
1. !important (penulis/author)
2. Inline style: style="..."
3. Selector dengan ID
4. Selector class / attribute / pseudo-class
5. Selector element / pseudo-element
6. Universal * dan inheritance

Dengan catatan jika sama kuatnya, yang muncul terakhir di file menang.  


-  Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Karena mayoritas akses web sekarang dari layar kecil (HP). Tanpa layout yang menyesuaikan, maka banyak bisa terjadi UX yang rusak, seperti teks kecil, tombol susah diklik, scroll horizontal, dan lain-lain. Responsive juga ngasih satu codebase untuk semua device, biaya maintenance lebih murah, performa lebih stabil, dan ramah SEO serta aksesibilitas.

Contoh:
Sudah responsive: toko online/e-commerce modern atau portal berita modern.
Belum responsive: situs lama berbasis tabel. Di mobile harus pinch-zoom, text terlalu kecil, tombol saling berhimpitan, horizontal scroll muncul.


- Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Margin = jarak di luar border, memisahkan elemen dengan elemen lain, gabisa diberi warna.
Border = garis pembatas di antara margin dan padding, bisa diwarnai.
Padding = jarak di dalam border, antara konten dengan border, mengembang bersama background.

- Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox: layout 1 dimensi (baris atau kolom), kegunaannya lebih cocok untuk navbar, alignment vertikal/horizontal, card actions.
CSS Grid: layout 2 dimensi (baris dan kolom), kegunaannya lebih cocok untuk dashboard, product listing multi-k


- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

1. Menambahkan tailwind di base
2. Menambahkan fitur edit dan delete Product dengan cara membuat function di views.py , lalu buat file html nya, lalu masukkan urls nya ke urls.py, lalu buat tombolnya di main.htmnl.
3. Membuat navigation bar (kayak header) dengan cara membuat file navbar.html lalu impor dengan cara include di main.html
4. Konfigurasi static files dengan cara menambahkan 'whitenoise.middleware.WhiteNoiseMiddleware' di MIDDLEWARE pada settings.py dan static_url
5. Membuat file global.css
6. Menghubungkan global.css dan tailwind ke base.html dengan modifikasi pada base.html
7. Membuat custom styling pada global.css
8. Styling navbar,login,register,home,card_product,product_detail,create_product,edit_product dengan css
9. Commit dan push




======= TUGAS 4 ========
- Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

AuthenticationForm adalah format form bawaan dari Django untuk sistem login (kayak ambil template login yang siap pake)

Kelebihan : 
a. Langsung pakai 
b. Aman karna mengikuti mekanisme authentication dan hashing Django

Kekurangan :
a. Terbatas, jika mau verifikasi tambahan kayak OTP


- Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi =  verifikasi identitas pengguna.
Otorisasi = apa yang bisa dilakukan pengguna yang sudah terautentikasi.

Implementasi dari django :
- Autentikasi: beberapa komponen django seperti,  authenticate(), login(), logout(), AuthenticationForm().
- Otorisasi: sistem permissions dan groups seperti, @login_required dan @permission_required, user.is_authenticated, user.has_perm()


- Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Cookies = ringan, tidak membebani server, tapi kapasitas kecil dan rawan dimodifikasi/dicuri kalau tidak diamankan.
Session = aman karena data di server, bisa simpan banyak, tapi butuh storage server dan konfigurasi skalabilitas.

- Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Tidak otomatis aman, ada risiko XSS/CSRF dan pencurian jika tanpa HTTPS karena Django secara default simpan state di server, cookie hanya berisi session ID. 

Django juga sediakan proteksi seperti, HttpOnly, Secure, SameSite, CSRF middleware.


- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Pertama aktifin virtual env dan akses file
2. Buat sistem registrasi dan login dengan membuat function di views.py dan membuat page register.html & login.html
3. Masukkan di urls.py agar dapat dibuka linknya/pagenya
4. Membuat sistem logout dengan membuat function di views.py dan masukkan di urls.py
5. Membuat sistem agar login terlebih dahulu untuk mengakses website, dengan membuat code @login_required di function utama views.py
6. Membuat code agar data dari cookies tercatat, dengan menggunakan HttpResponseRedirect, reverse, dan datetime, lalu mengimplementasikannya di function" utama seperti show_main, login, logout.
7. Menghubungkan Model Product dengan user, dengan menambahkan "user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)" pada class Product agar terhubung.
8. Buat migration
9. Test run di local dan test uji ke fitur yang baru dibuat
10. Push ke github dan pws


======= TUGAS 3 ========

- Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Agar menjadi data di backend dengan format yang mudah dibaca dan bisa dilihat/digunakan datanya oleh beberapa pihak. Dan agar dapat dikembangkan oleh tim developer lebih mudah


- Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

JSON karena lebih ringkas dan mudah dibaca, karena lebih cocok dengan struktur di programming language yang populer


- Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

untuk menjalankan

is_valid() ngecek input di form dan jika hasilnya true, maka data bersihnya ada di form.cleaned_data dan aman dipakai. Jika tidak maka input yang salah bisa ikut tersimpan dan berpotensi bikin error



- Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token mencegah Cross-Site Request Forgery (CSRF), yaitu serangan yang memaksa browser pengguna terautentikasi mengirim request tanpa sepengetahuan mereka. Jika tidak dilindungi token, penyerang bisa menanam halaman/skrip yang saat dikunjungi user akan mengirim suatu tindakan seperti hack/grief ke situs kita. Token memastikan request berasal dari halaman milik aplikasi, bukan dari sumber asing.



- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat model Product sesuai dengan spesifikasi/requirement tugas yang diminta sebelumnya
2. Menambahkan method increment_views() untuk menambah product_views.
3. Membuat model form "ProductForm" dengan ketentuan yang diminta : name, price, description, thumbnail, category, is_featured.
4. Menambah form.is_valid() sebelum form.save().
5. Membuat tampilan di views.py untuk tiap segmen di websitenya :
- show_main : untuk main page sebagai page utama yang menampilkan barang-barang dan informasi
- create_product : untuk page tambah produk, mengisi data barang dan post
- show_product : mengambil produk berdasarkan UUID, memanggil increment_views(), lalu render product_detail.html.
6. Membuat code untuk data delivery XML/JSON, dengan membuat function show_xml dan show_json untuk memberi label seri semua Product ke XML/JSON.
7. Routing urls.py menginclude main.urls. 
- Page : "" -> show_main, "add/" -> create_product, "detail/<uuid:id>/" -> show_product
- Data delivery : "xml/", "json/", "xml/<uuid:id>/", "json/<uuid:id>/"
8. Membuat template html :
- main.html : menampilkan data mahasiswa, dan daftar produk dengan tombol add dengan link per item
- create_product.html : form sederhana dengan {% csrf_token %} dan tombol Simpan, 
- product_detail.html : menampilkan detail produk termasuk product_views dan created_at.
9. Test menjalankan runserver, dan test add 1 produk
10. Coba akses 4 endpoint data delivery di Postman: /xml/, /json/, /xml/<UUID>/, /json/<UUID>/.
11. Push ke git dan PWS



Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
-


Foto Postman :
<img width="1280" height="822" alt="image" src="https://github.com/user-attachments/assets/308ba3c7-17f7-4bce-b223-7244aedd016b" />
<img width="1280" height="918" alt="image" src="https://github.com/user-attachments/assets/ea96ef3f-70e0-4931-826a-0764f50517ba" />
<img width="1280" height="676" alt="image" src="https://github.com/user-attachments/assets/30b14c8a-37fb-4e5a-8666-16d7563ff136" />
<img width="1280" height="653" alt="image" src="https://github.com/user-attachments/assets/be0e9680-4bd8-43ba-bde1-7fbe4498acba" />







======= TUGAS 2 ========


Link PWS:  https://omar-suyuf-tugas2.pbp.cs.ui.ac.id


- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
1. Membuat repository baru untuk Tugas 2 agar terpisah dari repo tutorial
2. Bikin file folder baru
3. Aktifkan virtual environment pada terminal di direktori file 
4. Download requirements + start project dengan django 
5. Konfigurasi file dengan hosting yang sesuai
6. Membuat model Product di main/models.py sesuai dengan yang diminta:
   - name: CharField
   - price: IntegerField
   - description: TextField
   - thumbnail: URLField
   - category: CharField
   - is_featured: BooleanField
6. Menjalankan "makemigrations" dan "migrate" 
7. Membuat fungsi "home" di views.py untuk menampilkan nama aplikasi, nama, kelas, dan NPM  
8. Mengatur routing pada main/urls.py dan shopproj/urls.py 
9. Membuat template untuk desain html "main.html" di folder templates yang menampilkan data dari context
10. Commit dan push ke github
11. Tambah list "ALLOWED_HOSTS" dan sesuaikan environment variables, lalu push branch `master` untuk deploy di PWS
12. Ubah beberapa coding untuk adjust yang masih kurang, lalu commit lagi


- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Bagan :

Client di browser -> urls.py (cocokin url, lalu lanjut ke view) -> views.py (app) -> models.py (app) -> template (tampilan html) -> response pada client

urls.py: mencocokkan URL dengan fungsi view.  
views.py: menjalankan logika aplikasi, memanggil model bila perlu, lalu render template.  
models.py: definisi struktur data (seperti "Product") dan akses database.  
template (HTML): file yang mendapat data context dari view untuk ditampilkan ke user.  


- Jelaskan peran settings.py dalam proyek Django!
-> Kurang lebih seperti menyimpan konfigurasi settingan dari proyek, seperti daftar aplikasi (INSTALLED_APPS), database , templates , allowed_hosts, dan lain lain.


- Bagaimana cara kerja migrasi database di Django?
1. Tulis coding model di "models.py" -> buat perubahan agar menyesuaikan model yang kita mau
2. Run command di terminal "python manage.py makemigrations" → membuat file migrasi di direktori migration dari aplikasi yang kita buat
3. Run command di terminal "python manage.py migrate" → migrasi diterapkan ke database 


- Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Karna Django bisa dibilang cukup lengkap dalam struktur yang dibutuhkan untuk jadi kerangka utama aplikasi. Juga ada template engine bawaan dan Pola MVT yang sederhana untuk dipahami, cocok belajar konsep dasar web.  



- Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Udah cukup, namun mungkin penjelasannya bisa dipermudah yang di textnya, karna susah dipahami gitu dan jadi cenderung copy-paste isinya aja
