import emoji

emojis_disponiveis = {
    ":red_heart:": emoji.emojize(":red_heart:"),
    ":thumbs_up:": emoji.emojize(":thumbs_up:"),
    ":thinking_face:": emoji.emojize(":thinking_face:"),
    ":sunglasses:": emoji.emojize(":sunglasses:"),
    ":partying_face:": emoji.emojize(":partying_face:"),
    ":smiling_face_with_halo:": emoji.emojize(":smiling_face_with_halo:"),
    ":dotted_line_face:": emoji.emojize(":dotted_line_face:"),
    ":exploding_head:": emoji.emojize(":exploding_head:"),
    ":pile_of_poo:": emoji.emojize(":pile_of_poo:"),
    ":face_with_symbols_on_mouth:": emoji.emojize(":face_with_symbols_on_mouth:"),
}

print("Emojis disponíveis:")
for emoji_text, emoji_symbol in emojis_disponiveis.items():
    print(f"{emoji_text} - {emoji_symbol}")
print("")
print("Digite uma frase e ela será emojizada: ")
frase_codificada = input("")

frase_decodificada = emoji.emojize(frase_codificada)

print("Frase emojizada: ")
print(frase_decodificada)