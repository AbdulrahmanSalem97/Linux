import subprocess
import os

# List all files with the ".txt" extension in the current directory
txt_files = [f for f in os.listdir(".") if f.endswith(".c")]
print(txt_files)

# Compile the C files
result =subprocess.run(['avr-gcc', '-mmcu=atmega32', '-Os', '-c', txt_files[0], '-o', 'main.o'])
result =subprocess.run(['avr-gcc', '-mmcu=atmega32', '-Os', '-c', txt_files[1], '-o', 'DIO_program.o'])
result =subprocess.run(['avr-gcc', '-mmcu=atmega32', '-Os', '-c', txt_files[2], '-o', 'LED_program.o'])

# Link the object files
result =subprocess.run(['avr-gcc', '-mmcu=atmega32', '-Os', 'main.o', 'DIO_program.o','LED_program.o', '-o', 'output.elf'])

# Generate the hex file
result =subprocess.run(['avr-objcopy', '-O', 'ihex', '-R', '.eeprom', 'output.elf', 'output.hex'])


