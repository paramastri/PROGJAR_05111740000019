# Tugas 4
## Rancangan Protokol Upload, Download, Lihat List File

* Ketentuan membaca format

format: COMMAND ((spasi)) PARAMETER

* Fitur

1. meletakkan file (upload)
2. mengambil file (download)
3. melihat list file (lihat)

* Request Command & Response

1. UPLOAD

upload : untuk meletakkan/mengunggah file ke data
request : upload
parameter : nama_file yang ingin di upload
response : 
- berhasil mengupload -> 'File berhasil diupload.'
- gagal mengupload -> error

2. LIHAT LIST

lihat : untuk melihat daftar file yang ada di server
request: lihat
parameter: tidak ada
response: daftar file yang ada di server

3. DOWNLOAD

download : untuk mengambil/mengunduh file
request: download
parameter: nama_file yang ingin di download
response: 
- berhasil mendownload -> 'File berhasil didownload.'
- gagal mendownload -> error

4. jika command tidak dikenali akan merespon dengan ERRCMD
