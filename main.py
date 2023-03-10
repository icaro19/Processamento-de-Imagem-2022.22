from PIL import Image, ImageFilter
import pytesseract
import cv2
import numpy as np
from filtros import openimage, negative, grayscale


path = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = path + r"\tesseract.exe"

selecionada = 'img' + input("Digite um num de 1 a 6\n") + '.png'
img = openimage(selecionada)
img.save("tratada.png")

img = cv2.imread("tratada.png")

while True:

    print("0:Fecha e Lê\n 1: Escala de Cinza\n 2:Negativo\n 3:Contraste e Brilho\n 4:Erodir\n 5:Dilatar\n 6:Abertura ou Fecho\n 7:Reseta\n 8:Color map \n 9:Matrizes de Convolução\n 10:Blur\n 11:Blur Glaussin\n 12:Median Blur\n 13:Laplace\n 14:Mask\n 15:Sobel ")
    edita = int(input("Escolha\n"))

    match edita:
        case 0:
            break
#Escala de Cinza
        case 1:
            img = openimage("tratada.png")
            img = grayscale(img)
            img.save("tratada.png")
            img = cv2.imread("tratada.png")

#negativo
        case 2:
            img = openimage("tratada.png")
            img = negative(img)
            img.save("tratada.png")
            img = cv2.imread("tratada.png")

#Contraste e Brilho
        case 3:
            img = cv2.imread("tratada.png")
            Contraste = input("Contraste: 0 a 100\n")
            Brilho = input("Brilho: 0 a 100\n")
            img = cv2.convertScaleAbs(img, alpha=int(Contraste)/100, beta=int(Brilho))
            cv2.imwrite("tratada.png", img)

#Erosao
        case 4:
            img = cv2.imread("tratada.png")
            kernel = np.ones((3, 3), np.uint8)
            erosion = cv2.erode(img, kernel, iterations=10)
            cv2.imwrite("tratada.png", img)

#Dilatacao
        case 5:
            img = cv2.imread("tratada.png")
            kernel = np.ones((4, 4), np.uint8)
            dilation = cv2.dilate(img, kernel, iterations=10)
            cv2.imwrite("tratada.png", img)

#Op. morfologicas (abertura, fecho e gradiente)
        case 6:
            img = cv2.imread("tratada.png")
            kernel = np.ones((10, 10), np.uint8)
            op = int(input("1:ABERTURA\n 2:FECHO\n 3:GRADIENTE"))
            match op:
                case 1:
                    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
                    cv2.imwrite("tratada.png", img)
                case 2:
                    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
                    cv2.imwrite("tratada.png", img)
                case 3:
                    img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
                    cv2.imwrite("tratada.png", img)

#Reseta pra imagem original
        case 7:
             img = openimage(selecionada)
             img.save("tratada.png")
             img = cv2.imread("tratada.png")

#Filtro de cores (feature, não utilizamos nos testes)
        case 8:
            img = cv2.imread("tratada.png")
            print("1:AUTUM\n 2:BONE\n 3:WINTER\n 4:RAINBOW\n 5:OCEAN\n 6:SUMMER\n 7:SPRING\n 8:COOL\n 9:HSV\n 10:PINK\n 11:HOT\n 12:JET\n")
            cm = int(input("Color Map\n"))
            match cm:
                case 1:
                    img = cv2.applyColorMap(img, cv2.COLORMAP_AUTUMN)
                case 2:
                    img = cv2.applyColorMap(img, cv2.COLORMAP_BONE)
                case 3:
                    img = cv2.applyColorMap(img, cv2.COLORMAP_WINTER)
                case 4:
                    img = cv2.applyColorMap(img, cv2.COLORMAP_RAINBOW)
                case 5:
                    img = cv2.applyColorMap(img, cv2.COLORMAP_OCEAN)
                case 6:
                    img = cv2.applyColorMap(img, cv2.COLORMAP_SUMMER)
                case 7:
                    img = cv2.applyColorMap(img, cv2.COLORMAP_SPRING)
                case 8:
                    img = cv2.applyColorMap(img, cv2.COLORMAP_COOL)
                case 9:
                    img = cv2.applyColorMap(img, cv2.COLORMAP_HSV)
                case 10:
                    img = cv2.applyColorMap(img, cv2.COLORMAP_PINK)
                case 11:
                    img = cv2.applyColorMap(img, cv2.COLORMAP_HOT)
                case 12:
                    img = cv2.applyColorMap(img, cv2.COLORMAP_JET)
                    cv2.imwrite("tratada.png", img)

