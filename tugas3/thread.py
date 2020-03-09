import threading
import logging
import requests
import datetime
import os

def download_picture(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        filename = os.path.basename(url)
        extension = tipe[content_type]
        logging.warning(f"writing {filename}.{extension}")
        fp = open(f"{filename}.{extension}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


if __name__=='__main__':
    picture_list = [
        'https://i.pinimg.com/474x/3f/df/a3/3fdfa3c237e228c38a0311e170be78a9--why-do-men-heavens.jpg',
        'https://i.etsystatic.com/13298123/r/il/cd2108/2032802252/il_794xN.2032802252_jlui.jpg',
        'https://i.pinimg.com/originals/c7/9b/a7/c79ba794d04613d1bd3ad54a8f4c8022.jpg'
        
    ]
    
threads = []
for i in picture_list:
    t = threading.Thread(target=download_picture,args=(i,))
    threads.append(t)
    t.start()