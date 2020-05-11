# Tugas 9
## Performance Test

1. Jalankan kedua model tersebut
* Server_async_http.py di port 45000
* Server_thread_http.py di port 46000

2. Uji cobalah dengan apache benchmark untuk 1000 request dan konkurensi yang bervariasi
* Jumlah request: 1000
* Konkurensi (bervariasi): 1, 2, 3, 4, 5

### Server_async_http (PORT 45000)

| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 | 4.367 seconds | 1000 | 0 | 122000 bytes | 228.98 [#/sec] | 4.367 ms | 27.28 Kbytes/sec |
| 2 | 2 | 1.837 seconds | 1000 | 0 | 122000 bytes | 544.23 [#/sec] | 3.675 ms | 64.84 Kbytes/sec |
| 3 | 3 | 1.780 seconds | 1000 | 0 | 122000 bytes | 561.94 [#/sec] | 5.339 ms | 66.95 Kbytes/sec |
| 4 | 4 | 1.360 seconds | 1000 | 0 | 122000 bytes | 735.43 [#/sec] | 5.439 ms | 87.62 Kbytes/sec |
| 5 | 5 | 1.235 seconds | 1000 | 0 | 122000 bytes | 809.87 [#/sec] | 6.174 ms | 96.49 Kbytes/sec |

### Server_thread_http (PORT 46000)

| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 | 744.548 seconds | 1000 | 0 | 122000 bytes | 1.34 [#/sec] | 744.548 ms | 0.16 Kbytes/sec |
| 2 | 2 | 445.892 seconds | 1000 | 0 | 122000 bytes | 2.24 [#/sec] | 891.783 ms | 0.27 Kbytes/sec |
| 3 | 3 | 382.434 seconds | 1000 | 0 | 122000 bytes | 2.61 [#/sec] | 1147.301 ms | 0.31 Kbytes/sec |
| 4 | 4 | 364.884 seconds | 1000 | 0 | 122000 bytes | 2.74 [#/sec] | 364.884 ms | 0.33 Kbytes/sec |
| 5 | 5 | 379.678 seconds | 1000 | 0 | 122000 bytes | 2.63 [#/sec] | 1898.389 ms | 0.31 Kbytes/sec |
