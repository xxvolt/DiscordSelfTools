from collections import defaultdict
import time

def count_messages(file_path):
    user_message_count = defaultdict(int)

    # Apri il file e leggi riga per riga
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Estrai il nome utente dalla riga
            if "Message by" in line:
                # Trova l'inizio e la fine del nome utente
                start_index = line.find("by ") + 3  # Posizione dopo "by "
                end_index = line.find(" in ", start_index)  # Trova " in " dopo il nome utente
                username = line[start_index:end_index]

                # Incrementa il conteggio dei messaggi per l'utente
                user_message_count[username] += 1

    return user_message_count

def display_leaderboard(user_message_count):
    sorted_users = sorted(user_message_count.items(), key=lambda item: item[1], reverse=True)
    content = "Leaderboard:\n"
    for user, count in sorted_users[:5]:
        content += f"{user}: {count} messages\n"
    return content

while True:
    file_path = 'output.txt'
    message_counts = count_messages(file_path)
    time.sleep(5)
    if message_counts:
        with open("Leaderboard.txt", "w") as f:
            f.write(display_leaderboard(message_counts))

    else:
        print("No messages found.")
