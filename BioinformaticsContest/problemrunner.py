# problemrunnner.py
# controller script for Bioinformatics Contest 2021

import argparse
import problems
import utils
from multiprocessing import freeze_support

def main():
    parser = argparse.ArgumentParser()
    # problem identifies the function as well as the I/O files
    parser.add_argument('problem', help='name of prblem function')
    # -s flags whether or not to use the sample input file
    parser.add_argument('-s', default=False, help='indicates to use sample input')
    # parser.add_argument('-v', default=True, help='do not validate number of outputs to number of inputs')
    args = parser.parse_args()

    inputstring = './inputs/sampleinput.txt' if args.s else f'./inputs/{args.problem}.txt'

    # load input file
    lines = utils.load_input(inputstring)

    # call problem function on inputs
    results = getattr(problems, args.problem)(lines)

    # validate number of expected answers
    if results:
    # if results and (args.v or len(results) == int(cases)):
        # save output
        utils.save_output(f'./outputs/{args.problem}_output.txt', results)
    elif not args.s:
        print('oops')
    else:
        pass

if __name__ == '__main__':
    main()