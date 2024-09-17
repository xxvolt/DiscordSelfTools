from collections import defaultdict

def userLookup(user):
    with open("output.txt", "r") as f:
        messages = defaultdict(str)
        for line in f:
            if "Message by" in line:
                start_index = line.find("by ") + 3
                end_index = line.find(" in ", start_index)
                username = line[start_index:end_index]

                messages[username] += line
        return messages[user]
inpt = input("Enter the username to look for: ")
if inpt[-2:] != "#0":
    inpt = inpt + "#0"
print(f"{userLookup(inpt)}\n{inpt} has sent {userLookup(inpt).count("\n") + 1} messages ")
