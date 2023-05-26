from enum import Enum


class ClickStatistics(str, Enum):
    NONE = 'none'
    COUNT = 'count'
    AVERAGE = 'average'