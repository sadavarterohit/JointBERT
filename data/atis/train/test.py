a = open('seq.out')

text = a.read()

a.close()

a=open('seq.out', 'w')

text = text.replace(',', ' ')

a.write(text)

a.close()

