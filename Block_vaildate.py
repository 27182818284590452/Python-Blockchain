from blockchain import Blockchain

block_one_transactions = {"Block one"}
block_two_transactions = {"Block two"}
block_three_transactions = {"Block three"}
fake_transactions = {" this is fake! "}

# make a new blockchain
local_blockchain = Blockchain()

# init blocks and print the out
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()
print("\033[37m---------------------------------END of verified chain----------------------------------------------\033[0m")

# this changes the value of the second block
# uncomment it to manipulate the blockchain
# local_blockchain.chain[2].transactions = fake_transactions
local_blockchain.print_blocks()
local_blockchain.validate_chain()