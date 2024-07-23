from pydantic import BaseModel, ImportString

class Demo(BaseModel):
    dep: ImportString

demo = Demo(dep="pandas")
