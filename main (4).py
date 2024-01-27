import re

text = input()
text = re.sub(r' +', ' ',text.strip())
text = re.sub(r"\\n", "\n",text)

formatted_text = ""
text_list =list(text)
tmp = 0

for char in b:
    if char == "@":
        formatted_text += '@'
        tmp += 1
    elif char == '#' and tmp > 0:
        tmp -= 1
    else:
        formatted_text += char
        
print('Formatted Text: '+formatted_text)
