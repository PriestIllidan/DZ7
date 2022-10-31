import calc
import view
import logger

def button_click ():
    exp = view.expression()
    if exp.find('j'):
        result = calc.calc_complex(exp)
        view.view(result)
        logger.calc_logger(result)
    else:
        result = calc.calc_ratio(exp)
        logger.calc_logger(result)
