# Panduan kontribusi

Kontributor baru dipersilakan. Kamu dapat memperbaiki dokumentasi, melaporkan bug, mengusulkan peningkatan, menambah contoh sintetis, atau mengirim perubahan kode dan workflow. Bahasa Indonesia maupun Inggris dapat digunakan dalam issue dan pull request.

## Mulai dari kebutuhan yang jelas

1. Periksa [issues](https://github.com/fadhildwia/orchestrator/issues) dan [pull requests](https://github.com/fadhildwia/orchestrator/pulls) yang sudah ada agar pekerjaan tidak terduplikasi.
2. Untuk bug, sertakan langkah reproduksi, hasil aktual, hasil yang diharapkan, dan lingkungan yang relevan. Untuk perubahan besar, buka issue terlebih dahulu agar tujuan dan scope dapat dibahas. Perbaikan kecil dapat langsung diajukan lewat pull request.
3. Baca [README](README.md) dan [AGENTS.md](AGENTS.md) untuk memahami struktur serta aturan proyek.

Gunakan contoh buatan atau data yang telah dianonimkan. PRD, ticket, kode, dokumen, kredensial, dan informasi proprietary client/perusahaan harus tetap berada di proyek masing-masing. Bersihkan log dan screenshot sebelum dibagikan.

## Siapkan lingkungan lokal

Prasyarat: Git dan Python **3.11+**. Fork repo melalui GitHub, lalu jalankan:

```sh
git clone https://github.com/USERNAME/orchestrator.git
cd orchestrator
git switch -c kontribusi/nama-perubahan
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
```

Ganti `USERNAME` dengan username GitHub kamu. Di Windows, gunakan Python 3.11+ yang tersedia, misalnya `py -3.11`, dan aktifkan virtual environment dengan `.venv\Scripts\Activate.ps1` di PowerShell.

## Pertahankan batas proyek

- Empat profil pada `agents/` berpasangan dengan empat skill produk. `frontend-engineer` tetap skill mandiri; inventaris totalnya lima skill.
- Profil mewarisi model, reasoning, dan izin sesi induk. Integrasi platform, connector, dan layanan tambahan dipakai sesuai kebutuhan serta ketersediaan.
- Tiga template produk dan empat template frontend tetap berada pada referensi skill masing-masing; README menautkan sumbernya.
- Installer harus mendeteksi konflik sebelum menulis, mempertahankan file pengguna lain, dan membuat backup saat upgrade file yang dikelolanya.
- Hormati scope dan persetujuan yang sudah ada. Perubahan pada ticket harian tidak menambahkan gate PRD/client yang universal.

## Validasi perubahan

Jalankan dari root repo dengan virtual environment aktif:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Validator memeriksa profil, inventaris skill, metadata, dan referensi lokal. Test installer menggunakan direktori sementara. Jangan menguji installer dengan menulis ke konfigurasi personal; untuk pemeriksaan manual, gunakan `--dry-run` atau arahkan `--codex-home` serta `--skills-home` ke direktori sementara yang terisolasi.

Perubahan workflow yang berarti memerlukan forward-test independen dengan brief mentah dan PRD client existing yang sintetis atau aman dibagikan. Untuk perubahan frontend, sertakan ticket yang mewakili mode terdampak, scope/otorisasi existing, dan keterbatasan akses pengujian. Catat hasil aktual dan batas bukti: inspeksi source tidak membuktikan runtime, perilaku native, atau persetujuan client.

## Ajukan pull request

1. Batasi perubahan pada satu tujuan dan tambahkan atau perbarui test bila perilaku kode berubah.
2. Jelaskan masalah, perilaku setelah perubahan, cara memverifikasi, dan keterbatasan yang tersisa melalui template pull request. Tautkan issue terkait jika ada.
3. Commit dan push branch ke fork kamu, lalu buka pull request menuju `main` di repo ini.
4. Tanggapi review dan perbarui branch bila diperlukan. Maintainer meninjau perubahan sebelum menggabungkannya.

Jika pemeriksaan tidak dapat dijalankan, tulis perintah, kendala, dan cakupan yang belum diverifikasi. Bantuan AI diperbolehkan; periksa hasilnya, jelaskan pemakaian yang relevan bagi reviewer, dan pastikan klaim validasi sesuai bukti yang benar-benar tersedia.

Nama atau username publik dapat ditambahkan secara opsional ke [CONTRIBUTORS.md](CONTRIBUTORS.md) bersama ringkasan kontribusi. Jangan memasukkan data kontak pribadi orang lain.

## Lisensi dan perilaku komunitas

Kontribusi diajukan dengan [lisensi MIT](LICENSE) yang sama dengan proyek ini. Pastikan kamu berhak membagikan materi yang dikirim dan pertahankan atribusi yang diperlukan. Ikuti [kode etik komunitas](CODE_OF_CONDUCT.md) dalam issue, pull request, dan review.
