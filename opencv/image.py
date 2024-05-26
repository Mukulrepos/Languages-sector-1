# import os

# # Print the current working directory
# print("Current working directory:", os.getcwd())

# # Use the absolute path to the file
# file_path = 'D:/Languages sector 1/download.jpeg'

with open('x.mp4', 'rb')as f:
    m = f.read()
    # print(len(m))


with open('recived.mp4','wb') as q:
    q.write(m)
    