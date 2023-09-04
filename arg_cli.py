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
    parser.add_argument('--remove_salt',
                        action=argparse.BooleanOptionalAction,
                        default='',
                        help='Removing salts from SMILE.',
                        type=bool)
    parser.add_argument('--method',
                        choices=['all','descriptor','fingerprint'],
                        default='all',
                        help='Calculation descriptors and/or fingerprint',
                        type=str)
    parser.add_argument('--fp_type',
                        choices=['Morgan', 'RDKit', 'Atom', 'MACCS', 'Topological'],
                        default='Morgan',
                        help='(Optional) Types of Fingerprint',
                        type=str)
    parser.add_argument('--n_bits',
                        default=2048,
                        help='(Optional) Number of bits of a given fingerprints type',
                        type=int)

    args = parser.parse_args()
    return args
