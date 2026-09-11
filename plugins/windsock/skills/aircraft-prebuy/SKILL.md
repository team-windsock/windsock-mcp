---
name: aircraft-prebuy
description: Evaluate a specific aircraft (US N-number or international registration) the way a careful buyer, broker or lender would — worth, cost to own, comparables, airworthiness directives, and what to check before buying — using the Windsock MCP tools. Use when someone names a tail number and asks what it is worth, whether it is a good buy, what it costs to own, or what to look at before purchase.
---

# Aircraft pre-buy workflow (Windsock)

Use the Windsock MCP tools in this order. Each step feeds ids into the next; do not skip the lookup.

1. **Identify** — `lookup_aircraft` with the registration. Read `make_model_id`, `avionics_ids`, year, engine(s), registrant and the `registration_authority` block (non-US tails: FAA ADs/STCs apply to the *type*, not the registration).
2. **Value** — `value_aircraft` with the registration (or `make_model_id` + specs). If hours/condition are unknown, run `impute_aircraft_specs` first and pass its output. Ask for `include: ["uncertainty"]` when the user is deciding on price. State the value as a range, never a single number without the band.
3. **Cost to own** — `estimate_cost_of_ownership` with the registration; accept overrides the user gives (hours/year, hangar, base airport).
4. **Comparables** — `find_similar_aircraft` (same register by default). Use `search_aircraft` / `count_aircraft` only for fleet-wide questions.
5. **Airworthiness** — `search_airworthiness_directives` and `search_stcs` scoped to `make_model_id`. Summarise recurring ADs and cost drivers; do not list every AD.
6. **Usage and risk** (paid) — `analyze_flight_usage` and `assess_flight_activity_risk` when the buyer cares about how the aircraft has been flown.
7. **Market context** — `get_market_metric` for the aircraft's segment (`list_market_categories` for the key) when the user asks about timing.
8. **Report** (paid) — only if the user wants a verified value report: `create_valuation_report`, then `generate_diligence_checklist` and `search_logbooks` on it.

Rules:
- Check `get_account_usage` before spending a report or logbook allowance; say so if the account is on the free tier.
- A `tools/call` result with `isError: true` and "requires Windsock PRO" means the plan, not the aircraft — tell the user which tool needs an upgrade and continue with the free tools.
- Quote Windsock values as machine estimates with an error band, not appraisals.
