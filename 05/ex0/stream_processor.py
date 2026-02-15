"""
Code Nexus - Data Processor Foundation.
Module providing base processing capabilities for numeric, text, and log data
through a polymorphic interface.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Union, List, Generator


class ValidationError(Exception):
    pass


class DataProcessor(ABC):
    """
    Abstract base class defining the common interface for all data processors
    within the Code Nexus.
    """
    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the input data and return a result string"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if the provided data is appropriate for this processor"""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string for display[cite: 145]."""
        return ""

    def final_output(self, index: int) -> str:
        """Generate a summary string for polymorphic demonstrations."""
        return ""

    def get_stats(self) -> Dict[str, Any]:
        """Retrieve processing statistics and metadata."""
        return {}


class NumericProcessor(DataProcessor):
    """
    Specialized processor for numeric data streams.
    """
    def __init__(self) -> None:
        """Initialize numeric counters and status."""
        self.processed = 0
        self.avg = 0
        self.sum = 0

    def process(self, data: Any) -> str:
        """Calculate sum and average from numeric list."""
        self.processed = len(data)
        self.sum = sum(data)
        self.avg = self.sum / self.processed
        char_data = [str(n) for n in data]
        return f"Processing data: [{', '.join(char_data)}]"

    def validate(self, data: Any) -> bool:
        """Check if all elements in data are integers or floats."""
        if not data:
            return False

        for n in data:
            if not isinstance(n, (int, float)):
                return False
        return True

    def format_output(self, result: str) -> str:
        """Format numeric results with count, sum, and average."""
        template = "Output: Processed {} numeric values, sum={}, avg={}"
        return template.format(self.processed, self.sum, self.avg)

    def final_output(self, index: int) -> str:
        """Provide a indexed summary of numeric processing."""
        template = "Result {}: Processed {} numeric values, sum={}, avg={}"
        return template.format(index, self.processed, self.sum, self.avg)

    def get_stats(self) -> Dict[str, Union[str, int, bool]]:
        """Return a dictionary of numeric processing statistics."""
        stats = {
            "type": "Numeric",
            "subtype": "data",
            "sum": self.sum,
            "avg": self.avg,
            "processed": self.processed
        }
        return stats


class TextProcessor(DataProcessor):
    """Specialized processor for text-based data streams."""

    def __init__(self) -> None:
        """Initialize text metrics and status."""
        self.chars = 0
        self.words = 0

    def process(self, data: Any) -> str:
        """Calculate character and word counts from text."""
        self.chars = len(data)
        self.words = len(data.split())
        return f'Processing data: "{data}"'

    def validate(self, data: Any) -> bool:
        """Validate if the input data is a string."""
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        """Format text results with character and word counts."""
        template = "{} Processed text {} characters, {} words"
        return template.format(result, self.chars, self.words)

    def final_output(self, index: int) -> str:
        """Provide a indexed summary of text processing."""
        template = "Result {}: Processed text {} characters, {} words"
        return template.format(index, self.chars, self.words)

    def get_stats(self) -> Dict[str, Union[str, int, bool]]:
        """Return a dictionary of text processing statistics."""
        stats = {
            "type": "Text",
            "subtype": "data",
            "chars": self.chars,
            "words": self.words,
        }
        return stats


class LogProcessor(DataProcessor):
    """Specialized processor for system log entries."""

    def __init__(self) -> None:
        """Initialize log message and level placeholders."""
        self.text = "..."
        self.msg = "..."

    def process(self, data: Any) -> str:
        """Identify log data for processing."""
        if "ERROR:" in data:
            self.text = "ALERT"
            self.msg = data[7:].strip()
        else:
            self.text = "INFO"
            self.msg = data[6:].strip()
        return f'Processing data: "{data}"'

    def validate(self, data: Any) -> bool:
        """Parse log level (ERROR/INFO) and extract message."""
        return isinstance(data, str) and (":" in data)

    def format_output(self, result: str) -> str:
        """Format log results with alert level and message."""
        tmp = "ERROR" if self.text == "ALERT" else "INFO"
        template = "{} [{}] {} level detected: {}"
        return template.format(result, self.text, tmp, self.msg)

    def final_output(self, index: int) -> str:
        """Provide a indexed summary of log processing."""
        tmp = "ERROR" if self.text == "ALERT" else "INFO"
        template = "Result {}: [{}] {} level detected: {}"
        return template.format(index, self.text, tmp, self.msg)

    def get_stats(self) -> Dict[str, Any]:
        """Return a dictionary of log entry statistics."""
        stats = {
            "type": "Log",
            "subtype": "entry",
            "msg": self.msg,
            "error": self.text
        }
        return stats


class AllProcessor():
    """
    Orchestrator class that handles multiple
    processors polymorphically.
    """
    def polymorphic_process(self, list: List[tuple]) -> Generator:
        """
        Iterate through a list of processor/data pairs and execute methods
        through the common interface.
        """
        for proc, data in list:
            try:
                stats = proc.get_stats()
                yield f"\nInitializing {stats['type']} Processor"

                if not proc.validate(data):
                    template = "Error: Validation {} data failed"
                    raise ValidationError(template.format(stats['type']))
                yield proc.process(data)
                template = "Validation {} {} verified"
                yield template.format(stats['type'], stats['subtype'])
                yield proc.format_output("Output:")
            except (ValidationError, TypeError, ValueError) as e:
                yield f"{e}"

        print("\n=== Polymorphic Processing Demo ===")
        print("Processing multiple data types through same interface...")

        for i, (proc, data) in enumerate(list, 1):
            stats = proc.get_stats()
            yield proc.final_output(i)


def main():
    """
    Main entry point for the Code Nexus diagnostic program.
    """
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    payloads = [
        (numeric, [1, 2, 3, 4, 5]),
        (text, "Hello World"),
        (log, "INFO: Connection lost")
    ]

    orchestrator = AllProcessor()
    for message in orchestrator.polymorphic_process(payloads):
        print(message)

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
