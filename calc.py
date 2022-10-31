def calc_ratio(exp): # калькулятор с предыдущего семинара
    if exp.find('(') >= 0 and exp.find(')') >= 0:
        exp = exp[:exp.find('(')] + str(calc_ratio(exp[exp.find('(')+1:exp.find(')')])) + exp[exp.find(')') + 1:]
    if exp.find('+') >= 0:
        return calc_ratio(exp[:exp.find('+')]) + calc_ratio(exp[exp.find('+')+1:])
    if exp.find('-') >= 0:
        return calc_ratio(exp[:exp.find('-')]) - calc_ratio(exp[exp.find('-')+1:])
    if exp.find('*') >= 0:
        return calc_ratio(exp[:exp.find('*')]) * calc_ratio(exp[exp.find('*')+1:])
    if exp.find('/') >= 0:
        return calc_ratio(exp[:exp.find('/')]) / calc_ratio(exp[exp.find('/')+1:])

    return float(exp)


def calc_complex (data):
    return eval(data) # функция eval работает и с комплексными числами
