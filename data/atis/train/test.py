import json

f = open('file.json',)
lines = f.readlines()

seqin = open('seq.in','w')
seqout = open('seq.out','w')
label = open('label','w')


for i in lines[1000:]:
    a = json.loads(i)
    if('code_mixed_sentence' in a):
        slots = str(a["code_mixed_slots"]).strip().replace(',',' ')+ "\n"
        sentence = str(a['code_mixed_sentence']).strip()+ "\n"
        l = str(a['intents']).strip() + "\n"

        if(len(slots.split()) == len(sentence.split())): 

            seqin.write(sentence)
            seqout.write(slots)
            label.write(l)

seqin.close()
seqout.close()
label.close()

    

f.close()