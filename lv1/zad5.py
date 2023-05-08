
with open('lv1\SMSSpamCollection.txt', 'r') as f:
    SMS = f.readlines()

# inicijalizacija varijabli
ham_count = 0
spam_count = 0
ham_word_count = 0
spam_word_count = 0

spam_exclamation_count = 0

# prolazak kroz svaku liniju datoteke
for line in SMS:
    # dijeljenje linije na labelu (ham ili spam) i tekst poruke
    label, message = line.strip().split('\t')
    # brojanje poruka tipa ham i spam
    if label == 'ham':
        ham_count += 1
        # brojanje riječi u porukama tipa ham
        ham_word_count += len(message.split())
    else:
        spam_count += 1
        # brojanje riječi u porukama tipa spam
        spam_word_count += len(message.split())
        # brojanje poruka tipa spam koje završavaju uskličnikom
        if message[-1] == '!':
            spam_exclamation_count += 1

# izračun prosječnog broja riječi u porukama tipa ham i spam
ham_avg = ham_word_count / ham_count
spam_avg = spam_word_count / spam_count

# ispis rezultata
print('Prosječan broj riječi u porukama koje su tipa ham:', ham_avg)
print('Prosječan broj riječi u porukama koje su tipa spam:', spam_avg)
print('Broj poruka tipa spam koje završavaju uskličnikom:', spam_exclamation_count)
