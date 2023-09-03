
from utils import Molecule


def convert_to_molecule(smiles: str):
    try:
        return Molecule(smiles)
    except ValueError:
        return None