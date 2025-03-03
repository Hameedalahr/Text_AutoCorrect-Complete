import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load a grammar correction model fine-tuned for this task
tokenizer = T5Tokenizer.from_pretrained("prithivida/grammar_error_correcter_v1")
model = T5ForConditionalGeneration.from_pretrained("prithivida/grammar_error_correcter_v1")

def correct_grammar(text):
    """Corrects grammar using a fine-tuned T5 model for grammar correction."""
    input_text = "gec: " + text  # Task prefix for grammar correction
    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)

    # Generate corrected text
    outputs = model.generate(**inputs, max_length=512, num_beams=5, early_stopping=True)

    corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected_text