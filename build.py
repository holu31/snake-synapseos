import os, shutil, sys, tarfile, os.path

CCFLAGS = "-g -I include/ -ffreestanding -Wall -Wextra -w -O0"
LD = "-nostdlib -lgcc -T link.ld -o"
CC = "i686-elf-gcc " + CCFLAGS
O_LIBC = " ./bin/libc/stdio.o ./bin/libc/ports.o ./bin/libc/stdlib.o ./bin/libc/string.o ./bin/libc/learntask.o ./bin/libc/vesa.o ./bin/libc/scancodes.o"
data = []
files = []


def build(file_name):
    try:
        shutil.rmtree("./bin", ignore_errors=True)
        os.mkdir("./bin")
        os.mkdir("./bin/libc")
    except Exception as E:
        print(E)
    
    print("Building")
    os.system(f"i686-elf-gcc -nostdlib -w -lgcc -ffreestanding -I include/ -c {file_name} -o ./bin/a.o")

    os.system("i686-elf-gcc -nostdlib -w -lgcc -ffreestanding -I include/ -c libc/stdio.c -o ./bin/libc/stdio.o")
    os.system("i686-elf-gcc -nostdlib -w -lgcc -ffreestanding -I include/ -c libc/ports.c -o ./bin/libc/ports.o")
    os.system("i686-elf-gcc -nostdlib -w -lgcc -ffreestanding -I include/ -c libc/stdlib.c -o ./bin/libc/stdlib.o")
    os.system("i686-elf-gcc -nostdlib -w -lgcc -ffreestanding -I include/ -c libc/string.c -o ./bin/libc/string.o")
    os.system("i686-elf-gcc -nostdlib -w -lgcc -ffreestanding -I include/ -c libc/learntask.c -o ./bin/libc/learntask.o")
    os.system("i686-elf-gcc -nostdlib -w -lgcc -ffreestanding -I include/ -c libc/vesa.c -o ./bin/libc/vesa.o")
    os.system("i686-elf-gcc -nostdlib -w -lgcc -ffreestanding -I include/ -c libc/scancodes.c -o ./bin/libc/scancodes.o")

    
    os.system("i686-elf-gcc -nostdlib -lgcc -T link.ld -o a.elf ./bin/a.o" + O_LIBC)
    shutil.copyfile('a.elf', 'synapse/apps/a.elf')


if __name__ == "__main__":
    try:
        build(sys.argv[1])
    except Exception as E:
        print(E)
        input()