

import os
import argparse




if __name__ == '__main__':
    DEPLOY_DIR = os.path.join(os.getcwd(), 'deploy')
    deploy = lambda x: os.path.join(DEPLOY_DIR, x)
    version_missing = lambda: \
        True if 'version' not in args or not args.version else False
    RUN_FILE = ('run.sh', "python main.py")
    parser = argparse.ArgumentParser(__name__)

    parser.add_argument('-i', '--install',
                        type=str,
                        help='install service name')
    parser.add_argument('-v', '--version',
                        type=float,
                        help='version for service name')
    parser.add_argument('-l', '--list',
                        action="store_true",
                        help='show services')
    parser.add_argument('-f', '--files',
                        help='show files for service name')
    parser.add_argument('-s', '--start',
                        help='start service name')
    parser.add_argument('-c', '--clean',
                        help='clean one or "ALL" services')
    parser.add_argument('-d', '--deploy',
                        help='set the active service version')

    args = parser.parse_args()
    if args.install:
        if version_missing():
            raise Exception('Missing version number')
        dsn = os.path.join(deploy(args.install), str(args.version))
        os.system('rm -rf {} && mkdir {}'.format(dsn, dsn))
        dsn2 = os.path.join(dsn, RUN_FILE[0])
        with open(dsn2, 'w', encoding='utf-8') as wf:
            wf.write(RUN_FILE[1])
        dsn3 = os.path.join(dsn, 'main.py') # to do VERSIONING
        with open(dsn3, 'w') as wf:
            with open('main.py') as rf:
                wf.write(rf.read())
        print('Installed {}'.format(args.install))
    elif args.list:
        try:
            files = os.listdir(DEPLOY_DIR)
            print('\n'.join([x for x in files]))
        except FileNotFoundError:
            print('No services exist')
    elif args.start:
        path = deploy(args.start, RUN_FILE[0])
        res = os.system('bash {}'.format(path))
    elif args.files:
        path = deploy(args.files)
        os.system('ls -a --color=auto {}'.format(path))
    elif args.clean:
        if args.clean.strip().upper() == 'ALL':
            rsp = input('Should you remove all files?! yes/no:  ')
            if rsp.strip() == 'yes':
                os.system('rm -rf {}'.format(DEPLOY_DIR))
                print('All files removed!')
            else:
                print('Operation canceled :)')
        else:
            if version_missing():
                raise Exception('Missing version number')
            path = deploy(args.clean, args.version)
            os.system('rm -rf {}'.format(path))
    elif args.deploy:

        path = deploy()
    else:
        print('Try --help')
