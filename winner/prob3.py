d={".-":'A',"-...":'B',"-.-.":'C',"-..":'D',".":'E',"..-.":'F',"--.":'G',"....":'H',"..":'I',".---":'J',"-.-":'K',".-..":'L',"--":'M',"-.":'N',"---":'O',".--.":'P',"--.-":'Q',".-.":'R',"...":'S',"-":'T',"..-":'U',"...-":'V',".--":'W',"-..-":'X',"-.--":'Y',"--..":'Z',".----":'1',"..---":'2',"...--":'3',"....-":'4',".....":'5',"-....":'6',"--...":'7',"---..":'8',"----.":'9',"-----":'0',"":' '}
s=input()
l=""
for c in range(len(s)):
 if(s[c]==" "):print(d[l],end="");l=""
 else:l+=s[c]
 if c==len(s)-1:print(d[l],end="")
