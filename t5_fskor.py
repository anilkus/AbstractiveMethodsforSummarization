
with open("Original_Text.txt", 'r',encoding="utf-8") as text2:
    abstract=text2.read()
with open("Target_Text.txt", 'r',encoding="utf-8") as text:
    summary=text.read()
    
from rouge import Rouge
ROUGE = Rouge()

print(ROUGE.get_scores(summary, abstract))


        
