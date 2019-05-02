from datetime import datetime
import hashlib as hasher


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def __str__(self):
        return f'La Bloc #{self.index}'

    def hash_block(self):
        sha = hasher.sha256()
        seq = (str(x) for x in (
              self.index, self.timestamp, self.data, self.previous_hash))
        sha.update(''.join(seq).encode('utf-8'))
        return sha.hexdigest()


def make_genesis_block():
    """Creer la premiere bloc de la blockchain."""
    block = Block(index=0,
                  timestamp=datetime.now(),
                  data="Genesis Block",
                  previous_hash="0")
    return block


def next_block(last_block, data=''):
    """Retourne le bloc suivant dans une blockchain."""
    idx = last_block.index + 1
    block = Block(index=idx,
                  timestamp=datetime.now(),
                  data=f'{data},{idx}',
                  previous_hash=last_block.hash)
    return block

counter = 0
nb_blocks = 20

file = open('blockchain.txt', 'w')


def lunch_app():
    """Test creating chain of 20 blocks."""
    blockchain = [make_genesis_block()]
    prev_block = blockchain[0]
    for _ in range(counter, nb_blocks):
        block = next_block(prev_block, data='some data here')
        blockchain.append(block)
        prev_block = block
        file.writelines(f'{block} a été ajouté à la blockchain\n')
        file.writelines(f'Hash: {block.hash}\n')
        print(f'{block} a été ajouté à la blockchain')
        print(f'Hash: {block.hash}\n')


# run the test code
lunch_app()
