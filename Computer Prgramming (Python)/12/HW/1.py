# abb = {"be": "b", "because": "cuz", "see": "c", "the": "da", "okay": "ok", "are": "r", "you": "u",
#         "without": "w/o", "why": "y", "see you": "cu", "ate": "8", "great": "gr8", "mate": "m8",
#         "wait": "w8", "later": "l8r", "tomorrow": "2mro", "for": "4", "before": "b4", "once": "1ce",
#         "and": "&", "Your": "ur", "You're": "ur", "As far as I know": "afaik", "As soon as possible": "ASAP",
#         "At the moment": "atm", "Be right back": "brb", "By the way": "btw", "For your Information": "FYI",
#         "In my humble opinion": "imho", "In my opinion": "imo", "Laughing out loud": "lol", "Oh my god": "omg",
#         "Rolling on the floor laughing": "rofl", "Talk to you later": "ttyl"}

# def textese(txt):
#     new = txt
#     for k in sorted(abb, key=len, reverse=True):  
#         new = new.replace(k, abb[k])
#     return new


# txt1 = 'For your Information Imma be back later'
# txt2 = 'I am Rolling on the floor laughing'
# txt3 = "In my humble opinion, You're so cute, I want to Talk to you later"
# print(textese(txt3))


# def untextese(s):
#     reversed_abb = {v: k for k, v in abb.items()}
#     words = s.split()
#     new = []
#     for word in words:
#         if word in reversed_abb:
#             new.append(reversed_abb[word])
#         else:
#             new.append(word)

#     return ' '.join(new)


# txt4 = "FYI Imma b back l8r"
# txt5 = "I am rofl"
# txt6 = "imho , ur so cute, I want to ttyl"
# # print(untextese(txt4))  
# # print(untextese(txt5)) 
# print(untextese(txt6))  
def textese(text):
    word_dict = {'as far as I know': 'afaik',
                 'as soon as possible': 'ASAP',
                 'at the moment': 'atm',
                 'be right back': 'brb',
                 'by the way': 'btw',
                 'for your information': 'FYI',
                 'in my humble opinion': 'imho',
                 'in my opinion': 'imo',
                 'laughing out loud': 'lol',
                 'oh my god': 'omg',
                 'rolling on the floor laughing': 'rofl',
                 'talk to you later': 'ttyl',
                }
    word_replace = {'be': 'b', 
                    'because': 'cuz',
                    'see': 'c', 
                    'the': 'da', 
                    'okay': 'ok',
                    'are': 'r',
                    'you': 'u',
                    'without': 'w/o',
                    'why': 'y',
                    'see you': 'cu',
                    'ate': '8',
                    'great': 'gr8',
                    'mate': 'm8',
                    'wait': 'w8',
                    'later': 'l8r',
                    'tomorrow': '2mro',
                    'for': '4',
                    'before': 'b4',
                    'once': '1ce',
                    'and': '&',
                    "you're": "ur",
                    'your': 'ur',
                    }

    for phrase, abbrev in word_dict.items():
        text = text.replace(phrase, abbrev)

    words = text.split()
    output_words = []

    for word in words:
        output_words.append(word_replace.get(word.lower(), word))

    return ' '.join(output_words).replace(" ,", ",")

text = "Why you're so cute,by the way don't forget the party tomorrow, talk to you later"
output = textese(text)

print(output)
