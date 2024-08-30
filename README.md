# Data dumper for Valve's Deadlock

### Requirements
- Deadlock installed
- Python 3.8 or higher
- dotnet SDK (and Runtime) 8.0 or higher (for extracting vdata files using [deadlockery](https://github.com/ouwou/deadlockery/))

### Usage
1. Clone the repository with submodules 
```
git clone --recurse-submodules https://github.com/STmihan/deadlock-data-extractor.git
```
2. All data in `data` folder
3. For updating the data, run
```
python extract.py
```
4. **Optional**: Maybe you will need to change `DEADLOCK_PATH` in config.py to the path of your Deadlock installation

### Data

- `data/heroes.json` - Contains all the heroes in the game and their abilities
- `data/items.json` - Contains all the items in the game
- `data/abilities`, `data/items`, `data/heroes` - Contains the extracted images of the abilities, items and heroes respectively
- `data/vdata` - Contains the extracted data from the game files (Thanks to [deadlockery](https://github.com/ouwou/deadlockery/))
- `DataTypes.py` - Contains the data types of json data files