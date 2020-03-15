import copy
from matplotlib import pyplot as plt
from typing import List, Dict
from pull_monthy_transactions_from_csv import grab_monthly_transactions


# def _check_if_category_exists(category: str, categories: List) -> bool:
#     for cat in categories:
#         if category == cat:
#             return True
#     return False
#
#
# def _get_category_index(category: str, categories: List) -> int:
#     index = 0
#     print(categories)
#     for cat in categories:
#         if category == cat:
#             return index
#         index += 1
#
#
# def _consolidate_categories(transactions: List[Dict]):
#     categories = []
#     print(len(transactions))
#     count = 0
#     for transaction in transactions:
#         category = transaction["category"]
#
#         if category == "Payment":
#             continue
#         if len(categories) == 0:
#             categories.append({transaction["category"]: [transaction]})
#
#         if _check_if_category_exists(category, copy.deepcopy(categories)):
#             category_index = _get_category_index(category, copy.deepcopy(categories))
#             # categories[category_index][category].append(transaction)
#         else:
#             categories.append({transaction["category"]: [transaction]})
#             count += 1
#             print(transaction["category"])
#             # print(transaction)
#
#     print(count)
#     return categories


# TODO Update this to be dynamic
def _set_up_categories() -> Dict:
    return {
        "restaurants": 0,
        "transportation": 0,
        "gas": 0,
        "other": 0,
        "payments": 0
    }


def plot_transactions() -> None:
    monthly_transactions = grab_monthly_transactions()
    categories = _set_up_categories()

if __name__ == "__main__":
    plot_transactions()
