import re

parag = " Hari Pendidikan Nasional, disingkat HARDIKNAS, adalah hari nasional yang bukan hari libur yang ditetapkan oleh pemerintah Indonesia untuk memperingati kelahiran Ki Hadjar Dewantara, tokoh pelopor pendidikan di Indonesia dan pendiri lembaga pendidikan Taman Siswa, diperingati pada tanggal 2 Mei setiap tahunnya.Daftar isiWikisource memiliki naskah sumber yang berkaitan dengan artikel ini:Salinan pembetulan Pembaharuan Keputusan Presiden RepublikIndonesia No. 330 tahun 1954 tentang Hari-Hari Nasional yang Bukan Hari Libur.pdf/1 Hari Pendidikan Nasional diperingati setiap tanggal 2Mei, bertepatan dengan hari ulang tahun Ki Hadjar Dewantara, pahlawan nasional yang dihormati sebagai bapak pendidikan nasional di Indonesia. Ki Hadjar Dewantara lahir dari keluarga kaya Indonesia selama era kolonialisme Belanda, ia dikenal karena berani menentangkebijakan pendidikan pemerintah Hindia Belanda pada masa itu, yang hanya memperbolehkan anak-anak kelahiran Belanda atau orang kaya yang bisa mengenyam bangku pendidikan. Hari nasional ini ditetapkan melalui Keppres No. 316 Tahun9 tanggal 16 Desember 1984. Kritiknya terhadap kebijakan pemerintah kolonial menyebabkan ia diasingkan ke Belanda, dan ia kemudian mendirikan sebuah lembaga pendidikan bernama Taman Siswa setelah kembali ke Indonesia. Ki Hadjar Dewantara diangkat sebagai menteri pendidikan setelah kemerdekaan Indonesia. Filosofinya, tut wuri handayani (di belakang memberi dorongan), digunakan sebagai semboyan dalam dunia pendidikan Indonesia. Ia wafat pada tanggal 26 April 1969. Untuk menghormati jasa-jasanya terhadap dunia pendidikan Indonesia, pemerintah Indonesia menetapkan tanggal kelahirannya sebagai Hari Pendidikan Nasional."


cocok = re.findall(r"ia\w+", parag)
print(cocok)