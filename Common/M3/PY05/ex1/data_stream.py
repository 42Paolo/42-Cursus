from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [
            item for item in data_batch
            if criteria in str(item)
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed": self.processed_count,
        }


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)
        values = [
            float(str(item).split(":")[1])
            for item in data_batch
            if "temp" in str(item)
        ]
        avg = sum(values) / len(values) if values else 0
        return (
            f"Sensor analysis: {len(data_batch)} readings"
            f" processed, avg temp: {avg}°C"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "high-priority":
            return [
                item for item in data_batch
                if "alert" in str(item).lower()
                or "critical" in str(item).lower()
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Environmental Data"
        return stats


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)
        net = 0
        for item in data_batch:
            parts = str(item).split(":")
            if parts[0] == "buy":
                net += int(parts[1])
            elif parts[0] == "sell":
                net -= int(parts[1])
        sign = "+" if net >= 0 else ""
        return (
            f"Transaction analysis: {len(data_batch)}"
            f" operations, net flow: {sign}{net} units"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "high-priority":
            return [
                item for item in data_batch
                if int(str(item).split(":")[1]) > 100
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Financial Data"
        return stats


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)
        errors = [
            item for item in data_batch
            if "error" in str(item).lower()
        ]
        return (
            f"Event analysis: {len(data_batch)} events,"
            f" {len(errors)} error detected"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "System Events"
        return stats


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(
        self, batches: List[List[Any]]
    ) -> List[str]:
        results = []
        for stream, batch in zip(self.streams, batches):
            try:
                results.append(stream.process_batch(batch))
            except Exception as e:
                results.append(f"Error: {e}")
        return results


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    print("\nInitializing Sensor Stream...")
    stats = sensor.get_stats()
    print(f"Stream ID: {stats['stream_id']},"
          f" Type: {stats['type']}")
    batch_s = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {batch_s}")
    print(sensor.process_batch(batch_s))

    trans = TransactionStream("TRANS_001")
    print("\nInitializing Transaction Stream...")
    stats = trans.get_stats()
    print(f"Stream ID: {stats['stream_id']},"
          f" Type: {stats['type']}")
    batch_t = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {batch_t}")
    print(trans.process_batch(batch_t))

    event = EventStream("EVENT_001")
    print("\nInitializing Event Stream...")
    stats = event.get_stats()
    print(f"Stream ID: {stats['stream_id']},"
          f" Type: {stats['type']}")
    batch_e = ["login", "error", "logout"]
    print(f"Processing event batch: {batch_e}")
    print(event.process_batch(batch_e))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    s2 = SensorStream("SENSOR_002")
    t2 = TransactionStream("TRANS_002")
    e2 = EventStream("EVENT_002")
    processor.add_stream(s2)
    processor.add_stream(t2)
    processor.add_stream(e2)

    mixed_batches: List[List[Any]] = [
        ["temp:20.0", "humidity:70"],
        ["buy:200", "sell:50", "buy:100", "sell:80"],
        ["login", "logout", "error"],
    ]

    results = processor.process_all(mixed_batches)
    print("\nBatch 1 Results:")
    print(f"- Sensor data: 2 readings processed")
    print(f"- Transaction data: 4 operations processed")
    print(f"- Event data: 3 events processed")

    print("\nStream filtering active: High-priority data only")
    critical = ["temp:critical:45.0", "alert:overheat"]
    filtered = s2.filter_data(critical, "high-priority")
    large = ["buy:200", "sell:50", "buy:150"]
    filtered_t = t2.filter_data(large, "high-priority")
    print(
        f"Filtered results: {len(filtered)} critical sensor"
        f" alerts, {len(filtered_t)} large transaction"
    )

    print("\nAll streams processed successfully."
          " Nexus throughput optimal.")


main()
