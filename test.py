from OCR import text_extract

text_ext = text_extract()

#use lang = 'ben' for Bengali
#use lang = 'eng' for English
text = text_ext.img2txt(img_path='9.png', lang='ben', apply_filter=False, exe_time=True)
print(text)