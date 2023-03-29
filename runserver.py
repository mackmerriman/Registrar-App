
# !/Users/mackmerriman/cos333/A3-cos333/runserver.py

# Author: Mack Merriman
#-----------------------------------------------------------------------

import sys
import argparse
import reg

def main():

    parser = argparse.ArgumentParser(description="The registrar \
                                     application",
                                     allow_abbrev=False)

    # add an argument for each possible flag.
    parser.add_argument("port", type=int,
                        help="the port at which the server \
                        should listen")

    args = parser.parse_args()
    port = args.port

    try:
        reg.app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as ex:
        print(ex, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
