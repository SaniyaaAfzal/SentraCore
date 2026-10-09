
import argparse
import csv
from pathlib import Path


def detect_event(event, threshold=20):
    """Return ALERT or NORMAL using a simple demonstration rule."""
    try:
        count = int(event["connection_count"])
    except (KeyError, ValueError, TypeError):
        raise ValueError("Each event needs a valid connection_count")

    return "ALERT" if count >= threshold else "NORMAL"


def process_csv(csv_path, threshold=20, serial_connection=None):
    """Classify CSV events and optionally transmit results to an ESP32."""
    results = []

    with Path(csv_path).open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames or "connection_count" not in reader.fieldnames:
            raise ValueError("CSV must contain a connection_count column")

        for event in reader:
            status = detect_event(event, threshold)
            event_id = event.get("event_id", "unknown")
            print(f"Event {event_id}: {status}")
            results.append((event_id, status))

            if serial_connection is not None:
                serial_connection.write((status + "\n").encode("utf-8"))
                serial_connection.flush()

    return results


def main():
    parser = argparse.ArgumentParser(
        description="SentraCore rule-based event detector"
    )
    parser.add_argument(
        "--csv",
        default="sample_data/network_events.csv",
        help="Path to the event CSV file",
    )
    parser.add_argument(
        "--port",
        help="Optional serial port, e.g. COM3 or /dev/ttyUSB0",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=20,
        help="Demonstration connection-count threshold",
    )
    args = parser.parse_args()

    if args.threshold < 1:
        parser.error("--threshold must be at least 1")

    if not Path(args.csv).is_file():
        parser.error(f"CSV file not found: {args.csv}")

    if args.port:
        try:
            import serial
        except ImportError:
            parser.error("Install pyserial first: python -m pip install pyserial")

        with serial.Serial(args.port, 115200, timeout=1) as connection:
            # Allow the ESP32 to reset after opening its serial port.
            import time
            time.sleep(2)
            process_csv(args.csv, args.threshold, connection)
    else:
        process_csv(args.csv, args.threshold)


if __name__ == "__main__":
    main()
