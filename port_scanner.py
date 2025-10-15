#!/usr/bin/env python3
"""
Simple TCP port scanner (beginner-friendly).

Usage examples:
  # Scan default range (1-1024) on localhost
  python3 port_scanner.py 127.0.0.1

  # Scan ports 20-80 on example.com with a 0.3s timeout
  python3 port_scanner.py example.com --start 20 --end 80 --timeout 0.3

  # Save results to a file
  python3 port_scanner.py 192.168.1.10 --start 1 --end 200 --out open_ports.txt
"""

import socket
import argparse
from typing import List


class PortScanner:
    """A small synchronous TCP port scanner."""

    def __init__(self, host: str, timeout: float = 0.5) -> None:
        """
        :param host: target hostname or IP address
        :param timeout: socket timeout in seconds
        """
        self.host = host
        self.timeout = timeout
        self.open_ports: List[int] = []

    def _is_port_open(self, port: int) -> bool:
        """
        Check whether a single TCP port is open.

        Uses connect_ex: returns 0 on success (connected).
        We create a short-lived socket per check and always close it.
        """
        sock = None
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            # connect_ex returns 0 when the connection succeeds (port open)
            result = sock.connect_ex((self.host, port))
            return result == 0
        except socket.gaierror:
            # DNS/name resolution error (invalid host)
            raise
        except socket.error:
            # Any other socket error — treat as closed/unreachable for that port
            return False
        finally:
            if sock:
                try:
                    sock.close()
                except Exception:
                    pass

    def scan(self, start_port: int, end_port: int) -> List[int]:
        """
        Scan the inclusive range [start_port, end_port]. Returns list of open ports.

        Raises ValueError if ports are out of range or start > end.
        Raises socket.gaierror for an unresolvable host.
        """
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError("Port range must be: 1 <= start <= end <= 65535")

        self.open_ports = []
        for port in range(start_port, end_port + 1):
            try:
                if self._is_port_open(port):
                    self.open_ports.append(port)
            except socket.gaierror:
                # propagate host resolution errors immediately
                raise
            except KeyboardInterrupt:
                # Allow user to cancel scan
                print("\nScan cancelled by user.")
                break
        return self.open_ports

    def write_results(self, filepath: str) -> None:
        """Write discovered open ports to a file (one per line)."""
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                for p in self.open_ports:
                    f.write(f"{p}\n")
        except OSError as e:
            print(f"Failed to write results to {filepath}: {e}")


def parse_args() -> argparse.Namespace:
    """Argument parser. `host` is a required positional argument."""
    parser = argparse.ArgumentParser(description="Basic TCP port scanner")
    parser.add_argument("host", help="Target hostname or IP address")
