

import re
from typing import Dict, List

PATTERNS = {
    "email": re.compile(
        r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
    ),
    "telefone": re.compile(
    r"(?:\+351[\s-]?)?(?:9[1236]\d{2}[\s-]?\d{3}[\s-]?\d{3}|2\d{2}[\s-]?\d{3}[\s-]?\d{3})"
    ),
    "ip": re.compile(
        r"\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}"
        r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b"
    ),
    "nome_completo": re.compile(
        r"\b[A-ZÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇ][a-záàâãéèêíïóôõöúç]+"
        r"(?:\s+[A-ZÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇ][a-záàâãéèêíïóôõöúç]+){1,3}\b"
    ),
    "data_nascimento": re.compile(
        r"\b(?:0?[1-9]|[12]\d|3[01])[-/](?:0?[1-9]|1[0-2])[-/](?:19\d{2}|20\d{2})\b"
    ),
    "cartao_credito": re.compile(
        r"\b(?:\d[ -]*?){13,19}\b"
    ),
}


def detect_personal_data(message: str) -> Dict[str, List[str]]:
    findings: Dict[str, List[str]] = {}

    for data_type, pattern in PATTERNS.items():
        matches = pattern.findall(message)
        cleaned_matches = []

        for match in matches:
            if isinstance(match, tuple):
                cleaned_matches.append("".join(match))
            else:
                cleaned_matches.append(match)

        if cleaned_matches:
            findings[data_type] = cleaned_matches

    return findings


def should_block_message(findings: Dict[str, List[str]]) -> bool:
    return len(findings) > 0


def format_findings(findings: Dict[str, List[str]]) -> str:
    parts = []
    for data_type, values in findings.items():
        parts.append(f"{data_type}: {', '.join(values)}")
    return " | ".join(parts)
