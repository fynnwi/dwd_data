import argparse
import dwdapi.dwd.products as products


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
    print("VM arguments:", args)


    # check if arguments are valid

    if args.load_all is None and args.last is None:
        raise Exception("Neither --all nor --last was specified!")

    # --last
    if args.last is not None:
        if args.last < 1:
            raise Exception("Please enter a negative integer value for --last!")




    product = products.DWDProduct(args.product)
    product.print()



    # TODO implement the rest also
    if args.load_all is True or args.last > 500:
        warnings.warn("Loading data older than 500 days is not yet implemented! Only data from last 500 days will be loaded.")
