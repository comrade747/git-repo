import shutil
import PyPDF2
import pytesseract
from PIL import Image
import cv2
import os
import logging
from stat import S_ISDIR, S_ISREG
import project_settings as pss
import items
from pymongo import MongoClient
import re

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level = logging.DEBUG, filename = u'Lesson7.log')
# https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
pytesseract.pytesseract.tesseract_cmd = pss.TSRCT_PATH


def create_folder(name):
    try:
        os.mkdir(name)
        logging.info( u'был создан каталог {}'.format(name) )
    except FileExistsError as fee:
        logging.info( u'{} каталог уже существует'.format(fee) )


def getColorSpace(obj):
    if '/ColorSpace' not in obj:
        mode = None
    elif obj['/ColorSpace'] == '/DeviceRGB':
            mode = "RGB"
    elif obj['/ColorSpace'] == '/DeviceCMYK':
        mode = "CMYK"
    elif obj['/ColorSpace'] == '/DeviceGray':
        mode = "P"
    else:
        if type(obj['/ColorSpace']) == PyPDF2.generic.ArrayObject:
            if obj['/ColorSpace'][0] == '/ICCBased':
                colorMap = obj['/ColorSpace'][1].getObject()['/N']
                if colorMap == 1:
                    mode = "P"
                elif colorMap == 3:
                    mode = "RGB"
                elif colorMap == 4:
                    mode = "CMYK"
                else:
                    mode = None
            else:
                mode = None
        else:
            mode = None
    return mode


def find_number(img_obj:object) -> str:
    
    phrases = list({'заводской (серийный) номер',
                    'заводской номер номера',
                    'заводской (сернйный) номер',
                    'заводской номер (номера)',})
    text = pytesseract.image_to_string(img_obj, config='-l rus')
    text = re.sub('\n\n+', '\n', text)
    for phrase in phrases:
        pos = text.lower().find(phrase)
        if pos + 1:
            for idx, line in enumerate(text.split('\n')):
                pos = line.lower().find(phrase)
                if pos + 1:
                    eng_text = pytesseract.image_to_string(img_obj, config='-l eng')
                    eng_text = re.sub('\n\n+', '\n', eng_text)
                    line_text = eng_text.split('\n')[idx]
                    number = line_text.split(' ')[-1]
                    return number

    text = pytesseract.image_to_string(img_obj, config='-l eng')
    text = re.sub('\n\n+', '\n', text)
    pattern = re.compile('\w+\W+B COCTaBe')
    phrase = pattern.search(text)
    if phrase is not None:
        return phrase.group().split('\n')[0]
                

def parse_image(original_file_name:str,
                buffered_file_name:str):

    image = cv2.imread(buffered_file_name)
    buffer_file_name = f'{os.getcwd()}\\temporary_buffer.png'
    if os.path.exists(buffer_file_name):
        os.remove(buffer_file_name)
            
    if image is not None:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        gray = cv2.medianBlur(gray, 3)
        cv2.imwrite(buffer_file_name, gray)
    else:
        buffer_file_name = buffered_file_name

    img_obj = Image.open(buffer_file_name)
    number = find_number(img_obj)

    if number is None:
        raise NotImplementedError()

    filename = original_file_name.replace(pss.ROOT_PATH, '')
    item = items.CasheMachineFileData(filename, number)
    item.SaveData(collection)


def parse_pdf(original_file_name:str):
    logging.info( u'начинаем обработку файла {}'.format(original_file_name) )
    pdf_file = PyPDF2.PdfFileReader(open(file=original_file_name, mode='rb'), strict=False)
    for page_num in range(0, pdf_file.getNumPages()):
        crnt_page = pdf_file.getPage(page_num)
        page_obj = crnt_page['/Resources']['/XObject'].getObject()

        if page_obj['/Im0'].get('/Subtype') == '/Image':
            size = (page_obj['/Im0']['/Width'], page_obj['/Im0']['/Height'])
            data = page_obj['/Im0']._data
            if page_obj['/Im0']['/ColorSpace'] == '/DeviceRGB':
                mode = 'RGB'
            else:
                mode = 'P'

            buffer_file_name = f"{os.getcwd()}\\image"
            if '/Filter' in page_obj['/Im0']:
                if page_obj['/Im0']['/Filter'] == '/FlateDecode':
                    img = Image.frombytes(mode, size, data)
                    buffer_file_name += '.png'
                    img.save(buffer_file_name)
                elif page_obj['/Im0']['/Filter'] == '/DCTDecode':
                    if page_obj['/Im0']['/Filter'] == '/DCTDecode' or '/DCTDecode' in page_obj['/Im0']['/Filter']:
                        buffer_file_name += '.jpg'
                        img = open(buffer_file_name, "wb")
                        img.write(data)
                        img.close()
                    elif page_obj['/Im0']['/Filter'] == '/FlateDecode' or '/FlateDecode' in page_obj['/Im0']['/Filter']:
                        mode = getColorSpace(page_obj['/Im0'])
                        if mode != None:
                            img = Image.frombytes(mode, size, data)
                            if mode == 'CMYK':
                                img = img.convert("RGB")
                            buffer_file_name += '.png'
                            img.save(buffer_file_name)
                        else:
                            logging.error( u'Color map не поддерживается для файла {}'.format(original_file_name) )
                            return
                    elif page_obj['/Im0']['/Filter'] == '/JPXDecode':
                        buffer_file_name += '.jp2'
                        img = open(buffer_file_name, "wb")
                        img.write(data)

                logging.info( u'Картинка успешно записана в буферный файл {}'.format(buffer_file_name) )
                parse_image(original_file_name, buffer_file_name)


def dispatch(filename:str):
    file_extension = os.path.splitext(filename)[1]
    file_name = os.path.basename(filename)
    error_folder_name = f'{os.getcwd()}\\Errors'
    try:
        if file_extension == '.pdf':
            parse_pdf(filename)
        elif file_extension == '.jpg' or file_extension == '.png':
            parse_image(filename, filename)
        else:
            pass
    except Exception as ex:
        if not os.path.exists(error_folder_name):
            create_folder(error_folder_name)
        logging.error( u'Не удалось обработать файл {}\n{}'
                      .format(filename, ex) )
        destFileName = f'{error_folder_name}\\{file_name}'
        shutil.copy(filename, destFileName)


def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print('Skipping %s' % pathname)


if __name__ == '__main__':

    connection = MongoClient(pss.DB_HOST, 27017)
    connection[pss.DB_NAME].authenticate(pss.DB_USER, pss.DB_PWRD)
    collection = connection[pss.DB_NAME].CashBoardData
    walktree(pss.ROOT_PATH, dispatch)