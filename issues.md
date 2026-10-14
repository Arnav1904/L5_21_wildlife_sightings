# Issue Log

Line numbers refer to the original `wildlife_sightings.py` file in the repository.

| Issue | Type | Line(s) | Description | Fix |
|---|---|---:|---|---|
| SQL injection risk | Security — High | 9 | Input was added directly to an SQL query. | Use SQL placeholders and pass input values separately. |
| Mutable default argument | Correctness — Medium | 8 | `extras={}` could share data between calls. | Use `None` and create a new dictionary when needed. |
| Empty sightings crash | Correctness — Medium | 27 | `min()` fails when there are no sightings. | Return `None` when the table is empty. |
| Weak hash choice | Security / privacy — Medium | 15 | MD5 is not suitable for security-sensitive hashing. A hash of a predictable name is not secure anonymisation. | Use SHA-256 and state its limits. |
| Missing input checks | Data integrity — Medium | 8–9 | Empty names and invalid counts could be stored. | Check names and require a positive integer count. |
| Inconsistent function names | Style — Low | 8, 14, 17 | Function names did not use `snake_case`. | Rename them to `log_sighting`, `observer_id`, and `zone_summary`. |
| Work ran during import | Design — Low | 4–5, 39 | The database was created and the demo ran when the file was imported. | Create the database in a function and use a `__main__` guard. |
| Hard to read and maintain | Style — Low | Throughout | Formatting and documentation were inconsistent. | Use consistent formatting, clear names, and short docstrings. |

## Fixes made

The corrected program uses parameterised SQL, validates inputs, avoids a shared default dictionary, uses SHA-256, follows `snake_case`, handles an empty table, and runs the demo only when launched directly. The demo records 25 sightings in the North zone and reports Leopard as the rarest species.
