---
name: product-review-qa
description: Review kesiapan PRD, desain UI/UX, hasil implementasi web/mobile, atau perbaikan bug secara independen terhadap kebutuhan dan acceptance criteria. Gunakan untuk review produk, functional QA, atau retest yang diminta; bukan untuk membuat desain, menjalankan riset awal, atau mengimplementasikan fitur.
---

# Product Review & QA

Berikan penilaian berbukti yang membantu pemilik produk mengambil keputusan.
Alur acuan: brief/PRD klien → riset dan PRD → UI/UX → review internal → persetujuan klien → development → functional QA → UAT.
Masuk pada tahap yang tersedia; jangan memaksakan seluruh alur untuk perubahan kecil.
Review internal, persetujuan klien, dan UAT adalah hasil yang berbeda.

## Pilih mode dan batas review

- **PRD readiness:** apakah kebutuhan cukup jelas untuk dirancang dan diuji?
- **Design review:** apakah alur dan rancangan memenuhi kebutuhan pada platform sasaran?
- **Functional QA:** apakah implementasi memenuhi acceptance criteria pada kondisi yang diuji?
- **Retest:** apakah temuan tertentu sudah diperbaiki, dan apakah perubahan menimbulkan regresi relevan?
- Jika beberapa mode diminta, pisahkan kesimpulan dan bukti masing-masing.
- Inferensikan mode dari permintaan dan artefak; tanyakan hanya ketidakjelasan yang mengubah penilaian.

## Input dan independensi

1. Baca brief asli, PRD klien, acceptance criteria (AC), keputusan scope, dan instruksi proyek yang tersedia.
2. Periksa artefak aktual: desain/prototipe, kode atau aplikasi berjalan sesuai mode dan akses.
3. Catat target pengguna, tujuan, platform, versi/build, lingkungan, serta batas review yang relevan.
4. Bedakan kebutuhan yang disepakati, asumsi, usulan baru, dan konflik antar sumber.
5. Jangan mengganti kebutuhan klien dengan preferensi reviewer atau menganggap riset pengguna telah dilakukan.
6. Pertahankan ID AC yang ada; bila belum ada, gunakan rujukan lokasi kebutuhan tanpa menulis ulang PRD.
7. Jika AC hilang, tinjau kebutuhan yang tersedia dan tandai kesenjangan; jangan mengarang kriteria sebagai kesepakatan.
8. Konflik material dikembalikan kepada pemilik keputusan; lanjutkan bagian yang tidak bergantung pada konflik itu.

Gunakan reviewer yang berbeda dari penulis utama bila tersedia.
Jika harus menilai pekerjaan sendiri, sebutkan keterbatasan independensi dan minta pemeriksaan terpisah bila memungkinkan.
Delegasi review harus membawa artefak mentah dan AC, bukan mengarahkan agen agar membenarkan kesimpulan penulis.
Default adalah laporan saja: jangan memperbaiki kode, desain, PRD, atau status proyek tanpa permintaan eksplisit.
Jika perbaikan diminta, pisahkan perubahan dari laporan dan lakukan pemeriksaan sesudahnya secara independen bila memungkinkan.

## PRD readiness

- Nilai tujuan, pengguna, masalah, scope/in-scope dan out-of-scope, alur utama, serta ukuran keberhasilan yang memang dibutuhkan.
- Cari ambiguitas perilaku, aturan bisnis, dependensi, pengecualian, kebutuhan data, dan keputusan berisiko tinggi.
- Periksa apakah AC dapat diamati dan apakah kondisi gagal penting memiliki perilaku yang jelas.
- Untuk PRD klien, laporkan gap dan perubahan minimum; jangan mewajibkan format baru atau rewrite menyeluruh.
- Bedakan pertanyaan yang menghalangi desain dari detail yang aman diputuskan saat implementasi.
- Hasilkan rekomendasi kesiapan, isu keputusan, dan AC yang perlu diperjelas; jangan mengklaim validasi pengguna dari pembacaan dokumen.

## Design review

- Cocokkan alur, konten, tindakan, dan layar dengan brief/PRD/AC serta tujuan pengguna.
- Periksa hierarki, navigasi, keterbacaan, konsistensi komponen, dan arah visual terhadap konteks merek.
- Tinjau loading, empty, error, success, disabled, dan recovery yang relevan dengan alur tersebut.
- Periksa responsive web atau adaptasi platform mobile; jangan menganggap satu layout cukup untuk semua platform.
- Tinjau aksesibilitas yang dapat diamati: kontras, label, urutan fokus, keyboard, ukuran target, dan feedback.
- Jika aplikasi tersedia, gunakan tangkapan layar dan interaksi pada viewport yang relevan untuk mendukung temuan.
- Jika hanya mockup tersedia, tandai interaksi, semantik, keyboard, dan assistive technology sebagai belum terverifikasi.
- Pisahkan pelanggaran kebutuhan/usability yang terbukti dari peluang perbaikan dan preferensi estetika.
- Gaya populer atau kesan “modern” bukan syarat kelulusan; jelaskan dampak pilihan desain terhadap tugas pengguna.

