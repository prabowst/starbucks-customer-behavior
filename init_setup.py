def progress_bar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '='):
    '''
    Print a progress bar

    Args:
        iteration (integer): Current iteration
        total (integer): Total number of iteration
        prefix (string): Prefix to print sentence
        suffix (string): Suffix to print sentence
        decimals (integer): Number of decimal place(s)
        length (integer): Number of iteration print for bar
        fill (string): Char to print
    Returns:
        None, print progress bar
    '''
    printEnd = "\r"
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()