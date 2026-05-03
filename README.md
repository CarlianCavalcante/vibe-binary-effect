# 🌌 Vibe Binary Overlay (Photo & Video)

Este projeto utiliza **Python**, **OpenCV** e **Pillow** para aplicar um efeito estético de sobreposição binária ("Matrix Vibe") em fotos e vídeos. O diferencial deste script é o uso de Inteligência Artificial (Haar Cascades) para detectar rostos e preservar a face do usuário, além de filtros de brilho para aplicar o efeito preferencialmente no fundo ou em áreas de alto contraste.

---

## ✨ Funcionalidades

*   **Detecção Facial:** Utiliza IA para impedir que os números cubram o rosto, mantendo a identidade clara.
*   **Segmentação por Brilho:** O binário é aplicado de forma inteligente, focando em áreas claras (como o céu) ou sombras profundas.
*   **Processamento de Vídeo:** Transforma vídeos `.mov` ou `.mp4` frame a frame com performance otimizada via NumPy.
*   **Estética Customizável:** Fácil ajuste de tamanho de fonte, caracteres, opacidade e densidade.

---

## 🛠️ Tecnologias Utilizadas

*   [Python 3.x](https://www.python.org/)
*   [OpenCV](https://opencv.org/) - Processamento de imagem e detecção facial.
*   [Pillow (PIL)](https://python-pillow.org/) - Renderização de texto e composição de camadas.
*   [NumPy](https://numpy.org/) - Cálculos matriciais de brilho em alta velocidade.

---

## 🚀 Como Usar

### 1. Pré-requisitos
Certifique-se de ter o Python instalado. Instale as dependências necessárias via terminal:
```bash
pip install opencv-python pillow numpy
```
### 2. Configuração de CaminhosDentro de cada script (gerador_video.py ou gerador_imagem.py), altere as variáveis de caminho para os seus arquivos:

    caminho_entrada = r"C:\Caminho\Para\Seu\Arquivo.mp4"

    caminho_saida = r"C:\Caminho\Para\Resultado.mp4"

### 3. ExecuçãoExecute os scripts conforme sua necessidade:Bash
```bash
   python gerador_video.py
```
```bash
   python gerador_imagem.py
```
   
⚙️ Ajustes de EstiloVocê pode personalizar o visual alterando as variáveis no topo das funções: 

tamanho_fonte: Define o tamanho dos caracteres '0' e '1'.

espacamento: Controla a densidade da grade (quanto menor, mais cheio).

brilho_minimo: Limiar de luz para o efeito aparecer (ideal para focar no céu).

opacidade: Transparência do texto (0 a 255).

### 📝 Licença

Este projeto é para fins de estudo e uso criativo. 

Sinta-se à vontade para clonar, modificar e melhorar!

"The world is binary. You are the exception." 🌌
