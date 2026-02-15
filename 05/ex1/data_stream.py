"""
Code Nexus - Polymorphic Stream System.
Module for processing different types of data streams
(Sensor, Transaction, Event) using object-oriented principles.
"""

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Generator


class DataStream(ABC):
    """Abstract base class for all data stream types."""

    def __init__(self, stream_id: str):
        """Initialize the stream with a unique identifier."""
        self.stream_id: str = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a summary string."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter data based on given criteria."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return a dictionary containing stream statistics."""
        return {}

    @abstractmethod
    def get_analysis(self) -> str:
        """Provide a detailed textual analysis of the processed data."""
        pass


class SensorStream(DataStream):
    """Stream for environmental sensor data."""

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.avg: float = 0
        self.ops: int = 0
        self.errors: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Calculate averages and format sensor output."""
        if not data_batch:
            self.avg = 0.0

        self.avg = round(sum(v["temp"] for v in data_batch)
                         / len(data_batch), 2)
        self.ops = sum(len(value) for value in data_batch)

        line: str = ""
        template: str = "[temp:{temp}, " \
            "humidity:{humidity}, pressure:{pressure}]"
        for item in data_batch:
            line += template.format(**item)
        return f"Processing sensor batches: {line}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Dict[str, float]]:
        """Apply thresholds to sensor readings and count errors."""
        if not criteria:
            return data_batch

        for value in data_batch:
            if not (-20 <= value['temp'] <= 25):
                self.errors += 1
            elif not (0 <= value['humidity'] <= 95):
                self.errors += 1
            elif not (0 <= value['pressure'] <= 2500):
                self.errors += 1
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str, Union[str, int, float]] = {
            "id": self.stream_id,
            "type": "Sensor",
            "subtype": "Environmental Data",
            "opt": "readings",
            "qty": self.ops,
            "avgtmp": self.avg,
            "errors": self.errors
        }
        return stats

    def get_analysis(self) -> str:
        template = "Sensor analysis: {} readings processed, avg temp: {}ºC"
        return template.format(self.ops, self.avg)


class TransactionStream(DataStream):
    """Stream for financial transaction data."""

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.ops: int = 0
        self.sum: Union[str, int] = 0
        self.errors: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process buys/sells and calculate net flow."""
        self.ops = len(data_batch)
        total: float = 0
        line: List[str] = []
        for v in data_batch:
            key: str = "sell" if v < 0 else "buy"
            value: float = -v if key == "sell" else v
            total += v
            line.append(f"{key}:{value}")
        sign: str = "+" if total > 0 else ""
        self.sum = f"{sign}{total}"
        return f"Processing transaction batches: {', '.join(line)}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Filter transactions based on range limits."""
        if not criteria:
            return data_batch
        for num in data_batch:
            if not (-200 <= num <= 200):
                self.errors += 1
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str, Union[str, int, float]] = {
            "id": self.stream_id,
            "type": "Transaction",
            "subtype": "Financial Data",
            "opt": "operations",
            "qty": self.ops,
            "errors": self.errors,
            "net": self.sum
        }
        return stats

    def get_analysis(self) -> str:
        template = "Transaction analysis: {} operations, net flow: {} units"
        return template.format(self.ops, self.sum)


class EventStream(DataStream):
    """Stream for system event logs."""

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.ops: int = 0
        self.errors: int = 0
        self.msg: str = "error"

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process event batch and join as string."""
        self.ops = len(data_batch)
        line: str = ", ".join(map(str, data_batch))
        return f"Processing event batch: [{line}]"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Count specific error events and update status message."""
        for data in data_batch:
            if data == "error":
                self.errors += 1
        if self.errors > 1:
            self.msg = "errors"
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str, Union[str, int, float]] = {
            "id": self.stream_id,
            "type": "Event",
            "subtype": "System Events",
            "opt": "events",
            "qty": self.ops,
            "errors": self.errors,
            "text": self.msg
        }
        return stats

    def get_analysis(self) -> str:
        template = "Event analysis: {} events, {} {} detected"
        return template.format(self.ops, self.errors, self.msg)


class StreamProcess():
    """Manager to orchestrate multiple data streams."""

    def __init__(self):
        """Initialize the processor with an empty list of streams."""
        self.streams: List[DataStream] = []
        self.count: int = 0

    def add_streams(self, stream: DataStream) -> None:
        """Add a stream to the processing list."""
        self.streams.append(stream)

    def process_all(self, data: List[Any]) -> None:
        """Process all batches at once"""

        for stream, data, criteria in data:
            s_dict = stream.get_stats()
            print(f"\nInitializing {s_dict['type']} Stream...")
            print(f"Stream ID: {s_dict['id']}, Type: {s_dict['subtype']}")

            stream.filter_data(data, criteria)
            print(stream.process_batch(data))
            print(stream.get_analysis())

            self.add_streams(stream)

        for line in self.batch_result():
            print(line)

        s_stats = self.streams[0].get_stats()
        t_stats = self.streams[1].get_stats()

        print("\nStream filtering active: High-priority data only")

        template = "Filtered results: {} critical " \
            "sensor alerts, {} large transaction"
        print(template.format(s_stats['errors'], t_stats['errors']))

    def batch_result(self) -> Generator[str, None, None]:
        """Generator that yields results for all registered streams."""
        self.count += 1

        print(f"\nBatch {self.count} Results:")

        for stream in self.streams:
            stats = stream.get_stats()
            template = "- {} data: {} {} processed"
            yield template.format(stats['type'], stats['qty'], stats['opt'])


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    s = SensorStream("SENSOR_001")
    t = TransactionStream("TRANS_001")
    e = EventStream("EVENT_001")
    payloads = [
        (s, [{"temp": 20.5, "humidity": 65, "pressure": 1013}], "high"),
        (t, [100, -250, 75], "high"),
        (e, ["login", "error", "error"], None)
    ]

    orchestrator = StreamProcess()
    orchestrator.process_all(payloads)

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
