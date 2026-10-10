# Project Roadmap: Advanced Rogue Combat Simulator

## Phase 1: Foundation and Basic Loop
- [x] Initialize Rogue and Enemy base models
- [ ] Implement fluid energy regeneration and combo points
- [ ] Implement simulation clock controller (Real-Time vs. Step/Pause Mode)
- [ ] Implement Global Cooldown (GCD) and Stealth flag tracking
- [ ] Implement first baseline ability (Backstab)

## Phase 2: Rotation and Control Mechanics
- [ ] Implement core abilities and keybindable routing framework
- [ ] Implement self-buffs and enemy debuffs (e.g., Slice and Dice, Rupture)
- [ ] Implement Crowd Control (CC) stuns and Diminishing Returns (DR) tracking

## Phase 3: Customization and Utilities
- [ ] Implement player and enemy races and racial trait structures
- [ ] Implement important talent toggles (e.g., Vigor energy scaling)
- [ ] Implement weapon coating and poison configuration systems

## Phase 4: Advanced Stats and Enemy Intelligence
- [ ] Implement enemy class, level, stats, and armor mitigation tables
- [ ] Implement full character stat profiles (Agility, Attack Power, Weapon Damage ranges)
- [ ] Implement enemy trinket AI and reactive combat logic

## Technical Stack
- Language: Python 3
- Framework: FastAPI & Uvicorn
- Validation: Pydantic