with open('bng.txt', 'r') as f:
    lines = f.readlines()
address = []
for i in lines:
    if 'ঠিকানা' in i:
        address.append(i.replace(']', '').replace('[', '').replace('<', '').replace(')', '').replace('\n', ''))
    elif 'ডাকঘর' in i:
        address.append(i.replace(']', '').replace('[', '').replace('<', '').replace(')', '').replace('\n', ''))
    elif 'উপশহর' in i:
        address.append(i.replace(']', '').replace('[', '').replace('<', '').replace(')', '').replace('\n', ''))

print(address)