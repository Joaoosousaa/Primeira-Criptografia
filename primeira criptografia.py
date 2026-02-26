def cifrar_cesar (palavra, chave):
  texto_cifrado = ""
  for caractere in palavra:
      novo_char = chr((ord(caractere) + chave))
      texto_cifrado += novo_char
  return texto_cifrado

def decifrar_cesar (texto_cifrado, chave):
  return cifrar_cesar(texto_cifrado, - chave)



palavra_original = "Python"
chave = 3
palavra_cifrada = cifrar_cesar(palavra_original, chave)
print(f"Original:{palavra_original}")
print(f"Cifrada:{palavra_cifrada}")
print(f"Decifrada: {decifrar_cesar(palavra_cifrada,chave)}")