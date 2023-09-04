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

	if args.method == 'all':
		tqdm.pandas(desc='Calculating descriptors.....')
		descriptors = moles.progress_apply(lambda mol: mol.descriptor_generator())
		descriptors = pd.DataFrame(descriptors.to_list(), index=descriptors.index)
		tqdm.pandas(desc=f"Calculating { args.fp_type} fingerprints.....")
		fingerprints_dataframe = moles.progress_apply(lambda mol:mol.fingerprint_generator(args.fp_type, args.n_bits))
		fingerprints_dataframe = pd.DataFrame(fingerprints_dataframe.to_list(), index=fingerprints_dataframe.index)

		final_all = pd.merge(pd.merge(smiles_from_file,descriptors, how='left', left_index=True, right_index=True),fingerprints_dataframe, how='left', left_index=True, right_index=True)
		final_all.to_csv(args.output_file[:-4]+"_descriptor_and_fingerprint.csv", index=False)


	elif args.method == 'descriptor':
		tqdm.pandas(desc='Calculating descriptors.....')
		descriptors = moles.progress_apply(lambda mol: mol.descriptor_generator())
		descriptors = pd.DataFrame(descriptors.to_list(), index=descriptors.index)
		all_descriptors = pd.merge(smiles_from_file, descriptors, how='left', left_index=True, right_index=True)
		all_descriptors.to_csv(args.output_file[:-4]+"_descriptor.csv", index=False)

	elif args.method == 'fingerprint':
		tqdm.pandas(desc=f"Calculating { args.fp_type} fingerprints.....")
		fingerprints_dataframe = moles.progress_apply(lambda mol:mol.fingerprint_generator(args.fp_type, args.n_bits))
		fingerprints_dataframe = pd.DataFrame(fingerprints_dataframe.to_list(), index=fingerprints_dataframe.index)

		final_fingerprint = pd.merge(smiles_from_file,fingerprints_dataframe, how='left', left_index=True, right_index=True)
		final_fingerprint.to_csv(args.output_file[:-4]+"_fingerprint.csv", index=False)

if __name__ == '__main__':
    main()