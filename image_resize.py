import subprocess
# import sys
import os
from sys import platform
import time


def check_os():
    # print(platform)
    return platform


def check_result_folder(check_dir):
    if not os.path.exists(check_dir):
        os.makedirs(check_dir)
        print('Создан каталог {}'.format(check_dir))


def copy_all_files(source_dir, remote_dir):
    # list_files = []
    for d, dirs, files in os.walk(source_dir):
        # print('{} - {} - {}'.format(d, dirs, files))
        for f in files:
            sf = os.path.join(source_dir, f)
            rf = os.path.join(remote_dir, f)
            subprocess.run('cp {} {}'.format(sf, rf), shell=True)
            resize_file(rf, 200)
    print('Всего {} файлов было обработано.'.format(len(files)))


def resize_file(source_file, resize_width):
    my_os = check_os()
    if my_os == "linux" or my_os == "linux2":
        pass
    elif my_os == "darwin":
        process = subprocess.run('sips --resampleWidth {} {}'.format(resize_width, source_file), shell=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    elif my_os == "win32":
        process = subprocess.run('convert {} -resize {} {}'.format(source_file, resize_width, source_file), shell=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # print('ARGV', process.args)
    # print('STDOUT', str(process.stdout))
    # print('STDERR', process.stderr)
    # print('RETURN_CODE', process.returncode)


def main():
    start_time = time.time()

    source_dir = 'Source'
    source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), source_dir)
    result_dir = 'Result'
    result_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), result_dir)

    check_result_folder(result_dir)
    copy_all_files(source_dir, result_dir)

    print('Время выполнения %s секунд' % (time.time() - start_time))


if __name__ == '__main__':
    main()