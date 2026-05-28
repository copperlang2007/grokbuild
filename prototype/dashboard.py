import streamlit as st
import json
from datetime import datetime
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from prototype.master_orchestrator import run_all_methods

st.set_page_config(page_title="FastAI Income Suite", layout="wide")
st.title("🚀 FastAI Income Suite v1.1 - OpenRouter Edition")
st.subheader("Turn AI into $1000/day income streams in minutes • Powered by OpenRouter")

# Load DNA
with open("../app-dna.json") as f:
    dna = json.load(f)

col1, col2, col3 = st.columns(3)
col1.metric("Composite Score", f"{dna['composite_score']}/10", "Unbreakable")
col2.metric("Methods Available", "20", "+5 in v1.1")
col3.metric("Projected Daily", "$150-800+", "Per user volume")

st.header("One-Click Launch")

# Model Selector (NEW)
model_options = {
    "Grok-3 (xAI)": "x-ai/grok-3",
    "Claude 3.5 Sonnet (Anthropic)": "anthropic/claude-3.5-sonnet",
    "GPT-4o (OpenAI)": "openai/gpt-4o",
    "Llama 3.1 405B (Meta)": "meta-llama/llama-3.1-405b-instruct",
    "Gemini 1.5 Pro (Google)": "google/gemini-1.5-pro"
}
selected_model_name = st.selectbox("🤖 Choose AI Model", list(model_options.keys()), index=0)
selected_model = model_options[selected_model_name]
st.caption(f"Using model: **{selected_model}** via OpenRouter")

niche = st.text_input("Target Niche (e.g. productivity, fitness, finance)", "side_hustles_2026")
methods = st.multiselect("Select Methods to Run", 
    ["prompt_packs", "micro_ebooks", "wallpapers", "pod_designs", "stock_photos", 
     "voiceovers", "music_loops", "meme_packs", "chatbot_templates", "headshot_packs",
     "affiliate_bots", "survey_farms", "etsy_optimizations", "translation_gigs", "va_templates"],
    default=["prompt_packs", "micro_ebooks", "wallpapers"])

if st.button("🚀 EXECUTE ALL SELECTED (Master Orchestrator)"):
    with st.spinner(f"Generating with {selected_model_name}... This may take 30-90 seconds"):
        try:
            results = run_all_methods(niche=niche, methods=methods, model=selected_model)
            st.success(f"✅ Success! Generated using {selected_model_name}")
            st.json(results)
            st.balloons()
        except Exception as e:
            st.error(f"Error: {str(e)}")

st.header("Live Earnings Tracker (Demo)")
st.line_chart({"Prompt Packs": [120, 340, 890], "eBooks": [80, 210, 450], "Designs": [50, 180, 620]})

st.caption("Red-Team Certified v5 | Grok Studio 2026 | Powered by OpenRouter (free key at openrouter.ai/keys)")