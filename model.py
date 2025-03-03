import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def predict_next_words(text, num_words=4, num_variations=4):
    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt")

    # Generate multiple variations
    outputs = model.generate(
        **inputs,
        max_length=inputs["input_ids"].shape[1] + num_words,
        num_return_sequences=num_variations,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.2,
        temperature=0.9
    )

    # Decode generated text
    generated_texts = [tokenizer.decode(output, skip_special_tokens=True)[len(text):].strip()
                       for output in outputs]

    return [" ".join(generated.split()[:num_words]) for generated in generated_texts]
