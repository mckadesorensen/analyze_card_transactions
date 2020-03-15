from typing import List, Dict, Tuple

from matplotlib import pyplot as plt
from pull_monthy_transactions_from_csv import get_category_spending, get_monthly_transactions
import pandas as pd


def _convert_to_list(transactions: Dict) -> Tuple[List, List]:
    categories = []
    total_spent = []

    for key, value in transactions.items():
        if key == "payment":
            continue

        categories.append(key)
        total_spent.append(float(value))

    return categories, total_spent


def _get_list_of_merchants(transactions: List[Dict]) -> List:
    merchants = []
    for transaction in transactions:
        merchant = transaction["merchant"]
        if len(merchants) == 0:
            merchants.append(merchant)
        elif float(transaction["amount"]) < 0:
            continue
        elif merchant not in merchants:
            merchants.append(merchant)

    return merchants


def _add_up_total_spent_at_merchant(merchants: List, transactions: List[Dict]) -> List:
    total_spent = [0]
    for index, merchant in enumerate(merchants):
        for transaction in transactions:
            if index >= len(total_spent):
                total_spent.append(0)

            if transaction["merchant"] == merchants[index]:
                total_spent[index] += float(transaction["amount"])

    return total_spent


def pie_graph(transactions) -> None:
    categories, total_spent = _convert_to_list(transactions)
    plt.pie(total_spent, labels=categories, autopct='%1.1f%%')
    plt.savefig('Feb-transactions-pie.png', dpi=300, bbox_inches='tight')


def _shorten_name(merchants: List) -> List:
    new_merchant = []
    for merchant in merchants:
        if len(merchant) > 15:
            new_merchant.append(merchant[:15])
        else:
            new_merchant.append(merchant)

    return new_merchant


def bar_graph(transactions) -> None:
    merchants = _get_list_of_merchants(transactions)
    totals = _add_up_total_spent_at_merchant(merchants, transactions)

    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Helvetica'

    # set the style of the axes and the text color
    plt.rcParams['axes.edgecolor'] = '#333F4B'
    plt.rcParams['axes.linewidth'] = 0.8
    plt.rcParams['xtick.color'] = '#333F4B'
    plt.rcParams['ytick.color'] = '#333F4B'
    plt.rcParams['text.color'] = '#333F4B'

    merchants = _shorten_name(merchants)

    percentages = pd.Series(totals, index=merchants)
    df = pd.DataFrame({'percentage': percentages})
    df = df.sort_values(by='percentage')

    my_range = list(range(1, len(df.index) + 1))

    fig, ax = plt.subplots(figsize=(5, 3.5))

    plt.hlines(y=my_range, xmin=0, xmax=df['percentage'], color='#228B22', alpha=0.2, linewidth=5)

    plt.plot(df['percentage'], my_range, "o", markersize=5, color='#228B22', alpha=0.6)

    ax.set_xlabel('Total Spent', fontsize=15, fontweight='black', color='#333F4B')
    ax.set_ylabel('')

    ax.tick_params(axis='both', which='major', labelsize=12)
    plt.yticks(my_range, df.index)

    fig.text(-0.23, 0.96, "Merchant", fontsize=15, fontweight='black', color='#333F4B')

    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')

    ax.spines['bottom'].set_position(('axes', -0.04))
    ax.spines['left'].set_position(('axes', 0.015))

    plt.savefig('Feb-transactions-bar.png', dpi=300, bbox_inches='tight')


def plot_transactions() -> None:
    pie_graph(get_category_spending())
    bar_graph(get_monthly_transactions())


if __name__ == "__main__":
    plot_transactions()
