import copy
from matplotlib import pyplot as plt
from typing import List, Dict
from pull_monthy_transactions_from_csv import grab_monthly_transactions


def plot_transactions() -> None:
    monthly_transactions = grab_monthly_transactions()


if __name__ == "__main__":
    plot_transactions()
