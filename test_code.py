from .parse_transactions import main, cleanup_merchant
from .inputs_for_testing import RAW_MONTHLY_TRANSACTIONS, CLEAN_MONTHLY_TRANSACTIONS


def test_remove_numbers() -> None:
    cleaned_up_transactions = cleanup_merchant(RAW_MONTHLY_TRANSACTIONS)
    for cleaned_up_transaction, clean_transaction in zip(cleaned_up_transactions, CLEAN_MONTHLY_TRANSACTIONS):
        assert cleaned_up_transaction["merchant"] == clean_transaction["merchant"]


def test_main() -> None:
    assert type(main()) == list
