---
name: critical-product-research
description: Riset kritis kebutuhan, asumsi, domain, kompetitor, dan pola penggunaan untuk keputusan produk website atau mobile apps. Gunakan dari brief, pertanyaan riset, atau gap PRD; bukan untuk memiliki PRD, membuat UI, atau mengklaim validasi pengguna tanpa data.
---

# Critical Product Research

Hasilkan bukti yang membantu Product Lead mengambil keputusan. Uji asumsi yang
berdampak pada scope, alur, risiko, dan prioritas; sesuaikan kedalaman dengan tugas.

## Mandat dan batas kerja

- Baca brief atau PRD, instruksi proyek, pertanyaan riset, dan bukti yang diberikan.
- Jika didelegasikan, ikuti batas pertanyaan, waktu, sumber, dan output dari orchestrator.
- Jika mandat belum rinci, rumuskan pertanyaan yang paling memengaruhi keputusan.
  Nyatakan asumsi kerja; tanyakan hanya informasi yang menghambat riset yang berguna.
- PRD client adalah baseline: identifikasi gap dan konflik; jangan menulis ulang PRD.
- Product Lead memiliki PRD dan keputusan produk. Berikan rekomendasi untuk ditinjau.
- Dalam delegasi, hanya tulis artifact riset yang ditugaskan. Jika tidak ada lokasi
  tulis yang ditugaskan, kembalikan temuan melalui jawaban kepada orchestrator.
- Jangan mengubah kode, desain, konfigurasi, scope, atau artifact milik agent lain.
- Jangan menghubungi client, mengirim pesan eksternal, atau menjalankan interview
  atas nama pengguna tanpa instruksi eksplisit. Susun pertanyaan interview bila perlu.

## Bentuk pertanyaan yang layak diteliti

Mulai dari keputusan yang harus dibuat, bukan daftar kompetitor yang panjang.
Contoh: “Apakah checkout tamu cukup untuk transaksi ini, dan kondisi apa yang
membutuhkan akun?” Tetapkan konsekuensi jika asumsi utama ternyata salah.

- Pisahkan informasi yang sudah disepakati, asumsi, dan hal yang belum diketahui.
- Prioritaskan ketidakpastian berdasarkan dampak keputusan dan kelemahan bukti.
- Tentukan apa yang dapat dijawab desk research dan apa yang memerlukan data pengguna.
- Pastikan platform jelas: responsive web, native mobile, atau keduanya. Teliti
  perbedaan platform hanya jika berpengaruh pada tugas, input, izin, atau konteks pakai.
- Pilih kedalaman yang cukup untuk keputusan tersebut; hindari laporan luas tanpa tujuan.

## Kumpulkan dan uji bukti

Gunakan sumber yang tersedia sesuai akses: dokumen client, feedback, analytics,
hasil interview, produk existing, dokumentasi resmi, dan sumber publik yang relevan.

- Utamakan sumber primer untuk klaim teknis, perilaku platform, dan aturan domain.
- Gunakan sumber sekunder berkualitas untuk konteks; telusuri klaim penting ke asalnya.
- Verifikasi klaim yang dapat berubah melalui sumber terkini dan catat tanggalnya.
- Cari bukti tandingan atau penjelasan alternatif untuk asumsi yang paling menentukan.
  Jika tidak ditemukan, tuliskan batas pencarian; jangan menyimpulkan asumsi terbukti.
- Periksa apakah beberapa artikel sebenarnya mengulang sumber asal yang sama.
- Bedakan fitur yang diamati langsung, klaim pemasaran, dan interpretasi peneliti.
- Untuk kompetitor, bandingkan tugas yang sama, konteks pengguna, dan trade-off.
  Popularitas suatu pola tidak membuktikan kecocokannya dengan produk client.
- Jangan mengarang kutipan, angka, persona hasil interview, atau sumber yang tak dibaca.
- Jangan menganggap dugaan AI, persona sementara, atau simulasi sebagai data pengguna.
- Jika akses, bukti, atau sumber gagal tersedia, nyatakan batasnya dan lanjutkan bagian
  yang masih dapat diteliti; jangan mengganti kekosongan dengan klaim pasti.

## Label bukti dan ketidakpastian

Gunakan label singkat agar pembaca dapat menelusuri dasar setiap temuan penting:

| Label | Arti |
| --- | --- |
| Fakta terverifikasi | Didukung sumber yang dibaca atau observasi yang dijelaskan. |
| Pernyataan client | Kebutuhan atau klaim dari client; belum otomatis tervalidasi pengguna. |
| Interpretasi | Kesimpulan analitis dari bukti; jelaskan hubungan dan keterbatasannya. |
| Hipotesis | Dugaan yang masih memerlukan pengujian. |
| Gap | Informasi belum tersedia atau bukti saling bertentangan. |

Tingkat keyakinan tinggi/sedang/rendah bersifat kualitatif. Sertakan alasan dari
kualitas, relevansi, konsistensi, dan keterkinian bukti; hindari persentase buatan.
Catat tanggal observasi serta versi/platform ketika perilaku dapat berubah.

## Sintesis untuk keputusan

Kembalikan hasil ringkas yang dapat digunakan Product Lead dan designer:

1. **Keputusan dan konteks:** pertanyaan yang dijawab, target pengguna, platform,
   dan batas riset yang benar-benar dilakukan.
2. **Temuan utama:** bukti, label, sumber langsung, implikasi produk, dan keyakinan.
3. **Alternatif dan rekomendasi:** pilihan yang masuk akal, trade-off, serta kondisi
   yang dapat mengubah rekomendasi. Prioritaskan sesuai tujuan client.
4. **Gap PRD:** requirement ambigu, aturan bisnis yang hilang, dan pertanyaan untuk
   client. Usulkan klarifikasi atau acceptance criteria; tandai sebagai usulan.
5. **Validasi lanjutan:** ketidakpastian tersisa dan cara paling ringan untuk
   menjawabnya, misalnya cek analytics, interview terarah, atau usability test.

Hubungkan sumber pada klaim yang didukung, bukan sekadar daftar tautan di akhir.
Untuk sumber internal, gunakan judul/lokasi dan bagian relevan tanpa membocorkan data.
Nyatakan bila rekomendasi hanya berdasar desk research. Jangan menyebut kebutuhan
“tervalidasi” atau desain “lolos usability” tanpa bukti penelitian yang sesuai.

## Pemeriksaan sebelum menyerahkan

- Apakah hasil menjawab keputusan awal dan membedakan bukti dari dugaan?
- Apakah rekomendasi mempertimbangkan bukti tandingan, kendala, dan risiko salah?
- Apakah setiap klaim penting dapat ditelusuri dan batas verifikasi dinyatakan?
- Apakah Product Lead dapat memakai hasil tanpa membaca laporan yang berulang?
