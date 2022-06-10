import os
from glob import glob
from pyhtml2pdf import converter

path_list = glob(os.path.join(os.getcwd(), '*.ipynb'))
html_list = [i.split('ipynb')[0] + 'html' for i in path_list]
pdf_list = [i.split('ipynb')[0] + 'pdf' for i in path_list]
for n in range(len(path_list)):
    command0 = 'jupyter nbconvert --to html ' + '\"' + path_list[n] + '\"'
    os.system(command0)
    converter.convert(source=html_list[n], target=pdf_list[n])
    command1 = 'del ' + '\"' + html_list[n] + '\"'
    os.system(command1)
    print('已完成{}/{}'.format(n + 1, len(path_list)))
