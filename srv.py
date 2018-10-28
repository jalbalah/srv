

import os
import datetime
import argparse




if __name__ == '__main__':
    DEPLOY_DIR = os.path.join(os.getcwd(), 'deploy')
    deploy = lambda x: os.path.join(DEPLOY_DIR, x)
    RUN_FILE = ('run.sh', "python main.py")

    version_missing = lambda: \
        True if 'version' not in args or not args.version else False

    def check_version_missing(raise_error=True):
        if version_missing():
            if raise_error:
                raise Exception('Missing version number')
            else:
                return True

    parser = argparse.ArgumentParser(__name__)
    parser.add_argument('-l', '--list',
                        action="store_true",
                        help='show services')
    parser.add_argument('-i', '--install',
                        type=str,
                        help='install service name')
    parser.add_argument('-v', '--version',
                        type=float,
                        help='version for service name')
    parser.add_argument('-f', '--files',
                        help='show files for service name')
    parser.add_argument('-F', '--Files',
                        help='show files for service name of version')
    parser.add_argument('-d', '--deploy',
                        help='set the active service version')
    parser.add_argument('-s', '--start',
                        help='start service name active version')
    parser.add_argument('-c', '--clean',
                        help='clean service name version or "ALL <service>"')
    args = parser.parse_args()

    # install new service version
    if args.install:
        check_version_missing()
        dsn = os.path.join(deploy(args.install), str(args.version))
        os.system('rm -rf {} && mkdir {}'.format(dsn, dsn))
        dsn2 = os.path.join(dsn, RUN_FILE[0])
        with open(dsn2, 'w', encoding='utf-8') as wf:
            wf.write(RUN_FILE[1])
        os.system('cp -rf * {} 2> out.txt'.format(dsn))
        os.system('rm out.txt')
        os.system('rm {}/out.txt && rm -rf {}/deploy'.format(dsn, dsn))
        os.system('rm {}/install.sh && rm -rf {}/README.md'.format(dsn, dsn))
        path = os.path.join(dsn, 'timestamp.txt')
        with open(path, 'w') as wf:
            wf.write('{}\n'.format(str(datetime.datetime.now())))
        print('Installed {}'.format(args.install))

    # list services
    elif args.list:
        try:
            files = os.listdir(DEPLOY_DIR)
            if not files:
                raise FileNotFoundError()
            print('\n'.join([x for x in files]))
        except FileNotFoundError:
            print('No services exist')

    # view service versions
    elif args.files:
        path = deploy(args.files)
        os.system('ls -a --color=auto {}'.format(path))

        # view service versions
    elif args.Files:
        check_version_missing()
        path = os.path.join(deploy(args.Files), str(args.version))
        os.system('ls -a --color=auto {}'.format(path))
        os.system('cat {}'.format(os.path.join(path, 'timestamp.txt')))

    # set versions.txt to version number
    elif args.deploy:
        check_version_missing()
        path = os.path.join(deploy(args.deploy), 'version.txt')
        with open(path, 'w') as wf:
            wf.write('{}\n'.format(str(args.version)))
        print('Wrote version.txt as: ', args.version)

    # run main.py from deployed service version
    elif args.start:
        if not args.version:
            try:
                path = os.path.join(deploy(args.start), 'version.txt')
                with open(path) as rf:
                    version = rf.read().strip()
                path = os.path.join(deploy(args.start), version, RUN_FILE[0])
                res = os.system('bash {}'.format(path))
            except FileNotFoundError:
                print('Try --deploy')
        else:
            try:
                path = os.path.join(deploy(args.start), str(args.version), RUN_FILE[0])
                res = os.system('bash {}'.format(path))
            except FileNotFoundError:
                print('Try --deploy')

    # erase deploy dir (all) or service version
    elif args.clean:
        cmd = args.clean.strip().split(' ')
        if cmd[0].upper() == 'ALL':
            rsp = input('Should you remove all files?! yes/no:  ')
            if rsp.strip() == 'yes':
                os.system('rm -rf {}'.format(deploy(cmd[1])))
                print('All files removed from {}'.format(cmd[1]))
            else:
                print('Operation canceled :)')
        else:
            check_version_missing()
            path = os.path.join(deploy(args.clean), str(args.version))
            os.system('rm -rf {}'.format(path))

    else:
        print('Try --help')
