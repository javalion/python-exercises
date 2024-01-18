# Class Strategy with Environment Variables

import os
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Strategy A")

class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Strategy B")

def get_strategy():
    strategies = {
        "A": ConcreteStrategyA,
        "B": ConcreteStrategyB
    }
    return strategies.get(os.environ.get("STRATEGY", "B"), ConcreteStrategyB)()

def main():
    strategy = get_strategy()
    strategy.execute()

if __name__ == "__main__":
    main()