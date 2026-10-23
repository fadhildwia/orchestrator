# Panduan PRD yang proporsional

Gunakan dokumen client atau PRD aktif proyek sebagai baseline. Pilih bagian yang relevan; fitur kecil tidak memerlukan seluruh struktur berikut. Jika lokasi/template sudah ditetapkan proyek, ikuti itu.

## Isi yang membantu keputusan

- **Konteks dan tujuan:** masalah, pengguna/aktor, tugas yang ingin diselesaikan, dan hasil bisnis yang dicari.
- **Dasar kebutuhan:** sumber brief, data pengguna yang memang tersedia, riset pendukung, asumsi, dan gap bukti.
- **Scope:** fitur yang termasuk, batas scope, prioritas beserta alasannya, serta dependency.
- **Platform:** web/native/cross-platform yang disepakati, konteks perangkat, batas teknis dan integrasi yang relevan.
- **Alur dan aturan:** perjalanan utama, hak akses, aturan bisnis, data/input/output, kondisi gagal dan pemulihan.
- **Requirement dan AC:** identitas stabil jika pekerjaan membutuhkannya, perilaku yang dapat diamati, dan hubungan ke tujuan.
- **Kualitas:** kebutuhan aksesibilitas, responsivitas, konektivitas, performa, privasi atau keamanan hanya pada kedalaman yang relevan.
- **Keputusan terbuka:** pertanyaan, penanggung jawab keputusan, dampak pada scope, dan bagian yang tetap dapat dikerjakan.
- **Persetujuan/perubahan:** versi atau tanggal baseline bila berguna, keputusan pengguna/client yang benar-benar diberikan, dan dampak perubahan material.

## Menulis AC

Nyatakan pemicu/kondisi, perilaku yang diharapkan, dan hasil yang dapat diperiksa. Tambahkan skenario negatif ketika risikonya relevan. Gunakan metrik numerik jika ada dasar atau target yang disepakati; usulan angka tetap berlabel usulan.

Contoh requirement booking:

- `REQ-BOOK-01`: Pengguna dapat memilih slot yang tersedia dan membuat booking.
- `AC-BOOK-01`: Ketika slot masih tersedia dan input wajib valid, konfirmasi menampilkan identitas booking dan waktu yang dipilih.
- `AC-BOOK-02`: Bila slot telah diambil sebelum konfirmasi, aplikasi menjelaskan konflik dan memungkinkan pengguna memilih slot lain tanpa kehilangan input yang masih relevan.

Offline booking membutuhkan keputusan produk/arsitektur: apakah pengguna hanya dapat menyusun permintaan, apakah slot bisa dijamin, bagaimana sinkronisasi, dan bagaimana konflik diselesaikan. Jangan mengasumsikan booking terkonfirmasi ketika server belum memvalidasi ketersediaan.

## Meninjau PRD dari client

Kembalikan rujukan requirement, gap atau konflik, dampak, pertanyaan/usulan perubahan, dan bagian yang dapat dilanjutkan. Pertahankan bagian yang sudah memadai. Bedakan hal yang menghalangi keputusan berikutnya dengan detail yang dapat dipastikan kemudian.

## Handoff desain/development

Berikan baseline yang sama kepada specialist: tujuan, aktor, alur, AC, bukti penting, batas scope/platform, keputusan terbuka dan status otorisasi. Hubungkan perubahan desain atau hasil test ke requirement yang relevan tanpa membuat salinan PRD yang saling berbeda.
