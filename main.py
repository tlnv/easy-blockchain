from hashlib import sha256
from datetime import datetime


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = sha256()
        sha.update((str(self.index)).encode() + (str(self.timestamp)).encode() +
                    self.data.encode() + self.previous_hash.encode())
        return sha.hexdigest()


def create_primary_block():
    return Block(0, datetime.now(), "Hello, I'm Primary block", "0")


def create_next_block(last_block):
    next_index = last_block.index + 1
    next_timestamp = datetime.now()
    next_data = f"Hello, I'm block number {str(next_index)}"
    next_hash = last_block.hash
    return Block(next_index, next_timestamp, next_data, next_hash)


blockchain = [create_primary_block()]
previous_block = blockchain[0]
blockchain_size = 100
for transaction in range(0, blockchain_size):
    block_to_add = create_next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print(f"Block {block_to_add.index} has been added to the Blockchain")
    print(f"Added block hash: {block_to_add.hash}")
    print()
print("Blockchain is full")
