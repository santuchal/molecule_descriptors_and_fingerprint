import os
import sys
import pandas as pd
from tqdm import tqdm

from arg_cli import _parse_args
from helper import convert_to_molecule

# from file import function

def main():
	args = _parse_args()
	smiles_from_file = pd.read_csv(args.input_file)
	smiles_from_file.rename(columns=lambda x: x.title(), inplace=True)

	if 'Smiles' not in smiles_from_file.columns:
		print("Inn file there is no smiles columns")
		sys.exit()

	tqdm.pandas(desc='Converting SMILES to mol objects.....')
	moles = smiles_from_file['Smiles'].progress_apply(convert_to_molecule).dropna()

	if args.remove_salt:
		tqdm.pandas(desc="Removing Salts .....")
		moles.progress_apply(lambda mol: mol.remove_salt())

	if args.method == 'descriptors':
		tqdm.pandas(desc='Calculating descriptors.....')
		descriptors = moles.progress_apply(lambda mol: mol.descriptor_generator())
		descriptors = pd.DataFrame(descriptors.to_list(), index=descriptors.index)
		all_descriptors = pd.merge(smiles_from_file, descriptors, how='left', left_index=True, right_index=True)
		all_descriptors.to_csv(args.output_file, index=False)

if __name__ == '__main__':
    main()