"""
Grocery List Manager

This script demonstrates core Python list operations using a simple grocery list.
It loads an initial list of items from a CSV file and then:
  - Adds new items
  - Removes some items
  - Sorts the list
  - Shows counts and unique items

The final state and intermediate steps are written to results/grocery_list_report.txt
for use in a professional portfolio.
"""

import pandas as pd
from pathlib import Path

DATA_PATH = Path("data") / "grocery_list.csv"
RESULTS_PATH = Path("results") / "grocery_list_report.txt"


def load_grocery_list(path: Path) -> list:
    """Load grocery items from a one-column CSV into a Python list."""
    df = pd.read_csv(path)
    # Assume a single column named 'item'
    grocery_list = df["item"].dropna().tolist()
    return grocery_list


def save_report(text: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    lines = []

    # Load initial list
    grocery_list = load_grocery_list(DATA_PATH)
    lines.append("=== Initial Grocery List ===")
    lines.append(f"Total items: {len(grocery_list)}")
    lines.append(str(grocery_list))

    # Add some items (from original notebook: Kiwis, Raspberries, Cinnamon, Paprika)
    items_to_add = ["Kiwis", "Raspberries", "Cinnamon", "Paprika"]
    lines.append("\n=== Adding New Items ===")
    lines.append(f"Items to add: {items_to_add}")
    grocery_list.extend(items_to_add)
    lines.append(f"List after adding items ({len(grocery_list)} total):")
    lines.append(str(grocery_list))

    # Simulate user input step from the lab with a fixed example for reproducible results
    simulated_user_item = "Dark Chocolate"
    lines.append("\n=== Simulated User Input Item ===")
    lines.append(f"Pretend the user typed: {simulated_user_item!r}")
    grocery_list.append(simulated_user_item)
    lines.append("List after adding user item:")
    lines.append(str(grocery_list))

    # Remove some items (from the notebook: Eggs and Apples) if they exist
    items_to_remove = ["Eggs", "Apples"]
    lines.append("\n=== Removing Items ===")
    lines.append(f"Items to remove (if present): {items_to_remove}")
    for item in items_to_remove:
        if item in grocery_list:
            grocery_list.remove(item)
            lines.append(f"Removed: {item}")
        else:
            lines.append(f"Item not found, cannot remove: {item}")
    lines.append("List after removals:")
    lines.append(str(grocery_list))

    # Sort list alphabetically
    lines.append("\n=== Sorted Grocery List (A–Z) ===")
    grocery_list_sorted = sorted(grocery_list)
    lines.append(str(grocery_list_sorted))

    # Basic stats: unique items, count
    unique_items = sorted(set(grocery_list_sorted))
    lines.append("\n=== Summary Statistics ===")
    lines.append(f"Final total items: {len(grocery_list_sorted)}")
    lines.append(f"Unique item count: {len(unique_items)}")
    lines.append("Unique items:")
    lines.append(str(unique_items))

    report_text = "\n".join(lines)
    save_report(report_text, RESULTS_PATH)

    print("Grocery list analysis complete.")
    print("Report written to:", RESULTS_PATH)


if __name__ == "__main__":
    main()
