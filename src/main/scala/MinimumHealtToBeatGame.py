class Solution:
    def minimumHealth(self, damage, armor):
        # assert self._minimumHealth([0], 7) == 1,'test1'
        # assert self._minimumHealth([3], 1) == 3,'test2'
        # assert self._minimumHealth([6,6,6,6], 3) == 22,'test3'
        # assert self._minimumHealth([0,4,3,0,0], 1) == 7, 'test4'
        return self._minimumHealth(damage, armor)

    def _minimumHealth(self, damage: List[int], armor: int) -> int:
        sum_damage = sum(damage)
        max_damage = max(damage)
        sum_damage -= max_damage
        max_damage -= armor
        left = max(0, max_damage)
        sum_damage += left
        return sum_damage + 1