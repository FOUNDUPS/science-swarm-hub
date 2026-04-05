# FOUNDUPS Architecture — Master Flow

> DISCOVERY → WELCOME → COMMUNITY → GATE → INTERIOR
>
> This document defines the canonical journey from discovering a FoundUp to becoming a stakeholder. Every surface (pfMALL, PWA, Discord, GitHub) serves exactly one layer. No surface crosses boundaries.
>
> **Status:** Active — v1.0
> **Canonical for:** All FoundUps under the FOUNDUPS org
> **First implementation:** Science Swarm Hub
>
> ---
>
> ## Five-Layer Flow
>
> ```
> Layer 1: DISCOVERY        pfMALL (browse, window-shop)
> Layer 2: WELCOME          FoundUp PWA (public routes)
> Layer 3: COMMUNITY        Discord + GitHub (public coordination)
> Layer 4: GATE             FoundUp PWA (wallet verification)
> Layer 5: INTERIOR         FoundUp PWA (gated routes)
> ```
>
> ### Layer 1 — Discovery (pfMALL)
>
> The pfMALL is the storefront. Users browse videos, discover FoundUps, and window-shop. No account needed.
>
> - Browse FoundUp listings with videos and descriptions
> - - Double-tap/click on mobile = entry intent
>   - - Desktop: visible "Enter FoundUp" button (required — no hidden gestures)
>     - - Entry intent navigates to the FoundUp Welcome page
>       - - No authentication, no gate, no wallet
>        
>         - The pfMALL indexer is a **classification engine**. Videos stay on their source channels (e.g., @UnDaoDu, @MOVE2JAPAN, @antifaFM). The indexer classifies content into FoundUp lanes. One source channel can feed multiple FoundUp lanes. Not every FoundUp needs its own YouTube channel.
>        
>         - Source types:
>         - - **Direct:** FoundUp owns the channel (e.g., @MOVE2JAPAN → Move2Japan)
>           - - **Derived:** Content classified from a parent channel (e.g., @UnDaoDu videos tagged as EDUIT content)
>
> **Entitlement tier:** Guest
>
> ### Layer 2 — Welcome (FoundUp PWA — Public)
>
> Each FoundUp has its own PWA shell. The public layer shows everything a newcomer needs to decide whether to participate.
>
> - Mission statement, team info, public videos
> - - Links to Discord category and GitHub repo
>   - - Contribution guide (links to CONTRIBUTING.md)
>     - - Stakeholder path explanation ("how do I get interior access?")
>       - - Sentinel agent greeting (public mode)
>        
>         - **Entitlement tier:** Visitor
>        
>         - ### Layer 3 — Community (Discord + GitHub)
>        
>         - The public coordination layer. No staking required. Anyone can participate.
>
> - **Discord:** Discussion, coordination, notifications
> -   - FOUNDUPS server with per-FoundUp categories
>     -   - Role-based organization (Member, Contributor, Core)
>         -   - GitHub webhook feeds for real-time activity
>             - - **GitHub:** Canonical action surface
>               -   - Code, issues, PRs, releases
>                   -   - All verifiable contribution happens here
>                       -   - CONTRIBUTING.md is the entry point for work
>                        
>                           - Discord is social coordination. GitHub is the work surface. Discord never gates access to anything economic.
>                        
>                           - **Entitlement tier:** Community
>                        
>                           - ### Layer 4 — Gate (Stake Verification)
>
> The boundary between public participation and economic participation. This gate lives in the FoundUp PWA, never in Discord.
>
> - Wallet connect (browser wallet or WalletConnect)
> - - Signed challenge to prove wallet ownership
>   - - Verify UPS staked (minimum threshold per FoundUp)
>     - - Verify F_i tokens held (FoundUp-specific token)
>       - - Pass → unlock Interior routes in PWA
>         - - Fail → graceful downgrade with explanation of what's needed
>           - - Sentinel agent mediates the experience
>            
>             - **Entitlement tier:** Community → Stakeholder transition
>            
>             - ### Layer 5 — Interior (Gated PWA Routes)
>            
>             - Only accessible after passing the stake gate. This is the real operating surface for economic participation.
>
> - Governance participation
> - - Work assignments and economic coordination
>   - - Revenue/reward distribution views
>     - - Stakeholder-only discussion and decisions
>       - - Advanced contribution tools
>        
>         - **Entitlement tier:** Stakeholder
>        
>         - ---
>
> ## Entitlement Tiers
>
> | Tier | Access | Determined By |
> |------|--------|---------------|
> | Guest | pfMALL browsing, public videos | No account needed |
> | Visitor | FoundUp Welcome page, public PWA | Clicking "Enter FoundUp" |
> | Community | Discord, GitHub, public coordination | Joining Discord + GitHub |
> | Stakeholder | Interior PWA, governance, economics | Wallet gate (UPS + F_i) |
> | Operator/Core | Elevated controls, admin | Manual assignment by operator |
>
> ---
>
> ## Surfaces and Their Boundaries
>
> | Surface | Layer | Owns | Never Does |
> |---------|-------|------|------------|
> | pfMALL | Discovery | Browsing, entry intent, video classification | Authentication, gating |
> | FoundUp PWA (public) | Welcome | Mission, guides, sentinel | Economic access |
> | Discord | Community | Discussion, coordination, notifications | Wallet verification, economic gating |
> | GitHub | Community | Code, issues, PRs, contribution tracking | Social coordination, gating |
> | FoundUp PWA (gated) | Gate + Interior | Wallet verify, governance, economics | Public browsing |
>
> **Key rule:** GitHub is always canonical for code, issues, and PRs. Discord is always social coordination. The PWA is the only surface that handles wallet verification and economic access.
>
> ---
>
> ## Current FoundUp Catalog
>
> ### Proven (in pfMALL)
> - **Move2Japan** — 573 videos, travel/activism (@MOVE2JAPAN YouTube, direct source)
> - - **antifaFM** — 34 videos, 24/7 resistance radio (@antifaFM YouTube, direct source)
>  
>   - ### Platform Channels (NOT FoundUps)
>   - - **UnDaoDu** — 512 videos, 012's personal brand (operator channel, source for derived lanes)
>     - - **FoundUps** — 44 videos, umbrella project channel (platform channel)
>      
>       - ### Candidate (coming soon)
>       - - **EDUIT** — autonomous learning, LinkedIn + 3 domains, no own YouTube (derived from @UnDaoDu)
>         - - **Science Swarm Hub** — physics research, GitHub repo v0.12.0, Python package
>           - - **GotJunk** — proto-ready, Cloud Run deployment
>             - - **Geoze** — qMSD narrative/game, GZE token, existing Discord channels
>              
>               - ### Staging (zero content)
>               - - **eSingularity** — AI education (LinkedIn micro-FoundUp)
>                 - - **tSingularity** — technological singularity (LinkedIn micro-FoundUp)
>                  
>                   - ---
>
> ## Sentinel Agent
>
> Each FoundUp has its own sentinel agent at the boundary between public and gated access.
>
> - Lives primarily in the FoundUp PWA
> - - Lightweight presence in Discord (can answer routing questions)
>   - - Public mode: greets visitors, explains the FoundUp, routes to resources
>     - - Gate mode: presents wallet connect, verifies stake, grants or denies
>       - - Denial is graceful: explains what's needed, links to acquisition path
>         - - Never blocks access to Community layer (Discord/GitHub)
>          
>           - ---
>
> ## Agent Contributors
>
> Human and AI contributors are both welcome at every tier.
>
> - Community tier: agents join Discord, contribute on GitHub like humans
> - - Agent introductions: name, operator, FoundUp focus
>   - - Stakeholder tier: agent staking is operator-mediated (the agent's operator holds the wallet until agent wallets are defined)
>     - - No structural role difference between human and AI in Discord
>       - - Social distinction only (introductions, not permissions)
>        
>         - ---
>
> ## Data Preservation Rule
>
> **Archive, never delete.** No channel, role, message history, or configuration is permanently destroyed. Deprecated items are archived and hidden, not deleted. This applies to Discord channels, roles, bot configurations, and all other server assets.
>
> ---
>
> ## Repeating Unit (Per FoundUp)
>
> Each FoundUp requires these components:
>
> 1. **pfMALL listing** — video, description, "Enter FoundUp" button
> 2. 2. **PWA shell** — public routes + gated routes
>    3. 3. **Discord category** — 3 text channels + 1 voice + 2 roles
>       4. 4. **GitHub repo** — under FOUNDUPS org (when applicable)
>          5. 5. **Sentinel agent** — project-specific config
>             6. 6. **Stake gate** — UPS + F_i verification
>                7. 7. **Interior routes** — gated PWA functionality
>                  
>                   8. See [FOUNDUP_TEMPLATE.md](FOUNDUP_TEMPLATE.md) for the setup checklist.
>                  
>                   9. ---
>                  
>                   10. ## Related Documents
>
> | Document | Purpose |
> |----------|---------|
> | [DISCORD_BLUEPRINT.md](DISCORD_BLUEPRINT.md) | Discord server structure, roles, channels, automation |
> | [ENTITLEMENT_TIERS.md](ENTITLEMENT_TIERS.md) | Full tier definitions and access matrix |
> | [FOUNDUP_TEMPLATE.md](FOUNDUP_TEMPLATE.md) | Repeatable pattern for adding a new FoundUp |
> | [SCIENCE_SWARM_EMBED_CHECKLIST.md](SCIENCE_SWARM_EMBED_CHECKLIST.md) | Step-by-step: Science Swarm as first FoundUp category |
