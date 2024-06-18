from transformers import pipeline


async def translator(text: str, source: str, target: str) -> str:
    pipe = pipeline("translation", model="facebook/nllb-200-distilled-600M")
    translation = pipe(text, src_lang=source, tgt_lang=target)
    return translation[0]['translation_text']
