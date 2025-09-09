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
