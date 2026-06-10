Pedro Afonso Bertolini Pietro Bom
RA: 1139549

# 🎮 Jogo Pygame - Converta os Gremistas

Um jogo endless runner em Pygame onde você controla uma bola vermelha que se move para frente e trás, atacando inimigos azuis que vêm em sua direção.

## 📖 Prólogo

> **PRÓLOGO**  
> Após uma era triste de derrotas não sobrou ninguém para torcer pro Inter...
> 
> Depois de tanto perder, o Internacional está com apenas 1 torcedor e esse é você.
> 
> Não tem quase nenhum colorado no mundo. Vague pelo mundo, e converta os gremistas.

---

## 🛠️ Bibliotecas Utilizadas

| Biblioteca | Versão | Para Quê? |
|------------|--------|-----------|
| **pygame-ce** | 2.5.7 | Motor gráfico principal - renderização de objetos, colisões e entrada de usuário |
| **random** | - | Geração procedural de números aleatórios (spawn de inimigos, nuvens e velocidades) |
| **math** | - | Cálculos matemáticos (função seno para animar o sol pulsante) |
| **sys** | - | Controle do sistema (sair da aplicação com `sys.exit()`) |
| **json** | - | Serialização de dados - salvar e carregar o leaderboard (`leaderboard.json`) |
| **os** | - | Operações do sistema de arquivos - verificar se arquivo existe |
| **pyinstaller** | 6.10.0 | Compilação do código Python em executável standalone `.exe` |

---

## 🎯 Resumo das Funcionalidades

### Jogabilidade Principal
- **Movimento infinito**: Sem fim pré-determinado, jogue até morrer
- **Sistema de combate**: Ataque inimigos para marcar pontos
- **Punição ao erro**: Um toque de inimigo azul é morte instantânea
- **Feedback visual**: Inimigos atacados ficam vermelhos permanentemente
- **Pausa em tempo real**: Pause a qualquer momento para descansar

### Telas
1. **Leaderboard**: Top 5 recordes - aparece antes de tudo
2. **Prólogo**: Introdução da história (editável)
3. **Gameplay**: Jogo principal com HUD (score e dica de pausa)
4. **Game Over**: Entrada de nome (3 caracteres) e opção de reiniciar
5. **Pausa**: Overlay semitransparente com mensagem

### Cenário
- **Sol pulsante**: Animado continuamente ao fundo
- **Nuvens flutuantes**: Passam continuamente (sem interação)
- **Terreno**: Padrão de blocos que cria ilusão de movimento
- **Céu gradiente**: Fundo azul claro
- **Resolução**: 1000x700 pixels

---

## ⌨️ Mapeamento de Teclas

| Tecla | Ação |
|-------|------|
| **A** | Mover personagem para trás (esquerda) |
| **D** | Mover personagem para frente (direita) |
| **O** | Atacar inimigos próximos |
| **ESPAÇO** | Pausar/Despausar o jogo |
| **ESC** | Sair do jogo (fecha aplicação) |
| **R** | Reiniciar após Game Over |

---

## 🎮 Como Jogar

### Objetivo
Elimine o máximo de inimigos (gremistas) sem deixar eles tocarem em você. Cada inimigo derrotado soma 1 ponto.

### Dinâmica
1. Inimigos azuis aparecem do lado direito da tela
2. Pressione **O** para atacar quando estiverem perto
3. Inimigos atacados ficam vermelhos e deixam de ser uma ameaça
4. Inimigos azuis que tocarem em você = **morte instantânea**
5. Seu score é salvo se estiver entre os top 5

