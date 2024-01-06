class Solution {
    fun isValidSudoku(board: Array<CharArray>): Boolean {
        
        var boardFreq = mutableMapOf<Int,Int>()

        // frequency in row
        for (row in 0 until 9) {
            for (col in 0 until 9) {
                // check if current element's frequency is greater > 2
                if (board[row][col].isDigit()) {
                    val key = board[row][col].digitToInt()
                    boardFreq[key] = boardFreq.getOrDefault(key, 0) + 1
                    if (boardFreq[key] ?: 0 >= 2) return false
                }
            }
            // reset freq
            boardFreq = mutableMapOf<Int,Int>()
        }

        // frequency in col
        boardFreq = mutableMapOf<Int,Int>()
        for (col in 0 until 9) {
            for (row in 0 until 9) {
                // check if current element's frequency is greater > 2
                if (board[row][col].isDigit()) {
                    val key = board[row][col].digitToInt()
                    boardFreq[key] = boardFreq.getOrDefault(key, 0) + 1
                    if (boardFreq[key] ?: 0 >= 2) return false
                }
            }
            println("Column freq -> $boardFreq")
            // reset freq
            boardFreq = mutableMapOf<Int,Int>()
        }

        boardFreq = mutableMapOf<Int,Int>()
        for (row in 0 until 9 step 3)  {
            for (col in 0 until 9 step 3) {
                if (board[row][col].isDigit())
                    boardFreq[board[row][col].digitToInt()] = boardFreq.getOrDefault(board[row][col].digitToInt(), 0) + 1

                if (board[row][col + 1].isDigit())
                    boardFreq[board[row][col + 1].digitToInt()] = boardFreq.getOrDefault(board[row][col + 1].digitToInt(), 0) + 1
                
                if (board[row][col + 2].isDigit())    
                    boardFreq[board[row][col + 2].digitToInt()] = boardFreq.getOrDefault(board[row][col + 2].digitToInt(), 0) + 1

                if (board[row + 1][col].isDigit())
                    boardFreq[board[row + 1][col].digitToInt()] = boardFreq.getOrDefault(board[row + 1][col].digitToInt(), 0) + 1
                
                if (board[row + 1][col + 1].isDigit())
                    boardFreq[board[row + 1][col + 1].digitToInt()] = boardFreq.getOrDefault(board[row + 1][col + 1].digitToInt(), 0) + 1
                
                if (board[row + 1][col + 2].isDigit())
                    boardFreq[board[row + 1][col + 2].digitToInt()] = boardFreq.getOrDefault(board[row + 1][col + 2].digitToInt(), 0) + 1

                if (board[row + 2][col].isDigit())
                    boardFreq[board[row + 2][col].digitToInt()] = boardFreq.getOrDefault(board[row + 2][col].digitToInt(), 0) + 1
                if (board[row + 2][col + 1].isDigit())
                    boardFreq[board[row + 2][col + 1].digitToInt()] = boardFreq.getOrDefault(board[row + 2][col + 1].digitToInt(), 0) + 1
                if (board[row + 2][col + 2].isDigit())
                    boardFreq[board[row + 2][col + 2].digitToInt()] = boardFreq.getOrDefault(board[row + 2][col + 2].digitToInt(), 0) + 1

                println()
                println("Board in 3x3 is ${boardFreq}")
                println()

                // check map before moving to next box in sudoku board
                for ((_, value) in boardFreq) {
                    // println("Current element is $_ -> value $value")
                    if (value >= 2) {
                        return false
                    }
                }

                // reset board for each new box check
                boardFreq = mutableMapOf<Int,Int>()

                println("${board[row][col]} | ${board[row][col + 1]} | ${board[row][col + 2]}")
                println("--------")
                println("${board[row + 1][col]} | ${board[row+ 1][col + 1]} | ${board[row+ 1][col + 2]}")
                println("--------")
                println("${board[row + 2][col]} | ${board[row+ 2][col + 1]} | ${board[row+ 2][col + 2]}")

                println("--------")
            }
        }

        return true
    }
}