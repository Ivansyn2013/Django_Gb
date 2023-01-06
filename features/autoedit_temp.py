import re
import os
import fileinput

RE  = re.compile(r'\"\/(?!href=)')
RE_JS = re.compile(r'\"/(?!scr=)')
root_dir = r'..\mainapp\templates\mainapp'
# print(os.getcwd())
# os.chdir(r'G:\Python project\Django_Gb\mainapp\templates')
# print(os.getcwd())
for r,d,f in os.walk(root_dir):
    for file_name in f:
        #print(r,d,f)
        #print(os.path.join(root_dir,file_name))
        file_path = os.path.join(root_dir,file_name)
        #print(file_path)


        for line in fileinput.input(file_path, inplace=True):
            print('{} {}'.format(fileinput.filelineno(), line), end='') # for Python 3


        # with open(file_path, 'r+', encoding='utf-8') as f:
        #     while True:
        #         line  = f.readline()
        #         if not line:
        #             break
        #         zam = re.sub(RE, '/static/', line)
        #         print(line)
        #         print(zam)

    break