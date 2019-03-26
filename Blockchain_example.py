from blockchain import Blockchain

# define transactions
transaction1 = {
  'amount': '500',
  'sender': 'Max',
  'receiver': 'Jakob'}
transaction2 = {
  'amount': '2000',
  'sender': 'Bob',
  'receiver': 'Alice'}
transaction3 = {
  'amount': '10',
  'sender': 'Alice',
  'receiver': 'Timothy' }
transaction4 = {
  'amount': '300',
  'sender': 'Rodrigo',
  'receiver': 'Thomas' }
transaction5 = {
  'amount': '200',
  'sender': 'Xavier',
  'receiver': 'Josep' }
transaction6 = {
  'amount': '400',
  'sender': 'Tiffany',
  'receiver': 'Xavier' }

# list of your transactions
mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6]

# define a new blockchain
myblockchain = Blockchain()

for transaction in mempool:
  myblockchain.add_block(transaction)

# validate the blockchain and print the block contents
myblockchain.validate_chain()
myblockchain.print_blocks()