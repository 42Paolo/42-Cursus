from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data
        )

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")
        total = sum(data)
        avg = total / len(data)
        result = (
            f"Processed {len(data)} numeric values,"
            f" sum={total}, avg={avg}"
        )
        return self.format_output(result)

    def format_output(self, result: str) -> str:
        return result


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")
        chars = len(data)
        words = len(data.split())
        result = f"Processed text: {chars} characters, {words} words"
        return self.format_output(result)

    def format_output(self, result: str) -> str:
        return result


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log data")
        level = data.split(":")[0].strip()
        message = data.split(":", 1)[1].strip()
        result = f"[{level}] {level} level detected: {message}"
        return self.format_output(result)

    def format_output(self, result: str) -> str:
        return result


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric = NumericProcessor()
    print("\nInitializing Numeric Processor...")
    print("Processing data: [1, 2, 3, 4, 5]")
    print("Validation: Numeric data verified")
    print(numeric.process([1, 2, 3, 4, 5]))

    text = TextProcessor()
    print("\nInitializing Text Processor...")
    print('Processing data: "Hello Nexus World"')
    print("Validation: Text data verified")
    print(text.process("Hello Nexus World"))

    log = LogProcessor()
    print("\nInitializing Log Processor...")
    print('Processing data: "ERROR: Connection timeout"')
    print("Validation: Log entry verified")
    print(log.process("ERROR: Connection timeout"))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]
    data_samples: List[Any] = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready",
    ]

    for i, (proc, sample) in enumerate(
        zip(processors, data_samples), 1
    ):
        try:
            print(f"Result {i}: {proc.process(sample)}")
        except ValueError as e:
            print(f"Result {i}: Error - {e}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


main()
