import subprocess
# import sys
import os
from sys import platform
import multiprocessing
import time


def check_os():
    # print(platform)
    return platform


def check_result_folder(check_dir):
    if not os.path.exists(check_dir):
        os.makedirs(check_dir)
        print('Создан каталог {}'.format(check_dir))


def copy_all_files(source_dir, remote_dir):
    list_files = []
    for d, dirs, files in os.walk(source_dir):
        # print('{} - {} - {}'.format(d, dirs, files))
        for f in files:
            sf = os.path.join(source_dir, f)
            rf = os.path.join(remote_dir, f)
            subprocess.run('cp {} {}'.format(sf, rf), shell=True)
            list_files.append(rf)
            # resize_file(rf, 200)
    print('Всего {} файлов для обработки.'.format(len(files)))
    return list_files


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
    print(time.time())
    # print(source_file)
    # print('ARGV', process.args)
    # print('STDOUT', str(process.stdout))
    # print('STDERR', process.stderr)
    # print('RETURN_CODE', process.returncode)


def main():
    start_time = time.time()
    mp = []
    resize_width = 210
    source_dir = 'Source'
    source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), source_dir)
    result_dir = 'Result'
    result_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), result_dir)

    check_result_folder(result_dir)
    my_list_files = copy_all_files(source_dir, result_dir)

    for f in my_list_files:
        mp.append(multiprocessing.Process(target=resize_file, args=(f, resize_width)))

    # p1 = multiprocessing.Process(target=resize_file, args=(my_list_files[0], resize_width))

    for item in mp:
        item.start()

    # p1.start()

    for item in mp:
        item.join()

    # p1.join()

    print('Tasks done! Time: %s seconds' % (time.time()-start_time))


if __name__ == '__main__':
    main()
