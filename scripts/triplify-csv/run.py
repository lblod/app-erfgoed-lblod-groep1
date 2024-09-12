from triplify_csv.triplify_csv import Rml, CsvOptions

def main():
    # config mapping files are .ttl files
    configfile = "config/erfgoed-config.ttl"

    # csv files should be .csv files
    # csvfile1, csvfile2 = 'mycsv1.csv', 'mycsv2.csv'
    csvfile = "csv/erfgoed.csv"

    # output file must have either a .ttl extension for turtle triples
    # or a .nq extension for quads
    outputfile = "erfgoed.ttl"

    rml = Rml()

    # default date format of dates in your CSV files is '%Y-%m-%d'
    # default csv delimiter is ','
    # override the defaults by setting options
    options = CsvOptions(dateformat="%d/%m/%Y", delimiter="	")

    # load one rml and one or more csvs
    rml.loadFile(configfile, [csvfile], options)

    rml.create_triples()

    # "nquads" for named graphs need a .nq extension
    # here we are generating triples so .ttl for turtle syntax
    rml.write_file(outputfile, format="ttl")


if __name__ == "__main__":
    main()
