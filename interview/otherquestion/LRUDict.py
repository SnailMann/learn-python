from collections import OrderedDict


class LRUDict(OrderedDict):
    """
    通过OrderedDict实现LRU
    OrderedDict本质就是dict + 双向链表
    """

    def __init__(self, capacity, **kwargs):
        """
        :param capacity: LRUDict的最大容量
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.capacity = capacity
        self.items = OrderedDict()

    def __setitem__(self, key, value):
        old_value = self.items.get(key)
        # 如果key键已存在，则先弹出该键值对，重新插入新值,同时存储位置也换了
        if old_value is not None:
            self.items.pop(key)
            self.items[key] = value

        # 如果LRUDict的容量够，且key不存在容器中，则直接插入
        elif len(self.items) < self.capacity:
            self.items[key] = value

        # 如果LRUDict容量不够，且key不在容器中，则执行LRU淘汰算法，弹出队头元素，新元素插入队尾
        else:
            self.items.popitem(last=False)
            self.items[key] = value

    def __getitem__(self, key):
        value = self.items.get(key)
        if value is not None:
            self.items.pop(key)
            self.items[key] = value
        return value

    def __repr__(self):
        return repr(self.items)


lru = LRUDict(10)
for i in range(1, 15):
    lru[i] = i
print(lru)
