class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map:
                if not stack:
                    return False
                top_element = stack.pop()
                if bracket_map[char] != top_element:
                    return False
    
        
        return not stack

        