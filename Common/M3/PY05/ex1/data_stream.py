from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict


class DataStream(ABC):

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
            self, data_batch: List[Any],
            criteria: Optional[str] = None
            ) -> List[Any]:
        try:
            if criteria is None:
                return data_batch
            else:
                i: int = 0
                selected: List[Any] = []
                while i < len(data_batch):
                    if criteria == data_batch[i]:
                        selected += [data_batch[i]]
                    i += 1
                return selected
        except Exception as e:
            print(f"ERROR: {e}")
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {}


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.tot_read: int = 0
        self.tot_temp: float = 0.0
        self.avg_temp: float = 0.0
        self.type = "Sensor"
        print("\nInitializing Sensor Stream...")
        print(f"Stream ID: {stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        self.tot_read = 0
        self.tot_temp = 0.0
        self.avg_temp = 0.0
        try:
            idx: int = 0
            while idx < len(data_batch):
                self.tot_read += 1
                self.tot_temp += data_batch[idx]["temp"]
                idx += 1
        except Exception as e:
            return f"Error: {e}"
        try:
            self.avg_temp = self.tot_temp / self.tot_read
        except Exception as e:
            return f"ERROR: {e}"

        return (
            f"Processing sensor batch: {data_batch}\n"
            f"Sensor analysis: {self.tot_read} readings processed, "
            f"avg temp: {self.avg_temp}°C"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "readings processed": self.tot_read,
        }

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None
            ) -> List[Any]:
        try:
            if criteria is None:
                return data_batch
            elif criteria == "temp":
                result: List[Any] = []
                idx: int = 0
                while idx < len(data_batch):
                    item = data_batch[idx]
                    if criteria in item and item[criteria] > 100:
                        result += [item]
                    idx += 1
                return result
            else:
                raise Exception("WRONG INPUTED CRITERIA")
        except Exception as e:
            print(f"ERROR: {e}")
            return []


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.net_flow: float = 0
        self.tot_ops: int = 0
        self.type = "Transaction"
        print("\nInitializing Transaction Stream...")
        print(f"Stream ID: {stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        self.net_flow = 0
        self.tot_ops = 0
        try:
            idx: int = 0
            while idx < len(data_batch):
                self.tot_ops += 1
                index = data_batch[idx]
                if "sell" in index:
                    self.net_flow -= index["sell"]
                elif "buy" in index:
                    self.net_flow += index["buy"]
                else:
                    raise Exception("Wrong type of data inserted")
                idx += 1
        except Exception as e:
            return f"Error: {e}"
        sign = "+" if self.net_flow >= 0 else ""
        return (
            f"Processing transaction batch: {data_batch}\n"
            f"Transaction analysis: {self.tot_ops} operations, "
            f"net flow: {sign}{int(self.net_flow)} units"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "operations processed": self.tot_ops,
        }

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None
            ) -> List[Any]:
        try:
            if criteria is None:
                return data_batch
            elif criteria == "sell":
                result: List[Any] = []
                idx: int = 0
                while idx < len(data_batch):
                    item = data_batch[idx]
                    if "sell" in item and item["sell"] > 100:
                        result += [item]
                    idx += 1
                return result
            elif criteria == "buy":
                result = []
                idx = 0
                while idx < len(data_batch):
                    item = data_batch[idx]
                    if "buy" in item and item["buy"] > 100:
                        result += [item]
                    idx += 1
                return result
            else:
                raise Exception(
                    "Wrong criteria inputed: 'buy' or 'sell' valid"
                    )
        except KeyError as ke:
            print(f"KEY_ERROR: {ke}")
            return []
        except Exception as e:
            print(f"ERROR: {e}")
            return []


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.tot_evt: int = 0
        self.tot_err: int = 0
        self.type = "Event"
        print("\nInitializing Event Stream...")
        print(f"Stream ID: {stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        self.tot_err = 0
        self.tot_evt = 0
        try:
            idx: int = 0
            while idx < len(data_batch):
                k = data_batch[idx]
                self.tot_evt += 1
                if k == "error":
                    self.tot_err += 1
                elif k == "login" or k == "logout":
                    idx += 1
                    continue
                else:
                    raise Exception("Wrong inputed data")
                idx += 1
        except Exception as e:
            return f"Error: {e}"

        return (
            f"Processing event batch: {data_batch}\n"
            f"Event analysis: {self.tot_evt} events, "
            f"{self.tot_err} error detected"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "events processed": self.tot_evt,
        }

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None
            ) -> List[Any]:
        try:
            if criteria is None:
                return data_batch
            else:
                result: List[Any] = []
                idx: int = 0
                while idx < len(data_batch):
                    item = data_batch[idx]
                    if item == criteria:
                        result += [item]
                    idx += 1
                return result
        except Exception as e:
            print(f"ERROR: {e}")
            return []


