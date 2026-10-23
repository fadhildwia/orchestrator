# Memelihara product workflow

- Repo ini adalah sumber empat profil agent dan lima skill personal Codex. Konteks, PRD, riset, ticket, kode, dan dokumen proprietary client/perusahaan tetap berada pada proyek masing-masing.
- Pertahankan pasangan empat profil di `agents/` dan skill di `skills/`. `frontend-engineer` adalah skill mandiri tanpa profil agent kelima. Semua profil mewarisi model/reasoning serta izin induk kecuali pengguna meminta pengaturan lain.
- Orchestrator memiliki PRD; researcher memberi bukti; designer memberi UX/UI; reviewer menilai secara independen. Hormati persetujuan client yang sudah diberikan dan batas tahap yang diotorisasi.
- `frontend-engineer` menangani ticket harian dalam mode `task`, `bugfix`, `feature`, dan `refactor`: investigasi, implementasi, validasi, serta review sesuai risiko hingga siap PR. Gunakan ticket/AC dan otorisasi existing; jangan menerapkan gate PRD/client universal pada pekerjaan yang sudah disetujui.
- Pertahankan tiga template produk pada referensi orchestrator dan empat template frontend pada referensi skill mandiri. README menautkan sumber tersebut tanpa menyalin seluruh prompt.
- Jaga skill tetap fokus dan self-contained. Referensi platform serta skill/tool tambahan bersifat sesuai kebutuhan; jangan membuat ketergantungan pada connector atau layanan berbayar yang belum tersedia.
- Installer harus mempertahankan file pengguna lain, mendeteksi konflik sebelum mutasi, dan mem-backup upgrade file yang dikelolanya. Jangan mengubah konfigurasi personal ketika hanya menguji installer.
- Jalankan `python3 scripts/validate.py` dengan dependency dari `requirements-dev.txt`, serta `python3 -m unittest discover -s tests -v` untuk perubahan installer, inventaris skill, atau paket referensi.
- Untuk perubahan workflow yang berarti, lakukan forward-test independen dengan brief mentah dan PRD client existing; untuk frontend, sertakan ticket yang mewakili mode terdampak, scope/otorisasi existing, dan keterbatasan akses pengujian. Catat batas bukti; jangan mengklaim runtime/native/client approval dari inspeksi source.
