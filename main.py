from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")

app = FastAPI(
    title = "Rogue Opener Simulation",
    description = "a simulator that allows you to plan various rogue opener strategies for wow:forever",
    version = "0.1.0"
)

# 1. Config blueprints #

class AbilityConfig(BaseModel):
    name: str
    energy_cost: float
    combo_point_cost: int
    combo_point_gain: int
    cooldown: float
    flat_damage: float
    weapon_damage_percent: float
    global_cooldown: float
    applies_debuff: str | None = None
    applies_buff: str | None = None

BACKSTAB = AbilityConfig(
    name="Backstab",
    energy_cost=60.0,
    combo_point_cost=0,
    combo_point_gain=1,
    cooldown=0.0,
    flat_damage=225.0,         
    weapon_damage_percent=150.0, # Ready for weapon scaling in Phase 4
    global_cooldown=1.0,
    applies_debuff=None,
    applies_buff=None
)

# 2. Runtime states #

class RogueState(BaseModel):
    energy: float = 100.0
    max_energy: int = 100
    energy_regen_per_sec: float = 1.0
    combo_points: int = 0
    max_combo_points: int = 5
    is_stealthed: bool = True
    global_cooldown_remaining: float = 0.0
    #future hook for talents - phase 3
    talents: dict[str, int] = {} # probably something like { "improved_backstab": 2} - showing 2 of 3 ranks 

class EnemyState(BaseModel):
    name: str = "Dummy Target"
    health: int = 1000
    max_health: int = 1000

class GameState(BaseModel):
    rogue: RogueState = RogueState()
    enemy: EnemyState = EnemyState()
    abilities: list[AbilityConfig] = []

game_state = GameState(abilities=[BACKSTAB])

@app.get("/state", response_model=GameState)    
def get_game_state():
    return game_state

@app.post("/use_ability/{ability_name}")
def use_ability(ability_name: str):
    ability = next((a for a in game_state.abilities if a.name.lower() == ability_name.lower()), None)
    if not ability:
        raise HTTPException(status_code=404, detail="Ability not found")

    rogue = game_state.rogue
    enemy = game_state.enemy

    # Check if rogue has enough energy
    if rogue.energy < ability.energy_cost:
        raise HTTPException(status_code=400, detail="Not enough energy")

    # Check if rogue has enough combo points
    if rogue.combo_points < ability.combo_point_cost:
        raise HTTPException(status_code=400, detail="Not enough combo points")

    # Apply ability effects
    rogue.energy -= ability.energy_cost
    rogue.combo_points -= ability.combo_point_cost
    rogue.combo_points += ability.combo_point_gain

    # Calculate damage (simplified)
    damage = ability.flat_damage + (ability.weapon_damage_percent / 100) * 100  # Assuming weapon damage is 100 for now
    enemy.health -= damage

    # Ensure health doesn't go below zero
    enemy.health = max(enemy.health, 0)

    return {"message": f"Used {ability.name}, dealt {damage} damage to {enemy.name}. Remaining health: {enemy.health}."}