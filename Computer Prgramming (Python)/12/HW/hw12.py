#Q1
abb = {"be": "b", "because": "cuz", "see": "c", "the": "da", "okay": "ok", "are": "r", "you": "u",
        "without": "w/o", "why": "y", "see you": "cu", "ate": "8", "great": "gr8", "mate": "m8",
        "wait": "w8", "later": "l8r", "tomorrow": "2mro", "for": "4", "before": "b4", "once": "1ce",
        "and": "&", "Your": "ur", "You're": "ur", "As far as I know": "afaik", "As soon as possible": "ASAP",
        "At the moment": "atm", "Be right back": "brb", "By the way": "btw", "For your Information": "FYI",
        "In my humble opinion": "imho", "In my opinion": "imo", "Laughing out loud": "lol", "Oh my god": "omg",
        "Rolling on the floor laughing": "rofl", "Talk to you later": "ttyl"}

def textese(txt):
    new = txt
    for k in sorted(abb, key=len, reverse=True):  
        new = new.replace(k, abb[k])
    return new


txt1 = 'For your Information Imma be back later'
txt2 = 'I am Rolling on the floor laughing'
txt3 = "In my humble opinion, You're so cute, I want to Talk to you later"
print(textese(txt3))


def untextese(s):
    reversed_abb = {v: k for k, v in abb.items()}
    words = s.split()
    new = []
    for word in words:
        if word in reversed_abb:
            new.append(reversed_abb[word])
        else:
            new.append(word)

    return ' '.join(new)


txt4 = "FYI Imma b back l8r"
txt5 = "I am rofl"
txt6 = "imho , ur so cute, I want to ttyl"
print(untextese(txt4))  
print(untextese(txt5)) 
print(untextese(txt6))  


#Q2
dict1 = {}
dict2 = {}
def composite(dict1, dict2):
    dict3 = {}
    for k1, v1 in dict1.items():
        for k2,v2 in dict2.items():
            if v1 == k2:
                dict3[k1] = v2

    return dict3


dict1 = {'a':'p', 'b':'r', 'c':'q', 'd':'p', 'e':'s'}
dict2 = {'p':'1','q':'2','r':'3'}

print(composite(dict1, dict2))


#Q3
def product(*sets):
    if not sets:
        return set([])
    if len(sets) == 1:
        return set([(item,) for item in sets[0]])
    
    sub_product = product(*sets[1:])
    cartesian = [(item,) + tuple_ for item in sets[0] for tuple_ in sub_product]
    return set(cartesian)

s1 = set([1,2,3])
s2 = set(['p','q'])
s3 = set(['a','b','c'])
print(product(s1,s2))
print(product(s1, s2, s3))
print(product(s1))