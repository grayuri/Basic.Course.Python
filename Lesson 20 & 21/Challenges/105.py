def getNotesSituation(*notes, situation=False):
  quantityOfNotes = len(notes)
  highestNote = -999
  lowestNote = 999
  totalOfNotes = 0
  actualSituation = ""

  for note in notes:
    if note > highestNote:
      highestNote = note
    
    if note < lowestNote:
      lowestNote = note
    
    totalOfNotes += note
  
  notesMedia = totalOfNotes / quantityOfNotes

  print(f"- Quantity of Notes: {quantityOfNotes}")
  print(f"- Highest Note: {highestNote:.1f}")
  print(f"- Lowest Note: {lowestNote:.1f}")
  print(f"- Notes Media: {notesMedia:.1f}")

  if situation == True:
    if (notesMedia >= 7): actualSituation = "Good"
    elif (notesMedia < 7): actualSituation = "Bad"

    print(f"- Situation: {actualSituation}")

getNotesSituation(8, 7, 6, 6, 4, 8, 9, 9.5, situation=True)