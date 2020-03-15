from ..parse_transactions import main


def test_main() -> None:
    assert type(main()) == list
