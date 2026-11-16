#!/usr/bin/env python3
"""示例脚本：打印问候语。"""


def greet(name: str = "GitHub") -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
