# Contoh memulai workflow

Pakai skill `product-orchestrator` pada chat utama di proyek yang sedang dikerjakan. Profil custom `product_orchestrator` juga tersedia untuk penugasan koordinasi yang didelegasikan; membuat profil tidak otomatis mengganti peran chat utama.

## Client memberi brief

```text
Gunakan $product-orchestrator sebagai Product Lead untuk proyek ini.
Brief client: [tempelkan brief atau berikan lokasi sumber].
Platform dan batas yang diketahui: [jelaskan bila tersedia].
Gunakan researcher dan reviewer untuk mempertajam kebutuhan, kemudian
susun/perbarui PRD pada sumber aktif proyek. Tampilkan keputusan yang
perlu saya konfirmasi. Setelah scope cukup jelas, lanjutkan desain UX/UI
dan review internal. Siapkan bahan review client sebelum development.
```

## Client sudah memberi PRD

```text
Gunakan $product-orchestrator. PRD client ada di [lokasi].
Status persetujuan dan scope tugas: [jelaskan yang sudah disepakati].
Audit kesiapan PRD, riset gap yang berpengaruh, lalu kerjakan desain dan
review sesuai scope yang sudah diotorisasi. Pertahankan baseline client
dan ajukan perubahan material beserta dampaknya.
```

## Melanjutkan setelah persetujuan

```text
Gunakan $product-orchestrator. Client menyetujui PRD [versi/lokasi] dan
desain [versi/lokasi] untuk scope [rincian]. Lanjutkan development dalam
scope itu dan jalankan reviewer pada mode functional QA ketika hasil
siap diuji. Laporkan bukti pengujian serta bagian yang belum terverifikasi.
```

## Memanggil satu specialist

- `$critical-product-research`: minta jawaban atas pertanyaan produk beserta sumber dan ketidakpastiannya.
- `$product-ui-ux`: berikan brief/PRD, platform, batas scope, dan hasil desain yang diperlukan.
- `$product-review-qa`: sebutkan mode PRD, desain, functional QA, atau retest; sertakan baseline, artefak dan akses pengujian yang tersedia.

Jelaskan lokasi proyek dan sumbernya. Tool, connector, model, serta izin mengikuti sesi tempat workflow dipakai. Profil agent dan skill tidak membuat akses ke Figma, browser, backend, simulator, atau perangkat menjadi tersedia secara otomatis.
