

import json
from typing import Any, Dict


def encode_message(payload: Dict[str, Any]) -> bytes:
    return (json.dumps(payload, ensure_ascii=False) + "\n").encode("utf-8")


def decode_message(raw_data: str) -> Dict[str, Any]:
    return json.loads(raw_data)
