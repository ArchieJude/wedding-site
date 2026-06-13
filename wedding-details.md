# Wedding Website — Reference Details

> Reference doc for building the wedding site with Claude Code.
> Last updated: June 13, 2026
> **Status note:** Date and venue are NOT yet finalized. Keep these fields easy to edit until the deposit is paid. Leading option is 12/22 at Beitou Museum, but not yet booked.

---

## The Couple
- **Names:** Ariel & Achbold
- **Planning from:** United States (wedding is in Taiwan)
- **Languages:** Couple reads/speaks Chinese fluently

## Event Basics
- **Location:** Taipei, Taiwan
- **Date:** December 2026 — targeting **12/21 or 12/22** (12/22 currently leading)
- **Time:** Evening dinner reception
- **Guest count:** Intimate, ~40–50 guests (50 or fewer)
- **Format:** Western-style vows + traditional Chinese tea ceremony
- **Vibe:** Small, cozy, personal (not grand). Same room for ceremony and dinner.
- **Aesthetic:** Garden / heritage / Japandi / romantic European; mountain, valley, waterfront, or historic-building backdrops appealing
- **Food:** Good-quality Chinese food (Taiwanese, Cantonese, or other — no strong preference)

## Venue (NOT YET LOCKED — leading candidate)
**北投文物館 (Beitou Museum)** — historic Japanese-style venue in Taipei
- 12/21: closed (regular closure day)
- **12/22: can host evening banquet, 17:00–21:00**
- Venue minimum spend: **NT$200,000**
- Menu options (both +10% service charge), 12-course Japanese kaiseki style w/ high-mountain tea:
  - 佳山瑰麗風華 (lower tier): NT$2,580/person
  - 佳山盛彩雅饌 (higher tier): NT$3,280/person — upgraded dishes + unlimited fruit-vinegar drinks
- Process: confirm package + guest count + add-ons → they issue 報價單 (quote/contract) → NT$40,000 deposit within 2 weeks locks the date

**Other venues considered:** Frigga Garden 蕾莉嘉, Gen. Sun Li-Jen Residence, 泉源閣 Bando Club at Wellspring Beitou, 草山夜未眠, Club 63, 1956 Vintage, 扶日 Wedding, Na'vi Garden, Ark Manor (Taichung)

## Wedding Planner (signed)
- Studio retained: NT$58,800 (Mandarin planning & coordination)
- Contact: **Ruby**
- Day-of coverage: 5 hours; overtime NT$4,000/hr

---

## Website Requirements

### Core pages / content
- Landing/hero: couple names, date, location
- Event details: ceremony + reception time, address, map link
- Story / about section (optional)
- Travel & accommodations: hotels, directions, parking
- FAQ: dress code, kids, parking, timing
- Registry links (optional)
- Schedule/timeline of the day

### RSVP form fields
- Name
- Attending (yes/no)
- Number in party
- Plus-one / guest name fields
- Meal preference (if seated dinner) — *open decision below*
- Dietary restrictions / allergies (free text)
- Song requests or notes (optional)
- Confirmation message after submitting

### RSVP tracking / admin
- Stored responses viewable in a dashboard
- Running counts (total yes/no, headcount, meal tallies)
- CSV export
- Guest list filtering/search
- (Nice to have) Email notification on new RSVP; reminder mechanism for non-responders

### Technical decisions
- **Data storage:** static sites can't store RSVPs alone. Options discussed: Supabase or Firebase (backend/db), or no-code (Airtable / embedded Google Form). Supabase free tier is a common pick.
- **Hosting:** Vercel, Netlify, or GitHub Pages (free tiers)
- **Domain:** custom (~$12/yr) vs. free subdomain
- **Access control:** open RSVP vs. guest-only (passcode or unique per-guest links) — *open decision below*
- **Mobile-first:** most guests open from a texted link on a phone

### Design
- Theme/palette + fonts matching the wedding aesthetic (garden/heritage/Japandi/romantic)
- Hero image or photo
- Fast loading (phone-first)

---

## Open Decisions to Resolve
1. **Seated dinner with meal choices?** (determines whether RSVP needs a meal-selection field)
2. **Guest-only access (unique links) vs. open RSVP form?**
3. **Final date + venue** — keep editable until deposit is paid

---

## Logistics Notes
- Digital invites only (no physical) — plan to text guests a link to the site
- Mongolian-passport guests need a tourist visa for Taiwan (apply in person at a Taiwanese embassy/consulate; passport valid 6+ months, 2 blank pages; fill out Taiwan Arrival Card online ~3 days before flying)
