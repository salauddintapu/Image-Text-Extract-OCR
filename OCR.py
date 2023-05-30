import pytesseract as pyt
import  cv2
import numpy as np
from time import time

class text_extract:
    
    def filter_img(self, img):
        img = cv2.medianBlur(img, 5)             #median filter
        kernel = np.array([[-1,-1,-1], [-1,11,-1], [-1,-1,-1]])   #sharpness kernel
        img = cv2.filter2D(img, -1, kernel)     #sharp image
        return img
   
    def ext_address(self, txt):
        text = txt.replace('!', '').replace('', '').replace('#', '').replace('@', '').lstrip().rstrip().replace(']', '').replace('[', '').replace('<', '').replace(')', '').splitlines()
        ext = []
        for i in text:
            if 'ঠিকানা' in i:
                ext.append(i.replace('\n', ''))
            elif 'ডাকঘর' in i:
                ext.append(i.replace('\n', ''))
            elif 'উপশহর' in i:
                ext.append(i.replace('\n', ''))
        adrs = ' '.join(ext)
        return adrs
        
    def img2txt(self, img_path, lang, apply_filter=False, exe_time=False):
        try:
            start = time()
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            
            #if filter is True. apply median filter and increase sharpness
            if apply_filter:
                img = self.filter_img(img)
            
            text = pyt.image_to_string(img, lang=lang)
            text = self.ext_address(text)
            end = time()

            #if exe_time is true, print execution time
            if exe_time:
                print(f'Execution Time: {(end-start) * 10**3} ms')

            return text
        except:
            print('Unavailable image path or wrong language command')