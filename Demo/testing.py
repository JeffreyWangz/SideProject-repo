# import base64
# # base64解码(解成二进制串)
# decode_jpg = base64.b64decode(a)
# # print(decode_jpg)
# # 写入jpg文件
# with open('./new.jpg', 'wb') as f:
#     f.write(decode_jpg)

# query = """{
#     getAemassQeDevMainWorkFlowStatus(id: "ID_PARA"){
#         end
#         stages
#         id
#         start
#         status
#         type
#     }
# }"""


# query = query.replace("ID_PARA", "123456")
# print(query)

import os

def list_files(startpath):

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        a = (root.replace(startpath, '')).count('\\')
        if((root.replace(startpath, '')).count('\\') <= 5):
            print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        a = (root.replace(startpath, '')).count('\\')
        if((root.replace(startpath, '')).count('\\') <= 4):
            for f in files:
                print('{}{}'.format(subindent, f))

list_files("C:/dev/Phy Mobile Lite/phy-mobile-lite")


# a = 'C:/dev/Python'
# root = 'C:/dev/Python\\.vscode'
# root = root.replace(a,'')
# print(root)
# print(root.count('\\'))