import pytest

from src.utils import translator


@pytest.mark.asyncio
async def test_translation():
    text = "Bitte ergänzen Sie die Liste."
    source_lang = "deu_Latn"
    target_lang = "ben_Beng"
    expected_translation = "দয়া করে এই তালিকাটি সম্পূর্ণ করুন।"

    translation = await translator(text, source_lang, target_lang)

    assert translation == expected_translation
