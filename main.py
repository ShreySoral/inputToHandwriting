import pywhatkit as pw
txt = input("Enter the text: ")
color = (255, 0, 0)  # red color
pw.text_to_handwriting(txt, "demo1.png", color)
print("END")
