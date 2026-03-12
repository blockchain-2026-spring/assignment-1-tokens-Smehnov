# ============================================================
# TASK: FILL IN WITH YOUR DATA
# ============================================================
# See the provided task document for detailed instructions.
#
# You can use different wallets for each part of the task.
# For each section, provide both the wallet address and the relevant data.
# ============================================================

STUDENT_DATA = {
      # --- ERC20 Token ---
      "erc20_wallet": "0xb1Dd2d0Db4cC92162855c743503F91a0a7804465",
      "erc20_address": "0x4eff872d9bd5924c3862566075af7d6e180075a1",
      "erc20_transfer_tx": "0xdab10467c991b198a595d71c30e832d4dc7750baf27cc78f73f3168f6421459b",
      # ^ FAILS: This is a mint (from 0x0), not a transfer

      # --- Uniswap Pool ---
      "pool_wallet": "0xb1Dd2d0Db4cC92162855c743503F91a0a7804465",
      "pool_address": "0xD91669333CF32D42d05adc1C2307fF9030EBba2E",
      # ^ FAILS: Pool currently has 0 liquidity

      # --- NFT (ERC721) ---
      "nft_wallet": "0x48BDa9Cf5267DE3391CAFC956Bd948C54278ab89",
      "erc721_address": "0xc9Da3A1322f54aE2F173B54463Eff7C6b3e327b2",
      "nft_mint_tx": "0xc7afbc567e503889ac7918764d7e51d96f9315feae2a2ffaa189fb24bbf42946",
      # ^ PASSES: Valid NFT mint
  }
