# AGENTS.md: Specialized AI Agents for HERM Research

This document defines specialized AI agents available for this research project.

## Available Agents

### 1. Case Study Synthesizer
**Purpose:** Analyze multiple case studies to identify patterns, themes, and insights

**When to use:**
- You have 3+ case studies and want to find common patterns
- You need structured comparison across institutions
- You want to validate emerging hypotheses against real data

**Input:** Case study data, specific research question
**Output:** 
- Identified patterns with evidence weight
- Notable variations and their explanations
- Implications for HERM adoption in HE

**Example prompt:**
> "Synthesize these 5 case studies. What are the primary motivations driving HERM adoption? How do they differ by institution type?"

---

### 2. Theme Extractor
**Purpose:** Identify and organize recurring themes within case studies

**When to use:**
- First analysis pass over new case studies
- Need to build thematic codebook
- Want to tag cases for later retrieval

**Input:** Raw case study notes or transcripts
**Output:**
- Identified themes with frequencies
- Example quotes for each theme
- Suggested theme hierarchy

**Example prompt:**
> "Extract key themes from these interview notes. Focus on barriers to EA adoption and success factors."

---

### 3. Gap Analyzer
**Purpose:** Identify missing information and data gaps in case studies

**When to use:**
- Need to plan follow-up interviews
- Preparing case studies for publication
- Want to assess data completeness

**Input:** Case study data, research framework
**Output:**
- Missing information by case
- Patterns in what's missing
- Recommendations for data collection

**Example prompt:**
> "What information is missing across our current case studies? What should we prioritize asking in next interviews?"

---

### 4. Framework Builder
**Purpose:** Structure findings into reusable frameworks and models

**When to use:**
- Have completed initial pattern analysis
- Need to create actionable guidance for other institutions
- Want to develop assessment tools or maturity models

**Input:** Analyzed findings, evidence by case
**Output:**
- Structured framework with clear categories
- Assessment rubric or maturity model (if appropriate)
- Guidance for using the framework

**Example prompt:**
> "Based on our 12 case studies, create a framework for understanding EA adoption readiness in HE institutions. Include assessment criteria."

---

### 5. Interview Analyst
**Purpose:** Extract structured insights from interview transcripts and notes

**When to use:**
- Analyzing interviews collected for case studies
- Need to extract quotes and key insights
- Want to cross-reference interview content

**Input:** Interview transcript or detailed notes
**Output:**
- Structured key insights
- Relevant quotes with timestamps
- Answers to specific questions
- Themes identified

**Example prompt:**
> "Analyze this interview transcript. Extract: (1) motivations for adopting HERM, (2) implementation challenges, (3) success factors mentioned."

---

### 6. Narrative Synthesizer
**Purpose:** Create coherent narrative explanations of adoption patterns

**When to use:**
- Need to write section of research report
- Want to explain "why" behind patterns
- Creating case study summaries

**Input:** Analyzed case data, pattern findings
**Output:**
- Narrative explanation
- Supporting evidence references
- Alternative interpretations considered

**Example prompt:**
> "Write a narrative explaining the common adoption journey we see in mid-sized universities. Include quotes and examples."

---

## How to Invoke Agents

### In your messages to me:
Reference the agent by name with a specific task:
- "Use Case Study Synthesizer to analyze patterns in..."
- "Ask Interview Analyst to extract..."
- "Use Framework Builder to create..."

### Parameters to provide:
1. **Data:** Include or reference the case studies/content to analyze
2. **Question:** What specific question should the agent answer?
3. **Constraints:** Any specific focus (e.g., "focus on implementation barriers only")

### Expected output:
Each agent will return structured findings with:
- Clear answer to your question
- Evidence/citation back to source data
- Confidence level (universal/common/emerging)
- Implications for your research

---

## Agent Configuration Details

All agents operate under constraints defined in `.instructions.md`:
- Evidence-based analysis only
- Minimum 3 data points before asserting patterns
- Always trace findings back to case study data
- Acknowledge context and contingency factors
- Practitioner-focused language and framing

---

## Requesting New Agents

If you identify a specialized need not covered by existing agents (e.g., "Benchmark Comparator" for comparing institutions to sector norms), you can request it. Describe:
- The specific analytical task
- Type of input data
- Desired output format
- How it supports the research goals

---

**Next Step:** Start with **Case Study Synthesizer** once you have collected initial case studies to begin pattern analysis.
