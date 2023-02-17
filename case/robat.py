import aiml
import os
import sys

# os.chdir('../src/alice')
# alice = aiml.Kernel()
# alice.

def get_module_dir(name):
  # print(sys.modules['aiml'])
  path = getattr(sys.modules['aiml'], '__file__', None)
  # print(path)
  os_path = os.path.dirname(os.path.abspath(path))
  print(os_path)
  return os_path

if __name__ == '__main__':
  alice_path = get_module_dir('aiml') + '\\botdata\\alice'

  os.chdir(alice_path)

  alice = aiml.Kernel()
  alice.learn('startup.xml')
  alice.respond('LOAD ALICE')

  while True:
    message = input('Enter your message >> ')
    if('exit' == message):
      exit()

    res = alice.respond(message)
    print(res)