# EA and HERM Adoption Survey of Higher Education in Europe — Blueprint

**Status:** Revised Draft  
**Audience:** EA practitioners and related decision-makers at higher education institutions  
**Distribution:** EUNIS and national organizations via member channels
**Last updated:** 2026-09-01

---

## 1. Study Goals

1. Describe the use of Enterprise Architecture (EA) and HERM among participating higher education institutions.
2. Identify which EA frameworks, reference models, modelling languages, and in-house approaches are used.
3. Understand how HERM is used, including artifacts, application areas, adoption stage, and organizational embedding.
4. Identify barriers and enabling conditions for HERM adoption.
5. Identify concrete HERM use cases that may be suitable for community sharing or follow-up case studies.
6. Capture open questions and support needs related to EA and HERM.

---

## 2. Unit of Analysis and Response Perspective

The primary unit of analysis is the **institution**.

Respondents answer on behalf of their institution to the best of their knowledge. Where institutional knowledge cannot reasonably be assumed, a **Don't know / Cannot assess** option is provided.

Respondent-level variables such as role and familiarity with HERM are treated separately from institution-level variables.

If multiple responses are received from the same institution, they must be identifiable where possible and handled during data cleaning and analysis.

---

## 3. Question Flow

```text
Section 1: Respondent & Institution Profile        everyone
Section 2: EA Practice                             everyone
Section 3: HERM Awareness & Adoption               everyone

If HERM status = Evaluating / Pilot / Active / Embedded
    -> Section 4: HERM Usage Details
Else
    -> Section 5: HERM Non-Adoption & Barriers

Section 6: Open Questions & Support Needs          everyone
Section 7: Knowledge Sharing & Follow-up           everyone, partly conditional
Section 8: Naming & Contact Consent                conditional
```

---

# Section 1: Respondent & Institution Profile

## 1.1 Institution name

**Type:** Text, optional

> Institution name

Optional. If you prefer not to identify your institution, leave this field blank.

---

## 1.2 Country

**Type:** Single select

- European country list
- Other

If **Other**: free text.
- Please state the country in which your institution is based.

---

## 1.3 Institution type

**Type:** Single select

- University
- University of Applied Sciences / Polytechnic
- Specialized higher education institution
- Arts or Music institution
- Research institution
- Don't know / Cannot assess
- Other + Text

---

## 1.4 Approximate number of students

**Type:** Single select

- Fewer than 1,000
- 1,000–4,999
- 5,000–9,999
- 10,000–19,999
- 20,000–39,999
- 40,000–79,999
- 80,000 or more
- Not applicable
- Don't know

---

## 1.5 Approximate staff headcount

**Type:** Single select

- Fewer than 250
- 250–999
- 1,000–2,499
- 2,500–4,999
- 5,000–9,999
- 10,000 or more
- Don't know

---

## 1.6 Your role

**Type:** Multi-select

- Enterprise / Business / Solution / IT Architect
- IT Strategy / Digital Strategy
- CIO / IT Director / Head of IT
- CDO / Digital Office
- IT or Digital Project / Programme Management
- Academic / Researcher with EA context
- Educator / Lecturer with EA context
- Other

---

## 1.7 Your knowledge of your institution's EA practice

**Type:** Single select

- I am directly responsible for or actively involved in it
- I work closely with the EA practice
- I have general knowledge of it
- I have limited knowledge of it

---

# Section 2: Enterprise Architecture Practice

## 2.1 Current status of Enterprise Architecture at your institution

**Type:** Single select, randomized

> To the best of your knowledge, what is the current status of Enterprise Architecture at your institution?

- Established operational practice
- Early operational practice / currently being established
- Exploring or planning EA
- No EA practice
- Don't know / Cannot assess

---

## 2.2 Organizational age of the EA practice

**Condition:** Show if 2.1 = Established / Early operational practice

**Type:** Single select

> Approximately how long has your institution had an operational EA practice?

- Less than 1 year
- 1–3 years
- 4–7 years
- More than 7 years
- Don't know

---

## 2.3 EA approaches currently used

**Condition:** Show if 2.1 = Established / Early operational / Exploring

**Type:** Multi-select

> Which of the following frameworks/methods/etc. does your institution currently use, pilot, or actively evaluate for Enterprise Architecture?

