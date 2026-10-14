"""Record wildlife sightings and summarise sanctuary observations."""

import hashlib
import sqlite3


def create_connection() -> sqlite3.Connection:
    """Create an in-memory database and initialise its sightings table."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE sightings (
            id INTEGER PRIMARY KEY,
            species TEXT NOT NULL,
            zone TEXT NOT NULL,
            count INTEGER NOT NULL CHECK (count > 0)
        )
        """
    )
    return connection


def log_sighting(
    connection: sqlite3.Connection,
    species: str,
    zone: str,
    count: int,
    extras: dict[str, int] | None = None,
) -> dict[str, int]:
    """Store a sighting and update the caller's per-species totals."""
    if not isinstance(species, str) or not species.strip():
        raise ValueError("species must be a non-empty string")
    if not isinstance(zone, str) or not zone.strip():
        raise ValueError("zone must be a non-empty string")
    if isinstance(count, bool) or not isinstance(count, int) or count <= 0:
        raise ValueError("count must be a positive integer")

    if extras is None:
        extras = {}

    connection.execute(
        "INSERT INTO sightings (species, zone, count) VALUES (?, ?, ?)",
        (species.strip(), zone.strip(), count),
    )
    extras[species.strip()] = extras.get(species.strip(), 0) + count
    return extras


def observer_id(observer: str) -> str:
    """Return a stable short SHA-256 label for an observer name.

    This label is for demonstration, not authentication or guaranteed
    anonymisation; predictable names can still be guessed.
    """
    if not isinstance(observer, str) or not observer.strip():
        raise ValueError("observer must be a non-empty string")
    digest = hashlib.sha256(observer.strip().encode("utf-8")).hexdigest()
    return digest[:12]


def zone_summary(connection: sqlite3.Connection, zone: str) -> int:
    """Return the total animals recorded for a zone, or zero if none exist."""
    row = connection.execute(
        "SELECT SUM(count) FROM sightings WHERE zone = ?", (zone,)
    ).fetchone()
    return int(row[0] or 0)


def rarest(connection: sqlite3.Connection) -> str | None:
    """Return the species with the fewest recorded sightings, if any."""
    rows = connection.execute(
        """
        SELECT species, SUM(count) AS total
        FROM sightings
        GROUP BY species
        ORDER BY total ASC, species ASC
        """
    ).fetchall()
    if not rows:
        return None
    return str(rows[0][0])


def main() -> None:
    """Run the small demonstration described in the lab instructions."""
    connection = create_connection()
    try:
        totals = log_sighting(connection, "Leopard", "North", 1)
        log_sighting(connection, "Chital", "North", 24, totals)
        log_sighting(connection, "Hornbill", "East", 3, totals)
        print(
            observer_id("Arun"),
            zone_summary(connection, "North"),
            rarest(connection),
        )
    finally:
        connection.close()


if __name__ == "__main__":
    main()
