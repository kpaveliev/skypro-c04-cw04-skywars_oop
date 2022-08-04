from assets.arena import BaseSingleton
from assets.units import BaseUnit


class Arena(metaclass=BaseSingleton):
    """Class for Arena"""
    STAMINA_RECOVERY_PER_TURN: float = 1
    player: BaseUnit = None
    enemy: BaseUnit = None
    game_on: bool = False

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
        self.player.stamina_points += self.STAMINA_RECOVERY_PER_TURN * self.player.unit_class.stamina_modifier
        self.enemy.stamina_points += self.STAMINA_RECOVERY_PER_TURN * self.enemy.unit_class.stamina_modifier

        # Check it isn't greate than maximum
        if self.player.stamina_points > self.player.unit_class.max_stamina:
            self.player.stamina_points = self.player.unit_class.max_stamina
        if self.enemy.stamina_points > self.enemy.unit_class.max_stamina:
            self.enemy.stamina_points = self.enemy.unit_class.max_stamina

    def _check_health(self) -> bool | str:
        """Check if players have health left"""
        if self.player.health_points > 0 and self.enemy.health_points > 0:
            return True
        if self.player.health_points <= 0 <= self.enemy.health_points:
            self.game_result = f'{self.player.name} loses to {self.enemy.name}'
        if self.player.health_points >= 0 >= self.enemy.health_points:
            self.game_result = f'{self.player.name} wins {self.enemy.name}'
        if self.player.health_points <= 0 and self.enemy.health_points <= 0:
            self.game_result = f'{self.player.name} and {self.enemy.name} draw!'
        return self._finish_game()

    def _finish_game(self):
        """Return game result"""
        self._instances = {}
        self.game_on = False
        return self.game_result

    def player_attack(self):
        """Call player attack and next round methods"""
        player_result = self.player.attack(target=self.enemy)
        enemy_result = self.next_round()
        return player_result + enemy_result

    def player_use_skill(self):
        """Call player use skill and next round methods"""
        player_result = self.player.use_skill(target=self.enemy)
        enemy_result = self.next_round()
        return player_result + enemy_result





