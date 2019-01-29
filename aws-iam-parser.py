#!/usr/bin/env python3

import sys
import json

# Get these from curl -s http://169.254.169.254/latest/meta-data/iam/security-credentials/<profile_name>
iam_security_creds = json.loads(sys.stdin.read())

print("export AWS_ACCESS_KEY_ID=%s" % iam_security_creds['AccessKeyId'])
print("export AWS_SECRET_ACCESS_KEY=%s" % iam_security_creds['SecretAccessKey'])
print("export AWS_SESSION_TOKEN=%s" % iam_security_creds['Token'])