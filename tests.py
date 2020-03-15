from parse_transactions import main, cleanup_merchant
from inputs_for_testing import RAW_MONTHLY_TRANSACTIONS, CLEAN_MONTHLY_TRANSACTIONS

def test_remove_numbers() -> None:
    for raw_transaction, clean_transaction in zip(RAW_MONTHLY_TRANSACTIONS, CLEAN_MONTHLY_TRANSACTIONS):
        assert cleanup_merchant(raw_transaction["merchant"]) == clean_transaction["merchant"]


def test_main() -> None:
    assert type(main()) == list
