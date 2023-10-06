# -*- coding: utf-8 -*-
class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class AgedBrie(Item):

    def update_quality(self):
        self.sell_in-=1
        self.quality += 1 if self.sell_in >=0 else 2
        self.quality = min(50, max(self.quality,0))


class Sulfuras(Item):

    def update_quality(self):
        self.sell_in-=1
        

class BackStagePasses(Item):
    
    def update_quality(self):
        self.sell_in-=1
        if self.sell_in > 10:
            self.quality += 1
        elif self.sell_in > 5:
            self.quality += 2
        elif self.sell_in > 0:
            self.quality += 3
        else:
            self.quality = float("-inf")
        
        self.quality = min(50, max(self.quality,0))

class Sulfuras(Item):

    def update_quality(self):
        self.sell_in-=1 

class Conjured(Item):

    def update_quality(self):
        self.sell_in-=1
        self.quality -= 2 if self.sell_in>=0 else 4
        self.quality = min(50, self.quality)

class Ordinary(Item):

    def update_quality(self):
        self.sell_in-=1
        self.quality -= 1 if self.sell_in>=0 else 2
        self.quality = min(50, self.quality)

class GildedRose(object):

    __itemDic = {
        "Aged Brie" : AgedBrie,
        "Backstage passes to a TAFKAL80ETC concert" : BackStagePasses,
        "Conjured Mana Cake" : Conjured,
        "Sulfuras, Hand of Ragnaros" : Sulfuras,
    }

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        self.__processItem()

    def __processItem(self):
        for i in range(len(self.items)):
            item=self.items[i]
            self.items[i] = self.__itemDic.get(item.name,Ordinary)(item.name,item.sell_in,item.quality)
    
    def update_quality(self):
        for item in self.items:
            item.update_quality()
