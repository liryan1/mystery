from bisect import bisect_right
from typing import TypedDict


# Level 2
class Account(TypedDict):
    balance_history: list[tuple[int, int]]
    currency: str


class LedgerCurrency:
    def __init__(self) -> None:
        self.accounts: dict[str, Account] = {}
        # cumulative transfer sum
        self.transfers: dict[str, list[tuple[int, int]]] = {}

    def create_account(self, timestamp: int, account_id: str, currency: str) -> bool:
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = Account(
            currency=currency,
            balance_history=[(timestamp, 0)],
        )
        self.transfers[account_id] = [(timestamp, 0)]
        return True

    def deposit(self, timestamp: int, account_id: str, amount: int) -> None | int:
        return self.__update_balance(timestamp, account_id, amount)

    def transfer(
        self, timestamp: int, source_id: str, target_id: str, amount: int
    ) -> str:
        if source_id not in self.accounts or target_id not in self.accounts:
            return "invalid_account"
        if self.accounts[source_id]["currency"] != self.accounts[target_id]["currency"]:
            return "different_currency"
        if source_id == target_id:
            return "same_account"

        new_bal = self.__update_balance(timestamp, source_id, -amount)
        if not new_bal:
            return "insufficient_funds"

        self.__update_balance(timestamp, target_id, amount)
        self.transfers[source_id].append(
            (timestamp, self.transfers[source_id][-1][-1] + amount)
        )

        return "success"

    def get_top_spenders(self, timestamp: int, n: int) -> list[str]:
        # def get_latest_spend(transfers: list[tuple[int, int]]) -> tuple[int, int]:
        #     i = bisect_right(transfers, lambda x: x[0] - timestamp) - 1
        #     return transfers[i]

        # spenders = sorted(
        #     self.transfers.items(), key=lambda x: (-get_latest_spend(x), x[0])
        # )

        # return spenders[:n]
        return []

    def __update_balance(
        self, timestamp: int, account_id: str, amount: int
    ) -> None | int:
        if account_id not in self.accounts:
            return None
        prev_time, prev_bal = self.accounts[account_id]["balance_history"][-1]
        new_bal = prev_bal + amount
        if prev_time > timestamp or new_bal < 0:
            return None
        self.accounts[account_id]["balance_history"].append((timestamp, new_bal))
        return new_bal


# Level 1
class LedgerBasic:
    def __init__(self):
        self.accounts: dict[str, list[tuple[int, int]]] = {}

    def create_account(self, timestamp: int, account_id: str) -> bool:
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = [(timestamp, 0)]
        return True

    def deposit(self, timestamp: int, account_id: str, amount: int) -> None | int:
        return self.__update_balance(timestamp, account_id, amount)

    def transfer(
        self, timestamp: int, source_id: str, target_id: str, amount: int
    ) -> str:
        if source_id not in self.accounts or target_id not in self.accounts:
            return "invalid_account"
        if source_id == target_id:
            return "same_account"
        new_bal = self.__update_balance(timestamp, source_id, -amount)
        if not new_bal:
            return "insufficient_funds"
        self.__update_balance(timestamp, target_id, amount)

        return "success"

    def __update_balance(
        self, timestamp: int, account_id: str, amount: int
    ) -> None | int:
        if account_id not in self.accounts:
            return None
        prev_time, prev_bal = self.accounts[account_id][-1]
        new_bal = prev_bal + amount
        if prev_time > timestamp or new_bal < 0:
            return None
        self.accounts[account_id].append((timestamp, new_bal))
        return new_bal
