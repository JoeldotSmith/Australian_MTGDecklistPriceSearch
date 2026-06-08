import re
import urllib.request
import urllib.parse
from models import CardResult

EXCLUDE_CONDITIONS = {
    "heavily played",
    "damaged",
    "heavily played foil",
    "damaged foil",
}


def fetch_all(cards: list[str]) -> tuple[dict[str, CardResult], dict[str, int]]:
    """
    Fetch cheapest available listing per card from Good Games.
    Returns:
      results  : dict  card_name_lower -> CardResult (cheapest in-stock, excl. bad conditions)
      nm_prices: dict  card_name_lower -> int cents  (cheapest NM regardless of stock)
    """
    results = {}
    nm_prices = {}

    for card_name in cards:
        print(f"  [GoodGames] Searching: {card_name}...", end=" ", flush=True)
        result, nm = _fetch_card(card_name)
        if result:
            results[card_name.lower()] = result
            print("✓")
        else:
            print("not found")
        if nm is not None:
            nm_prices[card_name.lower()] = nm

    return results, nm_prices


def _fetch_card(card_name: str) -> tuple[CardResult | None, int | None]:
    encoded = urllib.parse.quote(card_name.replace(",", ""))
    url = (
        f"https://tcg.goodgames.com.au/search?q={encoded}"
        "&f_Availability=Exclude%20Out%20Of%20Stock"
        "&f_Product%20Type=mtg%20single"
    )

    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode("utf-8")
    except Exception as e:
        print(f"ERROR — {e}")
        return None, None

    pattern = re.compile(
        r"Spurit\.Preorder2\.snippet\.products\['[^']+'\]\s*=\s*(\{.*?\});", re.DOTALL
    )
    matches = pattern.findall(html)

    best: CardResult | None = None
    best_nm: int | None = None

    for match in matches:
        handle_match = re.search(r'handle:"([^"]+)"', match)
        handle = handle_match.group(1) if handle_match else None

        title_match = re.search(r'title:"([^"]+)"', match)
        if not title_match:
            continue
        title = title_match.group(1).replace("\\/\\/", "//")

        if card_name.lower().split(",")[0].strip() not in title.lower():
            continue
        if "art series" in title.lower():
            continue

        if re.search(r'\[[A-Z]{2,}[0-9]+\]', title):
            continue

        set_match = re.search(r"\[([^\]]+)\]$", title)
        set_name = set_match.group(1) if set_match else ""
        clean_title = title[: set_match.start()].strip() if set_match else title

        variant_blocks = re.split(r"(?=\{id:\d+,title:)", match)
        for block in variant_blocks:
            cond_match = re.search(r'title:"([^"]+)"', block)
            qty_match = re.search(r"inventory_quantity:(\d+)", block)
            price_match = re.search(r",price:(\d+),", block)

            if not (cond_match and qty_match and price_match):
                continue

            condition = cond_match.group(1)
            qty = int(qty_match.group(1))
            price = int(price_match.group(1))

            if qty > 0 and condition.lower() not in EXCLUDE_CONDITIONS:
                if best is None or price < best.price_cents:
                    best = CardResult(
                        card_name=clean_title,
                        set_name=set_name,
                        condition=condition,
                        qty=qty,
                        price_cents=price,
                        url=f"https://tcg.goodgames.com.au/products/{handle}" if handle else None,
                    )

            if condition == "Near Mint":
                if best_nm is None or price < best_nm:
                    best_nm = price

    return best, best_nm
