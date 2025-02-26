from app.domain.item import Item


class RegularItem(Item):
    def __init__(self, name: str, sell_in: int, quality: int):
        super().__init__(name, sell_in, quality)

    def update(self) -> None:
        if self.quality > 0:
            self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0 and self.quality > 0:
            self.quality = self.quality - 1