### EA frameworks / methods
- TOGAF
- Zachman Framework
- Don't know / Cannot assess
- Other EA framework or method

### Higher-education reference models / architectures
- HERM
- HORA / HOSA
- Don't know / Cannot assess
- Other higher-education reference model

### Modelling languages / standards
- ArchiMate
- BPMN
- Don't know / Cannot assess
- Other modelling language or notation

### Institution-specific approach
- Custom / in-house EA framework
- Just EA standards without customization
- No formal framework; pragmatic or ad hoc EA practice
- Other
- Don't know / Cannot assess

**Implementation note:** Store each option as a separate binary variable and retain the category grouping above.

---

## 2.4 Organizational home of the EA practice

**Condition:** Show if 2.1 = Established / Early operational / Exploring

**Type:** Multi-select

> Where is the EA practice organizationally located or formally anchored?

- Dedicated Enterprise Architecture team
- Central IT
- CIO office / IT leadership
- CDO / Digital Office
- Central administration outside IT
- Academic / teaching organization
- Research organization
- Cross-institutional / distributed model
- Undefined
- Don't know / Cannot assess
- Other + Text

---

## 2.5 Executive or organizational lead for EA

**Condition:** Show if 2.1 = Established / Early operational / Exploring

**Type:** Single select

> Who has primary organizational responsibility for Enterprise Architecture?

- CIO
- IT Director / Head of IT
- CDO / Head of Digital Transformation
- Dedicated Head of Enterprise Architecture / Chief Architect
- Vice-President / Vice-Rector / Executive Board member
- Central administration leader outside IT
- Distributed / shared responsibility without one formal lead
- Undefined
- Don't know / Cannot assess
- Other + Text

---

# Section 3: HERM Awareness & Adoption

## 3.1 Respondent awareness of HERM

**Type:** Single select

> Before starting this survey, how familiar were you personally with HERM?

- I know HERM well
- I know the basic concept
- I had heard of HERM but knew little about it
- I was not familiar with HERM before this survey

---

## 3.2 Institutional HERM adoption status

**Type:** Single select

> To the best of your knowledge, what is the current status of HERM at your institution?

- Not considered
- Being evaluated / considered
- Pilot or experimental use
- Active operational use
- Embedded in governance or standard EA processes
- Previously used, but no longer in use
- Don't know / Cannot assess

**Routing:**

- Being evaluated / considered -> Section 4
- Pilot or experimental use -> Section 4
- Active operational use -> Section 4
- Embedded in governance or standard EA processes -> Section 4
- All other responses -> Section 5

---

# Section 4: HERM Usage Details

## 4.1 Start of HERM engagement

**Type:** Year or Don't know

> Approximately when did your institution first start actively evaluating or using HERM?

---

## 4.2 HERM application area

**Type:** Multi-select, randomized

> In which areas of your organisation are the HERM artefacts mentioned earlier used?

- Institution-wide / cross-domain
- Teaching and learning (as topic)
- Research (as topic)
- Student lifecycle / student administration
- Finance and controlling
- Human resources
- IT management
- Facilities / infrastructure
- Governance / strategy
- Don't know / Cannot assess
- Other

**Type:** Text, optional

---

## 4.3 HERM artifacts used or evaluated

**Type:** Multi-select, randomized

> Which HERM artifacts does your institution currently use, pilot, or actively evaluate?

| Artifact                          | Not used | Evaluating | Pilot | Operational |
| --------------------------------- | -------- | ---------- | ----- | ----------- |
| Business Reference Model (BRM)    | ○        | ○          | ○     | ○           |
| Data Reference Model (DRM)        | ○        | ○          | ○     | ○           |
| Application Reference Model (ARM) | ○        | ○          | ○     | ○           |
| Technology Reference Model (TRM)  | ○        | ○          | ○     | ○           |
| Service Reference Model (SRM)     | ○        | ○          | ○     | ○           |

---

## 4.4 Additional artifacts used

**Type:** Multi-select, randomized

> Which EAM and HERM-related/supporting artefacts and approaches are in use?

- Business Model Canvas
- Recipe Cards
- Process Models
- Value Streams
- Don't know / Cannot assess
- Other

---

## 4.5 HERM application area (follow up to 4.2)

Visibility is conditional on 4.2 being something other than "Don't know"

