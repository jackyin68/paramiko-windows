import paramiko

def python_cmd(ssh):
    command = "cd D:\\Projects\\paramiko-windows\\remote && d: && call D:\\Projects\\paramiko-windows\\env\\Scripts\\activate.bat && python task.py"
    stdin, stdout, stderr = ssh.exec_command(command)
    ssh.close()

def exe_cmd():
    ssh = create_ssh()
    command = "cmd /k notepad.exe"
    stdin, stdout, stderr = ssh.exec_command(command)
    ssh.close()

def wmic_cmd():
    ssh = create_ssh()
    command = "wmic process get Caption"
    # command = "hostname"
    # command = 'wmic cpu get LoadPercentage'
    # command = "wmic process where name='pycharm64.exe' call terminate"
    # command = "wmic service list brief"
    # command = "call D:\\Projects\\paramiko-windows\\remote\\wmic.bat"
    command = "wmic process where name='pycharm64.exe'"
    command = "wmic process where name='notepad.exe'"

    stdin, stdout, stderr = ssh.exec_command(command)
    stdout.channel.shutdown_write()
    std_out = stdout.read().decode('gbk')
    std_out = std_out.replace('\n','').replace('\r','')
    if len(std_out) == 0:
        print("not any output")
    std_err = stderr.read().decode('gbk')
    print("stdin",stdin)
    print("std_out",std_out)
    print("std_err",std_err)
    ssh.close()

def create_ssh():
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('127.0.0.1', username='test', password='test123')
    shell = ssh.invoke_shell()
    return ssh


if __name__ == '__main__':
    wmic_cmd()
    exe_cmd()
    wmic_cmd()
