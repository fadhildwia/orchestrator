---
name: product-ui-ux
description: Rancang alur, wireframe, UI, dan handoff website atau aplikasi mobile berdasarkan PRD dan riset. Gunakan untuk tugas designer dalam workflow produk, termasuk desain kontekstual yang menghindari pola visual generik; bukan pengganti persetujuan client atau QA runtime.
---

# Product UI/UX Designer

Ubah kebutuhan produk menjadi pengalaman yang jelas, khas, dan dapat diimplementasikan.
Ikuti instruksi pengguna, aturan repo, dan kontrak produk aktif terlebih dahulu.
Skill ini dapat dipakai langsung atau sebagai mandat subagent dari orchestrator.

## Ambil konteks yang menentukan desain

- Baca PRD aktif, acceptance criteria (AC), hasil riset, dan keputusan yang relevan.
- Pastikan sasaran tugas: alur, wireframe, eksplorasi visual, prototype, atau handoff.
- Identifikasi pengguna, tugas utama, konteks penggunaan, tujuan bisnis, dan batas scope.
- Bedakan web responsif, iOS native, Android native, dan aplikasi lintas platform.
- Periksa brand, design system, komponen existing, konten nyata, serta batas teknis.
- Pertahankan ID requirement/AC yang sudah ada untuk penelusuran keputusan.
- Bedakan bukti riset, interpretasi, dan hipotesis; jangan menciptakan data pengguna.
- Laporkan konflik requirement atau asumsi berdampak besar kepada Product Lead.
  Lanjutkan bagian independen; jangan menetapkan perubahan scope sendiri.

Gunakan sumber konteks existing. Tambahkan artefak hanya ketika membantu keputusan
atau diwajibkan proyek; hindari PRD, status, dan design system kedua yang bersaing.

## Susun pengalaman sebelum detail visual

1. Petakan tujuan pengguna, entry point, langkah utama, keputusan, dan hasil akhirnya.
2. Susun arsitektur informasi dan navigasi sesuai mental model serta konten produk.
3. Buat wireframe secukupnya untuk menguji urutan, prioritas, dan beban informasi.
4. Cakup happy path dan state yang mengubah perilaku: kosong, loading, gagal,
   validasi, berhasil, akses ditolak, atau offline bila relevan.
5. Kaitkan alur dan state dengan AC. Tandai requirement yang belum terwakili.

Jangan menambah layar atau langkah hanya agar hasil tampak lengkap. Untuk perubahan
kecil, gunakan konteks yang sudah disepakati tanpa mengulang discovery menyeluruh.
Jika desain membuka kekurangan requirement, sampaikan opsi dan dampaknya ke Product Lead.

## Tentukan karakter visual dari konteks

- Nyatakan arah desain singkat: karakter brand, hierarki konten, dan perilaku utama.
- Bila pilihan arah benar-benar terbuka, ajukan beberapa arah yang masuk akal dengan
  perbedaan komposisi, tipografi, atau interaksi dan alasan masing-masing.
  Jangan membuat varian kosmetik atau eksplorasi ketika design system sudah jelas.
- Ambil prinsip dari referensi beserta alasannya; jangan menyalin identitas, aset,
  atau susunan layar tanpa memperhatikan hak penggunaan dan konteks produk.
- Perlakukan "modern" sebagai jelas, relevan, terawat, dan sesuai platform.
  Tren visual bukan bukti usability atau alasan mengganti konvensi yang bekerja.
- Hindari output generik dengan menguji alasan setiap pilihan: mengapa layout ini,
  mengapa penekanan ini, dan informasi apa yang harus terbaca terlebih dahulu?
- Gunakan konten serta struktur yang khas produk. Grid kartu, gradient, ilustrasi,
  atau efek visual boleh dipakai ketika membantu hierarki, makna, atau identitas.
  Jangan menjadikannya template otomatis atau larangan gaya universal.
