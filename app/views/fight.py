from flask import Blueprint, render_template, current_app

from app.setup import arena
from app.views.start import heroes

# Define Blueprint
fight_bp = Blueprint('Fight', __name__, url_prefix='/fight')



@fight_bp.route('/')
def main():
    """Display fight page"""
    arena.STAMINA_RECOVERY_PER_TURN = current_app.config['STAMINA_RECOVERY_PER_TURN']
    arena.start_game(player=heroes['player'],
                     enemy=heroes['enemy'])

    return render_template('fight.html', heroes=heroes)


@fight_bp.route('/hit/')
def hit():
    """Player attack"""
    if arena.game_on:
        result = arena.player_attack()
        return render_template('fight.html', heroes=heroes, result=result)
    return render_template('fight.html', heroes=heroes)


@fight_bp.route('/use-skill/')
def use_skill():
    """Display hero choosing page"""
    return "Use skill"


@fight_bp.route('/pass-turn/')
def pass_turn():
    """Display hero choosing page"""
    return "pass turn"


@fight_bp.route('/stop-fight/')
def stop_fight():
    """Display hero choosing page"""
    return "stop fight"
