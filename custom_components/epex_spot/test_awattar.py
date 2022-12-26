#!/usr/bin/env python3

from EPEXSpot import Awattar

service = Awattar.Awattar(market_area="de")
print(service.MARKET_AREAS)

service.fetch()
print(f"count = {len(service.marketprices)}")
for e in service.marketprices:
    print(f"{e.start_time}: {e.price_eur_per_mwh} {e.UOM_EUR_PER_MWh}")
