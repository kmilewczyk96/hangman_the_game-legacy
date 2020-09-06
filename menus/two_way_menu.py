import pygame


class TwoWayMenu:
    def __init__(self, question, answer_1, answer_2, action_1, action_2):
        self.clock = pygame.time.Clock()
        self.status = 0
        self.run_menu = True
        self.question = question
        self.answer_1 = answer_1
        self.answer_2 = answer_2
        self.action_1 = action_1
        self.action_2 = action_2

    def prompt(self, WIDTH, HEIGHT, WHITE, BLACK, LETTER_FONT_2, FONT_SIZE_2, win):
        while self.run_menu:
            self.clock.tick(60)
            win.fill(WHITE)

            question = LETTER_FONT_2.render(f"{self.question}", 1, BLACK)
            answer_1 = LETTER_FONT_2.render(f"{self.answer_1}", 1, BLACK)
            answer_2 = LETTER_FONT_2.render(f'{self.answer_2}', 1, BLACK)

            win.blit(question, (int(WIDTH / 2) - int(question.get_width() / 2),
                                int(FONT_SIZE_2)))
            win.blit(answer_1, (int(WIDTH / 2) - int(answer_1.get_width() / 2),
                                int(HEIGHT / 2 - FONT_SIZE_2)))
            win.blit(answer_2, (int(WIDTH / 2) - int(answer_2.get_width() / 2),
                                     int(HEIGHT / 2 + FONT_SIZE_2 / 2)))

            if self.status == 0:
                pygame.draw.line(win, BLACK,
                                 (int(WIDTH / 2) - int(answer_1.get_width() / 2), int(HEIGHT / 2)),
                                 (int(WIDTH / 2) + int(answer_1.get_width() / 2), int(HEIGHT / 2)),
                                 int(FONT_SIZE_2 / 10))

            else:
                pygame.draw.line(win, BLACK,
                                 (int(WIDTH / 2) - int(answer_2.get_width() / 2),
                                  int(HEIGHT / 2) + int(FONT_SIZE_2 * 5 / 3)),
                                 (int(WIDTH / 2) + int(answer_2.get_width() / 2),
                                  int(HEIGHT / 2) + int(FONT_SIZE_2 * 5 / 3)),
                                 int(FONT_SIZE_2 / 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if self.status == 0:
                            self.status = 1
                        print(self.status)

                    if event.key == pygame.K_UP:
                        if self.status == 1:
                            self.status = 0
                        print(self.status)

                    if event.key == pygame.K_RETURN:
                        if self.status == 0:
                            self.action_1()
                            self.run_menu = False
                        if self.status == 1:
                            self.action_2()
                            self.run_menu = False

            pygame.display.update()