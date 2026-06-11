import pygame
import random
import math
import sys
import json
import os


WIDTH, HEIGHT = 1000, 700
FPS = 60
GROUND_Y = HEIGHT - 70


Screen = (135, 206, 235)
ENEMY_COLOR = (50, 120, 255)  
ENEMY_HIT_COLOR = (200, 30, 30)  


ASSETS_BASE = "assets/base"
BACKGROUND_MUSIC = os.path.join(ASSETS_BASE, "audiodefundo.mp3")
 
background_image = None
player_image = pygame.image.load("base/inter.png")
player_image = pygame.transform.scale(player_image, (130, 100))


STORY_PARAGRAPHS = [
	"PRÓLOGO\nApós uma era triste de derrotas não sobrou ninguém para torcer pro Inter...",
	"\nDepois de tanto perder, o Internacional está com apenas 1 torcedor e esse é você. ",
	"\nNão tem quase nenhum colorado no mundo. Vague pelo mundo, e converta os gremistas."
]

def load_image(path, width, height):
	"""Carrega uma imagem e redimensiona para o tamanho especificado"""
	if not os.path.exists(path):
		print(f"⚠️ Imagem não encontrada: {path}")
		return None
	try:
		img = pygame.image.load(path)
		img = pygame.transform.scale(img, (width, height))
		return img
	except Exception as e:
		print(f"⚠️ Erro ao carregar imagem {path}: {e}")
		return None


def grayscale_image(image):
	"""Converte uma imagem para escala de cinza"""
	if image is None:
		return None
	return pygame.transform.grayscale(image)

