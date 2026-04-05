# FOUNDUPS Discord Blueprint

This document specifies the complete Discord server structure for FOUNDUPS.
Discord is **Layer 3 (Community)** in the FOUNDUPS architecture.

See [FOUNDUPS_ARCHITECTURE.md](FOUNDUPS_ARCHITECTURE.md) for the full five-layer flow.

**Server name:** FOUNDUPS
**Server owner:** UnDaoDu (username: foundups)
**Operator:** 012 (sole operator)
**Members:** 337 (as of April 2026 audit)
**Established:** February 2018

---

## Design Principles

1. GitHub is canonical for code, issues, and PRs
2. Discord is social coordination, never the economic gate
3. Archive, never delete -- all deprecated items are hidden, not destroyed
4. Each FoundUp gets its own category with a repeating 4-channel pattern
5. Minimum viable channels -- add when demand proves the need
6. Human and AI contributors use the same structure

---

## Server Layout

### FOUNDUPS (server-wide)

| Channel | Type | Purpose |
|---------|------|---------|
| #rules | text, read-only | Server rules, code of conduct |
| #start-here | text | Onboarding, reaction roles, FoundUp directory |
| #announcements | text, read-only | Server-wide updates |
| #introductions | text | New members say hello |

### COMMONS

| Channel | Type | Purpose |
|---------|------|---------|
| #general | text | Open discussion |
| #off-topic | text | Everything else |
| voice | voice | One general voice channel |

### OPERATOR

| Channel | Type | Purpose |
|---------|------|---------|
| #operator-log | text, read-only | Operator decisions, transparency |
| #bot-feeds | text, read-only | Consolidated bot/webhook noise |
| #mod-room | text, private | Bot commands, moderation |

### SCIENCE SWARM HUB (first FoundUp)

| Channel | Type | Purpose |
|---------|------|---------|
| #swarm-general | text | Project discussion |
| #swarm-github | text, read-only | Webhook feed from GitHub |
| #swarm-work | text | What are you working on |
| swarm-voice | voice | Project voice |

### GEOZE (existing FoundUp, reorganized)

| Channel | Type | Purpose |
|---------|------|---------|
| geoze-mud | forum | qMSD narrative forum |
| #geoze-docs | text | Renamed from #gmud-docs |
| #geoze-work | text | Renamed from #gmud_moshpit |
| geoze-voice | voice | New |

### ARCHIVE (hidden)

All deprecated channels move here. Operator-only visibility. History preserved.

---

## Role Hierarchy

| Role | Purpose | Assignment |
|------|---------|------------|
| @Operator | Full admin (012) | Manual |
| @Core | Trusted long-term contributors | Manual by Operator |
| @Contributor | Active on any FoundUp | Manual by Operator |
| @Stakeholder | Verified, onboarded | YAGPDB reaction role |
| @Unverified | Just joined, limited view | Default on join |
| @swarm-contributor | Active on Science Swarm | Manual |
| @swarm-notify | Opt-in Science Swarm pings | Self-assign |
| @geoze-contributor | Active on Geoze | Manual |
| @geoze-notify | Opt-in Geoze pings | Self-assign |

---

## Migration Maps

See FOUNDUPS_ARCHITECTURE.md for the complete channel and role migration tables.

KEEP: welcome->rules, chat->general, geoze-mud, gmud-docs->geoze-docs, gmud_moshpit->geoze-work, VC Foundups->voice, AFK

ARCHIVE: All other existing channels (20 channels) move to hidden ARCHIVE category.

CREATE: 13 new channels across FOUNDUPS, COMMONS, OPERATOR, SCIENCE SWARM HUB, and GEOZE categories.

---

## Automation

Single bot: YAGPDB.xyz (verification, reaction roles, automod, logging).
GitHub webhooks: native Discord webhooks per FoundUp repo.
Remove: Dyno, MEE6, Midjourney Bot, Patreon, OBAI, IFTTT, Streamcord, TikTok, Tempo.

---

## Execution Checklist

See [SCIENCE_SWARM_EMBED_CHECKLIST.md](SCIENCE_SWARM_EMBED_CHECKLIST.md).
