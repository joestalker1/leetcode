from copy import deepcopy

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def isvariable(value):
    return isinstance(value, str)

class Equation:
    def __init__(self, line):
        stripped_line = line.replace(' ', '')
        split_line = stripped_line.split('=')

        self.lhs = split_line[0]
        self.rhs = split_line[1].split('+')

        # Convert item in lhs and rhs to a number if possible
        if isfloat(self.lhs):
            self.lhs = float(self.lhs)

        for i, val in enumerate(self.rhs):
            if isfloat(val):
                self.rhs[i] = float(val)

    def variables(self):
        result = []
        if not isfloat(self.lhs):
            result.append(self.lhs)

        for val in self.rhs:
            if not isfloat(val):
                result.append(val)
        return result


def substitute(equation, mapping):
    '''Creates a new Equation with substituted values.'''
    copy = deepcopy(equation)
    if copy.lhs in mapping:
        copy.lhs = mapping[copy.lhs]

    for i, val in enumerate(copy.rhs):
        if val in mapping:
            copy.rhs[i] = mapping[val]

    return copy

def num_variables(equation):
    expns = [equation.lhs] + equation.rhs
    return sum(isvariable(v) for v in expns)

def solve_single_equation(equation):
    '''Given an equation with exactly one free variable, solves it and
    return a dict e.g. {'x': 3}
    '''
    # If variable is on lhs, then sum up rhs.
    if isvariable(equation.lhs):
        return { equation.lhs: sum(equation.rhs) }
    else:
        # If variable is on rhs, it's LHS - RHS (except for the variable)
        var = next(v for v in equation.rhs if isvariable(v))

        return { var: equation.lhs - sum(val for val in equation.rhs if isfloat(val)) }


def solve(s):
    equations = [Equation(line) for line in s.strip().split('\n')]

    # Collect all the variables into a set
    variables = set()
    for eqn in equations:
        variables |= set(eqn.variables())


    # Start a mapping of variables to their known values.
    mapping = {}

    while len(mapping) != len(equations):
        new_variables_added = False
        for eqn in equations:
            # Go through current equation.
            # Fill out all variables with known ones from mapping.
            # If there's one variable left, then we can infer its value
            # 1) If it's the lhs, then sum up all of rhs
            # 2) If it's in the rhs, then subtract lhs from all other values in rhs
            # 3) Add it to the mapping, and restart.
            substituted_equation = substitute(eqn, mapping)
            if num_variables(substituted_equation) == 1:
                single_mapping = solve_single_equation(substituted_equation)
                mapping.update(single_mapping)
                new_variables_added = True

        if not new_variables_added:
            return None

    return mapping


print(solve("y = x + 1\n 5 = x + 3\n 10 = z + y + 2\n"))