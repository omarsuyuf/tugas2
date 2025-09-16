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
