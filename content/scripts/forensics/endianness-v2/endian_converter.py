#!/usr/bin/env python3

import sys

def swap_32bit_endian(input_file, output_file):
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        while True:
            chunk = infile.read(4)
            if len(chunk) < 4:
                if chunk:
                    outfile.write(chunk)
                    # the last block, if it is shorter than 4, is NOT SWAPPED, but simply written as it is, and this is a condition for exiting the cycle
                    # The essence of the 32-bit endianness swap operation is to rotate ONLY FULL 4-BYTE BLOCKS.
                    # Swaps of incomplete blocks are essentially just garbage and do not need to be reversed.
                    # may also distort data
                break

            swapped = chunk[::-1]
            outfile.write(swapped)
#no rewriting because
#The write() method, in contrast to seek(), writes to the file,
#and moves the cursor by the same number of positions as the number of bytes written.

def check_file_type(filename):
    with open(filename, 'rb') as f:
        header = f.read(16) #16 to guarantee capturing magic bytes

    print(f'File: {filename}')
    print(f'Header (hex): {header.hex()}')
    print(f'Header ASCII: {header}')

# https://en.wikipedia.org/wiki/List_of_file_signatures
    if header.startswith(b'\x89\x50\x4E\x47'): #PNG
        print("✓ PNG image detected!")
        return True
    elif header.startswith(b'\x47\x49\x46'): #GIF
        print("✓ GIF image detected!")
        return True
    elif header.startswith(b'\xFF\xD8\xFF'): #JPEG
        print("✓ JPEG image detected!")
        return True
    elif header.startswith(b'\x42\x4D'): #BMP
        print("✓ BMP image detected!")
        return True
    elif header.startswith(b'\x50\x4B'): #ZIP
        print("✓ ZIP image detected!")
        return True
    elif header.startswith(b'\x7F\x45\x4C\x46'): #ELF
        print("✓ ELF image detected!")
        return True
    elif header.startswith(b'\x25\x50\x44\x46'): #PDF
        print("✓ PDF image detected!")
        return True
    else:
        print('??? Unknown type ???')
        return False

if __name__ == "__main__": #program entry point, standard Python idiom
    if len(sys.argv) != 2: #There must be an array of operands in the terminal command: python3 <sys.argv[0]> <sys.argv[1]>
                           # NO MORE THAN 2 (0, 1), otherwise, print an informational message about how to use the command.
        print('Usage: python3 endian_converter.py <input_file>')
        print("This will create <input_file_swapped with 32-bit endianness swapped>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file + "_swapped"

    print("=== Original File ===")
    check_file_type(input_file)

    print("\n=== Swapping 32-bit endianness===")
    swap_32bit_endian(input_file, output_file)
    print(f"Created: {output_file}")

    print("\n=== Swapped file ===")
    if check_file_type(output_file):
        print(f"\n🎉 Success! Try opening: {output_file}")
    else:
        print(f"\n❌ Still unknown file type. The original might already be in correct endianness.")





