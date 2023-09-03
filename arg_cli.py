import argparse

def _parse_args():
    parser = argparse.ArgumentParser(
        prog='app',
        description='Smiles innput and output descriptors fingerprints.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('--input_file',
                        help='Path to the input file',
                        type=str)
    parser.add_argument('--output_file',
                        help='Path to the output file',
                        type=str)
    parser.add_argument('--method',
                        choices=['descriptor'],
                        default='descriptor',
                        help='Calculation descriptors',
                        type=str)
    parser.add_argument('--remove_salt',
                        action=argparse.BooleanOptionalAction,
                        default='--remove_salt',
                        help='Removing salts from SMILE.',
                        type=bool)

    args = parser.parse_args()
    return args
