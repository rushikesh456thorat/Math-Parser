class TreeNode:
    def __init__(self, type: str, **kwargs):
        self.type = type
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        result = f"type = {self.type}"
        for key, value in self.__dict__.items():
            if key not in ("type"):  # Avoid duplicates for existing attributes
                result += f", {key}:{value}"
        return f"[{result}]"
