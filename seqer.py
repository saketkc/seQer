#!/usr/bin/env python
"""
Run pipelines, cleanly
"""

import subprocess
import ConfigParser
import io

class RawConfigParser:
    def __init__(self, location):
        self.config = ConfigParser.RawConfigParser(allow_no_value=True)
        self.config.readfp(io.BytesIO(location))

    def get_section(self, section):
        return self.config.get(section, section)


class Subprocessor:
    def __init__(self):
        self.cmd = ""
        self.stderr = None
        self.stdout = None
        self.returncode = None

    def cmd_formatter(self):
        return filter(lambda x: x!="", self.cmd.split(" "))

    def run(self):
        cmd = self.cmd_formatter()
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        returncode = p.returncode
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr
        return {'stdout': stdout, 'stderr': stderr, 'returncode': returncode}

if __name__ == "__main__":
    subp = Subprocessor()
    subp.cmd = "ls -l"
    run = subp.run()['stdout']
    assert(subp.returncode == 0)
