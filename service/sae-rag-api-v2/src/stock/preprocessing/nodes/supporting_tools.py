import re


def text_cleaning(text: str) -> str:
    """Cleaning text by removing unnecessary characters and spaces."""
    if isinstance(text, str):
        # Convert to lowercase
        text = text.lower()
        # Remove leading and trailing spaces
        text = text.strip()
        # Replace multiple spaces with a single space
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters except for common ones
        text = re.sub(r'[^\w\s.,!?$%&@()-]', '', text)
    return text


def content_parser(text: str, remove_after: str = None, patterns: list = None) -> str:
    if not isinstance(text, str):
        return text

    if remove_after:
        text = re.sub(fr"{remove_after}.*", "", text, flags=re.IGNORECASE)

    if patterns:
        combined_pattern = "|".join(patterns)
        text = re.sub(combined_pattern, "", text, flags=re.IGNORECASE)

    # Remove excessive whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text
