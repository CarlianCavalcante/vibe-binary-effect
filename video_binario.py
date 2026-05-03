import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def gerar_video_vibe_limpo(caminho_in, caminho_out):
    cap = cv2.VideoCapture(caminho_in)
    
    # Detector de rostos para garantir proteção extra na face
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Propriedades do vídeo
    largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    altura = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Configura o salvamento
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(caminho_out, fourcc, fps, (largura, altura))

    # --- CONFIGURAÇÕES DE ESTILO ---
    tamanho_fonte = 25    # Aumente aqui (estava 10)
    espacamento = 25      # Aumente para o mesmo valor da fonte (estava 18)
    brilho_minimo = 165   
    opacidade = 200     # De 0 a 255
    
    try:
        fonte = ImageFont.truetype("arial.ttf", tamanho_fonte)
    except:
        fonte = ImageFont.load_default()

    print("Iniciando processamento... Isso pode demorar alguns minutos.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 1. Detectar rostos
        cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rostos = face_cascade.detectMultiScale(cinza, 1.1, 4)

        # 2. Converter para Pillow
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(frame_rgb)
        draw = ImageDraw.Draw(img_pil)

        # 3. Lógica de desenho
        for y in range(0, altura, espacamento):
            for x in range(0, largura, espacamento):
                
                # Proteção de rosto
                no_rosto = False
                for (fx, fy, fw, fh) in rostos:
                    if fx <= x <= fx + fw and fy <= y <= fy + fh:
                        no_rosto = True
                        break
                if no_rosto: continue

                # Analisar brilho do fundo
                r, g, b = img_pil.getpixel((x, y))
                brilho = (r + g + b) / 3
                
                # SÓ DESENHA NO FUNDO CLARO (Onde o brilho é alto)
                # Isso impede que o binário entre no seu cabelo e blusa preta
                if brilho > brilho_minimo:
                    char = "1" if (x + y) % 2 == 0 else "0"
                    draw.text((x, y), char, font=fonte, fill=(255, 255, 255, opacidade))

        # 4. Salvar frame
        frame_final = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
        out.write(frame_final)

    cap.release()
    out.release()
    print(f"\nPronto! Vídeo salvo em: {caminho_out}")

# --- EXECUÇÃO ---
# Troque pelos seus caminhos reais:
video_input = r"C:\Users\Videos\seu-video.mov" 
video_output = r"C:\Users\Videos\resultado_vibe_limpo.mp4"

gerar_video_vibe_limpo(video_input, video_output)