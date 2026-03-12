# Assignment 1 - Deploy Tokens & Create Uniswap Pool

## Objective

Learn to deploy smart contracts (ERC20 and ERC721), create a liquidity pool on Uniswap V3, and add liquidity.

**Detailed task description is provided in the accompanying document.**

## Steps

### 1. Deploy Your ERC20 Token

Deploy an ERC20 token contract on Sepolia. You can use [Remix IDE](https://remix.ethereum.org/) with [OpenZeppelin Contracts](https://wizard.openzeppelin.com/).

Save the **contract address** after deployment.

### 2. Make an ERC20 Transfer

Transfer some of your tokens to another address (can be your second wallet).

Save the **transaction hash**.

### 3. Create a Uniswap V3 Pool

Create a liquidity pool on Uniswap V3 (Sepolia) pairing your ERC20 token with WETH and add liquidity.

- Uniswap V3 App: https://app.uniswap.org/
- Make sure you're on Sepolia network

Save the **pool address**.

### 4. Deploy Your ERC721 (NFT) Contract

Deploy an ERC721 contract on Sepolia.

Save the **contract address**.

### 5. Mint an NFT

Mint a token from your NFT contract.

Save the **mint transaction hash**.

### 6. Fill in `STUDENT_DATA` in `homework.py`

You can use different wallets for each part of the task.

```python
STUDENT_DATA = {
    # --- ERC20 Token ---
    "erc20_wallet": "0x...",        # Wallet that deployed/transferred ERC20
    "erc20_address": "0x...",       # Deployed ERC20 contract address
    "erc20_transfer_tx": "0x...",   # Transfer transaction hash

    # --- Uniswap Pool ---
    "pool_wallet": "0x...",         # Wallet that created the pool
    "pool_address": "0x...",        # Pool address

    # --- NFT (ERC721) ---
    "nft_wallet": "0x...",          # Wallet that deployed/minted NFT
    "erc721_address": "0x...",      # Deployed ERC721 contract address
    "nft_mint_tx": "0x...",         # Mint transaction hash
}
```

### 7. Test Locally

```bash
pip install -r requirements.txt
pytest tests/test_visible.py -v
```

### 8. Submit Your Solution

```bash
git add homework.py
git commit -m "solution"
git push
```

After `push`, autograding will run. Check results in the **Actions** tab.

## Grading Criteria (14 points)

| Points | Condition |
|--------|-----------|
| 1 | ERC20 wallet address is valid with balance |
| 3 | ERC20 token deployed (valid contract with name, symbol, totalSupply) |
| 2 | ERC20 transfer transaction is valid (not mint) |
| 3 | Uniswap V3 pool created with your token and has liquidity |
| 3 | ERC721 contract deployed |
| 2 | NFT mint transaction is valid |
| **14** | **Total** |

## Useful Links

- [OpenZeppelin Contracts Wizard](https://wizard.openzeppelin.com/)
- [Remix IDE](https://remix.ethereum.org/)
- [Uniswap V3 App](https://app.uniswap.org/)
- [Sepolia Etherscan](https://sepolia.etherscan.io/)
