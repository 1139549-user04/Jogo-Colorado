# 📦 Guia de Assets/base do Jogo

## Estrutura de Pastas

```
base/
└── assets/asset
    ├── logoInternacional.png              # Sprite do jogador
    ├── ImagemDeFundoDoWindows.jfif        # Fundo fixo do cenário
    └── HINO DO INTERNACIONAL - golaudio.mp3  # Música de fundo e game over
```

## Como Funciona

### 🎮 Jogador (logoInternacional.png)
- **Tamanho**: 34x48 pixels
- **Estado Normal**: Imagem colorida
- **Estado de Ataque**: Imagem em escala de cinza
- **Carregamento**: `assets/base/logoInternacional.png`

### 🌅 Cenário (ImagemDeFundoDoWindows.jfif)
- **Tipo**: Fundo fixo (não se move)
- **Tamanho**: 1000x700 pixels
- **Carregamento**: `assets/base/ImagemDeFundoDoWindows.jfif`

### 🎵 Música (HINO DO INTERNACIONAL - golaudio.mp3)
- **Durante o Jogo**: Toca em loop infinito
- **Ao Morrer**: Para o loop e toca uma vez
- **Carregamento**: `assets/base/HINO DO INTERNACIONAL - golaudio.mp3`

## Código Importante

### Carregamento de Recursos
```python
# Em main.py:
background_image = load_image(BACKGROUND_IMG, WIDTH, HEIGHT)
player_image = load_image(PLAYER_IMG, 34, 48)
player_image_attack = grayscale_image(player_image)  # Versão cinza
```

### Renderização
- O fundo é desenhado uma vez por frame via `background_image.blit()`
- O jogador usa a imagem normal ou cinza dependendo do `attack_timer`

### Música
```python
# Loop durante jogo:
pygame.mixer.music.play(-1)

# Game Over:
pygame.mixer.music.play(0)  # Toca uma vez

# Parar música:
pygame.mixer.music.stop()
```

## Testes

Para verificar se tudo está funcionando:
```bash
python main.py
```

Se der erro:
1. Verifique se `assets/base/` existe
2. Verifique se os 3 arquivos estão lá
3. Verificar extensão das imagens (`.png` e `.jfif`)
4. Verificar nome exato do arquivo de música

## Personalizações Fáceis

### Trocar Sprite do Jogador
- Substitua `logoInternacional.png` por outra imagem
- Tamanho recomendado: 34x48 pixels

### Trocar Fundo
- Substitua `ImagemDeFundoDoWindows.jfif`
- Tamanho recomendado: 1000x700 pixels

### Trocar Música
- Substitua `HINO DO INTERNACIONAL - golaudio.mp3`
- Formatos suportados: MP3, WAV, OGG, FLAC

