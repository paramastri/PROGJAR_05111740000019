# Tugas 9
## Performance Test

* Jumlah request: 1000
* Konkurensi: 10, 50, 100

### Server_async_http (PORT 45000)

| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 10 |  seconds | 10 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 2 | 50 |  seconds | 10 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 3 | 100 |  seconds | 10 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |

### Server_thread_http (PORT 46000)

| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 10 |  seconds | 10 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 2 | 50 |  seconds | 10 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
| 3 | 100 |  seconds | 10 | 0 |  bytes |  [#/sec] |  ms |  Kbytes/sec |
