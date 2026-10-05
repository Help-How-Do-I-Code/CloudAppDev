from pydantic import BaseModel, Field

# Base schema with common attributes
class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100,)
    description: str | None = Field(default=None, max_length=500)

# Schema for creating a new item
class ItemCreate(ItemBase):
    pass

# Schema for reading/returning an item (includes id)
class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True