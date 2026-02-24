import pyperclip as ppc

ppc.copy('test')
assert ppc.paste() == 'test'
