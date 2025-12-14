import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Financial Advisory Chatbot Presentation",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #1f77b4;
        padding: 20px;
        font-size: 48px;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 24px;
        margin-bottom: 30px;
    }
    .authors {
        text-align: center;
        color: #888;
        font-size: 18px;
        margin: 20px 0;
    }
    .section-title {
        color: #1f77b4;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 10px;
    }
    .subsection-title {
        color: #2c3e50;
        font-size: 28px;
        font-weight: bold;
        margin: 20px 0;
    }
    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .metric-number {
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .metric-label {
        font-size: 16px;
        opacity: 0.9;
    }
    .feature-box {
        background: #f8f9fa;
        padding: 25px;
        border-radius: 10px;
        margin: 15px 0;
        border-left: 5px solid #1f77b4;
    }
    .feature-icon {
        font-size: 48px;
        margin-bottom: 15px;
    }
    .feature-title {
        font-size: 20px;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 10px;
    }
    .feature-desc {
        color: #666;
        line-height: 1.6;
    }
    .flow-box {
        background: #e3f2fd;
        padding: 15px 30px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        color: #1976d2;
        margin: 10px 0;
        font-size: 18px;
    }
    .flow-arrow {
        text-align: center;
        font-size: 32px;
        color: #1976d2;
        margin: 10px 0;
    }
    .tech-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin: 15px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .tech-icon {
        font-size: 64px;
        margin-bottom: 15px;
    }
    .tech-name {
        font-size: 22px;
        font-weight: bold;
    }
    .comparison-table {
        margin: 20px 0;
    }
    .slide-content {
        padding: 20px;
        min-height: 500px;
    }
    .navigation-info {
        text-align: center;
        padding: 10px;
        background: #f8f9fa;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
        color: #495057;
    }
    .step-box {
        padding: 15px;
        margin: 10px 0;
        border-radius: 8px;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'slide_number' not in st.session_state:
    st.session_state.slide_number = 0

# Total slides
TOTAL_SLIDES = 13

# Navigation functions
def next_slide():
    if st.session_state.slide_number < TOTAL_SLIDES - 1:
        st.session_state.slide_number += 1

def prev_slide():
    if st.session_state.slide_number > 0:
        st.session_state.slide_number -= 1

def go_to_slide(n):
    st.session_state.slide_number = n

# Slide content functions
def slide_1():
    st.markdown('<div class="slide-content">', unsafe_allow_html=True)
    st.markdown("""
        <div class="main-title">
            🤖 Differentially Private GenAI Chatbot<br>for Financial Advisory
        </div>
        <div class="authors">
            Vamsi Krishna (se22uari039) • Bhuvan (se22uari212)<br>
            Chaitanya (se22uari047) • Siddharth (se22uari160)
        </div>
        <div class="authors">
            Mentor: Ravi Babu
        </div>
        <div class="subtitle">
            📚 Mahindra Ecole Centrale College of Engineering, Hyderabad
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def slide_2():
    st.markdown('<div class="slide-content">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Problem Statement</div>', unsafe_allow_html=True)
    st.markdown('<div class="subsection-title">Why Traditional Chatbots Fail?</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="feature-box">
            • 🚫 Rule-based systems (Dialogflow, Rasa) don't scale for complex domains<br>
            • 📚 Cannot dynamically access or update real-world knowledge<br>
            • 🔄 Struggle with paraphrased queries and unseen intents<br>
            • ❓ No explainability - users get template responses without sources<br>
            • 📈 Financial domain requires current data - markets change daily
        </div>
    """, unsafe_allow_html=True)
    
    st.error("**Challenge:** Build a chatbot that combines AI knowledge with real-time web data, handles 3+ financial domains, and provides verifiable, accurate responses.")
    st.markdown('</div>', unsafe_allow_html=True)

def slide_3():
    st.markdown('<div class="slide-content">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Our Solution</div>', unsafe_allow_html=True)
    st.markdown('<div class="subsection-title">Two-Phase Hybrid Architecture</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="feature-box">
                <div class="feature-title">Phase 1: RAG System</div>
                <div class="feature-desc">
                    • 3+ FAISS vector databases<br>
                    • Intent-based routing<br>
                    • LangChain orchestration<br>
                    • Dual LLM/SLM architecture<br>
                    • Sentence-BERT embeddings
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="feature-box">
                <div class="feature-title">Phase 2: Web Intelligence</div>
                <div class="feature-desc">
                    • Confidence-based triggering<br>
                    • Serper AI web search<br>
                    • Firecrawl content scraping<br>
                    • Context-augmented responses<br>
                    • Source citation & verification
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    st.success("**Result:** 🧠 AI Knowledge + 🌐 Real-time Web Data = Accurate & Current Responses")
    st.markdown('</div>', unsafe_allow_html=True)

def slide_4():
    st.markdown('<div class="slide-content">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Phase 1: RAG Architecture</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="flow-box">User Query</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-arrow">↓</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-box">Intent Classification (3 modes)</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-arrow">↓</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="flow-box">Hardcoded</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="flow-box">Classifier</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="flow-box">All-DB</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="flow-arrow">↓</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-box">FAISS Vector Search (3+ domains)</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-arrow">↓</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-box">RAG Context Assembly</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-arrow">↓</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="flow-box">Gemma 7b (SLM)</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="flow-box">Llama 33b (LLM)</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="flow-arrow">↓</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-box">Response with Sources</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def slide_5():
    st.markdown('<div class="slide-content">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Phase 2: Web Intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="subsection-title">Confidence-Based Decision Flow</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="flow-box">User Query</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-arrow">↓</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-box">LLM Confidence Check</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-arrow">↓</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="flow-box" style="background: #c8e6c9;">HIGH Confidence<br>Use LLM Knowledge</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="flow-box" style="background: #ffccbc;">LOW Confidence<br>Trigger Web Search</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="flow-arrow">↓ (if LOW)</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-box">Serper AI Web Search</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-arrow">↓</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-box">Firecrawl Content Scraping</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-arrow">↓</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-box">Context-Augmented LLM Response</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-arrow">↓</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow-box">Response + Source Citations</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def slide_6():
    st.markdown('<div class="slide-content">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Key Innovations</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="feature-box">
                <div class="feature-icon">🧠</div>
                <div class="feature-title">Unified Memory</div>
                <div class="feature-desc">
                    Single conversation history shared across SLM/LLM for seamless context flow
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="feature-box">
                <div class="feature-icon">🔍</div>
                <div class="feature-title">Confidence Mechanism</div>
                <div class="feature-desc">
                    Self-assessment triggers web search only when needed
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="feature-box">
                <div class="feature-icon">🎯</div>
                <div class="feature-title">Smart Routing</div>
                <div class="feature-desc">
                    Automatic model selection based on query complexity and cost optimization
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="feature-box">
                <div class="feature-icon">📚</div>
                <div class="feature-title">Source Attribution</div>
                <div class="feature-desc">
                    Every response includes verifiable citations for transparency
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def slide_7():
    st.markdown('<div class="slide-content">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Technology Stack</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="tech-box">
                <div class="tech-icon">🤖</div>
                <div class="tech-name">Llama 33b<br>Gemma 7b</div>
                <div>via Groq API</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="tech-box">
                <div class="tech-icon">📊</div>
                <div class="tech-name">FAISS</div>
                <div>Vector Search</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="tech-box">
                <div class="tech-icon">🔗</div>
                <div class="tech-name">LangChain</div>
                <div>Orchestration</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="tech-box">
                <div class="tech-icon">🧬</div>
                <div class="tech-name">Sentence-BERT</div>
                <div>Embeddings</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="tech-box">
                <div class="tech-icon">🔍</div>
                <div class="tech-name">Serper AI</div>
                <div>Web Search</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="tech-box">
                <div class="tech-icon">🕷️</div>
                <div class="tech-name">Firecrawl</div>
                <div>Content Scraping</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def slide_8():
    st.markdown('<div class="slide-content">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Experimental Results</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    metrics = [
        ("92%", "Phase 1 RAG Accuracy"),
        ("96%", "Phase 2 Web-Enhanced Accuracy"),
        ("89%", "Confidence Mechanism Precision"),
        ("40%", "Response Time Reduction"),
        ("4.6/5", "User Rating - Accuracy"),
        ("4.7/5", "User Rating - Clarity"),
        ("3x", "Faster Knowledge Updates"),
        ("67%", "Reduction in Hallucination")
    ]
    
    for i, (number, label) in enumerate(metrics):
        col = col1 if i % 2 == 0 else col2
        with col:
            st.markdown(f"""
                <div class="metric-box">
                    <div class="metric-number">{number}</div>
                    <div class="metric-label">{label}</div>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def slide_9():
    st.markdown('<div class="slide-content">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Why Our Approach Wins</div>', unsafe_allow_html=True)
    
    comparison_data = {
        "Feature": ["Scalability", "Current Information", "Explainability", "Hallucination", "Knowledge Updates"],
        "Rule-based (Dialogflow)": ["❌ Poor", "❌ No", "❌ Templates", "✅ None", "❌ Hours"],
        "Pure LLM": ["⚠️ Moderate", "❌ No", "⚠️ Limited", "❌ High Risk", "❌ Retraining"],
        "Our System": ["✅ Excellent", "✅ Yes (Web)", "✅ Full Citations", "✅ 67% Reduction", "✅ Minutes"]
    }
    
    import pandas as pd
    df = pd.DataFrame(comparison_data)
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

def slide_10():
    st.markdown('<div class="slide-content">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">System Workflow Example</div>', unsafe_allow_html=True)
    st.markdown('<div class="subsection-title">Query: "What are the latest Fed rate decisions?"</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="step-box" style="background: #e3f2fd;">', unsafe_allow_html=True)
    st.info("**Step 1:** LLM analyzes query → Detects 'latest' → **LOW confidence**")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="step-box" style="background: #fff3e0;">', unsafe_allow_html=True)
    st.warning("**Step 2:** Triggers Serper AI web search → Finds recent Federal Reserve announcements")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="step-box" style="background: #ffebee;">', unsafe_allow_html=True)
    st.error("**Step 3:** Firecrawl scrapes top 2 articles → Extracts key rate decision details")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="step-box" style="background: #e8f5e9;">', unsafe_allow_html=True)
    st.success("**Step 4:** Llama 33b synthesizes web content + training knowledge → Generates comprehensive answer")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="step-box" style="background: #e3f2fd;">', unsafe_allow_html=True)
    st.info("**Step 5:** Returns response with source citations (Fed website, Bloomberg, Reuters)")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def slide_11():
    st.markdown('<div class="slide-content">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Challenges & Solutions</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🚧 Challenges")
        st.markdown("""
        - Managing context across model switches
        - Balancing cost vs performance
        - Handling scraping failures
        - Calibrating confidence threshold
        - Avoiding information overload
        """)
    
    with col2:
        st.markdown("### ✅ Solutions")
        st.markdown("""
        - Unified LangChain memory buffer
        - Smart SLM/LLM routing
        - BeautifulSoup fallback scraper
        - 89% precision through testing
        - 3000-char content limit per source
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)

def slide_12():
    st.markdown('<div class="slide-content">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Future Enhancements</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### 🔐 Differential Privacy
    Implement privacy-preserving mechanisms for sensitive financial data
    
    ### 🌍 Multi-language Support
    Expand to regional languages for broader accessibility
    
    ### 🎯 RLHF Integration
    Reinforcement learning from human feedback to improve response quality
    
    ### 🎤 Voice Interface
    Add speech-to-text for hands-free financial advisory
    
    ### 👤 Personalization
    User profile-based recommendations and portfolio tracking
    
    ### ⚖️ Regulatory Compliance
    Automated compliance checking for financial advice
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

def slide_13():
    st.markdown('<div class="slide-content">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Conclusion</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="feature-box">
            <div class="feature-title">Key Achievements</div>
            <div class="feature-desc">
                ✅ Hybrid RAG + Web Search architecture<br>
                ✅ 96% accuracy with web-enhanced responses<br>
                ✅ 40% faster responses with smart routing<br>
                ✅ 67% reduction in hallucination<br>
                ✅ Full explainability with source citations
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.success("""
    **Impact:** Setting new standards for AI-powered financial advisory systems through 
    modular architecture, real-time information integration, and verifiable responses.
    """)
    
    st.markdown("""
        <div class="main-title" style="margin-top: 50px;">
            Thank You! 🙏
        </div>
        <div class="subtitle">
            Questions & Discussion
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Slide mapping
slides = {
    0: slide_1,
    1: slide_2,
    2: slide_3,
    3: slide_4,
    4: slide_5,
    5: slide_6,
    6: slide_7,
    7: slide_8,
    8: slide_9,
    9: slide_10,
    10: slide_11,
    11: slide_12,
    12: slide_13
}

# Display current slide
slides[st.session_state.slide_number]()

# Navigation controls
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Previous", disabled=st.session_state.slide_number == 0, use_container_width=True):
        prev_slide()
        st.rerun()

with col2:
    st.markdown(f"""
        <div class="navigation-info">
            Slide {st.session_state.slide_number + 1} / {TOTAL_SLIDES}
        </div>
    """, unsafe_allow_html=True)

with col3:
    if st.button("Next ➡️", disabled=st.session_state.slide_number == TOTAL_SLIDES - 1, use_container_width=True):
        next_slide()
        st.rerun()

# Sidebar with slide navigator
with st.sidebar:
    st.markdown("### 📑 Slide Navigator")
    
    slide_titles = [
        "Title",
        "Problem Statement",
        "Solution Overview",
        "Phase 1 Architecture",
        "Phase 2 Architecture",
        "Key Innovations",
        "Technology Stack",
        "Results",
        "Comparison",
        "Workflow Example",
        "Challenges & Solutions",
        "Future Work",
        "Conclusion"
    ]
    
    for i, title in enumerate(slide_titles):
        if st.button(f"{i+1}. {title}", key=f"nav_{i}", use_container_width=True):
            go_to_slide(i)
            st.rerun()
    
    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.info("""
    - Use Previous/Next buttons
    - Click slide titles in sidebar
    - Press F11 for fullscreen
    """)
