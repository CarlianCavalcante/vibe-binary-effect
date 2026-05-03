import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def gerar_efeito_vibe(caminho_entrada, caminho_saida):
    try:
        # 1. Carregar imagem
        img_cv = cv2.imread(caminho_entrada)
        if img_cv is None:
            print("Erro: Não encontrei a imagem no caminho especificado.")
            return

        # Converter para RGBA para suportar transparência no desenho
        img_pil = Image.open(caminho_entrada).convert("RGBA")
        camada_texto = Image.new("RGBA", img_pil.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(camada_texto)
        
        # 2. Detecção de rostos (OpenCV)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
        rostos = face_cascade.detectMultiScale(gray, 1.1, 4)

        # 3. Configurações de estilo
        espacamento = 14    # Aumentar para um look mais limpo
        limite_sombra = 110 # Áreas escuras
        limite_claro = 200  # Áreas muito claras (céu)
        tamanho_fonte = 11
        
        try:
            # Tenta carregar uma fonte monoespaçada para manter o alinhamento
            fonte = ImageFont.truetype("consola.ttf", tamanho_fonte) 
        except:
            fonte = ImageFont.load_default()

        largura, altura = img_pil.size
        # Converter para array para checagem rápida de brilho
        img_array = np.array(img_pil.convert("L")) 

        # 4. Percorrer a imagem
        print("Processando pixels...")
        for y in range(0, altura, espacamento):
            for x in range(0, largura, espacamento):
                
                # Regra 1: Pular se estiver no rosto
                no_rosto = False
                for (fx, fy, fw, fh) in rostos:
                    if fx <= x <= fx + fw and fy <= y <= fy + fh:
                        no_rosto = True
                        break
                if no_rosto: continue

                # Regra 2: Checar brilho no array NumPy
                brilho = img_array[y, x]
                
                # Aplica o binário apenas em áreas de interesse (muito escuras ou muito claras)
                if brilho < limite_sombra or brilho > limite_claro:
                    char = "1" if (x + y) % 2 == 0 else "0"
                    # Branco com 120 de opacidade (0-255)
                    draw.text((x, y), char, font=fonte, fill=(255, 255, 255, 120))

        # 5. Mesclar camadas e salvar
        resultado = Image.alpha_composite(img_pil, camada_texto).convert("RGB")
        resultado.save(caminho_saida, "PNG")
        print(f"Sucesso! Imagem salva em: {caminho_saida}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# --- EXECUÇÃO ---
arquivo_entrada = r"C:\Users\Videos\seu-imagem.jpg"
arquivo_saida = r"C:\Users\Videos\resultado_vibe.png"

gerar_efeito_vibe(arquivo_entrada, arquivo_saida)