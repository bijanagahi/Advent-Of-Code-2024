class Xorshift:
    def __init__(self, seed:int) -> None:
        self.state = seed
    
    def shift(self) -> None:
        '''
        Get the next state.

        This Xorshift is defined by the tuple [6,5,11]
        Meaning we shift left 6, right 5, left 11, xor-ing each time.
        '''
        # Perform a series of 'mix' operations
        self.state = (self.state << 6) ^ self.state
        self.state = self.state % 16777216 # we have to prune here because of the right shift
        self.state = (self.state >> 5) ^ self.state
        self.state = (self.state << 11) ^ self.state

        # 'Prune' the state to stay within 24 bits
        self.state = self.state % 16777216
    
    def get_ones(self) -> int:
        return int(str(self.state)[-1])


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
    