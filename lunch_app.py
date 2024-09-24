from python.yfks_model import YFKS

model = YFKS()

print(model.send_chat("自己紹介がてら、アシスタントとして、あなたのできることを簡潔に纏めてください。").text)

is_end = False

while not is_end:
    mes = input("You >")
    print(model.send_chat(mes).text)
