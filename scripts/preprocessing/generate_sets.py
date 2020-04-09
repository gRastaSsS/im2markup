import argparse
import logging
import sys
from os.path import join


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--train-size', dest='train_size', type=float, required=True)
    parser.add_argument('--test-size', dest='test_size', type=float, required=True)
    parser.add_argument('--data-file', dest='data_file', type=str, required=True)
    parser.add_argument('--output-path', dest='output_path', type=str, required=True)
    return parser.parse_args(args)


def main(args):
    output_p = args.output_path

    with open(join(output_p, 'train.lst'), 'w') as train_f, \
            open(join(output_p, 'test.lst'), 'w') as test_f, \
            open(join(output_p, 'validate.lst'), 'w') as validate_f:
        formulas = open(args.data_file).read().split('\n')

        train_size = int(args.train_size * len(formulas))
        test_size = int(args.test_size * len(formulas))

        train_formulas = formulas[:train_size]
        test_formulas = formulas[train_size:train_size + test_size]
        validate_formulas = formulas[train_size + test_size:]

        train_f.writelines([x + '\n' for x in train_formulas])
        test_f.writelines([x + '\n' for x in test_formulas])
        validate_f.writelines([x + '\n' for x in validate_formulas])


if __name__ == '__main__':
    main(parse_args(sys.argv[1:]))
    logging.info('Jobs finished')
