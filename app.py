
import streamlit as st
import random

st.set_page_config(page_title="Product Case Prep Buddy (Offline)", page_icon="🧠")

st.title("🧠 Product Case Prep Buddy (Offline Demo)")
st.write("Practice product management cases and view sample answers.")

case_type = st.sidebar.selectbox("Select Case Type", [
    "Design a New Feature",
    "Improve a Metric",
    "Evaluate a Product",
    "Prioritize Roadmap",
    "Launch Strategy"
])

hint_mode = st.sidebar.checkbox("Hint Mode")

example_prompts = {
    "Design a New Feature": "Design a new feature for Airbnb to help solo travelers.",
    "Improve a Metric": "Instagram engagement is down 20% among Gen Z. What would you do?",
    "Evaluate a Product": "Evaluate the success of Google Pixel phones.",
    "Prioritize Roadmap": "You're a PM at Spotify. How do you prioritize lyrics, AI DJ, and social listening?",
    "Launch Strategy": "How would you launch a new grocery delivery app in a mid-sized U.S. city?"
}

sample_responses = {'Design a New Feature': ["Add 'Solo Adventures' mode: curated stays and activities for solo travelers. Helps Airbnb differentiate while building community.", 'Feature: Match with local guides. Safety ratings, shared itineraries. Increases user confidence and engagement.', "Create 'Solo Badge' listings that highlight highly reviewed solo traveler hosts. Encourages trust and ease of planning.", 'SoloConnect: a feature to find other solo travelers nearby and sync plans. Builds trust and serendipitous community.', "Enable 'SafeCheck': location-based check-ins with emergency contact alerts. Boosts safety for solo guests.", 'Solo journey journals: travelers can write, share and connect through personal stories tied to destinations.', 'In-app concierge for solo travelers, prioritizing safety-rated listings and nearby low-key social events.', 'AI-curated solo trips with accommodation, events, and tips bundled for specific cities.', "Solo 'host meetups' – Airbnb hosts organize meet-and-greets to help solo guests feel welcome.", 'Collaborate with local cafes to create solo hangouts tagged in Airbnb maps with verified reviews.'], 'Improve a Metric': ['Conduct funnel analysis, segment Gen Z by behavior, and test Stories-like features. Optimize onboarding and retention.', 'Launch a streak-based engagement challenge with daily check-ins and content prompts. Gamifies return usage.', 'Reduce friction in the share feature. Peer invites and social integrations boost viral loops among Gen Z.', 'Introduce ephemeral content: Gen Z responds to time-sensitive interactions (e.g. questions of the day).', 'Gamify comments and likes with custom emojis or rewards that expire. Increases frequency of engagement.', 'Incentivize micro-posts and reactions. Short-form content is native to Gen Z behavior.', 'Add music/video mashup remix features with limited-time challenges. Builds creation habits.', 'Offer custom themes, avatars, or rewards based on daily activity streaks.', 'Highlight mutual connections in feed, increase FOMO-based reactivation nudges.', 'Deploy push notifications based on friend activity or event reminders tied to behavior clusters.'], 'Evaluate a Product': ['Pixel phones have niche appeal: strong camera, clean Android. Struggles with brand recognition vs. iPhone/Samsung.', 'Evaluate by retention, sales CAGR, user satisfaction. Pixel excels in tech crowd but lacks mass market reach.', 'Success in innovation, but unclear commercial dominance. Examine product-market fit outside U.S. and price tiers.', 'Look at Net Promoter Score and channel share. Pixel lags behind in telco distribution globally.', 'Focus on product-led metrics: satisfaction with camera, OS experience, and Google integration.', 'Pixel’s updates and security appeal to developers and privacy-focused users, but lacks retail visibility.', 'Evaluate cannibalization with other Android OEMs, especially Samsung and OnePlus.', 'Google’s hardware strategy is unclear—evaluate how Pixel ties into broader ecosystem monetization.', 'Check supply chain reliability and post-sale service coverage as part of product viability.', 'Assess differentiation from competitors: AI features, photo editing, and pricing tiers.'], 'Prioritize Roadmap': ['Prioritize AI DJ: high novelty, ties to engagement. Lyrics is expected, social listening adds complexity.', 'Use RICE scoring: AI DJ (Reach: High, Impact: High), Lyrics (Effort: Low), Social (Effort: High, Confidence: Low).', 'Focus on one big bet (AI DJ), maintain user trust with lyrics, and prototype social for feedback—not launch.', 'Social listening might cannibalize current usage. Test with power users before full rollout.', "AI DJ is high reward and ties to Spotify's long-term personalization strategy—fast-track it.", 'Lyrics is hygiene—delight factor is low but expectation is high. Ship it ASAP.', 'Conduct A/B tests with short-form social listening. Measure impact on session length.', "Layer usage data and voice-of-customer to score features. Don't rely on internal excitement.", 'Build fast, fail fast with social listening via limited market test, learn quickly.', 'Map each feature to company OKRs—AI DJ likely drives strategic growth metrics best.'], 'Launch Strategy': ['Target mid-size cities with dense urban zones (e.g., Raleigh, Madison). Launch with promos, partner with local grocers.', 'MVP with limited SKU set. Fast delivery in <30 mins. Focus on convenience and price transparency.', 'Use referral discounts + student ambassadors. Expand based on DAU and repeat purchase thresholds.', 'Test in college towns: high density, tech adoption, and delivery use cases are proven.', 'Launch with micro-warehouses and partner with local corner stores for inventory.', 'Target new parents and working professionals as initial ICPs (high willingness to pay).', 'Use local influencers and community groups for trusted word-of-mouth campaigns.', 'Deploy aggressive CAC-lowering tactics: bundling, free delivery threshold, and loyalty rewards.', 'Pilot in weather-affected cities where grocery runs are a pain point (e.g., Chicago, Seattle).', 'Partner with meal kit providers or restaurants for co-branded bundles to grow AOV.']}

st.subheader("📌 Case Prompt")
st.write(f"**Prompt:** {example_prompts[case_type]}")

user_response = st.text_area("Your Answer", height=250)

if st.button("Submit Answer"):
    st.subheader("💡 Sample Feedback")
    st.markdown(random.choice(sample_responses[case_type]))

st.markdown("---")
st.markdown("_Tip: In a live version, this would analyze your response and provide rubric-based AI feedback._")