> Which is currently the primary area? Provide HERM Business Capability name or identifier, if known.

**Type:** Text, optional

---

## 4.6 Problems and tasks addressed with HERM

**Type:** Multi-select, randomized

> For which tasks is HERM currently used or evaluated at your institution?

- Structuring or documenting the application landscape
- Structuring or communicating business capabilities
- Technology standardization or technology lifecycle management
- Data governance or data architecture
- Service design or service architecture
- Strategic or transformation planning
- Impact analysis and future-state planning for major change initiatives
- Risk, security, or compliance analysis
- Process or responsibility modelling
- Communication between IT and non-IT stakeholders
- Benchmarking or comparison with peer institutions
- Consolidation, merger, or shared-service planning
- Investment or project portfolio planning and prioritisation
- Don't know / Cannot assess
- Other

---

## 4.7 Value are you receiving from using HERM

**Type:** Multi-select, randomized

> What specific value can you now offer your organisation?

- No tangible outcome yet
- Shared terminology
- Improved landscape transparency
- Better decision support
- Accelerated project or analysis
- Improved stakeholder communication
- Reusable architecture artefact
- Cost or effort reduction
- Don't know / Cannot assess
- Other

---

## 4.8 Concrete HERM use case

**Type:** Text, optional

> **Please describe one specific HERM use case at your institution that you know particularly well. Please focus on what was actually done rather than on HERM in general.**  
>  
> You may use the following points as guidance:
> 
> - **Use case:** What was the problem, task, or decision?
> - **Actors:** Who was involved?
> - **HERM use:** Which HERM artifact(s) were used, and how were they applied?
> - **Outcome:** What was produced, decided, or changed?
> - **Benefit:** Who benefited from the result, and in what way?
> 
> _A concise description is sufficient; you do not need to address every point._

Prompt: "Your HERM use-case-description..."

---

## 4.9 What has worked well?

**Type:** Text, optional

> What aspects of using HERM have worked particularly well at your institution?

Prompt: "Please provide details how you applied HERM and why this was a sucess..."

---

### 4.10 Enabling factors

**Type:** Multi-select, randomized

> What factors enabled the implementation of HERM at your institution?

- Strong EA capability
- Executive sponsorship
- Active practitioner community
- Good documentation
- Concrete institutional use case
- Tool support
- Availability of reusable examples
- Alignment with existing EA models
- National / community support
- Individual champion or internal advocate
- Don't know / Cannot assess
- Other

---

## 4.11 What has been difficult or missing?

**Type:** Text, optional

> What aspects of using HERM have been difficult, insufficient, or missing?

Prompt: "Provide details on road blocks concerning HERM..."

---

## 4.12 Integration of HERM into broader EA practice

**Condition:** Show if 2.1 = Established / Early operational / Exploring

**Type:** Single select, randomized

> **What role does HERM play in your institution's broader EA practice?**

- Central foundation of the EA approach
- Integrated component of the EA approach
- Selectively connected for specific use cases
- Used independently of the broader EA practice
- No relationship established yet
- Don't know / Cannot assess

---

## 4.13 Adapted, extended or mapped HERM

**Type:** Multi-select, randomized

> Have you adapted, extended or mapped HERM in a way that might be useful to other institutions?

- Translation
- Capability extensions
- HORA mapping
- Application mapping
- Service catalogue
- Data mapping
- Tool implementation
- Governance model
- Visualization
- Don't know / Cannot assess
- Other

---

# Section 5: HERM Non-Adoption & Barriers

## 5.1 Reasons HERM is not currently in operational use

**Type:** Multi-select, randomized

> Which factors currently contribute to HERM not being used operationally at your institution?

- HERM is not sufficiently known at our institution
- No current need for an additional reference model
- Existing EA approaches already meet our needs
- HERM appears too complex for our current needs
- HERM appears too specific for our context
- HERM does not appear to fit our institutional context
- Insufficient tooling support
- Insufficient documentation or guidance
- Lack of implementation examples / peer cases
- Insufficient internal EA capacity
- Lack of leadership or organizational support
- Switching or adoption effort is too high
- Benefits are unclear compared with the required effort
- EA/HERM knowledge depends on too few individuals
- HERM was previously used but discontinued
- Don't know / Cannot assess
- Other

