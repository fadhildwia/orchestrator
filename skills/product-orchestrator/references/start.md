# Template prompt workflow

Pakai skill `product-orchestrator` pada chat utama di proyek yang sedang dikerjakan. Profil custom `product_orchestrator` juga tersedia untuk penugasan koordinasi yang didelegasikan; membuat profil tidak otomatis mengganti peran chat utama.

## Pilih titik masuk

- [Brief baru](templates/brief-baru.md): untuk kebutuhan mentah yang perlu diriset dan disusun menjadi PRD, lalu desain siap review client.
- [PRD dari client](templates/prd-client.md): untuk meninjau kebutuhan existing, meneliti gap yang relevan, dan melanjutkan desain dalam scope yang diotorisasi.
- [Lanjut development](templates/lanjut-development.md): untuk implementasi setelah persetujuan PRD/desain tersedia, dilanjutkan functional QA dan persiapan UAT.

Salin blok prompt ke chat proyek tujuan, lalu isi konteks dan lokasi sumbernya. Tandai informasi yang belum tersedia sebagai “belum ditentukan”. Dua template awal berhenti pada desain siap review client; lanjutkan dengan template development setelah persetujuan yang relevan tersedia. Pekerjaan berikutnya dapat diteruskan pada chat yang sama.

Template disimpan bersama referensi skill agar ikut terbawa saat pemasangan atau update personal. PRD, desain, dan hasil kerja client tetap berada pada proyek masing-masing.

## Memanggil satu specialist

- `$critical-product-research`: minta jawaban atas pertanyaan produk beserta sumber dan ketidakpastiannya.
- `$product-ui-ux`: berikan brief/PRD, platform, batas scope, dan hasil desain yang diperlukan.
- `$product-review-qa`: sebutkan mode PRD, desain, functional QA, atau retest; sertakan baseline, artefak dan akses pengujian yang tersedia.

Jelaskan lokasi proyek dan sumbernya. Tool, connector, model, serta izin mengikuti sesi tempat workflow dipakai. Profil agent dan skill tidak membuat akses ke Figma, browser, backend, simulator, atau perangkat menjadi tersedia secara otomatis.
