from engine import app, db
from engine.models import Query, Response

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Query":Query, "Response":Response}
