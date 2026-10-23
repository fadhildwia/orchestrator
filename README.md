# Product workflow untuk Codex

Setup personal untuk website dan mobile apps: orchestrator sebagai Product Lead/pemilik PRD, researcher kritis, UI/UX designer, dan reviewer/QA independen. Sumber konfigurasi disimpan di repo ini; pemasangan personal membuatnya dapat digunakan dari proyek lain.

## Peran dan skill

| Profil agent | Skill | Tanggung jawab |
| --- | --- | --- |
| `product_orchestrator` | [`product-orchestrator`](skills/product-orchestrator/SKILL.md) | Brief, sintesis riset, PRD, scope, delegasi dan handoff |
| `product_researcher` | [`critical-product-research`](skills/critical-product-research/SKILL.md) | Bukti, kontra-bukti, asumsi dan implikasi keputusan |
| `product_designer` | [`product-ui-ux`](skills/product-ui-ux/SKILL.md) | Flow, wireframe, arah visual, states dan adaptasi platform |
| `product_reviewer` | [`product-review-qa`](skills/product-review-qa/SKILL.md) | Kesiapan PRD, review desain, functional QA dan retest |

Skill memuat workflow. Profil TOML memberi mandat peran dan meminta agent membaca skill pasangannya. Semua profil mengikuti model, reasoning, izin dan tool sesi induk; setup ini tidak menetapkan model atau menambah akses layanan.

## Alur

```mermaid
flowchart TD
    A[Brief client] --> B[Klarifikasi dan riset terarah]
    B --> C[Susun PRD]
    D[PRD dari client] --> E[Audit gap dan klarifikasi]
    C --> F[Review PRD dan kesepakatan scope]
    E --> F
    F --> G[UX flow lalu wireframe dan UI]
    G --> H[Review internal dan revisi]
    H --> I[Review dan persetujuan client]
    I --> J[Development]
    J --> K[Functional QA dan UAT client]
```

Masuk pada tahap yang sesuai artefak dan persetujuan yang sudah ada. Riset dan audit independen dapat paralel; desain dapat mengungkap pertanyaan requirement baru. Perubahan material kembali ke Product Lead dan dicatat pada sumber aktif proyek. Reviewer internal memberikan rekomendasi; penerimaan client dicatat dari keputusan client yang nyata.

## Pasang personal

Prasyarat: Python **3.11+** dan Codex yang mendukung skill/custom agents. Installer memakai standard library; PyYAML hanya diperlukan untuk validasi pengembangan repo.

Jalankan dari checkout repo:

```sh
python3 scripts/install.py --dry-run
python3 scripts/install.py --apply
```

Di Windows, gunakan interpreter Python 3.11+ yang tersedia, misalnya `py -3.11` sebagai pengganti `python3`.

Default tujuan mengikuti `CODEX_HOME` jika disetel, atau `~/.codex`:

- Empat profil di `agents/`.
- Empat skill beserta referensinya di `skills/`.
- Manifest kepemilikan file dan backup upgrade di `product-workflow/`.

Untuk memakai direktori skill personal lain yang ditemukan Codex, misalnya `~/.agents/skills`, berikan `--skills-home`. `--codex-home` dapat dipakai untuk instalasi terisolasi. Simpan pilihan lokasi yang sama ketika memperbarui.

Installer memeriksa semua konflik sebelum menulis, mempertahankan file lain, dan tidak mengubah `config.toml` atau `AGENTS.md` personal/proyek. File dengan isi identik dibiarkan. Upgrade file yang sebelumnya dipasang hanya dilakukan ketika hash-nya masih sesuai manifest, dengan backup versi sebelumnya. Edit lokal yang berbeda akan dilaporkan sebagai konflik untuk direkonsiliasi.

Pembaruan: perbarui checkout sumber, periksa perubahan, lalu jalankan dry-run dan apply kembali. Edit sumber di repo sebagai tempat pemeliharaan; salinan personal adalah hasil pemasangan.

## Mulai di chat proyek

Di chat utama proyek tujuan, panggil skill orchestrator:

```text
Gunakan $product-orchestrator sebagai Product Lead untuk proyek ini.
Brief client ada di [lokasi atau tempelkan brief].
Platform: [web responsif / iOS / Android / cross-platform].
Kerjakan riset, PRD, dan desain sesuai flow, gunakan reviewer independen,
lalu siapkan bahan review client sebelum development.
```

Jika client sudah memberi PRD:

```text
Gunakan $product-orchestrator. PRD client ada di [lokasi].
Status persetujuan dan scope tugas: [jelaskan].
Audit gap yang relevan, pertahankan baseline, dan lanjutkan tahap yang
sudah diotorisasi. Ajukan perubahan material beserta dampaknya.
```

Profil `product_orchestrator` digunakan ketika koordinasi itu sendiri didelegasikan; membuat profil tidak otomatis mengubah chat utama menjadi orchestrator. Skill pada chat utama yang mengaktifkan workflow. Pemilihan profil custom bergantung pada client/tool; skill juga memberi fallback delegasi dengan mandat peran yang sama.

Contoh lanjutan dan pemanggilan specialist ada di [referensi penggunaan](skills/product-orchestrator/references/start.md). Jika skill/profil belum muncul, mulai chat baru atau restart Codex lalu periksa kembali. Jangan menganggap file terpasang sebagai bukti bahwa setiap client telah memuatnya.

## Cara menilai hasil

- Researcher membedakan fakta, pernyataan client, interpretasi, hipotesis dan gap. Riset internet tidak menggantikan data pengguna.
- Designer mendasarkan arah visual pada pengguna, konten, brand dan platform. Modern/anti-slop dinilai lewat keputusan yang kontekstual, tanpa larangan gaya universal. Skill desain proyek yang wajib tetap berlaku; `impeccable` dapat digunakan bila tersedia, sesuai scope, dan prasyaratnya dipenuhi.
- Reviewer memberi bukti dan cakupan aktual. Build atau screenshot web tidak membuktikan interaksi native, save/reload, screen reader, atau pengalaman pengguna nyata.
- PRD, hasil riset dan keputusan tetap tinggal pada sumber aktif proyek. Setup personal ini tidak mengumpulkan dokumen client ke repo konfigurasi.
- Integrasi Figma/browser/backend/simulator/perangkat digunakan hanya bila tersedia dan diotorisasi. Setup ini tidak menghubungi client atau mempublikasikan hasil secara otomatis.

## Validasi pengembangan setup

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Validator memeriksa TOML, frontmatter/metadata YAML, pasangan profil-skill, dan referensi lokal. Test installer berjalan dalam direktori sementara; tidak menulis konfigurasi personal. Pemeriksaan perilaku skill tetap memerlukan contoh tugas nyata dan review independen.

Format mengikuti dokumentasi resmi [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) dan [Build skills](https://learn.chatgpt.com/docs/build-skills). Kapabilitas dapat berbeda antar client/versi Codex.
