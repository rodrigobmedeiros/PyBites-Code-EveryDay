import argparse


def calc_bmi(weight, length):
    """Provided/DONE:
       Calc BMI give a weight in kg and length in cm, return the BMI
       rounded on 2 decimals"""
    bmi = int(weight) / ((int(length) / 100) ** 2)
    return round(bmi, 2)


def create_parser():
    """TODO:
       Create an ArgumentParser adding the right arguments to pass the tests,
       returns a argparse.ArgumentParser object"""
    argument_parser = argparse.ArgumentParser(
        prog='calc_bmi',
        add_help=True,
        descrition='Calculate your BMI.'
    )
    argument_parser.add_argument(
        '-l', 
        '--length', 
        help='Your weight in kg',
        type=int
    )
    argument_parser.add_argument(
        '-w', 
        '--weight', 
        help='Your length in cm',
        type=int
    )

    return argument_parser


def handle_args(args=None):
    """Provided/DONE:
       Call calc_bmi with provided args object.
       If args are not provided get them from create_parser"""
    if args is None:
        parser = create_parser()
        args = parser.parse_args()

    if args.weight and args.length:
        bmi = calc_bmi(args.weight, args.length)
        print(f'Your BMI is: {bmi}')
    else:
        # could enforce SystemExit in create_parser/add_argument, but argparse
        # docs are not clear how to do it, so raising the exception here manually
        raise SystemExit


if __name__ == '__main__':
    handle_args()