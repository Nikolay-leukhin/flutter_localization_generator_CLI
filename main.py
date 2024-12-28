import argparse
from localizer import Localizer


def main():
    parser = argparse.ArgumentParser(description='Localization tool for CSV files.')
    parser.add_argument('csv_path', type=str, help='Path to the CSV file containing localization data.')
    parser.add_argument('keyname_column', type=str, help='Name of the column containing keys for localization.')
    parser.add_argument('--country', type=str, help='Name of the country for which to generate the ARB file.')
    parser.add_argument('--output', type=str, help='Output file name for the ARB file (if --country is specified).')
    parser.add_argument('--all', action='store_true', help='Load ARB files for all countries in the CSV.')

    args = parser.parse_args()
    localizer = Localizer(args.csv_path, args.keyname_column)

    if args.all:
        localizer.load_all_files()
        print("All ARB files have been generated.")
    elif args.country and args.output:
        localizer.load_arb_country_file(args.country, args.output)
        print(f"ARB file for {args.country} has been generated as {args.output}.")
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
