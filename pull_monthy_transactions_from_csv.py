import csv
from typing import Dict, List


def _remove_column_names_from_data(transactions: List[Dict]) -> List[Dict]:
    transactions.__delitem__(0)
    return transactions


def get_monthly_transactions() -> List[Dict]:
    transactions = []
    with open('Apple_Card_Transactions_February_2020.csv') as spending:
        csv_reader = csv.reader(spending)
        for transaction in csv_reader:
            transactions.append(_structure_transaction_information(transaction))

    return _remove_column_names_from_data(transactions)


def _structure_transaction_information(transaction: List[str]) -> Dict:
    return {
        "transaction_date": transaction[0],
        "clearing": transaction[1],
        "description": transaction[2],
        "merchant": transaction[3],
        "category": transaction[4],
        "type": transaction[5],
        "amount": transaction[6]
    }


# TODO Update this to be dynamic
def _set_up_categories() -> Dict:
    return {
        "restaurants": 0,
        "transportation": 0,
        "gas": 0,
        "other": 0,
        "payment": 0,
        "grocery": 0
    }


def _add_up_category_spending(monthly_transactions) -> Dict:
    category_spending = _set_up_categories()
    for transaction in monthly_transactions:
        category_spending[transaction["category"].lower()] += float(transaction["amount"])

    return category_spending


def get_category_spending() -> Dict:
    return _add_up_category_spending(get_monthly_transactions())


if __name__ == "__name__":
    # TODO: Add arg-parsing to receive the csv as input
    pass
