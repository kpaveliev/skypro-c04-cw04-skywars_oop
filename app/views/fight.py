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
    return render_template('fight.html', heroes=heroes, battle_result=arena.battle_result)


@fight_bp.route('/use-skill/')
def use_skill():
    """Display hero choosing page"""
    if arena.game_on:
        result = arena.player_use_skill()
        return render_template('fight.html', heroes=heroes, result=result)
    return render_template('fight.html', heroes=heroes, battle_result=arena.battle_result)


@fight_bp.route('/pass-turn/')
def pass_turn():
    """Display hero choosing page"""
    if arena.game_on:
        result = arena.next_turn()
        return render_template('fight.html', heroes=heroes, result=result)
    return render_template('fight.html', heroes=heroes, battle_result=arena.battle_result)


@fight_bp.route('/end-fight/')
def stop_fight():
    """Display hero choosing page"""
    return render_template("index.html")
