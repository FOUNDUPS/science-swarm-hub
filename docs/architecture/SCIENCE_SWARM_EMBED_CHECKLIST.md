# Science Swarm Hub -- Discord Embed Checklist

Step-by-step checklist to add Science Swarm Hub as the first FoundUp category
in the FOUNDUPS Discord server. Also covers full server restructure.

Prerequisites: FOUNDUPS_ARCHITECTURE.md and DISCORD_BLUEPRINT.md committed.

---

## Phase 1: Create New Roles

- [ ] Create @Operator role (red, hoisted, admin permissions). Assign to 012.
- [ ] Create @Core role (keep existing CORE members, rename role)
- [ ] Create @Contributor role (green, hoisted)
- [ ] Create @Stakeholder role (rename existing Du role)
- [ ] Create @Unverified role (grey, limited visibility)
- [ ] Create @swarm-contributor role (blue)
- [ ] Create @swarm-notify role (light blue, self-assignable)
- [ ] Create @geoze-contributor role
- [ ] Create @geoze-notify role

## Phase 2: Map Existing Members to New Roles

- [ ] All existing Du members -> @Stakeholder (rename the role)
- [ ] Dao + Un members -> also get @Contributor
- [ ] CORE members -> @Core (rename the role)
- [ ] 0102 -> @Operator (rename the role)
- [ ] Verified members -> ensure they have @Stakeholder

## Phase 3: Create New Categories and Channels

### FOUNDUPS category
- [ ] Create category: FOUNDUPS
- [ ] Create #rules (text, read-only)
- [ ] Create #start-here (text, reactions enabled)
- [ ] Create #announcements (text, read-only)
- [ ] Create #introductions (text)

### COMMONS category
- [ ] Create category: COMMONS
- [ ] Move and rename #chat -> #general
- [ ] Create #off-topic (text)
- [ ] Move and rename VC Foundups -> voice

### OPERATOR category
- [ ] Create category: OPERATOR
- [ ] Create #operator-log (text, read-only, public)
- [ ] Create #bot-feeds (text, read-only, public)
- [ ] Create #mod-room (text, private to Operator only)

### SCIENCE SWARM HUB category
- [ ] Create category: SCIENCE SWARM HUB
- [ ] Create #swarm-general (text)
- [ ] Create #swarm-github (text, read-only)
- [ ] Create #swarm-work (text)
- [ ] Create swarm-voice (voice)

### GEOZE category
- [ ] Create category: GEOZE
- [ ] Move geoze-mud forum to GEOZE category
- [ ] Move and rename #gmud-docs -> #geoze-docs
- [ ] Move and rename #gmud_moshpit -> #geoze-work
- [ ] Create geoze-voice (voice)

## Phase 4: Archive Old Channels

- [ ] Create category: ARCHIVE (Operator-only visibility)
- [ ] Move to ARCHIVE: waiting-room, verify, js, Talks
- [ ] Move to ARCHIVE: memecoin_madness, trump_dump
- [ ] Move to ARCHIVE: antifafm-music, VC MOVE2JAPAN
- [ ] Move to ARCHIVE: Sleeping, DAWGS comms, Trumps SCIF
- [ ] Move to ARCHIVE: moshpit, discord-roadmap, bots-dev
- [ ] Move to ARCHIVE: whitepaper, landing-page, discord-dev
- [ ] Move to ARCHIVE: sale-marketing-crowdfunding, tempo-bot-commands, infoi
- [ ] Remove old category labels after channels moved out

## Phase 5: Archive Old Roles

- [ ] Archive Dao, Un roles (after members mapped to @Contributor)
- [ ] Archive EDUIT NPO, EDUIT Partners, Discord Dawg, Beneficial AI
- [ ] Archive Verified (after members confirmed in @Stakeholder)
- [ ] Archive Waiting Room, Pandez Guard, Purge, Tickets

## Phase 6: Bot Cleanup

- [ ] Ensure YAGPDB.xyz is installed and configured
- [ ] Remove: Dyno, MEE6, Midjourney Bot, Patreon, OBAI
- [ ] Remove: IFTTT, Streamcord, TikTok, Tempo
- [ ] Archive bot-specific roles after bot removal

## Phase 7: Configure YAGPDB

- [ ] Reaction role: checkmark in #start-here -> @Stakeholder (remove @Unverified)
- [ ] Reaction role: Science Swarm emoji -> @swarm-notify
- [ ] Reaction role: Geoze emoji -> @geoze-notify
- [ ] Configure automod: spam, link filter, raid protection
- [ ] Configure mod logging to #mod-room
- [ ] Set up welcome message on join

## Phase 8: GitHub Webhook

- [ ] Go to github.com/FOUNDUPS/science-swarm-hub/settings/hooks
- [ ] Add webhook: Discord webhook URL for #swarm-github
- [ ] Events: Issues, Pull requests, Releases, Issue comments
- [ ] Test: create test issue, verify it appears in #swarm-github

## Phase 9: Pinned Messages

- [ ] Pin #rules: server rules, five-layer flow, code of conduct
- [ ] Pin #start-here: onboarding, reaction roles, FoundUp directory with pfMALL + GitHub links
- [ ] Pin #swarm-general: project overview, GitHub link, how to contribute
- [ ] Pin #operator-log: what this channel is and why its public

## Phase 10: Set Permissions

- [ ] @everyone / @Unverified: see only #rules, #start-here, #announcements
- [ ] @Stakeholder: see and post in all public channels
- [ ] ARCHIVE category: Operator-only visibility
- [ ] #mod-room: Operator-only
- [ ] Read-only channels: send messages disabled except Operator/webhooks

## Phase 11: Verify

- [ ] Test onboarding flow with alt account
- [ ] Confirm GitHub webhook works
- [ ] Confirm ARCHIVE is hidden from members
- [ ] Post restructure announcement in #announcements

---

Done. Science Swarm Hub is live as first FoundUp category.
Next FoundUp follows FOUNDUP_TEMPLATE.md.
