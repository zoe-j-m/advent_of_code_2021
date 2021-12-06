from typing import List, TypeVar

T = TypeVar('T')


class Matrix:
    def __init__(self, rows: List[List[T]]):
        self.rows = rows

    def transpose(self):
        return Matrix([[self.rows[j][i] for j in range(len(self.rows))] for i in range(len(self.rows[0]))])

    def flatten(self):
        return [item for sublist in self.rows for item in sublist]