class Player:
	def __init__(self, player_img, player_img_gray):
		self.x = WIDTH // 3
		self.y = GROUND_Y
		self.w = 34
		self.h = 48
		self.speed = 4
		self.facing = 1
		self.attack_timer = 0
		self.image = player_img
		self.image_gray = player_img_gray

	def rect(self):
		return pygame.Rect(self.x - self.w // 2, self.y - self.h, self.w, self.h)

	def attack_rect(self):
		if self.facing >= 0:
			return pygame.Rect(self.x + self.w // 2, self.y - self.h + 10, 28, 20)
		else:
			return pygame.Rect(self.x - self.w // 2 - 28, self.y - self.h + 10, 28, 20)

	def update(self, keys):
		dx = 0
		
		if keys[pygame.K_d]:
			dx = self.speed
			self.facing = 1
		elif keys[pygame.K_a]:
			dx = -self.speed
			self.facing = -1

		self.x += dx
		self.x = max(40, min(WIDTH - 40, self.x))

		if self.attack_timer > 0:
			self.attack_timer -= 1

		return dx
	
	def draw(self, surf):
		"""Desenha o jogador. Cinza quando atacando, normal caso contrário"""
		if self.attack_timer > 0:
			
			if self.image_gray:
				surf.blit(self.image_gray, (self.x - self.w // 2, self.y - self.h))
			else:
				pygame.draw.circle(surf, (100, 100, 100), (int(self.x), int(self.y) - 10), 10)
		else:
		
			if self.image:
				surf.blit(self.image, (self.x - self.w // 2, self.y - self.h))
			else:
				pygame.draw.circle(surf, (200, 40, 40), (int(self.x), int(self.y) - 10), 10)


class Enemy:
	def __init__(self, x, y, speed):
		self.x = x
		self.y = y
		self.w = 30
		self.h = 40
		self.speed = speed
		self.dead = False
		self.hit = False

	def rect(self):
		return pygame.Rect(self.x - self.w // 2, self.y - self.h, self.w, self.h)

	def update(self, dx):
		self.x -= self.speed + dx * 0.05

	def draw(self, surf):
		color = ENEMY_HIT_COLOR if self.hit else ENEMY_COLOR
		pygame.draw.rect(surf, color, self.rect())



SCORES_FILE = "leaderboard.json"

def load_scores():
	if os.path.exists(SCORES_FILE):
		try:
			with open(SCORES_FILE, 'r') as f:
				return json.load(f)
		except:
			return []
	return []

def save_scores(scores):
	with open(SCORES_FILE, 'w') as f:
		json.dump(scores, f)

def add_score(name, score):
	scores = load_scores()
	scores.append({"name": name, "score": score})
	scores.sort(key=lambda x: x["score"], reverse=True)
	scores = scores[:5]
	save_scores(scores)
	return scores

def main():
	global background_image, player_image, player_image_attack
	
	pygame.init()
	pygame.mixer.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	clock = pygame.time.Clock()
	font = pygame.font.SysFont(None, 24)
	
	player_image_attack = grayscale_image(player_image)
	
	
	music_loaded = False
	if os.path.exists(BACKGROUND_MUSIC):
		try:
			pygame.mixer.music.load(BACKGROUND_MUSIC)
			music_loaded = True
		except Exception as e:
			print(f"⚠️ Erro ao carregar música: {e}")
	else:
		print(f"⚠️ Arquivo de música não encontrado: {BACKGROUND_MUSIC}")

	def show_start_screen():
		screen.fill(Screen)
		title = pygame.font.SysFont(None, 40).render('Pressione qualquer tecla para continuar', True, (30, 30, 30))
		screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT - 80))

		
		y = 40
		small = pygame.font.SysFont(None, 22)
		for p in STORY_PARAGRAPHS:
			lines = p.split('\n')
			# show the hashtag title (first line) in bold-ish
			tag = small.render(lines[0], True, (20, 20, 20))
			screen.blit(tag, (40, y))
			y += tag.get_height() + 4
			body = small.render(lines[1], True, (40, 40, 40))
			screen.blit(body, (50, y))
			y += body.get_height() + 14

		pygame.display.flip()

		waiting = True
		while waiting:
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if e.type == pygame.KEYDOWN or e.type == pygame.MOUSEBUTTONDOWN:
					waiting = False

	def show_pause_screen(scr):
		big = pygame.font.SysFont(None, 64)
		small = pygame.font.SysFont(None, 28)
		while True:
			# semi-transparent overlay
			overlay = pygame.Surface((WIDTH, HEIGHT))
			overlay.set_alpha(180)
			overlay.fill((0, 0, 0))
			scr.blit(overlay, (0, 0))
			
			pause_txt = big.render('PAUSADO', True, (230, 230, 230))
			info_txt = small.render('Aperte ESPAÇO para retomar', True, (200, 200, 200))
			scr.blit(pause_txt, (WIDTH // 2 - pause_txt.get_width() // 2, HEIGHT // 2 - 60))
			scr.blit(info_txt, (WIDTH // 2 - info_txt.get_width() // 2, HEIGHT // 2 + 20))
			pygame.display.flip()
			
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_SPACE:
						return

	def show_game_over(scr, final_score):
		big = pygame.font.SysFont(None, 64)
		small = pygame.font.SysFont(None, 28)
		tiny = pygame.font.SysFont(None, 20)
		
		
		name = ""
		entering_name = True
		while entering_name:
			scr.fill((30, 30, 30))
			go = big.render('GAME OVER', True, (220, 60, 60))
			score_surf = small.render(f'Score: {final_score}', True, (230, 230, 230))
			name_label = small.render('Digite seu nome (3 caracteres):', True, (200, 200, 200))
			name_surf = small.render(name.upper(), True, (100, 220, 100))
			
			scr.blit(go, (WIDTH // 2 - go.get_width() // 2, HEIGHT // 2 - 120))
			scr.blit(score_surf, (WIDTH // 2 - score_surf.get_width() // 2, HEIGHT // 2 - 40))
			scr.blit(name_label, (WIDTH // 2 - name_label.get_width() // 2, HEIGHT // 2 + 20))
			scr.blit(name_surf, (WIDTH // 2 - name_surf.get_width() // 2, HEIGHT // 2 + 60))
			
			if len(name) < 3:
				info = tiny.render('(números e letras apenas)', True, (150, 150, 150))
			else:
				info = tiny.render('Pressione ENTER para confirmar', True, (150, 220, 150))
			scr.blit(info, (WIDTH // 2 - info.get_width() // 2, HEIGHT // 2 + 100))
			
			pygame.display.flip()
			
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_BACKSPACE:
						name = name[:-1]
					elif e.key == pygame.K_RETURN and len(name) == 3:
						entering_name = False
					elif len(name) < 3 and (e.unicode.isalnum()):
						name += e.unicode
		
		return name
	
	def show_leaderboard(scr):
		scores = load_scores()
		small = pygame.font.SysFont(None, 24)
		big = pygame.font.SysFont(None, 40)
		
		waiting = True
		while waiting:
			scr.fill(Screen)
			title = big.render('TOP 5 RECORDES', True, (30, 30, 30))
			scr.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))
			
			y = 90
			if not scores:
				empty = small.render('Nenhum recorde ainda. Comece a jogar!', True, (60, 60, 60))
				scr.blit(empty, (WIDTH // 2 - empty.get_width() // 2, y))
			else:
				for i, entry in enumerate(scores, 1):
					line = f"{i}. {entry['name'].upper():3} - {entry['score']}"
					line_surf = small.render(line, True, (30, 30, 30))
					scr.blit(line_surf, (WIDTH // 2 - line_surf.get_width() // 2, y))
					y += 35
			
			hint = small.render('Pressione qualquer tecla para continuar', True, (80, 80, 80))
			scr.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT - 50))
			pygame.display.flip()
			
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if e.type == pygame.KEYDOWN or e.type == pygame.MOUSEBUTTONDOWN:
					waiting = False

	
	show_leaderboard(screen)

	
	while True:
		
		player = Player(player_image, player_image_attack)
		enemies = []
		spawn_timer = 60
		bg_offset = 0
		score = 0

		
		show_start_screen()

		
		if music_loaded:
			pygame.mixer.music.play(-1)

		running = True
		t = 0.0

		while running:
			dt = clock.tick(FPS) / 1000.0
			t += dt

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()
					
					if event.key == pygame.K_SPACE:
						show_pause_screen(screen)
				
					if event.key == pygame.K_o:
						player.attack_timer = 10

			keys = pygame.key.get_pressed()
			dx = player.update(keys)
			bg_offset += dx

			spawn_timer -= 1
			if spawn_timer <= 0:
				spawn_timer = random.randint(50, 140)
				ex = WIDTH + 40
				ey = GROUND_Y
				es = random.uniform(1.2, 2.2)
				enemies.append(Enemy(ex, ey, es))

			for e in enemies:
				e.update(dx)

			
			if player.attack_timer > 0:
				ar = player.attack_rect()
				for e in enemies:
					if not e.dead and ar.colliderect(e.rect()):
						if not e.hit:
							score += 1
							e.hit = True

			player_dead = False
			for e in enemies:
				
				if not e.dead and not e.hit and e.rect().colliderect(player.rect()):
					player_dead = True
					break

			enemies = [e for e in enemies if not (e.dead and e.x < -100)]

			
			if background_image:
				screen.blit(background_image, (0, 0))
			else:
				screen.fill((135, 206, 235))  
			for e in enemies:
				e.draw(screen)

			player.draw(screen)

			hud = font.render(f'Score: {score}', True, (20, 20, 20))
			screen.blit(hud, (10, 10))
			
			
			small_font = pygame.font.SysFont(None, 18)
			pause_msg = small_font.render('Aperte ESPAÇO para pausar', True, (100, 100, 100))
			screen.blit(pause_msg, (WIDTH - pause_msg.get_width() - 10, HEIGHT - pause_msg.get_height() - 10))

			pygame.display.flip()

			if player_dead:
				
				pygame.mixer.music.stop()
				
				
				if music_loaded:
					pygame.mixer.music.play(0)  
				
				player_name = show_game_over(screen, score)
				add_score(player_name, score)
				
				
				restart_screen = True
				while restart_screen:
					screen.fill((30, 30, 30))
					big = pygame.font.SysFont(None, 40)
					small = pygame.font.SysFont(None, 28)
					msg = big.render('Deseja jogar novamente?', True, (200, 200, 200))
					info = small.render('R - Reiniciar | ESC - Sair', True, (150, 150, 150))
					screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 50))
					screen.blit(info, (WIDTH // 2 - info.get_width() // 2, HEIGHT // 2 + 20))
					pygame.display.flip()
					
					for e in pygame.event.get():
						if e.type == pygame.QUIT:
							pygame.quit()
							sys.exit()
						if e.type == pygame.KEYDOWN:
							if e.key == pygame.K_r:
								running = False
								restart_screen = False
								break
							if e.key == pygame.K_ESCAPE:
								pygame.quit()
								sys.exit()

		
		continue


if __name__ == '__main__':
	main()