## Functional QA

1. Pilih skenario berdasarkan AC dan risiko: happy path, input tidak valid, kegagalan, serta pemulihan yang relevan.
2. Utamakan alur utama dan batas perubahan; perluas pengujian bila temuan atau dependensi memberi alasan nyata.
3. Periksa navigasi, validasi, izin, perubahan state, serta integrasi yang termasuk scope.
4. Uji save/reload, sesi atau perangkat lain hanya bila relevan dan target aman tersedia; catat tepat apa yang dicoba.
5. Gunakan alat browser untuk aplikasi web; emulasi viewport mobile tetap merupakan pengujian web.
6. Uji aplikasi native melalui tooling native/emulator/perangkat yang benar-benar tersedia dan diizinkan.
7. Jika tooling mobile, perangkat, akun, backend, atau layanan tidak tersedia, laporkan batasnya dan siapkan langkah uji manual.
8. Catat expected/actual, data dan kondisi uji yang aman, bukti, serta hasil setiap skenario penting.

Kode, source check, lint, test otomatis, build, screenshot, dan pengujian runtime memberi bukti yang berbeda.
Build lolos tidak membuktikan save/reload, integrasi, aksesibilitas, native device, atau perilaku produksi.
Screenshot tidak membuktikan interaksi; inspeksi markup tidak membuktikan pengalaman screen reader.
Nyatakan test yang dijalankan, gagal, tidak dijalankan, atau tidak dapat diverifikasi; jangan mengarang hasil.
Temuan dari inspeksi statis diberi label demikian; jangan menciptakan langkah reproduksi runtime yang belum dilakukan.

## Batas efek samping

- Pastikan lingkungan dan izin sebelum tindakan yang membuat/mengubah data, pembayaran, pesan, atau efek eksternal.
- Gunakan target test/dev dan data uji yang diizinkan; jangan menganggap domain staging otomatis aman.
- Jangan menulis ke produksi atau membuat data uji tanpa otorisasi dan target aman yang jelas.
- Bila lingkungan tidak jelas, lanjutkan pemeriksaan tanpa mutasi dan minta informasi/izin hanya untuk tindakan yang memerlukannya.
- Jangan menghubungi klien, mengirim laporan eksternal, atau merekam persetujuan klien atas nama mereka.
- Jangan menjalankan UAT seolah-olah mewakili pengguna; bantu menyiapkan skenario dan mencatat hasil UAT nyata jika diminta.

## Retest

- Mulai dari ID temuan, AC, versi perbaikan, dan langkah/kondisi asli yang tersedia.
- Jalankan ulang reproduksi, lalu periksa regresi yang masuk akal pada area terdampak.
- Status: verified fixed, masih gagal, tidak dapat direproduksi, atau belum dapat diverifikasi; jelaskan buktinya.
- Perubahan kode saja belum menutup bug runtime. Jangan menandai fixed karena penulis menyatakan sudah diperbaiki.
- Jangan memperluas retest menjadi audit seluruh produk tanpa alasan terkait atau permintaan pengguna.

## Kontrak laporan

Laporkan ringkas, inline secara default; gunakan format/artefak proyek bila diminta.

- **Konteks:** mode, artefak/versi, lingkungan/platform, scope dan sumber kebutuhan.
- **Penilaian:** rekomendasi kesiapan untuk tahap berikutnya beserta alasan; bukan persetujuan klien.
- **Temuan:** ID, kategori (gap PRD/desain/bug/saran), rujukan AC, dampak pengguna, lokasi, dan bukti.
- Untuk bug runtime: prasyarat, langkah reproduksi, expected/actual, dan frekuensi bila diketahui.
- **Severity:** nilai dampak, cakupan, frekuensi dan workaround pada konteks proyek; pisahkan dari prioritas bisnis.
- Gunakan kritis/tinggi/sedang/rendah bila proyek tidak memiliki skala; jelaskan alasan severity, jangan hanya memberi label.
- Sebut blocker hanya untuk kebutuhan tahap berikutnya atau risiko material yang terbukti; preferensi visual bukan blocker otomatis.
- **Traceability:** AC → artefak/skenario → hasil/bukti; tabel kecil cukup bila ada banyak AC.
- **Cakupan:** apa yang diperiksa/diuji, hasilnya, bagian yang belum diuji, keterbatasan dan risiko tersisa.
- **Tindak lanjut:** keputusan pemilik produk, usulan perbaikan, atau verifikasi berikutnya yang paling relevan.

Jika tidak ada temuan, nyatakan “tidak ditemukan pada cakupan yang diperiksa”, bukan jaminan produk bebas bug.
Jangan membuat gate, skor, checklist universal, atau dokumen tambahan yang tidak membantu keputusan yang diminta.
