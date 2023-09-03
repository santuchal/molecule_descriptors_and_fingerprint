from rdkit.Chem import MolFromSmiles, SaltRemover, MolToSmiles# AllChem, MACCSkeys, RDKFingerprint
from rdkit.Chem.Descriptors import CalcMolDescriptors

class Molecule:
	def __init__(self, smiles: str):

		if not smiles :
			print("Empty smiles are given")
			exit(0)
		self.smiles = smiles
		self.mol = MolFromSmiles(smiles)
		self.clean_smiles = None

	def remove_salt(self):
		salt_remover = SaltRemover.SaltRemover()
		self.mol = salt_remover.StripMol(self.mol, dontRemoveEverything=True, sanitize=True)
		self.clean_smiles = MolToSmiles(self.mol)

	def descriptor_generator(self):
		return CalcMolDescriptors(self.mol)
