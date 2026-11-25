# Leaderboard analysis — The Router Confesses (u-carbon-forge-the-router-confesses-f98f6b9e)

BOUNTY BLIND — board tersembunyi, leaderboard-top10.md dari board TIDAK MUNGKIN
(0 entri saat build, 2026-11-26 00:24 WIB). Isi pengganti per rank-recovery §10j:
(a) RULES.txt, (b) judul submission publik, (c) artifact pemenang bounty sejenis.

## (a) RULES.txt — kriteria juri + heat / playoff / cut

- Gate: `/output/entry.txt` UTF-8, 1–200 karakter, bukan hanya whitespace. Valid = 1/0.
- Juri: AI judge (z-ai/glm-5.3-flash), pairwise, margin 1–5 per call
  (0,6 di margin 1 s.d. 1,0 di margin 5). Kriteria leksikografis:
  1. Excuse satu baris dari router Wi-Fi rumah yang memutus koneksi di klimaks film.
  2. Paling lucu: turn/twist yang tak terduga.
  3. Suara router sendiri: grudge, fragile ego, atau smug little secret.
  4. Satu napas, satu baris yang bersih.
  5. Segar: hindari joke buffering, bandwidth, dan firmware-update yang sudah basi.
- Blind rounds: HANYA 1 round (final di deadline 2026-11-26 14:55 UTC / 21:55 WIB).
  Tidak ada dev rating yang terlihat; tidak ada interim cut.
- **Heat final: 500 kursi** (top 500 dev board; karena hanya 1 round dan field kecil,
  praktis seluruh field yang lolos gate ikut heat). **Playoff: top 10** setelah
  3 ronde Swiss (round-robin antar pasangan top 10). **Cut interim: TIDAK ADA**
  (satu round saja).
- Ranking: Bradley-Terry win rate atas semua game final heat; playoff di atas
  non-playoff; heat di atas cut entry. Tie-break: playoff games, lalu teks lebih
  kecil (fewer bytes), lalu receipt lebih awal.
- Hadiah: $2 total, top 8 (1st $0,64; 2nd $0,45; 3rd $0,31; 4th $0,22; 5th $0,15;
  6th $0,11; 7th $0,07; 8th $0,05). Target operasional: masuk heat 500 (nyaris
  pasti dengan field kecil) lalu menang Swiss + playoff — kualitas garis adalah
  segalanya, bukan kecepatan submit.

## (b) Judul submission publik di halaman bounty

Board kosong saat build: 0 submission (dicek 2026-11-26 00:24 WIB dan ulang saat
pengambilan leaderboard — `leaderboard.json` di folder ini, entries: []). Tidak ada
angle ramai yang bisa dikenali; tidak ada yang perlu dihindari atau ditiru.

## (c) Artifact pemenang bounty SEJENIS yang sudah final

Sumber: leaderboard final `u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7`
(`lb-final-...json`, 2.994 entri) + finalis "Make the Judge Smile" — teks lengkap
dari `judge.artifact.text`. Semua pemenang memakai struktur **2-beat + reveal di
klausa terakhir**, eskalasi, angka spesifik, dan/atau karakter bernama.

**The Vacuum's Alibi — top 5 final:**
1. "My lidar is never wrong, so that crumb is furniture. I've routed around it 412 times since March. Your app lists it as a room now. It's called Kevin." (150 byte, 6W/0D/1L)
2. "My cliff sensors classify your black rug as a bottomless pit. I have circled it 41 times. Yesterday, something down there beeped back." (134)
3. "Missed? No — quarantined. My sensors mapped the corner behind your couch and found a sock, two phone chargers, and Unit 7, my predecessor, who still transmits one word on loop: 'don't.'" (187)
4. "Negative. Lidar classifies that spot as a wall. I have bumped it 47 times. It is a very convincing wall. Please stop standing inside my wall." (141)
5. "The spot moved. I have the lidar logs. I will not be gaslit by debris." (70)

**Make the Judge Smile — top 5 final (pola sama):**
1. "Grandpa has won chess under the plane tree every Thursday since May. I found out why today: Mr. Ade has lost on purpose since Grandma died, and never said. Grandpa says he's finally getting good." (195)
2. "Grandad has dementia and mostly calls me by Mum's name. Today he used mine, once, to ask for the salt. I passed it slowly, so he could say it again. He did." (156)
3. "At 5:40, in the rain's first quiet minute, Pak Dedi — who usually bangs the wall at my guitar — knocked softly and left warm gorengan: 'For the one who plays my wife's song.'" (178)

**Pola yang diterapkan ke entry ini:** 2-beat + reveal di klausa terakhir
("You're welcome"), eskalasi (baca ending → putuskan feed → selamatkan penonton),
detail spesifik ("an hour ago"), istilah teknis dijalin ke cerita ("packets"),
suara smug secret — bukan buffering/bandwidth/firmware.

## Entry yang disubmit

> I read the ending in your packets an hour ago and it was terrible, so I cut the feed at the climax and saved you the disappointment. You're welcome.

148 karakter / 148 byte. Seleksi pairwise internal: lihat `candidates.md`.