---

## 5.2 Primary barrier

**Condition:** Show if at least one substantive option selected in 5.1

**Type:** Single select, piped from selected responses in 5.1

> Of the factors you selected, which is currently the most important barrier?

Added options:
Other (meaning the item you provided above)
None of the above
Don't know / Cannot assess

---

## 5.3 Future consideration of HERM

**Type:** Single select, randomized

> Is there currently an intention or plan to evaluate or pilot HERM within the next two years?

- Yes
- Under discussion
- No
- Don't know / Cannot assess

---

## 5.4 Potential role of HERM

**Condition:** Show if 5.3 = Yes / under discussion

**Type:** Single select, randomized

> If your institution adopted HERM, what role would it most likely play?

- Foundation for the overall EA approach
- Complement to an existing EA framework or method
- Reference model for selected domains or use cases
- Primarily a benchmarking / comparison reference
- Cannot assess
- Other

---

## 5.5 Requirements for future adoption

**Type:** Text, optional

> What would HERM need to offer, or what would need to change at your institution, for adoption to become more attractive?

---

# Section 6: Open Questions & Support Needs

## 6.1 Open questions about Enterprise Architecture

**Type:** Text, optional

> What are the most important unresolved questions about Enterprise Architecture at your institution?

---

## 6.2 Open questions about HERM

**Type:** Text, optional

> What questions about HERM would you most like the HERM community to address?

---

## 6.3 Support needs

**Type:** Multi-select, randomized

> What kind of support would your institution like HERM to provide to help move EA forward?

- None currently
- Introductory guidance
- Implementation guide / playbook
- Concrete use cases and examples
- Reference architectures / reusable patterns
- Tooling support
- Training or workshops
- Peer exchange with other institutions
- Benchmarking data
- Governance and organizational guidance
- Mapping to other EA frameworks or standards
- Don't know / Cannot assess
- Other

---

## 6.4 Most important support need

**Condition:** Show if at least one substantive option selected in 6.3

**Type:** Single select, piped from 6.3

> Which of these would be most valuable to your institution?

Added options:
Other (meaning the item you provided above)
None of the above
Don't know / Cannot assess

---

# Section 7: Knowledge Sharing & Follow-up

## 7.1 Potential value of the institution's experience

**Type:** Single select, randomized

> Do you believe your institution has an EA or HERM experience that could be useful for other higher education institutions?

Yes
Possibly
Unlikely
No
Cannot assess

---

## 7.2 Interest in community exchange

**Type:** Multi-select

> Would you or your institution be interested in any of the following?

Receiving the results of this survey
Sharing a use case or practical experience
Presenting and discussing your EA / HERM work
Joining a community workgroup on EA / HERM
Participating in a follow-up interview
Participating in a more detailed follow-up survey
None of these

---

# Section 8: Naming & Contact Consent


## 8.1 Contact email

**Condition:** Show if at least one follow-up option other than "None" was selected in 7.2

**Type:** Email, optional

> By providing your contact details, you consent to the purpose(s) provided in the previous question.
> Please note that your response will not be included in the publication of the dataset. It will only be processed internally by the EUNIS EA SIG.

Prompt: "Your e-mail address"

---

## 8.2 Permission to name institution

**Condition:** Show if institution name provided in 1.1

**Type:** Single select

> You had provided the name of your institution at the beginning of this survey.
> May your institution be named in publications or datasets resulting from this survey?

- Yes, the institution may be named
- No, use only anonymized or aggregated information

---

## 9.1 Thanks and final Question

Thank you for participating in this survey.
We will evaluate, discuss and publish the results as soon as possible.

### Feedback 

**Type:** Text, optional

> Do you have any final comments about the survey itself?

Thanks again for your personal supoort of the global HERM community!

---

# Data Quality and Implementation Rules

1. Do not force institution-level answers where respondents may reasonably lack knowledge; provide **Don't know / Cannot assess**.
2. Store multi-select responses as separate binary variables.
3. Randomize unordered option lists where supported by the survey platform.
4. Keep "Other" as a separate binary variable plus free-text field.
5. Keep "None" and "Don't know" mutually exclusive with substantive options.
6. Validate year fields against plausible bounds.
7. Retain respondent-level and institution-level variables separately.
8. Flag duplicate institution responses during data cleaning where institution identity is available.
9. Do not automatically merge conflicting responses from the same institution; define a reconciliation rule before analysis.
10. Preserve the exact survey version used for every response.

