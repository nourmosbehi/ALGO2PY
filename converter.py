import re
from typing import List, Tuple, Union, Callable

class AlgorithmConverter:
    """Robust bidirectional algorithm/Python converter"""
    
    def __init__(self):
        # Algorithm → Python patterns
        self.algo_to_py = [
            (r'(?i)\b(si|if)\s*(?:\((.*?)\)|(.*?))\s*(alors|then)?', self._handle_conditional),
            (r'(?i)\b(sinon\s+si|else\s+if)\s*(?:\((.*?)\)|(.*?))', 'elif \\2\\3:'),
            (r'(?i)\b(sinon|else)\b', 'else:'),
            (r'(?i)\bafficher\s*"([^"]*)"', 'print("\\1")'),
            (r'(?i)\bafficher\s+([^"\s]+)', 'print(\\1)'),
            (r'(?i)\b(variable|var)\s+(\w+)\s*:\s*(.+)', '\\2 = \\3'),
            (r'(?i)\b(pour|for)\s+(\w+)\s+(de|from)\s+(\d+)\s+(à|to)\s+(\d+)\s*(pas\s*(-?\d+))?', self._handle_for_loop),
            (r'(?i)\b(tant\s+que|while)\s+(.+?)\s+(faire|do)', 'while \\2:'),
            (r'(?i)\b(fonction|function)\s+(\w+)\s*\((.*?)\)', 'def \\2(\\3):'),
            (r'(?i)\b(retourner|return)\s+(.+)', 'return \\2'),
            (r'(?i)\b(vrai|true)\b', 'True'),
            (r'(?i)\b(faux|false)\b', 'False')
        ]
        
        # Python → Algorithm patterns
        self.py_to_algo = [
            (r'if\s*\((.*?)\):', 'si \\1 alors'),
            (r'if\s+(.*?):', 'si \\1 alors'),
            (r'elif\s*\((.*?)\):', 'sinon si \\1 alors'),
            (r'elif\s+(.*?):', 'sinon si \\1 alors'),
            (r'else:', 'sinon'),
            (r'print\("([^"]*)"\)', 'afficher "\\1"'),
            (r'print\(([^"\s]+)\)', 'afficher \\1'),
            (r'^(\w+)\s*=\s*(.+)', 'variable \\1 : \\2'),
            (r'for\s+(\w+)\s+in\s+range\((\d+),\s*(\d+)(?:,\s*(-?\d+))?\):', self._handle_py_for_loop),
            (r'while\s+(.+?):', 'tant que \\1 faire'),
            (r'def\s+(\w+)\s*\((.*?)\):', 'fonction \\1(\\2)'),
            (r'return\s+(.+)', 'retourner \\1'),
            (r'\bTrue\b', 'vrai'),
            (r'\bFalse\b', 'faux')
        ]

    def _handle_conditional(self, match) -> str:
        condition = match.group(2) if match.group(2) else match.group(3)
        return f'if {condition.strip()}:'

    def _handle_for_loop(self, match) -> str:
        var, start, end, step = match.group(2), match.group(4), match.group(6), match.group(8)
        step = f', {step}' if step else ''
        return f'for {var} in range({start}, {int(end)+1}{step}):'

    def _handle_py_for_loop(self, match) -> str:
        var, start, end, step = match.group(1), match.group(2), match.group(3), match.group(4)
        step_part = f" pas {step}" if step and step != '1' else ""
        return f'pour {var} de {start} à {int(end)-1}{step_part} faire'

    def convert(self, code: str, direction: str) -> str:
        patterns = self.algo_to_py if direction == "algorithm-to-python" else self.py_to_algo
        lines = code.split('\n')
        converted_lines = []
        indent_level = 0
        
        for line in lines:
            line = line.strip()
            if not line:
                converted_lines.append('')
                continue
                
            for pattern, replacement in patterns:
                if callable(replacement):
                    line = re.sub(pattern, replacement, line, flags=re.IGNORECASE)
                else:
                    line = re.sub(pattern, replacement, line, flags=re.IGNORECASE)
            
            # Fixed indentation calculation - properly closed parentheses
            indent_spaces = '    ' * (indent_level - (1 if line.endswith(':') else 0))
            converted_lines.append(indent_spaces + line)
            
            if line.endswith(':'):
                indent_level += 1
            elif line.startswith(('return', 'retourner')):
                indent_level = max(0, indent_level - 1)
        
        return '\n'.join(converted_lines)

# Interface functions
def convert_algorithm_to_python(code: str) -> str:
    return AlgorithmConverter().convert(code, "algorithm-to-python")

def convert_python_to_algorithm(code: str) -> str:
    return AlgorithmConverter().convert(code, "python-to-algorithm")

if __name__ == '__main__':
    # Test cases
    test_algo = """
    fonction exemple(x)
        si x > 5 alors
            afficher "Grand"
        sinon si x < 5 alors
            afficher "Petit"
        sinon
            afficher "Moyen"
        fin si
    fin fonction
    """
    
    print("=== Algorithm to Python ===")
    print(convert_algorithm_to_python(test_algo))
    
    test_py = """
    def example(x):
        if x > 5:
            print("Big")
        elif x < 5:
            print("Small")
        else:
            print("Medium")
    """
    
    print("\n=== Python to Algorithm ===")
    print(convert_python_to_algorithm(test_py))