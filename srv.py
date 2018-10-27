

import os
import argparse




if __name__ == '__main__':
    DEPLOY_DIR = os.path.join(os.getcwd(), 'deploy')
    RUN_FILE = ('run.sh', "echo hi")
    parser = argparse.ArgumentParser(__name__)

    parser.add_argument('-i', '--install',
                        type=str,
                        help='install service name')
    parser.add_argument('-l', '--list',
                        action="store_true",
                        help='show services')
    parser.add_argument('-s', '--start',
                        help='start service name')

    args = parser.parse_args()
    if args.install:
        dsn = os.path.join(DEPLOY_DIR, args.install)
        os.system('rm -rf {} && mkdir {}'.format(dsn, dsn))
        dsn2 = os.path.join(dsn, RUN_FILE[0])
        with open(dsn2, 'w', encoding='utf-8') as wf:
            wf.write(RUN_FILE[1])
        print('Installed {}'.format(args.install))
    elif args.list:
        try:
            files = os.listdir(DEPLOY_DIR)
            print('\n'.join([x for x in files]))
        except FileNotFoundError:
            print('No services exist')
    elif args.start:
        path = os.path.join(DEPLOY_DIR, args.start, RUN_FILE[0])
        res = os.system('bash {}'.format(path))
    else:
        print('Try --help')