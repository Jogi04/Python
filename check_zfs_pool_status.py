import subprocess
from colorama import Fore


def check_zfs_pool_health():
    output_bytes = subprocess.Popen(['sudo', 'zpool', 'list', '-H', '-o', 'health'], stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
    output = output_bytes.stdout.read().decode('utf-8')
    output = output.replace('\n', '')
    if output != 'ONLINE':
        print(Fore.RED + 'ZFS Pool not healthy! Requires manual intervention.')


if __name__ == '__main__':
    check_zfs_pool_health()
