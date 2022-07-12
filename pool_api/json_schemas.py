from pydantic import BaseModel
from typing import List


class Pool(BaseModel):
    poolId: int
    poolValues: List[int]


