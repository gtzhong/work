'''
Enum和IntEnum的区别

```python
from enum import Enum   # 枚举的值可以是数字或字符串
from enum import IntEnum  #限定枚举为数字
'''


from enum import Enum
from enum import IntEnum

class VIP(Enum):
    YELLOW =1
    GREEN =2
    BLACK=3
    RED=4


class VIP2(IntEnum):
    YELLOW =1
    GREEN ='str'   # 会报错,不允许为字符串
    BLACK=3
    RED=4


