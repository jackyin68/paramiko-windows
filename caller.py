import paramiko

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1', username='test', password='test123')
shell=ssh.invoke_shell()

command = "cd D:\\Projects\\paramiko-windows\\remote && d: && call D:\\Projects\\paramiko-windows\\env\\Scripts\\activate.bat && python task.py"
stdin, stdout, stderr = ssh.exec_command(command)
ssh.close()

# stdout.channel.shutdown_write()
# std_out = stdout.read().decode('gbk')
# std_err = stderr.read().decode('gbk')
# print("stdin",stdin)
# print("std_out",std_out)
# print("std_err",std_err)
