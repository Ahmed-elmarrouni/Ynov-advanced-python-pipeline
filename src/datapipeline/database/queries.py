import logging
from datapipeline.database.connection import get_db_connection

logger = logging.getLogger(__name__)


def get_revenue_by_country():
    conn = get_db_connection()
    # Return results as a dictionary so it is easier to read
    cur = (
        conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        if "psycopg2" in globals()
        else conn.cursor()
    )

    query = """
        SELECT c.country, SUM(o.quantity * o.price) as total_revenue
        FROM orders o
        JOIN customers c ON o.customer_id = c.id
        GROUP BY c.country
        ORDER BY total_revenue DESC;
    """
    try:
        cur.execute(query)
        return cur.fetchall()
    except Exception as e:
        logger.error(f"Query failed: {e}")
        raise
    finally:
        cur.close()
        conn.close()
