from assets.arena import BaseSingleton
from assets.units import BaseUnit


class Arena(BaseSingleton):
    """Class for Arena"""
    STAMINA_RECOVERY_PER_TURN: float = None
    player = None
    enemy = None
    game_on: bool

    def start_game(self, player: BaseUnit, enemy: BaseUnit):
        """Start game and assign player, enemy"""
        self.player = player
        self.enemy = enemy
        self.game_on = True

    def next_round(self) -> str:
        """Check health, regenerate stamina and enemy attack"""
        if self._check_health():
            self._regenerate_stamina()
            return self.enemy.attack(target=self.player)
        return self._check_health()

    def _regenerate_stamina(self) -> None:
        """Regenerate players stamina"""
        # Regenerate stamina
        self.player.stamina += self.STAMINA_RECOVERY_PER_TURN * self.player.unit_class.stamina_modifier
        self.enemy.stamina += self.STAMINA_RECOVERY_PER_TURN * self.enemy.unit_class.stamina_modifier

        # Check it isn't greate than maximum
        if self.player.stamina > self.player.unit_class.max_stamina:
            self.player.stamina = self.player.unit_class.max_stamina
        if self.enemy.stamina > self.enemy.unit_class.max_stamina:
            self.enemy.stamina = self.enemy.unit_class.max_stamina


    def _check_health(self) -> bool | str:
        """Check if players have health left"""
        if self.player.health > 0 and self.enemy.health > 0:
            return True
        if self.player.health <= 0 and self.enemy.health >= 0:
            self.game_result = f'{self.player.name} loses to {self.enemy.name}'
        if self.player.health >= 0 and self.enemy.health <= 0:
            self.game_result = f'{self.player.name} wins {self.enemy.name}'
        if self.player.health <= 0 and self.enemy.health <= 0:
            self.game_result = f'{self.player.name} and {self.enemy.name} draw!'
        return self._finish_game()

    def _finish_game(self):
        """Return game result"""
        self._instances = {}
        self.game_on = False
        return self.game_result

    def player_attack(self):
        """"""
        attack_result = self.player.attack(target=self.enemy)

        return self.player.attack(target=self.enemy)

    def player_use_skill(self):
        return self.player.use_skill(target=self.enemy)





