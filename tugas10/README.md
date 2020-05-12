# Tugas 10
## Performance Test

1. Jalankan async_server.py pada port 9002, 9003, 9004, 9005

2. Uji cobalah dengan apache benchmark untuk 1000 request dan konkurensi yang bervariasi
* Jumlah request: 1000
* Konkurensi (bervariasi): 1, 2, 3, 4, 5

### async_server (PORT 9002)

| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 3 | 3 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 2 | 2 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 4 | 4 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 5 | 5 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |

### async_server (PORT 9003)

| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 3 | 3 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 2 | 2 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 4 | 4 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 5 | 5 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |

### async_server (PORT 9004)

| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 3 | 3 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 2 | 2 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 4 | 4 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 5 | 5 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |

### async_server (PORT 9005)

| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 3 | 3 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 2 | 2 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 4 | 4 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 5 | 5 |  seconds | 1000 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |

