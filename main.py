from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title = "Rogue Opener Simulation"
    description = "a simulator that allows you to plan various rogue opener strategies for wow:forever"
    version = "0.1.0"
)
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

class GameState(BaseModel):
    rogue: RogueState = RogueState()
    enemy: EnemyState = EnemyState()
    abilities: list[AbilityConfig] = []