# Máscara de Convolução
        case 9:
            img = openimage("tratada.png")
            kernel_case9 = int(input(" 1:Traça a linha\n 2:Alteração Leve\n"))
            match kernel_case9:
                 case 1:
                    kernel_case9 = ImageFilter.Kernel((3, 3), (-1,-1,-1,-1,8,-1,-1,-1,-1,), 1, 0)
                 case 2:
                    kernel_case9 = ImageFilter.Kernel((3,3), (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,), 1, 0)
            img = img.filter(kernel_case9)
            img.save("tratada.png")
            img = cv2.imread("tratada.png")
# Passa Baixa (Blur, Blur Gaussiano e Median Blur)
        case 10:
            tamanho_do_blur = int(input("Quantidade de Blur\n"))
            img = cv2.imread("tratada.png")
            img = cv2.blur(img, (tamanho_do_blur,tamanho_do_blur))
            cv2.imwrite("tratada.png", img)
        case 11:
##            tamanho_do_blur = int(input("Quantidade de Blur\n"))
##            tamanho_da_destruicao = int(input("Quantidade de Destruição\n"))
            img = cv2.imread("tratada.png")
            img = cv2.GaussianBlur(img, (9, 9), cv2.BORDER_CONSTANT)
            cv2.imwrite("tratada.png", img)
        case 12:
#            tamanho_da_destruicao = int(input("Quantidade de Destruição\n"))
            img = cv2.imread("tratada.png")
            img = cv2.medianBlur(img, 9)
            cv2.imwrite("tratada.png", img)
#Passa Alta (Laplaciano)
        case 13:
            ker = int(input("ksize 3 ou 5\n"))
            img = cv2.imread("tratada.png")
            img = cv2.Laplacian(img, cv2.CV_64F, ksize = ker)
            cv2.imwrite("tratada.png", img)
#MASK (threshold)
        case 14:
            img = cv2.imread("tratada.png", 0)
            modo = int(input("1 Binário\n 2:Binário invertido\n 3:Adaptativo Mean\n "))
            match modo:
                case 1:
                    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
                case 2:
                    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
                case 3:
                    ret, img = cv2.threshold(img, 127, 255, cv2.ADAPTIVE_THRESH_MEAN_C)
            cv2.imwrite("tratada.png", img)
#Sobel (eixos X, Y e XY)
        case 15:
            img = cv2.imread("tratada.png")
            sobel = int(input(" 1:X\n 2:Y\n 3: X e Y"))
            match sobel:
                case 1:
                    img = cv2.Sobel(img,cv2.CV_64F,1,0,3)
                case 2:
                    img = cv2.Sobel(img, cv2.CV_64F, 0, 1, 3)
                case 3:
                    imgx = cv2.Sobel(img, cv2.CV_64F, 1, 0, 3)
                    imgy = cv2.Sobel(img, cv2.CV_64F, 0, 1, 3)
                    img = cv2.addWeighted(imgx, 0.5, imgy, 0.5, 0)
            cv2.imwrite("tratada.png", img)




    cv2.imshow("Janela", img)
    k = cv2.waitKey(0)


img = cv2.imread("tratada.png")
texto = pytesseract.image_to_string(img, lang="por")
print(texto)