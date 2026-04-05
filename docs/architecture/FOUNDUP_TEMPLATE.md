# FoundUp Template -- Adding a New FoundUp

Repeatable pattern for adding a new FoundUp to the FOUNDUPS ecosystem.
Follow this checklist when a project needs community coordination surfaces.

See FOUNDUPS_ARCHITECTURE.md for the full five-layer flow.
See DISCORD_BLUEPRINT.md for the Discord server structure.

---

## When to Create a FoundUp Category

Create a Discord category when the FoundUp has at least ONE of:
- A GitHub repo with active development
- A pfMALL listing with content
- Active contributors who need a coordination surface

Do NOT create a category for ideas without implementation,
staging projects with zero content, or FoundUps that only exist as a name.

---

## Prerequisites

- [ ] FoundUp name and short prefix decided (e.g., "Science Swarm Hub" / "swarm")
- [ ] GitHub repo exists under FOUNDUPS org (if code-based)
- [ ] At least one active contributor or operator champion

---

## Step 1: Create Discord Category

- [ ] Create category in FOUNDUPS Discord server
- [ ] Name format: "[FOUNDUP NAME]" (e.g., "SCIENCE SWARM HUB")

## Step 2: Create Channels (4 per FoundUp)

- [ ] #[prefix]-general (text) -- project discussion
- [ ] #[prefix]-github (text, read-only) -- webhook feed from GitHub
- [ ] #[prefix]-work (text) -- what are you working on
- [ ] [prefix]-voice (voice) -- project voice channel

Permissions: @Stakeholder and above can see/post. #[prefix]-github is read-only.

## Step 3: Create Roles (2 per FoundUp)

- [ ] @[prefix]-contributor -- active contributors (manual assignment)
- [ ] @[prefix]-notify -- opt-in notifications (self-assign via reaction role)

## Step 4: Set Up GitHub Webhook

- [ ] GitHub repo > Settings > Webhooks > Add webhook
- [ ] Payload URL: Discord webhook URL for #[prefix]-github
- [ ] Events: Issues, Pull requests, Releases, Issue comments
- [ ] Test with a test issue

## Step 5: Update #start-here

- [ ] Add reaction emoji for @[prefix]-notify role
- [ ] Update pinned message with new FoundUp listing

## Step 6: Pin Welcome Message in #[prefix]-general

Include: name, description, GitHub link, pfMALL link, how to contribute.

## Step 7: Announce

- [ ] Post in #announcements: new FoundUp category is live

---

## Time Estimate

| Step | Time |
|------|------|
| Create category | 1 min |
| Create 4 channels | 5 min |
| Create 2 roles | 3 min |
| GitHub webhook | 3 min |
| Update #start-here | 2 min |
| Pin welcome message | 2 min |
| Announce | 1 min |
| **Total** | **~15 min** |

---

## Current FoundUp Registry

| FoundUp | Prefix | Status | GitHub |
|---------|--------|--------|--------|
| Science Swarm Hub | swarm | Active | FOUNDUPS/science-swarm-hub |
| Geoze | geoze | Active (reorganized) | TBD |
| Move2Japan | m2j | Candidate | TBD |
| antifaFM | afm | Candidate | TBD |
| EDUIT | eduit | Candidate | TBD |
| GotJunk | gotjunk | Candidate | TBD |

---

## Data Preservation Rule

Archive, never delete. If a FoundUp becomes inactive, move its channels
to the ARCHIVE category. Do not delete them. History is preserved.
