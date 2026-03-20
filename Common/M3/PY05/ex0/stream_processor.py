from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Default Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        print("\nInitializing Numeric Processor...")
        self.count: int = 0
        self.total: int = 0
        self.mean: float = 0.0

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        self.count = 0
        self.total = 0
        self.mean = 0.0
        if self.validate(data) is True:
            print("Validation: Numeric data verified")
        else:
            print("Validation: Numeric data not verified")
            return (
                f"Processed {self.count} numeric values, "
                f"sum={self.total}, avg={self.mean}"
            )
        self.count = len(data)
        self.total = sum(data)
        self.mean = self.total / self.count
        return (
            f"Processed {self.count} numeric values, "
            f"sum={self.total}, avg={self.mean}"
        )

    def validate(self, data: Any) -> bool:
        try:
            _ = sum(data)
            return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    def __init__(self):
        print("\nInitializing Text Processor...")
        self.char_count: int = 0
        self.word_count: int = 0

    def str_len(self, string: str) -> int:
        return len(string)

    def counter_words(self, words: str) -> int:
        i: int = 0
        count: int = 0
        in_token: bool = False
        while i < len(words):
            if words[i] == " ":
                in_token = False
            elif in_token is False:
                in_token = True
                count += 1
            i += 1
        return count

    def process(self, data: Any) -> str:
        print(f'Processing data: "{data}"')
        if self.validate(data) is True:
            print("Validation: Text data verified")
        else:
            print("Validation: Text data not verified")
            return (
                f"Processed text: {self.char_count} characters, "
                f"{self.word_count} words"
            )
        self.char_count = self.str_len(data)
        self.word_count = self.counter_words(data)
        return (
            f"Processed text: {self.char_count} characters, "
            f"{self.word_count} words"
        )

    def validate(self, data: Any) -> bool:
        try:
            data += ""
            return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    def __init__(self):
        print("\nInitializing Log Processor...")

    def process(self, data: Any) -> str:
        print(f'Processing data: "{data}"')
        if self.validate(data) is True:
            print("Validation: Log entry verified")
        else:
            print("Validation: Log entry not verified")
            return "NOT_VALID_DATA_INSERTED"
        if data[:5] == "ERROR":
            level = "ERROR"
            msg = data[7:]
            return f"[ALERT] {level} level detected: {msg}"
        else:
            level = "INFO"
            msg = data[6:]
            return f"[INFO] {level} level detected: {msg}"

    def validate(self, data: Any) -> bool:
        try:
            if data[:5] == "ERROR":
                return True
            if data[:4] == "INFO":
                return True
            return False
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


if __name__ == "__main__":

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    np: NumericProcessor = NumericProcessor()
    print(np.format_output(np.process([1, 2, 3, 4, 5])))

    tp: TextProcessor = TextProcessor()
    print(tp.format_output(tp.process("Hello Nexus World")))

    lp: LogProcessor = LogProcessor()
    print(lp.format_output(lp.process("ERROR: Connection timeout")))

    print("=== Polymorphic Processing Demo ===")
    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    payloads: List[Any] = [[1, 2, 3], "Hello World", "INFO: System ready"]
    print("Processing multiple data types through same interface...")
    idx: int = 0
    while idx < 3:
        print(f"Result {idx + 1}: {processors[idx].process(payloads[idx])}")
        idx += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")
