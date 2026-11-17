import json 
from pathlib import Path
import pytest


TEST_CASES_FILE = Path(__file__).parent / "test_cases.json"

def load_test_cases():
    with TEST_CASES_FILE.open ("r", encoding="utf-8") as file:
        return json.load(file)

def evaluate_output(ai_output, expected_keywords, forbidden_keywords=None):
    if forbidden_keywords is None:
        forbidden_keywords = []

    if not isinstance(ai_output, str) or not ai_output.strip():
        return "Wrong"

    ai_output = ai_output.casefold()

    #check forbidden keywords 
    for keyword in forbidden_keywords:

         if keyword.casefold() in ai_output:
            return "Wrong"
    return "Correct"

@pytest.mark.parametrize(
    "case",
    load_test_cases(),
    ids=lambda case: case["id"]
)

def test_ai_output(case):

    result = evaluate_output(
        case["ai_output"],
        case["expected_keywords"],
        case.get("forbidden_keywords")
    )

    print (f'{case["id"]}: {result}')

    assert result == "Correct"    