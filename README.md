# AI-Legal-Assistant-Summarize-Court-Orders-Using-LangChain-Gemini-with-FAISS-Search-Hugging-Face

This project leverages powerful AI models and vector search technology to analyze and summarize court orders from publicly accessible PDFs. It automatically extracts key information such as case titles, petitioner/respondent names, and important points from legal documents using a Retrieval-Augmented Generation (RAG) pipeline.

---

## 🚀 Features

- 🔍 Load and parse legal PDF files from a public URL
- 🧩 Text splitting and semantic embedding using HuggingFace models
- 🧠 Vector storage and retrieval using FAISS
- 🤖 AI summarization and key point extraction using Google Gemini (via LangChain)
- ⚖️ Tailored for legal use-cases like summarizing court orders

---

## 🛠️ Technologies Used

- [LangChain](https://www.langchain.com/)
- [Google Gemini (via LangChain)](https://python.langchain.com/docs/integrations/chat/google_generative_ai)
- [HuggingFace Sentence Transformers](https://www.sbert.net/)
- [FAISS Vector Database](https://github.com/facebookresearch/faiss)
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## 📄 How It Works

1. **Load Court Order PDF**  
   Downloads a court order from a URL and splits the content into pages.

2. **Embed & Index**  
   Uses HuggingFace embeddings to convert text into vector format and indexes them using FAISS for fast retrieval.

3. **Retrieval-Augmented Generation (RAG)**  
   Combines the FAISS retriever with a prompt template and Google Gemini model to generate concise legal summaries.

4. **Query Execution**  
   Asks the model to extract and present key legal information, including case title, petitioner, and defendant.

---

## 🧑‍⚖️ Example Output

📄 22 pages loaded.

Here are the key points from the order:

**Case Title:**  
C.P. (CAA) / 20 / MB / 2023 IN C.A. (CAA) / 256 / MB / 2022

**Petitioner(s):**  
First Petitioner Company, Second Petitioner Company, Third Petitioner Company, Fourth Petitioner Company, and Fifth Petitioner Company.

**Defendant(s):**  
Not explicitly mentioned, but implied parties include:  
- Regional Director, Western Region (representing the Central Government)  
- Official Liquidator, High Court, Bombay

---

### 📝 Key Points from the Order

- **Scheme Sanctioned:**  
  The Scheme of Amalgamation of the First, Second, Third, and Fourth Petitioner Companies with the Fifth Petitioner Company is sanctioned.

- **Appointed Date:**  
  The Appointed Date of the Scheme is 1st April 2022.

- **Binding Nature:**  
  The Scheme is binding on all Petitioner Companies, their shareholders, secured creditors, unsecured creditors/trade creditors, employees, and other stakeholders.

- **Listing Status:**  
  - Equity shares of the Fifth Petitioner Company are listed on BSE Limited and National Stock Exchange of India Limited.  
  - Equity shares of the First to Fourth Petitioner Companies are not listed on any Indian stock exchange.

- **Subsidiary Status:**  
  The First, Second, Third, and Fourth Petitioner Companies are wholly-owned subsidiaries of the Fifth Petitioner Company.

- **Central Government Observations:**  
  - The Regional Director (Western Region) filed a report.  
  - Petitioner Companies submitted clarifications and undertakings.  
  - Tribunal accepted them; the Director had no objections.

- **Official Liquidator Observations:**  
  - The Official Liquidator filed a report with observations.  
  - Clarifications and undertakings were provided by the Petitioner Companies.

- **Share Capital Cancellation:**  
  Upon the Scheme becoming effective, the entire share capital of the First, Second, Third, and Fourth Petitioner Companies shall be cancelled and extinguished.

- **Statutory Compliance:**  
  All required statutory compliances have been fulfilled.

- **Filing Requirements:**  
  Petitioner Companies must file a certified copy of the Order and the Scheme with the Registrar of Companies in e-form INC-28 within 30 days (or extended with additional fees).

- **Benefits of the Scheme:**  
  - Eliminates administrative redundancy and record-keeping  
  - Reduces overall expenditure  
  - Enhances internal controls and operational efficiency  
  - Improves agility in responding to market changes across IT, HR, finance, legal, and management functions

---
