## Application for SMILE to descriptors and fingerprint generators

### To run this application you need to provide a csv file as input and it'll return you a csv file with molecule descriptors as output.

`
python fingerprint_and_descriptor.py --input_file data/smiles_input.csv --output_file data/smile.csv --remove_salt --method descriptors
`

You can run this application in three way:

1. Only Descriptor
2. Only Fingerprint
3. Descriptor and Fingerprint combined

1. When you are need only the descriptor file you need run as :

`python fingerprint_and_descriptor.py --input_file data/smiles_input.csv --output_file data/smile.csv --remove_salt --method descriptor`

It'll produce your <input filename>_descriptor.csv with the necessary header and value. 

2. When you are needed for fingerprint you need to run :

`python fingerprint_and_descriptor.py --input_file data/smiles_input.csv --output_file data/smile.csv --remove_salt --method fingerprint --fp_type Morgan --n_bits 1024`

In fingerprint types there are 5 different types of fingerprint added:
### Morgan
### RDKit
### Atom
### MACCS
### Topological
Default fingerprint type is Morgan and default n_bits is 2048

As an output it'll produce <input filename>_fingerprint.csv

3. When you need both descriptor and fingerprint together, you need to run :

`python fingerprint_and_descriptor.py --input_file data/smiles_input.csv --output_file data/smile.csv`

It'll give you output as <input filename>_descriptor_and_fingerprint.csv



There is also another parameter added to removing salts from the smiles. If you want to remove salts from molecule you need to add `--remove_salt` as a parameter in your cli. By default the remove_salt parameter is off. 



