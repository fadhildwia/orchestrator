# Prompt: lanjut development setelah persetujuan

Gunakan setelah persetujuan PRD, desain, dan scope yang relevan benar-benar tersedia. Isi rujukan persetujuan serta sumber proyek, lalu lanjutkan pada chat yang sama atau berikan konteksnya pada chat baru. Prompt ini memberi mandat development dan QA dalam scope tersebut; deployment mengikuti otorisasi tersendiri.

```text
Gunakan $product-orchestrator untuk melanjutkan proyek ini.
Baca instruksi repo dan keputusan existing terlebih dahulu.

Client sudah menyetujui:
- PRD: [versi/lokasi].
- Desain: [versi/lokasi].
- Scope: [rincian yang disepakati].
Rujukan persetujuan: [pesan, dokumen, atau keputusan client].
Platform: [web responsif / Android / iOS / cross-platform].
Lingkungan QA yang tersedia: [target test/dev, alat, akun/data uji
yang diizinkan, atau tulis belum tersedia].

Lanjutkan development dalam scope tersebut. Hormati persetujuan
yang sudah diberikan dan ajukan perubahan material beserta dampaknya.
Jaga hubungan requirement/AC, desain, implementasi, dan pengujian.

Gunakan reviewer independen pada mode functional QA ketika
implementasi siap diuji. Periksa perilaku terhadap acceptance
criteria dengan alat dan lingkungan yang benar-benar tersedia.
Laporkan hasil pengujian, temuan, dan bagian yang belum
terverifikasi, lalu siapkan skenario UAT untuk client.
```
