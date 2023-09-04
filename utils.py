from rdkit.Chem import MolFromSmiles, SaltRemover, MolToSmiles, AllChem, MACCSkeys, RDKFingerprint
from rdkit.Chem.Descriptors import CalcMolDescriptors

class Molecule:
	def __init__(self, smiles: str):

		if not smiles :
			print("Empty smiles are given")
			sys.exit()
		self.smiles = smiles
		self.mol = MolFromSmiles(smiles)
		self.clean_smiles = None

	def remove_salt(self):
		salt_remover = SaltRemover.SaltRemover()
		self.mol = salt_remover.StripMol(self.mol, dontRemoveEverything=True, sanitize=True)
		self.clean_smiles = MolToSmiles(self.mol)

	def descriptor_generator(self):
		return CalcMolDescriptors(self.mol)

	def fingerprint_generator(self, fp_type: str, n_bits: int=2048):
		fingerprint_type = {
		'Morgan': AllChem.GetMorganFingerprintAsBitVect,
		'RDKit': RDKFingerprint,
		'Atom': AllChem.GetHashedAtomPairFingerprintAsBitVect,
		'MACCS': MACCSkeys.GenMACCSKeys,
		'Topological': AllChem.GetHashedTopologicalTorsionFingerprintAsBitVect
		}

		if fp_type not in fingerprint_type:
			print("Unknown Fingerprint")
			sys.exit()
		if n_bits < 1:
			print("Number of bits can't be less than 1")
			sys.exit()
		fingerprint_function = fingerprint_type[fp_type]
		if fp_type == 'Morgan':
			fingerprint= fingerprint_function(self.mol, 2, nBits=n_bits)
		elif fp_type == 'MACCS':
			fingerprint = fingerprint_function(self.mol)
		else:
			fingerprint = fingerprint_function(self.mol, nBits=n_bits)

		fingerprint_list = fingerprint.ToList()
		fingerprint_dict = {f'{fingerprint_type}_{i}': int(bit) for i, bit in enumerate(fingerprint_list)}

		return fingerprint_dict

		
