# This program is intended to Write Blogs by referring to given webpage:
# - WebBaseLoader to read a PDF from a webpage
# - Convert the documents into embeddings and store into an FAISS DB
# - Create a Stuff document chain, create a retrieval chain from the FAISS DB
# - Create a Retrieval Chain using the FAISS retrevier and document chain


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.document_loaders import PyMuPDFLoader  
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()


loader = PyMuPDFLoader("https://nclt.gov.in/gen_pdf.php?filepath=/Efile_Document/ncltdoc/casedoc/2709138008372023/04/Order-Challenge/04_order-Challange_004_168441092321415434206466122b78ec3.pdf")
pages = loader.load_and_split()
print(len(pages), "pages loaded.")

# Set up the LLM object
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Use HuggingFace embeddings (runs locally, no API key required)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Convert the pages into Embeddings and store into FAISS Vector DB
vector = FAISS.from_documents(pages, embeddings)

prompt = ChatPromptTemplate.from_template("""
Answer the following questions based on the provided context:

<context>
{context}
</context>

Question: {input}
""")

document_chain = create_stuff_documents_chain(llm, prompt)

retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain) # document chain being part of the retrieval Chain

response = retrieval_chain.invoke({
    "context": "you are a lawyer who is creating the gist for a given Court Order.",
    "input": """Please list down the key points from the order.
Please mention the Case Title, Petitioner and Defendant names at the top."""
})

print(response["answer"])
