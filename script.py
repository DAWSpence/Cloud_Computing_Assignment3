from collections import Counter
import re
import os
import socket



if1_path = '/home/data/IF-1.txt'
always_path = '/home/data/AlwaysRememberUsThisWay-1.txt'
output_dir = '/home/data/output/result.txt'




def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address





def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read().lower()  
    content = re.sub(r"(\b\w+)'(\w+\b)", r"\1 \2", content)
    words = re.findall(r'\w+', content)
    return words

    

    

def main():


    if1_words = read_file(if1_path)
    always_words = read_file(always_path)


    if1_total = len(if1_words)
    always_total = len(always_words)
    grand_total_words = if1_total + always_total



    if1_count = Counter(if1_words)
    top_3_file_1 = if1_count.most_common(3)


    always_count = Counter(always_words)
    top_3_file_2 = always_count.most_common(3)


    ip_address = get_ip_address()








    result = (
        f"Total words in IF-1.txt: {if1_total}\n"
        f"Total words in AlwaysRememberUsThisWay-1.txt: {always_total}\n"
        f"Grand total words: {grand_total_words}\n\n"
        f"\nIP Address of the container: {ip_address}\n"
    )



    result+= f"Top 3 most frequent words in IF-1.txt:\n"
    for word, count in top_3_file_1:
        result += f"{word}: {count}\n"


    result+= f"Top 3 most frequent words in AlwaysRememberUsThisWay-1.txt:\n"
    for word, count in top_3_file_2:
        result += f"{word}: {count}\n"



    with open(output_dir, 'w') as output_file:
        output_file.write(result)



    print(result)

if __name__ == '__main__':
    main()
