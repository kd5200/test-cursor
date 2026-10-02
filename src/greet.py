"""Small greeting helper used by the GitHub demo."""


def greet(name: str, title: str | None = None) -> str:
    """Return a greeting for `name`, optionally prefixed with `title`."""
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be empty")

    if title:
        cleaned = f"{title.strip()} {cleaned}"

    return f"Hello, {cleaned}!"
