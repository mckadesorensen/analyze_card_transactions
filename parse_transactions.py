from typing import List, Dict
import re

from .pull_monthy_transactions_from_csv import get_monthly_transactions


def cleanup_merchant(transactions: List[Dict]) -> List:
    new_transactions = []
    NUMBERS = re.compile(r"(.*) ([0-9]+)")
    for transaction in transactions:
        m = re.match(NUMBERS, transaction["merchant"])
        if m:
            merchant, _ = m.groups()
            transaction["merchant"] = merchant
        new_transactions.append(transaction)

    return new_transactions


def main() -> List:
    return cleanup_merchant(get_monthly_transactions())


if __name__ == "__main__":
    for t in main():
        print(t["merchant"])
