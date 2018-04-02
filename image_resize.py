import subprocess
# import sys
import os


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
    process = subprocess.run('sips --resampleWidth {} {}'.format(resize_width, source_file), shell=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # print('ARGV', process.args)
    # print('STDOUT', str(process.stdout))
    # print('STDERR', process.stderr)
    # print('RETURN_CODE', process.returncode)


def main():
    source_dir = 'Source'
    source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), source_dir)
    result_dir = 'Result'
    result_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), result_dir)
    check_result_folder(result_dir)
    copy_all_files(source_dir, result_dir)


if __name__ == '__main__':
    main()