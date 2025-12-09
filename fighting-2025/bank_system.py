# Coinbase asssessment completed on 12/4
from banking_system import BankingSystem


class BankingSystemImpl(BankingSystem):
    expiry_period = 24 * 60 * 60 * 1000  # 1 day

    def __init__(self):
        self.accounts: dict[str, int] = {}
        self.transactions: dict[str, int] = {}
        self.transfers: dict[str, tuple] = {}
        self.transfer_id_counter = 0

    def create_account(self, timestamp: int, account_id: str) -> bool:
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = 0
        self.transactions[account_id] = 0
        return True

    def deposit(self, timestamp: int, account_id: str, amount: int) -> int | None:
        self.__expire_transfers(timestamp)
        if account_id not in self.accounts:
            return None
        self.accounts[account_id] += amount
        self.transactions[account_id] += amount
        return self.accounts[account_id]

    def pay(self, timestamp: int, account_id: str, amount: int) -> int | None:
        self.__expire_transfers(timestamp)
        if account_id not in self.accounts:
            return None
        curr_amount = self.accounts[account_id]
        if amount > curr_amount:
            return None
        self.accounts[account_id] -= amount
        self.transactions[account_id] += amount
        return self.accounts[account_id]

    def top_activity(self, timestamp: int, n: int) -> list[str]:
        transactions = list(self.transactions.items())
        transactions.sort(key=lambda x: (-x[1], x[0]))
        return [f"{t[0]}({t[1]})" for t in transactions][:n]

    def transfer(
        self,
        timestamp: int,
        source_account_id: str,
        target_account_id: str,
        amount: int,
    ) -> str | None:
        self.__expire_transfers(timestamp)
        if (
            source_account_id not in self.accounts
            or target_account_id not in self.accounts
            or source_account_id == target_account_id
        ):
            return None

        if self.accounts[source_account_id] < amount:
            return None

        self.transfer_id_counter += 1
        transfer_id = f"transfer{self.transfer_id_counter}"
        self.transfers[transfer_id] = (
            source_account_id,
            target_account_id,
            amount,
            timestamp,
        )
        self.accounts[source_account_id] -= amount

        return transfer_id

    def accept_transfer(
        self, timestamp: int, account_id: str, transfer_id: str
    ) -> bool:
        self.__expire_transfers(timestamp)
        if transfer_id not in self.transfers:
            return False

        source_account_id, target_account_id, amount, transfer_timestamp = (
            self.transfers[transfer_id]
        )
        if target_account_id != account_id:
            return False

        self.accounts[account_id] += amount
        self.transactions[source_account_id] += amount
        self.transactions[target_account_id] += amount
        del self.transfers[transfer_id]

        return True

    def merge_accounts(
        self, timestamp: int, account_id_1: str, account_id_2: str
    ) -> bool:
        if (
            account_id_1 not in self.accounts
            or account_id_2 not in self.accounts
            or account_id_1 == account_id_2
        ):
            return False

        to_delete = []
        for id, (
            source_account_id,
            target_account_id,
            amount,
            transfer_timestamp,
        ) in self.transfers.items():
            if source_account_id == account_id_2 or (
                source_account_id == account_id_1 and target_account_id == account_id_2
            ):
                to_delete.append((id, source_account_id, amount))
            elif target_account_id == account_id_2:
                self.transfers[id] = (
                    source_account_id,
                    account_id_1,
                    amount,
                    transfer_timestamp,
                )
        self.__cancel_transfers(to_delete)

        self.accounts[account_id_1] += self.accounts[account_id_2]
        self.transactions[account_id_1] += self.transactions[account_id_2]
        del self.accounts[account_id_2]
        del self.transactions[account_id_2]

        return True

    def get_balance(self, timestamp: int, account_id: str, time_at: int) -> int | None:
        if account_id not in self.accounts:
            return None
        return self.accounts[account_id]

    def __expire_transfers(self, timestamp):
        to_delete = []
        for id, transfer in self.transfers.items():
            source_account_id, target_account_id, amount, transfer_timestamp = transfer
            if timestamp > transfer_timestamp + self.expiry_period:
                to_delete.append((id, source_account_id, amount))
        self.__cancel_transfers(to_delete)

    def __cancel_transfers(self, to_delete: list[tuple]):
        for id, source_account_id, amount in to_delete:
            self.accounts[source_account_id] += amount
            del self.transfers[id]
