# Tugas 10
## Performance Test

1. Jalankan async_server.py pada port 9002, 9003, 9004, 9005
2. Jalankan file lb.py, jalankan di port 44444
3. Uji cobalah dengan apache benchmark untuk 1000 request dan konkurensi yang bervariasi
* Jumlah request: 1000
* Konkurensi (bervariasi): 1, 2, 3, 4, 5
4. Bandingkan penggunaan load balancer jika dijalankan di port seperti tugas9 (45000 dan 46000)

### PORT 44444

| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 3 | 3 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 2 | 2 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 4 | 4 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 5 | 5 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |

### PORT 45000

| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 3 | 3 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 2 | 2 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 4 | 4 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 5 | 5 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |

### PORT 46000

| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 3 | 3 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 2 | 2 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 4 | 4 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 5 | 5 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |

