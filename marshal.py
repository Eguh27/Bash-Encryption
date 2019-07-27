import marshal

print ('Masukkan File Anda')
inp = raw_input('File#  ')
file = open(inp).read()
com = compile(file,'','exec')
had = marshal.dumps(com)
file_out = open('out.py', 'w')
file_out.write('#Decrypt By MrIkuk \n')
file_out.write('#github : Https://github.com/Eguh27 \n')
file_out.write('import marshal\n')
file_out.write('exec(marshal.loads('+repr(had)+'))')
file_out.close()
print (type(had), len(had))

print ("-"*50)
print (repr(had))
print ("-"*50)