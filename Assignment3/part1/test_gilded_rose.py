# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_sulfarus(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10 ,80)]
        gilded_rose = GildedRose(items)
        for i in range(100):
            gilded_rose.update_quality()
            self.assertEqual(80, items[0].quality)

    def test_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 12 ,0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(3, items[0].quality)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEquals(14, items[0].quality)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_brie(self):
        items = [Item("Aged Brie", 10 ,0)]
        gilded_rose = GildedRose(items)
        for i in range(1,11):
            gilded_rose.update_quality()
            self.assertEqual(i,items[0].quality)
        for i in range(12,22,2):
            gilded_rose.update_quality()
            self.assertEqual(i,items[0].quality)
        for i in range(100):
            gilded_rose.update_quality()
        self.assertEqual(50,items[0].quality)
    
    def test_Ordinary(self):
        items = [Item("Drug", 2 ,20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(19,items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(18,items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(16,items[0].quality)
    
    def test_Multiple_Items(self):
        items = [Item("Drug", 2 ,20),Item("Drug", 2 ,20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(19,items[0].quality)
        self.assertEquals(19,items[1].quality)
        gilded_rose.update_quality()
        self.assertEquals(18,items[0].quality)
        self.assertEquals(18,items[1].quality)
        gilded_rose.update_quality()
        self.assertEquals(16,items[0].quality)
        self.assertEquals(16,items[1].quality)


            


if __name__ == '__main__':
    unittest.main()