### Dicas Estratégicas
- Coordene movimentos (**A**/**D**) com ataques (**O**)
- Use **ESPAÇO** para pausar e planejar
- Quanto mais tempo sobrevive, mais difícil fica
- Inimigos vermelhos ainda ocupam espaço - desvie deles

---

## 📊 Sistema de Recordes

- **Leaderboard**: Automático, top 5 apenas
- **Persistência**: Salvo em `leaderboard.json`
- **Nome do Jogador**: 3 caracteres (números e letras)
- **Visibilidade**: Mostrado antes de cada sessão

---

## � Sistema de Áudio

- **Trilha Sonora**: Toca em loop contínuo durante o jogo
- **Parada**: Automática quando o jogador morre
- **Reinício**: Toca novamente a cada nova sessão
- **Arquivo**: `assets/soundtrack.mp3`
- **Formatos Suportados**: MP3, WAV, OGG, FLAC

### Como Adicionar Música

1. Procure por música livre em sites como Freepik, YouTube Audio Library ou Pixabay
2. Salve como `soundtrack.mp3` na pasta `assets/`
3. Pronto! A música tocará automaticamente

Veja `assets/README.md` para mais detalhes.

---

## �🎨 Personagens e Objetos

### Jogador
- **Aparência**: Círculo vermelho (raio 10px)
- **Posição**: Terço esquerdo da tela
- **Movimento**: Horizontal apenas (sem pulos)

### Inimigos
- **Aparência**: Retângulos (30x40px)
- **Cor Padrão**: Azul (50, 120, 255)
- **Cor ao Atacar**: Vermelho (200, 30, 30)
- **Spawn**: Do lado direito, velocidade aleatória (1.2 a 2.2 px/frame)

### Cenário
- **Sol**: Círculo amarelo pulsante (30-36px de raio)
- **Nuvens**: Formas brancas procedurais, múltiplos tamanhos
- **Terreno**: Padrão repetido de blocos verdes (80x altura)

---

## ✨ Recursos Implementados

✅ **Executável Standalone**: Distribua sem necessidade de Python  
✅ **Leaderboard Persistente**: Recordes salvos localmente em JSON  
✅ **Prólogo Customizável**: Edite a história diretamente no código  
✅ **Sistema de Pausa**: Congelamento completo com overlay visual  
✅ **Animações Procedurais**: Sol pulsante com seno, nuvens flutuantes  
✅ **Feedback Visual Imediato**: Cores indicam estado do inimigo (azul → vermelho)  
✅ **Trilha Sonora**: Música em loop durante o jogo, para ao morrer
✅ **Interface Intuitiva**: Instruções na tela e dicas contextuais  

---

## 📝 Instalação e Execução

### Opção 1: Script Python (Desenvolvimento)
```powershell
pip install -r requirements.txt
python main.py
```

### Opção 2: Executável Standalone (Distribuição)
```powershell
python build_exe.py
# Aguarde compilação → dist/JogoProjetoGrego.exe
```

---

## 🎲 Classes e Estrutura de Dados

### Classes Principais

**`Sun`**: Objeto do sol pulsante
- Anima raio com função seno
- Renderiza círculo amarelo

**`Cloud`**: Nuvens procedurais
- Posição, velocidade, escala aleatória
- Renderiza com elipses

**`Player`**: Personagem (bola vermelha)
- Movimento horizontal (A/D)
- Rect de colisão e rect de ataque
- Renderiza círculo vermelho

**`Enemy`**: Inimigos azuis
- Spawn à direita, movimento para esquerda
- Estado: `hit` (foi atingido?)
- Renderiza retângulo (azul ou vermelho)

### Variáveis Globais
```python
WIDTH = 1000           # Largura da tela
HEIGHT = 700           # Altura da tela
GROUND_Y = 630         # Posição Y do terreno
FPS = 60               # Frames por segundo

# Paleta de cores
SKY = (135, 206, 235)        # Azul céu
GROUND = (90, 170, 70)       # Verde grama
PLAYER_COLOR = (200, 40, 40) # Vermelho jogador
ENEMY_COLOR = (50, 120, 255) # Azul inimigo
ENEMY_HIT_COLOR = (200, 30, 30) # Vermelho inimigo atingido
```

---

## 🔄 Loop Principal do Jogo

1. **Inicialização**: Leaderboard → Prólogo → Reset do estado
2. **Evento**: Captura entrada de teclado (A, D, O, ESPAÇO, ESC)
3. **Update**: Atualiza posições, spawna inimigos, move nuvens
4. **Colisão**: Detecta ataques e contatos fatais
5. **Render**: Desenha céu, sol, nuvens, terreno, inimigos, jogador
6. **HUD**: Mostra score e dica de pausa
7. **Display**: Atualiza tela
8. **Condição de Derrota**: Se tocado, salva score e volta ao leaderboard

---

## 📁 Arquivos do Projeto

```
ProjetoJogo.py/
├── main.py                    # Código principal do jogo
├── requirements.txt           # Dependências Python
├── build_exe.py              # Script para compilar .exe
├── README.md                 # Este arquivo
├── leaderboard.json          # Recordes (gerado automaticamente)
└── assets/
    ├── README.md             # Instruções para adicionar música
    └── soundtrack.mp3        # Trilha sonora (adicione aqui)
```

---

## 💡 Customização

### Editar Prólogo
Abra `main.py` e procure por:
```python
STORY_PARAGRAPHS = [
    "#PROLOGO#\nSeu texto aqui...",
    ...
]
```

### Mudar Velocidades
```python
self.speed = 4           # Velocidade do jogador
es = random.uniform(1.2, 2.2)  # Velocidade dos inimigos
```

### Ajustar Cores
```python
PLAYER_COLOR = (R, G, B)
ENEMY_COLOR = (R, G, B)
```

---

Desenvolvido com ❤️ usando Pygame-CE
