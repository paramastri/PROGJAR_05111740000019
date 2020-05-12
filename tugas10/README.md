# Tugas 10
## Performance Test

1. Jalankan async_server.py pada port 9002, 9003, 9004, 9005
2. Jalankan file lb.py, jalankan di port 44444
3. Uji cobalah dengan apache benchmark untuk 1000 request dan konkurensi yang bervariasi
* Jumlah request: 1000
* Konkurensi (bervariasi): 1, 2, 3, 4, 5
4. Bandingkan penggunaan load balancer jika lb.py dijalankan di port seperti tugas9 (45000 dan 46000)

### PORT 44444

| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 | 8.508 seconds | 1000 | 0 | 122000 bytes | 117.54 [#/sec] | 8.508 ms | 14.00 Kbytes/sec |
| 2 | 2 | 1.980 seconds | 1000 | 0 | 122000 bytes | 505.01 [#/sec] | 3.960 ms | 60.17 Kbytes/sec |
| 3 | 3 | 1.788 seconds | 1000 | 0 | 122000 bytes | 559.30 [#/sec] | 5.364 ms | 66.63 Kbytes/sec |
| 4 | 4 | 2.029 seconds | 1000 | 0 | 122000 bytes | 492.86 [#/sec] | 8.116 ms | 58.72 Kbytes/sec |
| 5 | 5 | 1.485 seconds | 1000 | 0 | 122000 bytes | 673.30 [#/sec] | 7.426 ms | 80.22 Kbytes/sec |

### PORT 45000

| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 | 4.514 seconds | 1000 | 0 | 122000 bytes | 221.54 [#/sec] | 4.514 ms | 26.39 Kbytes/sec |
| 2 | 2 | 2.752 seconds | 1000 | 0 | 0 bytes | 363.41 [#/sec] | 5.503 ms | 0.00 Kbytes/sec |
| 3 | 3 | 1.516 seconds | 1000 | 0 | 0 bytes | 659.68 [#/sec] | 4.548 ms | 0.00 Kbytes/sec |
| 4 | 4 | 1.239 seconds | 1000 | 0 | 0 bytes | 806.95 [#/sec] | 4.957 ms | 0.00 Kbytes/sec |
| 5 | 5 | 5.229 seconds | 1000 | 0 | 122000 bytes | 191.24 [#/sec] | 26.145 ms | 22.78 Kbytes/sec |

### PORT 46000

| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 | 4.105 seconds | 1000 | 0 | 122000 bytes | 243.60 [#/sec] | 4.105 ms | 29.02 Kbytes/sec |
| 2 | 2 | 2.760 seconds | 1000 | 0 | 122000 bytes | 362.26 [#/sec] | 5.521 ms | 43.16 Kbytes/sec |
| 3 | 3 | 2.485 seconds | 1000 | 0 | 122000 bytes | 402.40 [#/sec] | 7.455 ms | 47.94 Kbytes/sec |
| 4 | 4 | 2.720 seconds | 1000 | 0 | 122000 bytes | 367.58 [#/sec] | 10.882 ms | 43.79 Kbytes/sec |
| 5 | 5 | 2.089 seconds | 1000 | 0 | 122000 bytes | 478.73 [#/sec] | 10.444 ms | 57.04 Kbytes/sec |

