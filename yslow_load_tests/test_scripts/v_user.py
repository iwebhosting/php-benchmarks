import random
import subprocess
import json

class Transaction(object):

    def run(self):
        cmd_args = [
            'phantomjs', 'lib/js/yslow.js',
            '--info', 'stats',
            '--format', 'json',
            'http://localhost',
        ]
        proc = subprocess.Popen(
            cmd_args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        ret = proc.wait()
        if ret != 0:
            raise RuntimeError('Command failed: {}\n{}'.format(' '.join(cmd_args), proc.stderr.read()))
        data = json.load(proc.stdout)
        lt = data['lt']
        self.custom_timers['Response'] = int(lt) / 1000.0

if __name__ == '__main__':
    t = Transaction()
    t.run()
