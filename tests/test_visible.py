"""
Visible tests - you can run them locally:
    pytest tests/test_visible.py -v
"""

from homework import STUDENT_DATA


def test_student_data_has_required_fields():
    """STUDENT_DATA must contain all required keys."""
    required_keys = {
        "erc20_wallet",
        "erc20_address",
        "erc20_transfer_tx",
        "pool_wallet",
        "pool_address",
        "nft_wallet",
        "erc721_address",
        "nft_mint_tx",
    }
    missing = required_keys - set(STUDENT_DATA.keys())
    assert not missing, f"Missing keys in STUDENT_DATA: {missing}"


def test_addresses_are_hex_strings():
    """All addresses must be hex strings starting with 0x."""
    address_fields = [
        "erc20_wallet", "erc20_address",
        "pool_wallet", "pool_address",
        "nft_wallet", "erc721_address",
    ]
    for field in address_fields:
        val = STUDENT_DATA[field]
        assert isinstance(val, str), f"{field} must be a string"
        assert val.startswith("0x"), f"{field} must start with 0x"


def test_tx_hashes_are_hex_strings():
    """All transaction hashes must be hex strings starting with 0x."""
    tx_fields = ["erc20_transfer_tx", "nft_mint_tx"]
    for field in tx_fields:
        val = STUDENT_DATA[field]
        assert isinstance(val, str), f"{field} must be a string"
        assert val.startswith("0x"), f"{field} must start with 0x"
