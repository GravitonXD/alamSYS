"""
    GENERAL ABOUT: This stock symbols are selected based from the list of Blue Chip stocks in the PSEi
    In order to select the 19 stocks, the following method was used:
        a. Created a list of all Blue Chip stocks in the PSEi
        b. Used random.shuffle() to shuffle the list
        c. Selected the first 19 stocks in the shuffled list

    All Stock Information was taken from https://edge.pse.com.ph/companyPage/
"""
stock_symbols = [
    'MEG',
    'JGS',
    'BDO',
    'FGEN',
    'ICT',
    'ALI',
    'SMC',
    'TEL',
    'GLO',
    'BLOOM',
    'RLC',
    'MER',
    'AC',
    'PGOLD',
    'LTG',
    'MPI',
    'AP',
    'RRHI',
    'URC',
    'PSEI'
]


"""
    FUNCTION DESCRIPTION: This function will return the list of stock symbols
"""
def get_stock_symbols():
    return stock_symbols
