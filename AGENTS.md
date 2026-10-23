# Memelihara product workflow

- Repo ini adalah sumber empat profil agent dan empat skill personal Codex. Konteks, PRD, riset dan hasil kerja client tetap berada pada proyek masing-masing.
- Pertahankan pasangan profil di `agents/` dan skill di `skills/`. Semua profil mewarisi model/reasoning serta izin induk kecuali pengguna meminta pengaturan lain.
- Orchestrator memiliki PRD; researcher memberi bukti; designer memberi UX/UI; reviewer menilai secara independen. Hormati persetujuan client yang sudah diberikan dan batas tahap yang diotorisasi.
- Jaga skill tetap fokus dan self-contained. Referensi platform serta skill/tool tambahan bersifat sesuai kebutuhan; jangan membuat ketergantungan pada connector atau layanan berbayar yang belum tersedia.
- Installer harus mempertahankan file pengguna lain, mendeteksi konflik sebelum mutasi, dan mem-backup upgrade file yang dikelolanya. Jangan mengubah konfigurasi personal ketika hanya menguji installer.
- Jalankan `python3 scripts/validate.py` dengan dependency dari `requirements-dev.txt`, serta `python3 -m unittest discover -s tests -v` untuk perubahan installer.
- Untuk perubahan workflow yang berarti, lakukan forward-test independen dengan brief mentah dan PRD client existing. Catat batas bukti; jangan mengklaim runtime/native/client approval dari inspeksi source.
