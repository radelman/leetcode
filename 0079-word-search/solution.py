from typing import List

class Solution:
    def exist2(
            self,
            board: List[List[str]],
            word: str,
            i: int,
            j: int,
    ) -> bool:
        if board[i][j] == word:
            return True

        if board[i][j] != word[0]:
            return False

        temp = board[i][j]
        board[i][j] = ""

        if i > 0 and board[i - 1][j]:
            if self.exist2(board, word[1:], i - 1, j):
                return True

        if i < len(board) - 1 and board[i + 1][j]:
            if self.exist2(board, word[1:], i + 1, j):
                return True

        if j > 0 and board[i][j - 1]:
            if self.exist2(board, word[1:], i, j - 1):
                return True

        if j < len(board[0]) - 1 and board[i][j + 1]:
            if self.exist2(board, word[1:], i, j + 1):
                return True

        board[i][j] = temp

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.exist2(board, word, i, j):
                    return True

        return False

def main() -> None:
    test_cases = [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"),
    ]

    solution = Solution();

    for inputs in test_cases:
        board, word = inputs

        test = solution.exist(board, word)

        print(test)

if __name__ == '__main__':
    main()
