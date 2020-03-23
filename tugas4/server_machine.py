from server_view import View
import json
import logging

'''
PROTOCOL FORMAT

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...

FITUR

- upload : untuk meletakkan/mengunggah file ke data
  request : upload
  parameter : nama_file yang ingin di upload
  response : berhasil mengupload -> 'File berhasil diupload.'
             gagal mengupload -> error

- lihat : untuk melihat daftar file yang ada di server
  request: lihat
  parameter: tidak ada
  response: daftar file yang ada di server

- download : untuk mengambil/mengunduh file
  request: download
  parameter: nama_file yang ingin di download
  response: berhasil mendownload -> 'File berhasil didownload.'
            gagal mendownload -> error

- jika command tidak dikenali akan merespon dengan ERRCMD

'''
p = View()

class Machine:
    def proses(self,string_to_process,connection):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='upload'):
                logging.warning("mengunggah")
                nama_file = cstring[1].strip()

                "Menerima ukuran file yang diupload"
                ukuran_inbyte = connection.recv(4)
                ukuran_asli = int.from_bytes(ukuran_inbyte,byteorder='big')


                "Terima File nya"
                ukuran_diterima = 0
                recv_data=b''
                while ukuran_diterima < ukuran_asli:
                  data = connection.recv(64)
                  if data:
                      recv_data+=data
                      ukuran_diterima+=len(data)
                  else:
                      print(f"file diterima dari {client_address}")
                      break
                p.upload(nama_file,recv_data)

                return "File berhasil diupload."

            elif (command=='lihat'):
                logging.warning("melihat isi data")
                hasil = p.lihat()
                return json.dumps(hasil)

            elif (command=='download'):
                logging.warning("mengunduh")
                nama = cstring[1].strip()

                hasil = p.download(nama)
                if not hasil:
                    nol = 0
                    nol = nol.to_bytes(4,byteorder='big')
                    connection.send(nol)
                    return "File tidak ditemukan dalam data."
                ukuran = len(hasil['byte_data'])
                ukuran_inbyte = ukuran.to_bytes(4,byteorder='big')
                connection.send(ukuran_inbyte)
                connection.sendall(hasil['byte_data'])
                return "File berhasil didownload."
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    pm = Machine()
