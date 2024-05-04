#NFMLC QFYPC JCKML RWNC
import string
def main(plain:str,key:int) -> str:
    plain,charset=plain.lower(),{}
    letters=string.ascii_lowercase 

    for i in range(len(letters)):
        charset.update({letters[i-key]:letters[i]})
       
    def encode(plain:str,char_set:dict) -> str:
        es=''
        for char in plain:
            try:
                es+=charset[char]
            except:
                es+=char 
        return es 
    
    return encode(plain,charset).upper() 

#PHONE SHARE LEMON TYPE, Key:3
for i in range(26):
    cipher_input="NFMLC QFYPC JCKML RWNC"
    possible_answer=main(cipher_input,i)
    print(f'{possible_answer}, Key:{i+1}')
