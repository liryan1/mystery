def calculate_outstanding_balance(events: list[str]) -> int:
    balance = 0
    disputes = {}
    charges = {}

    for raw_event in events:
        event = parse_event(raw_event)
        if event["command"] == "CHARGE":
            balance += event["amount"]
            charges[event["id"]] = event["amount"]
        elif event["command"] == "PAYMENT":
            balance -= event["amount"]
        elif event["command"] == "DISPUTE":
            if event["id"] not in disputes and event["id"] in charges:
                disputes[event["id"]] = "PENDING"
                balance -= charges[event["id"]]
        elif event["command"] == "RESOLVE":
            if event["id"] in disputes and disputes[event["id"]] == "PENDING":
                disputes[event["id"]] = "RESOLVED"
                balance += charges[event["id"]]
        elif event["command"] == "CHARGEBACK":
            if event["id"] in disputes and disputes[event["id"]] == "PENDING":
                disputes[event["id"]] = "CHARGEDBACK"

    return balance


def parse_event(event: str) -> dict[str]:
    parts = event.split(" ")
    if len(parts) != 2 and len(parts) != 3:
        raise RuntimeError("Invalid input")
    # Add more validation here

    return {
        "command": parts[0],
        "id": parts[1],
        "amount": int(parts[2]) if len(parts) == 3 else None,
    }


if __name__ == "__main__":
    events = [
        "CHARGE txn_1 1000",  # Balance: 1000
        "CHARGE txn_2 500",  # Balance: 1500
        "PAYMENT p_1 200",  # Balance: 1300
        "DISPUTE txn_1",  # Balance: 300 (1000 is frozen)
        "CHARGE txn_3 100",  # Balance: 400
        "RESOLVE txn_1",  # Balance: 1400 (1000 is returned)
        "DISPUTE txn_2",  # Balance: 900 (500 is frozen)
        "CHARGEBACK txn_2",  # Balance: 900 (500 is permanently voided)
    ]
    print(calculate_outstanding_balance(events))

"""
Scenario:You are working on the core ledger team for a new credit card product. You need to write a function that processes a stream of events to calculate the final outstanding balance (the amount the user owes) for a specific account.The stream consists of standard transactions (charges, payments) and complex lifecycle events (disputes, chargebacks) that reference previous transaction IDs.Function Signature:Pythondef calculate_outstanding_balance(events: list[str]) -> int:
    pass
Input Format:events is a list of strings. Each string follows the format: COMMAND [ID] [AMOUNT?].ID: A unique string identifier for the transaction.AMOUNT: An integer (cents). Only present for CHARGE and PAYMENT.Business Logic (The Rules):CHARGE {id} {amount}A new purchase. Increases the outstanding balance by amount.Note: Save this id and amount; future events may reference it.PAYMENT {id} {amount}A payment towards the bill. Decreases the outstanding balance by amount.Note: Payments are straightforward and rarely disputed in this MVP.DISPUTE {id}The user claims a specific past CHARGE was fraudulent.Action: The original amount of that charge is subtracted from the balance (held in suspense).Edge Case: If the id does not exist, or refers to a PAYMENT, or is already under dispute, ignore this command.RESOLVE {id}The investigation determines the charge was valid.Action: The original amount is added back to the balance.Edge Case: If the id is not currently under dispute, ignore this command.CHARGEBACK {id}The investigation confirms fraud. The charge is permanently voided.Action: No change to the balance (it was already subtracted during the DISPUTE phase). The status of the transaction becomes "finalized" (cannot be disputed or resolved again).Edge Case: If the id is not currently under dispute, ignore this command.Example Input:Pythonevents = [
  "CHARGE txn_1 1000",   # Balance: 1000
  "CHARGE txn_2 500",    # Balance: 1500
  "PAYMENT p_1 200",     # Balance: 1300
  "DISPUTE txn_1",       # Balance: 300 (1000 is frozen)
  "CHARGE txn_3 100",    # Balance: 400
  "RESOLVE txn_1",       # Balance: 1400 (1000 is returned)
  "DISPUTE txn_2",       # Balance: 900 (500 is frozen)
  "CHARGEBACK txn_2"     # Balance: 900 (500 is permanently voided)
]
Expected Output: 900Constraints:Input list.Amounts are integers.You may assume the stream is chronologically sorted.
"""
