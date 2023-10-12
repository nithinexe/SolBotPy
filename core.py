from solathon import Client, Keypair, PublicKey, Transaction
from solathon.core.instructions import transfer

client = Client("https://api.devnet.solana.com")

new_account = Keypair()
print(new_account.public_key, new_account.private_key)
amount = 10000  # This is the amount in lamports

res = client.request_airdrop(new_account.public_key, amount)
print("Airdrop response: ", res)

# Check balance

public_key = PublicKey("9W9QHEBfx6fiZNqzMNrRWWZc3FAQcqyX64smYBd12gXA")
balance = client.get_balance(public_key)
print(balance)

sender = Keypair().from_private_key("your_private_key")
receiver = PublicKey("B3BhJ1nvPvEhx3hq3nfK8hx4WYcKZdbhavSobZEA44ai")
amount = 10000 # This is the amount in lamports

instruction = transfer(
    from_public_key=sender.public_key,
    to_public_key=receiver, 
    lamports=amount
)
transaction = Transaction(instructions=[instruction], signers=[sender])

result = client.send_transaction(transaction)
print(result)

