from phi.knowledge.website import WebsiteKnowledgeBase
from phi.vectordb.pgvector import PgVector

# Create knowledge base
knowledge_base = WebsiteKnowledgeBase(
    urls=["https://www.marketwatch.com", "https://www.investing.com"],
    max_links=20,
    vector_db=PgVector(
        table_name="market_data_documents",
        db_url="postgresql+psycopg2://ai:ai@localhost:5532/ai",
    ),
)