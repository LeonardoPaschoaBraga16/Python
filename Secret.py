import pygame

pygame.mixer.init()

pygame.mixer.music.load('yamete.wav')

pygame.mixer.music.play()

def medepau(a):
	tamanhopau = round(a * 100 / 161)
	utero = round(a * 7.5 / 161, 2)
	largura = tamanhopau * 3 / 100
	tamanhopau = round(8 * tamanhopau / 100 + 6, 2)
	print('a', nome, 'aguenta uma rola de até',tamanhopau,'cm de tamanho e',largura,'cm de largura sem se machucar\nCuriosidade: a',nome,'tem um útero de',utero,'cm')

nome = str(input('Nome da personagem: '))
tamanho = float(input('Tamanho da personagem: '))

medepau(tamanho)