---

# Open Items

The following design decisions require clarification of the study's intended claims or use of the results.

## OI-1 — Population claim and sampling strategy

What should the final study claim?

1. Descriptive results for participating institutions / respondents only
2. Approximate landscape of the EUNIS community
3. Estimates intended to describe European higher education institutions more broadly

The third objective would require a substantially more explicit sampling frame, recruitment strategy, and treatment of non-response.

> option 1 and 2 Defitively not 3, sinfe we dont have a good distribution channel beyond EUNIS.

## OI-2 — One response per institution vs. multiple expert responses

Should the study aim for:

1. one authoritative institutional response,
2. multiple expert responses that are analyzed independently, or
3. multiple responses that are reconciled into one institutional record?

This determines recruitment wording, duplicate handling, and the unit used in inferential analyses.

> option 2 is key. However, we will often get only one answer per institution had teeat ot as option 1. 

## OI-3 — Scope of "Higher Education Institution"

Should research institutes and other non-teaching organizations remain part of the target population, or should the survey focus strictly on higher education institutions?

> yes. Keep this. Just to see the differences.

## OI-4 — Required depth of framework comparison

Is it sufficient to know which frameworks / reference models / modelling languages are used, or should the study compare for each selected approach:

- adoption status,
- start year,
- organizational scope,
- purpose of use?

A framework-by-framework comparison would require a repeated question block or matrix.

## OI-5 — Meaning of HERM adoption

Should "adoption" require operational use, or should active evaluation and pilots also count as adoption in headline reporting?

A reporting definition should be fixed before fieldwork.

## OI-6 — HERM artifact taxonomy

Which artifacts are officially considered part of HERM for this study, and which are related artifacts or methods used alongside HERM?

The final answer options should use one agreed taxonomy and naming convention.

## OI-7 — Desired granularity of institutional application areas

Is a broad functional classification sufficient, or should HERM Business Capabilities be captured using a formal HERM capability hierarchy?

If formal capability-level analysis is intended, a controlled selection should replace optional free text.

## OI-8 — Case-study selection criteria

What makes a case "transfer-worthy" for the purposes of the study?

Possible criteria include:

- demonstrated outcome,
- reuse potential,
- documentation quality,
- cross-institutional relevance,
- maturity,
- novelty,
- willingness to share.

The criteria should be defined before using survey responses to rank cases.

## OI-9 — Intended analysis of institutional size

Will student and staff size be used only descriptively, or should they support statistical comparisons between institution-size groups?

If comparative analysis is planned, the final category boundaries should be aligned with expected sample sizes and relevant European higher-education classifications.

## OI-10 — Country-level analysis

Are country comparisons an intended output?

If yes, minimum case counts per country, treatment of uneven national recruitment, and aggregation rules should be specified before fieldwork.

## OI-11 — EA maturity beyond HERM status

Is the study intended to compare overall EA maturity between institutions?

If yes, the current EA status item is insufficient; a separate multi-item EA maturity construct would be required.

## OI-12 — Relationship to follow-up research

Which topics must be answered quantitatively in this first wave, and which are explicitly reserved for interviews, workshops, or a second survey?

Candidate follow-up topics include:

- detailed EA tooling,
- professional background of respondents,
- planning horizons,
- detailed governance arrangements,
- detailed maturity dimensions,
- implementation costs and resources,
- failure cases,
- detailed mappings between HERM and other frameworks.

## OI-13 — Publication and data-sharing model

Will the published output contain:

- aggregated statistics only,
- anonymized respondent-level data,
- named institution-level data with consent,
- or a public case-study directory?

The final consent and privacy wording depends on this decision.

## OI-14 — Survey language

Will the survey be English-only or translated into national languages?

If translated, a translation and reconciliation procedure should be defined to preserve measurement equivalence across language versions.

---

# Estimated Completion Time

- HERM operational user: approximately 8–10 minutes
- HERM evaluator / pilot: approximately 7–9 minutes
- HERM non-user with EA practice: approximately 5–7 minutes
- Respondent without active EA practice: approximately 4–5 minutes

