from Node import Node
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

class HashTable:
    def __init__(self) -> None:
        self.Table = np.empty(10, dtype=Node)

    def Hash(self,Key):
        Hash = 0
        for Char in Key:
            Hash += ord(Char)
        return Hash
    
    def Insert(self,Node:Node):
        Index = self.Hash(Node.Key)%10
        self.Table[Index] = Node

    def Delete(self,Key):
        Index = self.Hash(Key)%10
        self.Table[Index] = None

    def Find(self,Key):
        Index = self.Hash(Key)%10
        return self.Table[Index]