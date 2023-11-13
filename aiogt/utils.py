import re

translated_re = re.compile(r'(?s)class="(?:t0|result-container)">(.*?)<')


def parse_html(raw: str) -> str:
    return translated_re.findall(raw)[0]
