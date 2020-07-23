# --------------
file = open(file_path, 'r')
sentence = print(file.readline())  
file.close()

file = open(file_path_1,'r')
message_1 = print(file.readline())
file = open (file_path_2,'r')
message_2 = print (file.readline())
def fuse_msg(message_a, message_b):
    quotient = (int(message_b)//int(message_a))
    return quotient
secret_msg_1 = fuse_msg(2222,2477) 
print(secret_msg_1)  

file = open(file_path_3 , 'r')
message_3 = file.read()
print(message_3)
def substitute_msg(message_c):
    if message_c == "Red":
        sub = 'Army General'
    if message_c == "Green":
        sub = 'Data Scientist'
    if message_c == "Blue":
        sub = 'Marine Biologist'
    return sub     
secret_msg_2 = substitute_msg(message_3)
print(secret_msg_2)

file = open (file_path_4,'r')
message_4 = file.read()
print(message_4)
file = open (file_path_5, 'r')
message_5 = file.read()
print(message_5)
def compare_msg(message_d, message_e):
    a_list = message_d.split()
    b_list = message_e.split()
    c_list = [i for i in a_list if i not in b_list]
    print(c_list)
    final_msg = " ".join(c_list)
    return final_msg
secret_msg_3 = compare_msg(message_4, message_5) 
print(secret_msg_3)  

file = open (file_path_6, 'r')
message_6 = file.read()
print(message_6)
def extract_msg(message_f):
    a_list = message_f.split()
    even_word = lambda x : len(x)%2==0
    b_list = filter(even_word, a_list)
    final_msg = " ".join(b_list)
    return final_msg
secret_msg_4 = extract_msg(message_6)
print(secret_msg_4)

message_parts = ["you are now", "1", "step closer to become", "Data Scientist"]
secret_msg = " ".join(message_parts)
final_path= user_data_dir + '/secret_message.txt'
file = open (file_path, 'a+')
file.write(secret_msg)
file.close()
print(secret_msg)


