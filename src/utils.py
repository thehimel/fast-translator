import torch
from transformers import pipeline


async def translator(text: str, source: str, target: str) -> str:

    model = "facebook/nllb-200-distilled-600M"
    device = 0 if torch.cuda.is_available() else -1  # Use GPU if available

    pipe = pipeline("translation", model=model, device=device)
    translation = pipe(text, src_lang=source, tgt_lang=target)
    return translation[0]["translation_text"]
