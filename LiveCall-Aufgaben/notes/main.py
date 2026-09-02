# Hausaufgabe LiveCall

notes = [
    {"title": "Einkauf", "text": "Milch, Brot, Eier"},
    {"title": "Arbeit", "text": "Backendcall um 11"},
]

def show_notes():
    for note in notes:
        print(f"Title: {note['title']}, Text: {note['text']}")

def add_note(title, text):
    notes.append({"title": title, "text": text})

def delete_note(title):
    for note in notes:
        if note["title"] == title:
            notes.remove(note)
    
def update_note(oldTitle, newTitle, newText):
    for note in notes:
        if note["title"] == oldTitle:
            index = notes.index(note)
    notes[index] = {"title": newTitle, "text": newText}

add_note("Hausarbeit", "Fußboden wischen")
show_notes()
print("----")
delete_note("Hausarbeit")
show_notes()
print("----")
update_note("Arbeit", "Arbeit2", "Backendcall um 13 Uhr")
show_notes()

# ----
# Übung Logische Operatoren
# 1. Welche Wahrheitswerte kommen bei den folgenden Ausdrücken heraus? 
#  True and False and True or False - 1 && 0 && 1 // 0 Immer False
#  not False or not True -> Immer True
#  True and (False or not False) -> Immer true 
#  not (not False ^ True or not False) -> False
#  True and False ^ True and False -> False

# 2. Worin besteht der Unterschied zwischen den Operatoren ^ und or?
# ^ist ein X-or, welches besagt entweder oder. Es können aber nicht beide Bedingungen gleichzeitig true oder false sein.

# 3. Welche Wahrheitswerte kommen als Ergebnis heraus?
#  2 < 3 and not 2 > 5 -> True
#  not True ^ False or 3 == 2 + 1 -> True
#  not not not 2 % 5 == 7 % 5 -> False
#  True and False ^ True and False -> False
#  True ^ False ^ 0 ^ 1 ^ (2 > 3) -> False