class StreamProcessor:
    def __init__(self, streams: List[List[DataStream]]) -> None:
        self.streams = streams
        self.ssdata: List[Any] = [
            {"temp": 22.5, "humidity": 65, "pressure": 1013},
            {"temp": 120, "humidity": 10000, "pressure": 500},
            {"temp": 480, "humidity": 400, "pressure": 300},
        ]
        self.tsdata: List[Dict] = [
            {"buy": 120},
            {"sell": 120},
            {"buy": 75},
            {"buy": 20},
        ]
        self.esdata: List[str] = [
            "error", "login", "logout"
        ]

    def __len_res(self, stream: List[Any]) -> int:
        len_stream: int = 0
        try:
            idx: int = 0
            while idx < len(stream):
                len_stream += 1
                idx += 1
        except Exception as e:
            print(f"ERROR: {e}")
        return len_stream

    def process_batch(self) -> None:
        batch_counter: int = 0
        try:
            i: int = 0
            while i < len(self.streams):
                lst = self.streams[i]
                batch_counter += 1
                print(f"Batch {batch_counter} Results:")
                j: int = 0
                while j < len(lst):
                    s = lst[j]
                    data = s.get_stats()
                    keys = list(data)
                    k_i: int = 0
                    while k_i < len(keys):
                        k = keys[k_i]
                        print(f"- {s.type} data: {data[k]} {k}")
                        k_i += 1
                    j += 1
                i += 1
        except Exception as e:
            print(f"ERROR: {e}")

    def filter_batch(self) -> None:
        sensor_result: List[Any] = []
        trans_result: List[Any] = []
        event_result: List[Any] = []
        try:
            i: int = 0
            while i < len(self.streams):
                list_stream = self.streams[i]
                j: int = 0
                while j < len(list_stream):
                    st = list_stream[j]
                    if isinstance(st, SensorStream) is True:
                        sensor_result += st.filter_data(self.ssdata, "temp")
                    elif isinstance(st, TransactionStream) is True:
                        trans_result += st.filter_data(self.tsdata, "buy")
                    elif isinstance(st, EventStream) is True:
                        event_result += st.filter_data(self.esdata, "error")
                    else:
                        raise Exception("Wrong stream inputed")
                    j += 1
                i += 1
        except Exception as e:
            print(f"ERROR: {e}")
            return
        print(
            "Filtered results: "
            f"{self.__len_res(sensor_result)} critical sensor alerts, "
            f"{self.__len_res(trans_result)} large transaction"
        )


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    ssdata: List[Dict] = [
        {"temp": 22.5, "humidity": 65, "pressure": 1013},
        {"temp": 120, "humidity": 10000, "pressure": 500},
        {"temp": 480, "humidity": 400, "pressure": 300},
    ]
    tsdata: List[Dict] = [
        {"buy": 100},
        {"sell": 150},
        {"buy": 75},
        {"buy": 20},
    ]
    esdata: List[str] = [
        "login", "error", "logout"
    ]
    ss: SensorStream = SensorStream("SENSOR_001")
    print(ss.process_batch(ssdata))
    ts: TransactionStream = TransactionStream("TRANS_001")
    print(ts.process_batch(tsdata))
    es: EventStream = EventStream("EVENT_001")
    print(es.process_batch(esdata))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    ss2: SensorStream = SensorStream("SENSOR_002")
    ss2.process_batch([
        {"temp": 18.0, "humidity": 55, "pressure": 1010},
        {"temp": 27.3, "humidity": 70, "pressure": 1008},
    ])
    ts2: TransactionStream = TransactionStream("TRANS_002")
    ts2.process_batch([
        {"buy": 200}, {"sell": 50}, {"buy": 300}, {"sell": 150},
    ])
    es2: EventStream = EventStream("EVENT_002")
    es2.process_batch(["login", "error", "logout"])

    streamprocessor: StreamProcessor = StreamProcessor([[ss2, ts2, es2]])
    streamprocessor.process_batch()

    print("Stream filtering active: High-priority data only")
    streamprocessor.filter_batch()
    print("\nAll streams processed successfully. Nexus throughput optimal.")
