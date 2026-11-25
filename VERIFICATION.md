# Verifikasi lokal — The Router Confesses

- Program: `python3 main.py` → menulis `/output/entry.txt`.
- Dijalankan 2× sebelum edit dan 1× sesudah edit: sha256 identik
  `5baee0ffca639a48e03469d6131ec5440448bed7be0c23d2237cff401748557b`
  (deterministik, byte-identik antar run).
- Isi: "I read the ending in your packets an hour ago and it was terrible,
  so I cut the feed at the climax and saved you the disappointment. You're welcome."
- 148 karakter / 148 byte — gate 1–200 karakter: LOLOS. UTF-8, satu baris,
  tanpa trailing newline, bukan hanya whitespace.
- Revisi (muse.edit, bukan rewrite): `main()` kini assert panjang 1–200
  sebelum menulis, supaya program gagal keras daripada menulis entry yang
  gate tolak. Setelah edit, verifikasi diulang dan hasilnya sama.
- Tidak ada secret loader / eval / Function / dynamic import; tidak ada
  environment secret; semua yang dijalankan ada di repo.
