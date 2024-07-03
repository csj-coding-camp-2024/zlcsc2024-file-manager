import shutil
import socket

computer_id = socket.gethostname().split("-")[1]

folder_path = "使用者/user/桌面/" + computer_id

shutil.make_archive(computer_id, 'zip', folder_path)
