import os
import pandas as pd
import shutil

from datetime import datetime

principal_path = os.getcwd()
principal_file = principal_path + os.sep + 'principal.csv'
backups_path   = 'backups'
backup_path    = backups_path + os.sep + 'backup_' + datetime.now().strftime('%d%m%Y%H%M%I')
pdfs_path      = 'pdf'
xmls_path      = 'xml'

NAME_FILE = '2021-06'

def copyBackup(path: str, backup_type: str):
    if not os.path.exists(backup_path + os.sep + backup_type):
        os.mkdir(backup_path + os.sep + backup_type)

    shutil.copy(path, backup_path + os.sep + backup_type + os.sep + path.split(os.sep)[-1])

def renameFileByPath(keyFile: object, path: str, rename_type: str, key: int):
    for file in os.listdir(path):
        if file.startswith(keyFile['chave_acesso']):
            path_file = path + os.sep + file
            new_name = '({0}) - {1}.{2}'.format(addZeroRight(key), NAME_FILE, rename_type)
            print('Arquivo {0} encontrado'.format(path_file), 'Novo nome: ' + new_name)
            copyBackup(path_file, rename_type)
            os.rename(path_file, path + os.sep + new_name)

def addZeroRight(number: int):
    number_to_str = str(number)

    if (number < 10):
        return '00' + number_to_str

    if (number >= 10 and number < 100):
        return '0' + number_to_str

    return number_to_str

def main():
    for required_path in [principal_file, pdfs_path, xmls_path]:
        if not os.path.exists(required_path):
            print('Arquivo/pasta obrigatorio nao encontrado: ' + os.getcwd() + os.sep + required_path)
            exit(0)

    if not os.path.exists(backups_path):
        os.mkdir(backups_path)

    if not os.path.exists(backup_path):
        os.mkdir(backup_path)

    files = pd.read_csv(principal_file, sep=',').to_dict('records')

    for index, file in enumerate(files):
        renameFileByPath(file, pdfs_path, 'pdf', index + 1)
        renameFileByPath(file, xmls_path, 'xml', index + 1)

main()