import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from urllib.request import urlopen

html = urlopen(
  'http://activity.m.iqiyi.com/web/taskShow.html'
).read().decode('utf-8')

print(html)
