from transformers import GPT2Tokenizer, GPT2LMHeadModel
from nltk.translate.bleu_score import corpus_bleu, sentence_bleu


def abstractive_summarization(text):
    
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    # Tokenization
    inputs = tokenizer.encode(text, return_tensors='pt', max_length=512, truncation=True)

    # GPT-2 model
    model = GPT2LMHeadModel.from_pretrained('gpt2')

    # Summarization
    outputs = model.generate(inputs, max_length=1024, min_length=30, num_beams=4, early_stopping=True)

    # Decoding
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return summary


# Reading files
with open("Original_Abstract.txt", 'r',encoding="utf-8") as text2:
    abstract=text2.read()
with open("Target_Text.txt", 'r',encoding="utf-8") as text:
    text=text.read()
    

# Get summary
summary = abstractive_summarization(text)

# Print
print("Summary:")
print(summary)
from rouge import Rouge
ROUGE = Rouge()

print(ROUGE.get_scores(summary, abstract))

gercekmetinuzunlugu=len(text)
özetuzunlugu=len(summary)
orjinalozet=len(abstract)



