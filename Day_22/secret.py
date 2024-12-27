class Secret:
    def __init__(self, initial:int) -> None:
        self.initial_secret = initial
        self.secret:int = initial
    
    def get_next(self) -> None:
        # First, multiply by 64
        # mixer:int = 64 * self.secret
        self.mix_and_prune(64 * self.secret)
        self.mix_and_prune(self.secret // 32)
        self.mix_and_prune(2048 * self.secret)
    
    def mix_and_prune(self, value) -> None:
        self.mix(value)
        self.prune()


    def mix(self, value:int) -> None:
        self.secret = self.secret ^ value
    
    def prune(self) -> None:
        self.secret = self.secret % 16777216
    
    def __str__(self) -> str:
        return f"Secret[{self.initial_secret}] is now: {self.secret}"
    