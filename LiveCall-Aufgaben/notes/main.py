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
            break
    
def update_note(oldTitle, newTitle, newText):
    for note in notes:
        if note["title"] == oldTitle:
            index = notes.index(note)
            break
    notes[index] = {"title": newTitle, "text": newText}

# delete_note()
add_note("Hausarbeit", "Fußboden wischen")
show_notes()
delete_note("Hausarbeit")
print("----")
show_notes()
update_note("Arbeit", "Arbeit2", "Backendcall um 13 Uhr")
print("----")
show_notes()
