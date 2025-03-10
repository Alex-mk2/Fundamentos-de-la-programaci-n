#sabemos que 

# Los ataques tienen un nombre y caracteristicas:





#class Attack:
    def __init__(self, attack_name: str, attack_type: str, objective: str, damage: int, precision: int, recharge: int) -> None:
        self.attack_name = attack_name
        self.attack_type = attack_type
        self.objective = objective
        self.damage = damage
        self.precision = precision 
        self.recharge = recharge
        self.current_recharge = 0  ##### constructor