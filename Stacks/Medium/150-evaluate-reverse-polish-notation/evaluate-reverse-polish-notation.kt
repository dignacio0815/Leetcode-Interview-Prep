import java.util.ArrayDeque

class Solution {
    fun evalRPN(tokens: Array<String>): Int {
        var stack = ArrayDeque<Int>()
        
        // loop through tokens
        // if current token is an int, add to stack
        // if current token is ['+', '-', '*', '/']
        //      pop stack twice and perform operation
        //      add new value back to stack
        //      continue till end of tokens
        // return stack.pop()

        tokens.forEach { t ->
            if (t.toIntOrNull() != null) {
                // add to stack
                stack.push(t.toInt())
            } else {
                // pop stack twice and perform operation
                // add value back to stack
                var j = stack.pop(); var i = stack.pop()
                var k = when(t) {
                    "+" -> i + j
                    "-" -> i - j
                    "*" -> i * j
                    "/" -> i / j
                    else -> 0
                }
                stack.push(k)
            }
        }

        return stack.pop() ?: -1
    }
}