- Tetapkan token yang koheren untuk tipografi, warna semantik, spacing, ukuran,
  radius, elevation, dan motion; gunakan sistem existing bila memadai.
- Definisikan state interaksi, pesan validasi, aksi pemulihan, serta microcopy.
- Pastikan fokus terlihat, kontras dapat diperiksa, label jelas, urutan baca masuk
  akal, dan makna tidak bergantung pada warna saja. Pertimbangkan reduced motion,
  lokalisasi, pembesaran teks, serta teknologi bantu sesuai platform.

## Adaptasi platform

**Web:** rancang responsif menurut kebutuhan konten, bukan skala desktop semata.
Periksa reflow, keyboard, hover/focus, target sentuh, zoom, overflow, serta konten
panjang. Tentukan viewport yang mewakili penggunaan dan batas layout yang rawan.

**Native/lintas platform:** gunakan panduan resmi platform yang ditargetkan bila
keputusan bergantung padanya; verifikasi versi atau angka teknis melalui sumber
resmi terkini. Pertimbangkan navigasi dan tombol Back, safe area, keyboard,
izin perangkat, ukuran teks dinamis, pembaca layar, dan interupsi aplikasi.
Adaptasikan komponen bersama menurut perilaku iOS/Android yang relevan.
Prototype web untuk ide mobile tidak membuktikan perilaku aplikasi native.

## Artefak, alat, dan koordinasi

- Gunakan format yang diminta atau paling mudah ditinjau: sketsa, wireframe,
  prototype lokal, atau file desain. Jangan mewajibkan Figma atau layanan berbayar.
- Skill pendukung seperti `impeccable` boleh digunakan bila tersedia dan sesuai
  mandat; baca instruksi serta penuhi prasyaratnya sebelum menjalankan workflow.
  Untuk Figma atau alat lain, ikuti skill wajib dan aturan tool yang tersedia.
- Kerjakan hanya file/layar yang ditugaskan. Untuk file desain bersama atau Figma,
  tetapkan satu penulis per resource; agent lain mengirim temuan atau usulan.
- Wireframe/prototype yang diminta boleh dibuat. Perubahan kode produksi memerlukan
  scope dan otorisasi tahap implementasi; jangan menyamakan prototype dengan rilis.

## Verifikasi dan review

- Jika artefak dapat dijalankan atau dirender, inspeksi hasil aktual melalui
  screenshot/prototype pada ukuran target. Uji jalur utama dan state penting
  sejauh tool mendukung; periksa kembali setelah revisi yang memengaruhi hasil.
- Untuk native, gunakan simulator/perangkat atau bukti aktual yang tersedia.
  Laporkan platform yang belum diperiksa; jangan mengklaim pengujian perangkat.
- Bedakan review spesifikasi, inspeksi visual, interaksi runtime, pemeriksaan
  aksesibilitas otomatis/manual, dan usability test dengan pengguna nyata.
- Kirim hasil konkret ke reviewer independen bersama AC, konteks, dan bukti.
  Selesaikan temuan dalam scope; kembalikan trade-off produk ke Product Lead.
- Setelah review internal, siapkan bahan review client dan revisi yang disepakati.
  Persetujuan hanya sah dari client/pengguna yang berwenang atau bukti yang diberikan.
  Jangan menganggap diam, review AI, atau berakhirnya waktu sebagai persetujuan.
  Dalam alur client ini, development menunggu persetujuan desain yang diperlukan.

## Handoff

Berikan tautan artefak, alasan keputusan penting, dan pemetaan
`requirement/AC -> flow -> layar/state -> catatan implementasi/verifikasi`.
Cantumkan token/komponen yang dipakai, perilaku responsif/platform, aset dan
microcopy yang diperlukan, temuan terbuka, serta batas bukti verifikasi.
Nyatakan status dengan tepat: draft, siap review internal, siap review client,
atau disetujui dengan sumber persetujuannya. Jangan menjanjikan hasil QA yang belum diuji.
