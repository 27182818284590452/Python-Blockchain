# gets user input and stacks it onto the chain
from blockchain import Blockchain

# init blockchain
local_blockchain = Blockchain()

sender = raw_input("Enter the name of the sender: ")
print("Sender: " + sender)
receiver = raw_input("Enter the name of the receiver: ")
print("Receiver: " + receiver)
amount = raw_input("Enter the amount of the transaction: ")
print("Amount: " + amount)

transaction = {"sender":sender, "receiver":receiver, "amount":amount}

local_blockchain.add_block(transaction)
local_blockchain.validate_chain()
local_blockchain.print_blocks()