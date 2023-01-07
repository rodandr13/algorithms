def braille(text, is_cyrillic=False):
    cyrillic = {
        "1": "а", "12": "б", "2456": "в", "1245": "г", "145": "д", "15": "е",
        "16": "ё", "245": "ж", "1356": "з", "24": "и", "12346": "й", "13": "к",
        "123": "л", "134": "м", "1345": "н", "135": "о", "1234": "п",
        "1235": "р", "234": "с", "2345": "т", "136": "у", "124": "ф",
        "125": "х", "12345": "ч", "156": "ш", "1346": "щ", "12356": "ъ",
        "2346": "ы",  "23456": "ь", "246": "э", "1256": "ю", "1246": "я",
        "256": ".",  "2": ",",  "235": "!",  "26": "?",  "36": "-",
        "126": "(",  "345": ")"
    }

    cyr_to_braille = {
        "а": 10241,  "б": 10243,  "в": 10298, "г": 10267, "д": 10265,
        "е": 10257, "ё": 10273, "ж": 10273, "з": 10293, "и": 10250,
        "й": 10287,  "к": 10245, "л": 10247, "м": 10253, "н": 10269,
        "о": 10261, "п": 10255, "р": 10263, "с": 10254, "т": 10270,
        "у": 10277, "ф": 10251, "х": 10259, "ц": 10249, "ч": 10271,
        "ш": 10289, "щ": 10285, "ъ": 10295, "ы": 10286, "ь": 10302,
        "э": 10282, "ю": 10291, "я": 10283, ".": 10290, ",": 10242,
        "!": 10251, "?": 10274, "-": 10276, "(": 10275, ")": 10268, " ": 32
    }

    converted_text = ""
    if not is_cyrillic:
        for word in text:
            chars = word.strip().split()
            for char in chars:
                converted_text += cyrillic.get(char, "")
            converted_text += " "
    else:
        for words in text:
            for char in words.strip():
                converted_text += chr(cyr_to_braille.get(char, 0))
    print(converted_text)


text = []
while True:
    line = input()
    if line == "end":
        break
    text.append(line)

braille(text)