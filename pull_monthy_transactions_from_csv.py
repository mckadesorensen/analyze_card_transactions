import csv
from typing import Dict, List


def _remove_column_names_from_data(transactions: List[Dict]) -> List[Dict]:
    transactions.__delitem__(0)
    return transactions


def _open_monthly_transaction_statement() -> List[Dict]:
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


def grab_monthly_transactions() -> List[Dict]:
    monthly_transactions = _open_monthly_transaction_statement()
    return monthly_transactions


if __name__ == "__main__":
    grab_monthly_transactions()
