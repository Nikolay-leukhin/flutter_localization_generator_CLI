
# Localization Tool

This tool is designed to localize data from CSV files into ARB format, which is used for internationalizing applications.

## Installation

1. Make sure you have Python 3.x installed.
2. Install the required pandas:

   ```bash
   pip install pandas

## Usage

### Start CLI
You can use the command line to generate ARB files from CSV data.

### Arguments
* csv_path: Path to the CSV file with localization data.
* keyname_column: The name of the column containing the keys for localization.
* --country: Name of the country for which the ARB file should be generated (optional).
* --output: The name of the output file for the ARB file (required if --country is specified).
* --all: Flag to generate ARB files for all countries in CSV (optional).


------
### Example of use for generating a specific localization
   ```bash
    python main.py path/to/localization.csv keyname_column --country country_name --output output_file_name.arb
   ```
    
### Example of use for generating all
! Important ! In this case the columns in the table should be the same as the localization keys, i.e. for example for Russian localization ru, and for English localization en. i.e. everything is as per l10n standard.

   ```bash
   python main.py path/to/localization.csv keyname_column --all
   ```

## Best structure for the file 
| KEYNAME_COLUMN | LOCALIZE CODE ONE | LOCALIZE CODE TWO | LOCALIZE CODE THREE |
|----------------|--------------------|--------------------|---------------------|
| greeting       | Hello              | Hola               | Bonjour             |
| farewell       | Goodbye            | Adiós              | Au revoir           |

#   f l u t t e r _ l o c a l i z a t i o n _ g e n e r a t o r _ C L I 
 
 
