import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


f = open('./task.txt', 'r', encoding='utf-8')
file_data = f.read()
print(file_data)
f.close()
