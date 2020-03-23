import shelve
import uuid


class View:
    def __init__(self):
        self.data = shelve.open('mydata.dat')
    def upload(self,nama_file=None,byte_data=None):
        if (nama_file is None):
            return False

        "File disimpan di server"
        fileclient = open('datanya/'+nama_file, 'wb+')
        fileclient.write(byte_data)
        fileclient.close()

        "File disimpan di database"
        id=str(uuid.uuid4())
        data = dict(id=id,nama_file=nama_file,byte_data=byte_data)
        self.data[id]=data

        return True
        
    def download(self,nama=None):
        print('Proses mengunduh...')
        for i in self.data.keys():
            if (self.data[i]['nama_file'].lower() == nama.lower()):
                return self.data[i]
        return False

    def lihat(self):
        k = [dict(nama_file=self.data[i]['nama_file']) for i in self.data.keys()]
        return k

if __name__=='__main__':
    p = View()
