import argparse

from dwdapi.dwd.temperature_hourly import TemperatureHourly



if __name__ == '__main__':

    # parser arguments
    parser = argparse.ArgumentParser(
    description="Download weather data from Deutscher Wetterdienst (DWD)",
    epilog="Please note that for data older than 500 days, the complete dataset has to be downloaded which can take a while")

    parser.add_argument(
        'product', help='specify product to download from DWD (e.g. "temp_hourly")')

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('--all', dest='load_all',
                    action='store_true', help='download all available data')

    group.add_argument('--last', dest='last', metavar='n',
                    help='download data for the last n days', type=int)

    args = parser.parse_args()
    #print("VM arguments:", args)


    # check if arguments are valid

    if args.load_all is None and args.last is None:
        raise Exception("Neither --all nor --last was specified!")

    # --last
    if args.last is not None:
        if args.last < 1:
            raise Exception("Please enter a negative integer value for --last!")




    # TODO: build mechanism to instantiate appropriate class
    product = TemperatureHourly(args.product, load_all=args.load_all, last=args.last)
    product.download()
    product.print()

