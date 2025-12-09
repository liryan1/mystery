"""
A blockchain indexer is a software tool designed to efficiently organize, store, and retrieve data from a blockchain. Blockchains, such as those used in cryptocurrencies like Bitcoin or Ethereum, are decentralized and distributed ledgers that record transactions across a network of computers. Indexers play a crucial role in making blockchain data more accessible and searchable.

You are tasked with designing a basic blockchain indexer that can efficiently retrieve transaction information from a blockchain. The blockchain consists of blocks, each containing a list of transactions. Your goal is to create a simple indexer that allows for fast queries based on transaction IDs.

The indexer should implement two methods:**`add_block`**and**`get_account_balance`**.

**`add_block`**takes in an array of transactions. Transactions include "from" address, "to" address and a "value" amount of cryptocurrency. These transactions should be stored in a data structure that allows efficiently retrieval.

**`get_account_balance`**takes in an account address and a block number. It returns the balance for the address at that block number. If no block number is provided then return latest balance.

```
# Example usage
indexer = BlockchainIndexer()

# Adding blocks with transactions
indexer.add_block([
    {'from': 'init', 'to': 'acc1', 'value': 15},
    {'from': 'init', 'to': 'acc3', 'value': 20},
])

print(indexer.get_account_balance('acc1', 0))  # Should print 15
print(indexer.get_account_balance('acc2', 0))  # Should print 0
print(indexer.get_account_balance('acc3', 0))  # Should print 20

indexer.add_block([
    {'from': 'acc1', 'to': 'acc2', 'value': 10},
    {'from': 'acc3', 'to': 'acc1', 'value': 5},
])

print(indexer.get_account_balance('acc1', 1))  # Should print 10
print(indexer.get_account_balance('acc2', 1))  # Should print 10
print(indexer.get_account_balance('acc3', 1))  # Should print 15

indexer.add_block([
    {'from': 'acc2', 'to': 'acc1', 'value': 8},
    {'from': 'acc3', 'to': 'acc2', 'value': 3},
])

print(indexer.get_account_balance('acc1', 2))  # Should print 18
print(indexer.get_account_balance('acc2', 2))  # Should print 5
print(indexer.get_account_balance('acc3', 2))  # Should print 12

indexer.add_block([
    {'from': 'acc1', 'to': 'acc3', 'value': 12},
])

# Querying account balances
print(indexer.get_account_balance('acc1'))  # Should print 6
print(indexer.get_account_balance('acc2'))  # Should print 5
print(indexer.get_account_balance('acc3'))  # Should print 24

```

When an invalid block is added (such as insufficient funds to perform a transaction) it should return an error. Any transaction from 'init' to any other account is valid.
"""

from collections import defaultdict
from typing import TypedDict, Literal
from bisect import bisect_right

Transaction = TypedDict("Transaction", {"from": str, "to": str, "value": int})
Record = TypedDict("Record", {"block_id": int, "balance": int})


class BlockchainIndexer:
    """
    Basic implementation of a Blockchain indexer.
    Stores sorted list of transaction records and uses binary search to
    get the latest balance of each account at any block number.
    O(log n) look up for account balance

    Alternatively we can store an array of every block of every account.
    This would be space expensive and would be slow for creating new accounts
    at large block numbers. This would allow O(1) look up of account balance
    at any block number.
    """

    init_sender_id = "init"

    def __init__(self) -> None:
        self.current_block_idx = 0
        self.ledger: defaultdict[str, list[Record]] = defaultdict(list)

    def add_block(self, transactions: list[Transaction]) -> None:
        # 1. VALIDATION PHASE
        # Track pending changes locally.
        # We must seed this with current balances to handle multiple txs
        # involving the same account within one block.
        pending_balance = defaultdict(int)
        for tran in transactions:
            sender, receiver, value = tran["from"], tran["to"], tran["value"]

            if sender != self.init_sender_id:
                sender_bal = pending_balance.get(
                    sender, self.get_account_balance(sender)
                )
                if sender_bal < value:
                    raise ValueError(
                        f"Insufficient funds for {sender} sending {value} to {receiver}"
                    )
                pending_balance[sender] = sender_bal - value

            receiver_bal = pending_balance.get(
                receiver, self.get_account_balance(receiver)
            )
            pending_balance[receiver] = receiver_bal + value

        # 2. COMMIT PHASE
        # If we reached here, all transactions are valid.
        # Now we can safely mutate the persistent state.
        for account, new_bal in pending_balance.items():
            history = self.ledger[account]
            if history and history[-1]["block_id"] == self.current_block_idx:
                history[-1]["balance"] = new_bal
            else:
                history.append({"block_id": self.current_block_idx, "balance": new_bal})
        self.current_block_idx += 1

    def get_account_balance(self, account_id: str, block_number=None) -> int:
        history = self.ledger.get(account_id)
        if not history:
            return 0

        if block_number is None:
            return history[-1]["balance"]

        idx = bisect_right(history, block_number, key=lambda x: x["block_id"])
        if idx == 0:  # account was not created yet before this block
            return 0
        return history[idx - 1]["balance"]


