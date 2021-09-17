import numpy as np
import cv2

imagem = cv2.imread("casa1.png")
print (imagem.shape)
altura, largura = imagem.shape[:2]
cv2.imshow("Original", imagem)

cv2.waitKey(0)

deslocamento = np.float32([[1, 0, 25], [0, 1, 50]])
deslocado = cv2.warpAffine(imagem, deslocamento, (largura, altura))
cv2.imshow("Baixo e direita", deslocado)

cv2.waitKey(0)

deslocamento = np.float32([[1, 0, -50], [0, 1, -90]])
deslocado = cv2.warpAffine(imagem, deslocamento, (largura, altura))
cv2.imshow("Cima e esquerda", deslocado)

cv2.waitKey(0)

ponto = (largura / 2, altura / 2) #ponto no centro da figura
rotacao = cv2.getRotationMatrix2D(ponto, 45, 1.0)
rotacionado = cv2.warpAffine(imagem, rotacao, (largura, altura))
cv2.imshow("Rotacionado 45 graus", rotacionado)

cv2.waitKey(0)

rotacao = cv2.getRotationMatrix2D(ponto, 120, 1.0)
rotacionado = cv2.warpAffine(imagem, rotacao, (largura, altura))
cv2.imshow("Rotacionado 120 graus", rotacionado)

cv2.waitKey(0)