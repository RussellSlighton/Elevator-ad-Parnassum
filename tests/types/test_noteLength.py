from src.types2.noteLength import NoteLength

def testNoteLengthActsLikeNum():
    assert NoteLength.WHOLE + NoteLength.WHOLE == NoteLength.HALF, "NoteLength should act like an int"

def testWholeNoteLength():
    assert NoteLength.WHOLE == 1, "There should be one whole notes per bar"

def testHalfNoteLength():
    assert NoteLength.HALF == 2, "There should be two half notes per bar"

def testQuarterNoteLength():
    assert NoteLength.QUARTER == 4, "There should be four quarter notes per bar"

def testEighthNoteLength():
    assert NoteLength.EIGHTH == 8, "There should be eight eighth notes per bar"