"""
# First implementation, missed a few things
from collections import defaultdict
from typing import TypedDict, Literal
from bisect import bisect_left

Transaction = TypedDict("Transaction", {"from": str, "to": str, "value": int})
Record = TypedDict("Record", {"block_number": int, "balance": int})


class BlockchainIndexer:
    '''
    Basic implementation of a Blockchain indexer.
    Stores sorted list of transaction records and uses binary search to
    get the latest balance of each account at any block number.
    O(log n) look up for account balance

    Alternatively we can store an array of every block of every account.
    This would be space expensive and would be slow for creating new accounts
    at large block numbers. This would allow O(1) look up of account balance
    at any block number.
    '''

    def __init__(self) -> None:
        self.current_block = 0
        self.ledger: defaultdict[str, list[Record]] = defaultdict(list)

    def add_block(self, transactions: list[Transaction]) -> None:
        for transac in transactions:
            # For now we are validate every transaction in real time
            # e.g., assuming block contains chronologically sorted transactions
            # could have more sophisticated validation if assumption above is false
            self.__validate_transaction(transac)
            self.__create_or_update_record(transac["from"], "from", transac["value"])
            self.__create_or_update_record(transac["to"], "to", transac["value"])
        self.current_block += 1

    def get_account_balance(self, account_id: str, block_number=None) -> int:
        account = self.ledger[account_id]
        if not account:
            return 0
        if block_number is None:
            return account[-1]["balance"]
        idx = bisect_left([acc["block_number"] for acc in account], block_number)
        return account[idx]["balance"]

    def __validate_transaction(self, transaction: Transaction) -> None:
        if transaction["from"] == "init":
            return
        from_account = self.ledger[transaction["from"]]
        error = ValueError(
            f"{from_account} has too low balance {from_account[-1]["balance"]}"
            + f" to send {transaction["value"]}"
        )
        if not from_account and transaction["value"] > 0:
            raise error

        if from_account[-1]["balance"] < transaction["value"]:
            raise ValueError(
                f"{from_account} has too low balance {from_account[-1]["balance"]}"
                + f" to send {transaction["value"]}"
            )

    def __create_or_update_record(
        self, account_id: str, type: Literal["from"] | Literal["to"], value: int
    ) -> None:
        if account_id == "init":
            return
        account = self.ledger[account_id]
        record = self.__create_record(account_id, type, value)
        if account and account[-1]["block_number"] == self.current_block:
            account[-1]["balance"] += value
        else:
            account.append(record)

    def __create_record(
        self, account: str, type: Literal["from"] | Literal["to"], value: int
    ) -> Record:
        change = value if type == "to" else -value
        balance = (
            value
            if not self.ledger[account]
            else self.ledger[account][-1]["balance"] + change
        )
        return {"block_number": self.current_block, "balance": balance}
"""

indexer = BlockchainIndexer()

# Adding blocks with transactions
indexer.add_block(
    [
        {"from": "init", "to": "acc1", "value": 15},
        {"from": "init", "to": "acc3", "value": 20},
    ]
)

print(indexer.get_account_balance("acc1", 0))  # Should print 15
print(indexer.get_account_balance("acc2", 0))  # Should print 0
print(indexer.get_account_balance("acc3", 0))  # Should print 20

indexer.add_block(
    [
        {"from": "acc1", "to": "acc2", "value": 10},
        {"from": "acc3", "to": "acc1", "value": 5},
    ]
)

print(indexer.get_account_balance("acc1", 1))  # Should print 10
print(indexer.get_account_balance("acc2", 1))  # Should print 10
print(indexer.get_account_balance("acc3", 1))  # Should print 15

indexer.add_block(
    [
        {"from": "acc2", "to": "acc1", "value": 8},
        {"from": "acc3", "to": "acc2", "value": 3},
    ]
)

print(indexer.get_account_balance("acc1", 2))  # Should print 18
print(indexer.get_account_balance("acc2", 2))  # Should print 5
print(indexer.get_account_balance("acc3", 2))  # Should print 12

indexer.add_block(
    [
        {"from": "acc1", "to": "acc3", "value": 12},
    ]
)

# Querying account balances
print(indexer.get_account_balance("acc1"))  # Should print 6
print(indexer.get_account_balance("acc2"))  # Should print 5
print(indexer.get_account_balance("acc3"))  # Should print 24
