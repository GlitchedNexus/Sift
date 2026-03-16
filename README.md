# Sentinel – Predictive Portfolio Risk Agent
1. Overview
Sentinel is an automated intelligence layer designed for Sagard’s investment team. It bridges the gap between static portfolio data and the chaotic real-world news cycle. Instead of analysts manually searching for news affecting their holdings, Sentinel proactively identifies "High-Impact Events" (war logistics, policy shifts, etc.) and performs a first-pass cognitive analysis on how those events specifically threaten Sagard’s assets.

2. The Workflow
Data Ingestion: Pulls current holdings from a Central Portfolio Database (Mocked via Airtable/Google Sheets API).

Intelligence Gathering: Uses Tavily/Perplexity API to scan for domain-specific disruptions (e.g., "semiconductor neon shortages" or "maritime labor strikes").

Cognitive Analysis: A Claude 3.5 Sonnet agent performs a cross-correlation between the news and the asset's specific supply chain or regulatory exposure.

Human-in-the-Loop: Flags high-risk assets in a Lovable dashboard for a human partner to review and decide on hedging or divestment.

3. Tech Stack
Orchestration: n8n (for the logic flow and parallel processing).

LLM: Claude 3.5 Sonnet (chosen for superior reasoning on complex financial relationships).

Frontend: Lovable (for the investment team's review UI).

Connectivity: Internal Portfolio API & External News/Search APIs.

Addressing the Scaling Bottleneck: "The Signal-to-Noise Wall"
You mentioned that at 10x volume, the system might break. Here is a sophisticated way to explain that in your written submission:

What breaks first?
The Human Decision Bottleneck (Cognitive Overload).
While API rate limits are a technical hurdle, the true "systemic" failure at 10x scale is Alert Fatigue. If the portfolio grows from 50 to 500 assets, and the AI flags 30 "potential risks" daily, the human partner can no longer perform due diligence on each one. The system shifts from being a "helper" to being a "nuisance."

The Solution for 10x Scale:
To scale, we would implement a Hierarchical Agentic Filter:

Level 1 (Triage): A lightweight model (GPT-4o-mini) filters 90% of news as "irrelevant."

Level 2 (Analysis): A heavy model (Claude 3.5 Sonnet) performs deep reasoning only on the remaining 10%.

Level 3 (Ranking): The system ranks risks by Value at Risk (VaR), ensuring the human only sees the top 3 most critical threats to the fund's NAV (Net Asset Value).

Draft: Written Explanation (Max 250 Words)
What the user can now do:
Investment partners no longer have to "find the needle in the haystack." Sentinel moves the team from a reactive stance (reading news and wondering if it matters) to a proactive one. They now receive a curated "Risk Feed" where the AI has already connected the dots between a global event and a specific portfolio company’s vulnerability.

AI vs. Human Responsibility:
The AI is responsible for the cognitive heavy lifting: monitoring 24/7 global data, understanding complex industry dependencies, and generating a "Impact Hypothesis."
The AI stops at the recommendation.
The Human stays in the loop for the final investment decision. This is critical because AI lacks the "Long-Term Mandate" context—a human must decide if a short-term risk identified by the AI is an acceptable trade-off for a 5-year strategic partnership or if it violates specific Limited Partner (LP) agreements.

Scaling Failure Point:
At 10x volume, the primary failure point is Human Alert Fatigue. If the AI-to-Human ratio isn't managed, the partner will begin ignoring flags. Scaling requires a "Confidence Scoring" layer to prioritize alerts based on financial exposure, ensuring only the most existential threats reach the human desk.
